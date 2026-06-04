import * as github from '@actions/github';
import * as cp from 'child_process';
import * as fs from 'fs';
import * as path from 'path';
import * as util from 'util';

// Import Google AI SDK to reliably resolve conflicts instead of depending on an arbitrary CLI wrapper
import { GoogleGenerativeAI } from '@google/generative-ai';

const execFileAsync = util.promisify(cp.execFile);

const sleep = (ms: number) => new Promise(resolve => setTimeout(resolve, ms));

async function execCmd(command: string, args: string[], secretTokens: string[] = []): Promise<string> {
  // Mask secrets before logging
  let logArgs = [...args];
  for (const secret of secretTokens) {
    if (secret) {
      logArgs = logArgs.map(arg => arg.replace(new RegExp(secret, 'g'), '***'));
    }
  }

  console.log(`Executing: ${command} ${logArgs.join(' ')}`);

  const { stdout, stderr } = await execFileAsync(command, args);
  if (stderr && stderr.trim().length > 0 && !stderr.includes('Switched to') && !stderr.includes('Already on') && !stderr.includes('From https://github.com')) {
    let logStderr = stderr.trim();
    for (const secret of secretTokens) {
      if (secret) {
         logStderr = logStderr.replace(new RegExp(secret, 'g'), '***');
      }
    }
    console.warn(`[WARN] ${command} ${logArgs.join(' ')}: ${logStderr}`);
  }
  return stdout.trim();
}

