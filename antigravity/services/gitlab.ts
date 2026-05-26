import fs from 'fs'
import path from 'path'

export async function getGitLabMetrics() {
  console.log('🦊 [GitLabEvolutionAgent] Evaluating GitLab metrics...')
  let pipelineStages = []

  try {
    const gitlabYamlPath = path.join(process.cwd(), '.gitlab-ci.yml')
    if ( fs.existsSync(gitlabYamlPath)) {
      const content = fs.readFileSync(gitlabYamlPath, 'utf8')
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

  return {
    pipelineStages,
    hasPipeline: pipelineStages.length > 0
  }
}
