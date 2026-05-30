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

export async function triggerJenkinsPipeline(jobName: string, params?: Record<string, string>): Promise<boolean> {
  const jenkinsUrl = process.env.JENKINS_URL
  const jenkinsUser = process.env.JENKINS_USER
  const jenkinsToken = process.env.JENKINS_TOKEN

  if (!jenkinsUrl || !jenkinsUser || !jenkinsToken) {
    console.log(`⚠️ [Jenkins] Skipping pipeline trigger for ${jobName}. Jenkins configuration missing in environment.`)
    return false
  }

  try {
    console.log(`🚀 [Jenkins] Triggering Jenkins pipeline: ${jobName}`)
    const auth = Buffer.from(`${jenkinsUser}:${jenkinsToken}`).toString('base64')

    let url = `${jenkinsUrl}/job/${jobName}/build`
    if (params && Object.keys(params).length > 0) {
      url = `${jenkinsUrl}/job/${jobName}/buildWithParameters`
      const queryParams = new URLSearchParams(params).toString()
      url += `?${queryParams}`
    }

    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Authorization': `Basic ${auth}`
      }
    })

    if (!response.ok) {
      console.error(`❌ [Jenkins] Failed to trigger pipeline ${jobName}. Status: ${response.status} ${response.statusText}`)
      return false
    }

    console.log(`✅ [Jenkins] Successfully triggered Jenkins pipeline: ${jobName}`)
    return true
  } catch (error) {
    console.error(`❌ [Jenkins] Error triggering pipeline ${jobName}:`, error)
    return false
  }
}