async function resolvePrConflicts() {
  const token = process.env.GITHUB_TOKEN;
  if (!token) {
    throw new Error('GITHUB_TOKEN environment variable is missing.');
  }

  const geminiKey = process.env.GEMINI_API_KEY;
  if (!geminiKey) {
    throw new Error('GEMINI_API_KEY environment variable is missing.');
  }

  const octokit = github.getOctokit(token);
  const context = github.context;
  const genAI = new GoogleGenerativeAI(geminiKey);
  const model = genAI.getGenerativeModel({ model: "gemini-2.0-flash" });

  // Use repository from context or fallback to 8bukets/8bukets
  const owner = context.repo.owner || '8bukets';
  const repo = context.repo.repo || '8bukets';

  console.log(`Fetching open pull requests for ${owner}/${repo}...`);

  // Get all open PRs
  const { data: prs } = await octokit.rest.pulls.list({
    owner,
    repo,
    state: 'open',
    per_page: 100
  });

  console.log(`Found ${prs.length} open pull requests.`);

  // Get repository collaborators to ensure we only process trusted PRs
  const { data: collaborators } = await octokit.rest.repos.listCollaborators({
    owner,
    repo,
  });
  const trustedUsers = collaborators.map(c => c.login);

  for (const pr of prs) {
    console.log(`\n---------------------------------`);
    console.log(`Checking PR #${pr.number}: ${pr.title}`);

    // Security check: Only process PRs from trusted collaborators
    if (!trustedUsers.includes(pr.user?.login || '')) {
       console.log(`PR #${pr.number} is from untrusted user ${pr.user?.login}. Skipping for security reasons.`);
       continue;
    }

    // We need to fetch the PR details specifically to get accurate mergeable status
    const { data: prDetails } = await octokit.rest.pulls.get({
      owner,
      repo,
      pull_number: pr.number
    });

    const isConflicted = prDetails.mergeable === false || prDetails.mergeable_state === 'dirty';

    if (!isConflicted) {
      console.log(`PR #${pr.number} is not conflicted. mergeable: ${prDetails.mergeable}, mergeable_state: ${prDetails.mergeable_state}. Skipping.`);
      continue;
    }

    console.log(`PR #${pr.number} HAS CONFLICTS. Preparing to resolve...`);
    const prBranch = pr.head.ref;
    const baseBranch = pr.base.ref;
    const headRepoOwner = pr.head.repo?.owner.login || owner;
    const headRepoName = pr.head.repo?.name || repo;
    const isFork = headRepoOwner !== owner;

    try {
      if (isFork) {
        // Fetch PR from the source directly
        await execCmd('git', ['fetch', 'origin', `pull/${pr.number}/head:pr-${pr.number}`]);
        await execCmd('git', ['fetch', 'origin', baseBranch]);
        await execCmd('git', ['checkout', `pr-${pr.number}`]);
      } else {
        await execCmd('git', ['fetch', 'origin', prBranch]);
        await execCmd('git', ['fetch', 'origin', baseBranch]);
        await execCmd('git', ['checkout', prBranch]);
        await execCmd('git', ['reset', '--hard', `origin/${prBranch}`]);
      }

      console.log(`Merging origin/${baseBranch} to generate conflict markers...`);
      let mergeOutput = '';
      try {
        mergeOutput = await execCmd('git', ['merge', `origin/${baseBranch}`]);
      } catch (err: any) {
        mergeOutput = err.stdout || '';
        // If git merge fails, it's a conflict, which is expected
      }

      // Find conflicted files
      const conflictedFilesStr = await execCmd('git', ['diff', '--name-only', '--diff-filter=U']);
      const conflictedFiles = conflictedFilesStr.split('\n').map(f => f.trim()).filter(f => f.length > 0);

      if (conflictedFiles.length === 0) {
        console.log(`No actual conflict markers found in files. Aborting merge and skipping.`);
        await execCmd('git', ['merge', '--abort']);
        continue;
      }

      console.log(`Conflicted files: ${conflictedFiles.join(', ')}`);

      for (const file of conflictedFiles) {
        console.log(`Resolving conflicts in ${file} using Gemini API...`);
        const absolutePath = path.resolve(process.cwd(), file);
        const fileContent = fs.readFileSync(absolutePath, 'utf8');

        const prompt = `The following file has git merge conflicts indicated by <<<<<<<, =======, and >>>>>>> markers.
Please analyze the conflicting blocks and logically resolve them. Provide ONLY the fully resolved, complete file content.
Do NOT wrap the output in markdown code blocks like \`\`\` or include any explanations, just the raw file text.

Here is the file content:
${fileContent}`;

        try {
          const result = await model.generateContent(prompt);
          const responseText = result.response.text();

          // Remove Markdown formatting if Gemini hallucinated it despite instructions
          let cleanedOutput = responseText.trim();
          if (cleanedOutput.startsWith('```')) {
            const lines = cleanedOutput.split('\n');
            if (lines.length > 0 && lines[0].startsWith('```')) {
              lines.shift(); // remove first ```
            }
            if (lines.length > 0 && lines[lines.length-1].trim() === '```') {
              lines.pop(); // remove last ```
            }
            cleanedOutput = lines.join('\n');
          }

          // VERIFICATION: Ensure the LLM didn't just spit back conflict markers
          if (cleanedOutput.includes('<<<<<<<') || cleanedOutput.includes('=======')) {
              throw new Error(`LLM failed to resolve conflicts in ${file}. Conflict markers still present in output.`);
          }
          if (cleanedOutput.length === 0) {
              throw new Error(`LLM returned empty output for ${file}.`);
          }

          fs.writeFileSync(absolutePath, cleanedOutput);

          console.log(`Successfully resolved and wrote to ${file}`);
          await execCmd('git', ['add', file]);
        } catch (e: any) {
          console.error(`Failed to resolve ${file} with Gemini API:`, e);
          throw e; // abort the whole PR resolution if one file fails
        }
      }

      console.log(`All conflicts resolved. Committing and pushing...`);
      // Commit the merge resolution
      await execCmd('git', ['commit', '-m', "Autonomously resolved merge conflicts via Gemini API"]);

      if (isFork) {
         const remoteUrl = `https://x-access-token:${token}@github.com/${headRepoOwner}/${headRepoName}.git`;
         await execCmd('git', ['push', remoteUrl, `pr-${pr.number}:${prBranch}`], [token]);
      } else {
         await execCmd('git', ['push', 'origin', prBranch]);
      }

      console.log(`Successfully pushed resolved branch. Attempting to squash and merge PR #${pr.number}...`);

      // Wait for GitHub to recognize the pushed branch changes and update mergeable state
      let mergeableStateIsClean = false;
      let attempts = 0;
      while (!mergeableStateIsClean && attempts < 10) {
        await sleep(3000); // 3 seconds per attempt
        try {
           const { data: updatedPr } = await octokit.rest.pulls.get({
              owner,
              repo,
              pull_number: pr.number
           });
           // We expect mergeable: true after pushing the resolution
           if (updatedPr.mergeable === true) {
              mergeableStateIsClean = true;
           } else if (updatedPr.mergeable === false && attempts > 3) {
              console.log(`PR #${pr.number} is explicitly not mergeable after push.`);
              break;
           }
        } catch (e) {
           // ignore api errors
        }
        attempts++;
      }

      // The user explicitly requested to immediately squash and merge
      await octokit.rest.pulls.merge({
        owner,
        repo,
        pull_number: pr.number,
        merge_method: 'squash',
        commit_title: `Autonomously resolved and merged PR #${pr.number}`
      });

      console.log(`PR #${pr.number} squashed and merged successfully!`);

    } catch (err: any) {
      console.error(`Error processing PR #${pr.number}:`, err);
      try {
        await execCmd('git', ['merge', '--abort']);
      } catch (e) {
        // ignore
      }
    }
  }

  console.log(`Finished processing all open PRs.`);
}

resolvePrConflicts().catch(err => {
  console.error("Fatal Error:", err);
  process.exit(1);
});
