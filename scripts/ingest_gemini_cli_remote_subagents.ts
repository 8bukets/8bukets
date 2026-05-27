import * as fs from 'fs';
import * as path from 'path';

const RAW_FILE_PATH = path.join(process.cwd(), 'data/raw/gemini_cli_remote_subagents.md');

interface KnowledgeEntry {
    topic: string;
    description: string;
    details: string;
}

async function ingestGeminiCliRemoteSubagents() {
    console.log(`Ingesting Gemini CLI Remote Subagents knowledge from ${RAW_FILE_PATH}...`);
    try {
        if (!fs.existsSync(RAW_FILE_PATH)) {
            throw new Error(`File not found: ${RAW_FILE_PATH}`);
        }
        const rawContent = fs.readFileSync(RAW_FILE_PATH, 'utf8');

        const knowledgeEntries: KnowledgeEntry[] = [
            {
                topic: "Gemini CLI Remote Subagents",
                description: "Gemini CLI supports connecting to remote subagents using the Agent-to-Agent (A2A) protocol. This allows Gemini CLI to interact with other agents, expanding its capabilities by delegating tasks to remote services.",
                details: "Remote subagents are defined as Markdown files (.md) with YAML frontmatter. They can be placed in `.gemini/agents/*.md` (Project-level) or `~/.gemini/agents/*.md` (User-level)."
            },
            {
                topic: "Gemini CLI Remote Subagent Configuration Schema",
                description: "The YAML frontmatter configuration schema for remote subagents.",
                details: "Required fields include `kind: remote`, `name` (a valid slug), and either `agent_card_url` or `agent_card_json`. Optional `auth` object is used for authentication configuration."
            },
            {
                topic: "Gemini CLI Remote Subagent Authentication",
                description: "Gemini CLI supports multiple authentication types for remote agents: `apiKey`, `http`, `google-credentials`, and `oauth`.",
                details: "Secret values support dynamic resolution like `$ENV_VAR` or `!command`. `google-credentials` automatically selects access or identity tokens based on the host pattern (`*.googleapis.com` or `*.run.app`)."
            },
            {
                topic: "Gemini CLI Remote Subagent Proxy Support",
                description: "Gemini CLI routes traffic to remote agents through an HTTP/HTTPS proxy if configured.",
                details: "It uses `general.proxy` in `settings.json` or standard environment variables (`HTTP_PROXY`, `HTTPS_PROXY`)."
            },
            {
                topic: "Gemini CLI Managing Subagents",
                description: "Users can manage subagents using slash commands within Gemini CLI.",
                details: "Commands include `/agents list`, `/agents reload`, `/agents enable <agent_name>`, and `/agents disable <agent_name>`. Remote agents can be globally disabled by setting `experimental.enableAgents` to `false` in `settings.json`."
            }
        ];

        // Ensure data directory exists
        const dataDir = path.join(process.cwd(), 'data/knowledge');
        if (!fs.existsSync(dataDir)) {
            fs.mkdirSync(dataDir, { recursive: true });
        }

        const jsonPath = path.join(dataDir, "gemini_cli_remote_subagents.json");
        fs.writeFileSync(jsonPath, JSON.stringify(knowledgeEntries, null, 4), 'utf8');
        console.log(`Saved Gemini CLI Remote Subagents knowledge to ${jsonPath}`);

        // Save to Markdown
        const mdPath = path.join(dataDir, "gemini_cli_remote_subagents.md");
        let mdContent = `# Gemini CLI Remote Subagents Documentation\n\nIngested from raw documentation.\n\n`;

        for (const entry of knowledgeEntries) {
            mdContent += `## ${entry.topic}\n\n`;
            mdContent += `${entry.description}\n\n`;
            mdContent += `${entry.details}\n\n`;
        }

        fs.writeFileSync(mdPath, mdContent, 'utf8');
        console.log(`Saved Gemini CLI Remote Subagents knowledge to ${mdPath}`);

        // Append to CONSOLIDATED_INTELLIGENCE.md
        const consolidatedPath = path.join(process.cwd(), 'CONSOLIDATED_INTELLIGENCE.md');
        if (fs.existsSync(consolidatedPath)) {
            let consolidatedContent = fs.readFileSync(consolidatedPath, 'utf8');
            let newSection = `\n## Gemini CLI Remote Subagents\n\n`;
            newSection += `- **Definition:** Gemini CLI can connect to remote subagents using the A2A protocol, configured via Markdown files with YAML frontmatter.\n`;
            newSection += `- **Authentication:** Supports apiKey, http, google-credentials, and oauth.\n`;
            newSection += `- **Management:** Use \`/agents list\`, \`/agents reload\`, \`/agents enable\`, and \`/agents disable\`.\n`;

            // Look for 'All the best - https://markposition.wordpress.com'
            const signature = 'All the best - https://markposition.wordpress.com';
            if (consolidatedContent.includes(signature)) {
                 consolidatedContent = consolidatedContent.replace(signature, newSection + '\n' + signature);
            } else {
                 consolidatedContent += newSection + '\n' + signature;
            }
            fs.writeFileSync(consolidatedPath, consolidatedContent, 'utf8');
            console.log(`Appended Gemini CLI Remote Subagents knowledge to CONSOLIDATED_INTELLIGENCE.md`);
        }

        // Merge to KNOWLEDGE_MERGE.md using regex replacement
        const mergePath = path.join(process.cwd(), 'KNOWLEDGE_MERGE.md');
        if (fs.existsSync(mergePath)) {
            let mergeContent = fs.readFileSync(mergePath, 'utf8');

            let newObservation = `## Autonomous Observation: Gemini CLI Remote Subagents\n\n`;
            newObservation += `The system observed documentation regarding Gemini CLI Remote Subagents.\n`;
            newObservation += `Remote subagents are defined as Markdown files with YAML frontmatter containing \`kind: remote\`, \`name\`, and agent card details.\n`;
            newObservation += `Authentication supports \`apiKey\`, \`http\`, \`google-credentials\`, and \`oauth\`.\n\n`;

            const regex = /## Autonomous Observation: Gemini CLI Remote Subagents\n\n(?:(?!## Autonomous Observation)[\s\S])*/g;
            if (regex.test(mergeContent)) {
                 mergeContent = mergeContent.replace(regex, () => newObservation);
                 console.log("Updated existing observation in KNOWLEDGE_MERGE.md");
            } else {
                 mergeContent += newObservation;
                 console.log("Appended new observation to KNOWLEDGE_MERGE.md");
            }
            fs.writeFileSync(mergePath, mergeContent, 'utf8');
        }

        return true;
    } catch (error) {
        console.error("Failed to ingest Gemini CLI Remote Subagents knowledge:", error);
        return false;
    }
}

ingestGeminiCliRemoteSubagents();
