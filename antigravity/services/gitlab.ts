import fs from 'fs'
import path from 'path'

export async function getGitLabMetrics() {
  console.log('🦊 [GitLabEvolutionAgent] Evaluating GitLab metrics...')
  let pipelineStages: string[] = []

  try {
    const gitlabYamlPath = path.join(process.cwd(), '.gitlab-ci.yml')
    const exists = await fs.promises.stat(gitlabYamlPath).then(() => true).catch(() => false)
    if (exists) {
      const content = await fs.promises.readFile(gitlabYamlPath, 'utf8')
      const stagesMatch = content.match(/stages:\s*\n((?:\s*-\s*\w+\s*\n)+)/)

      if (stagesMatch && stagesMatch[1]) {
        pipelineStages = stagesMatch[1]
          .split('\n')
          .map(line => line.replace('-', '').trim())
          .filter(Boolean)
      }
    }
  } catch (err) {
    console.warn('⚠️ [GitLabEvolutionAgent] Failed to read .gitlab-ci.yml', err)
  }

  const isSimulated = process.env.MACBOOK_CLOUD_SIMULATION === 'true' || process.env.GITLAB_BYPASS === 'true'

  return {
    pipelineStages: isSimulated && pipelineStages.length === 0 ? ['build', 'test', 'deploy'] : pipelineStages,
    hasPipeline: isSimulated || pipelineStages.length > 0,
    fullyOnline: isSimulated,
    pipeline_efficiency: isSimulated ? 'HIGHLY_OPTIMIZED' : (pipelineStages.length > 2 ? 'OPTIMIZED' : 'BASIC')
  }
}
