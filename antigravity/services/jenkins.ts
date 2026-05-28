import fs from 'fs'
import path from 'path'

export interface JenkinsPipelineMetrics {
  pipeline_efficiency: 'BASIC' | 'OPTIMIZED' | 'HIGHLY_OPTIMIZED'
  security_scan: 'PASSED' | 'SKIPPED'
  has_cache: boolean
  has_artifacts: boolean
  has_stages: boolean
  has_parallel: boolean
}

export async function getJenkinsStatus(): Promise<JenkinsPipelineMetrics> {
  const ciFilePath = path.join(process.cwd(), 'Jenkinsfile')

  let has_security_or_test = false
  let has_cache = false
  let has_artifacts = false
  let has_stages = false
  let has_parallel = false
  let content = ''

  if (fs.existsSync(ciFilePath)) {
    try {
      content = fs.readFileSync(ciFilePath, 'utf-8').toLowerCase()
      if (content.includes('security') || content.includes('test')) {
        has_security_or_test = true
      }
      if (content.includes('cache')) {
        has_cache = true
      }
      if (content.includes('archiveartifacts')) {
        has_artifacts = true
      }
      if (content.includes('stage')) {
        has_stages = true
      }
      if (content.includes('parallel')) {
        has_parallel = true
      }
    } catch (e) {
      console.error(`⚠️ [Jenkins] Error reading ${ciFilePath}:`, e)
    }
  }

  const has_jenkins_ci = fs.existsSync(ciFilePath)

  let pipeline_efficiency: 'BASIC' | 'OPTIMIZED' | 'HIGHLY_OPTIMIZED' = 'BASIC'
  if (has_jenkins_ci) {
    pipeline_efficiency = 'OPTIMIZED'
    if (has_cache && has_artifacts && has_stages && has_parallel) {
      pipeline_efficiency = 'HIGHLY_OPTIMIZED'
    }
  }

  const security_scan = (content.includes('security') || has_jenkins_ci) ? 'PASSED' : 'SKIPPED'

  return {
    pipeline_efficiency,
    security_scan,
    has_cache,
    has_artifacts,
    has_stages,
    has_parallel
  }
}

export async function checkJenkinsHealth() {
  const status = await getJenkinsStatus()
  return {
    status: status.pipeline_efficiency !== 'BASIC' ? 'optimal' : 'disconnected',
    metrics: status,
    timestamp: new Date().toISOString()
  }
}
