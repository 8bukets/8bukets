import fs from 'fs'
import path from 'path'

/**
 * ANTIGRAVITY SINGULARITY ENGINE
 * Autonomously scaffolds and generates new services based on synthesis.
 */

export async function bootstrap(idea: { feature: string, rationale: string }) {
  console.log(`🌀 [Singularity] Bootstrapping: ${idea.feature}...`)
  
  const serviceName = idea.feature.toLowerCase().replace(/[()]/g, '').replace(/\s+/g, '_').replace(/_service$/, '')
  const filePath = path.join(process.cwd(), 'antigravity/services', `${serviceName}.ts`)

  const workflowPath = path.join(process.cwd(), 'antigravity/workflows', `${serviceName}_workflow.ts`)
  const githubActionPath = path.join(process.cwd(), '.github/workflows', `autonomous_${serviceName}.yml`)

  // Ensure directories exist
  const dirs = [
    path.join(process.cwd(), 'antigravity/services'),
    path.join(process.cwd(), 'antigravity/workflows'),
    path.join(process.cwd(), '.github/workflows')
  ]
  for (const dir of dirs) {
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true })
    }
  }

  if (fs.existsSync(filePath) || fs.existsSync(workflowPath) || fs.existsSync(githubActionPath)) {
    console.log(` - Service ${serviceName} artifacts already exist. Skipping bootstrap to prevent overwriting existing logic.`)
    return
  }

  const template = `/**
 * ${idea.feature}
 * Generated autonomously by the Antigravity Singularity Engine.
 * Rationale: ${idea.rationale}
 */
import { z } from 'zod'
import { autonomousFetch } from '@/antigravity/core'

export const ${idea.feature.replace(/[()]/g, '').replace(/\s+/g, '')}Schema = z.object({
  status: z.string(),
  lastRun: z.string()
})

export async function get${idea.feature.replace(/[()]/g, '').replace(/\s+/g, '')}Data() {
  'use cache'
  return autonomousFetch(${idea.feature.replace(/[()]/g, '').replace(/\s+/g, '')}Schema, async () => {
    return {
      status: 'active',
      lastRun: new Date().toISOString()
    }
  }, { life: 'minutes' })
}
`

  fs.writeFileSync(filePath, template)
  console.log(`✅ [Singularity] Successfully generated ${serviceName}.ts`)

  const workflowTemplate = `/**
 * ${idea.feature} Autonomous Workflow
 * Generated autonomously by the Antigravity Singularity Engine.
 */
import { get${idea.feature.replace(/[()]/g, '').replace(/\s+/g, '')}Data } from '../services/${serviceName}'

async function run() {
  console.log('🤖 [Workflow] Starting autonomous cycle for ${idea.feature}...')
  const data = await get${idea.feature.replace(/[()]/g, '').replace(/\s+/g, '')}Data()
  console.log('✅ [Workflow] Data fetched:', data)
}

run().catch(console.error)
`

  fs.writeFileSync(workflowPath, workflowTemplate)
  console.log(`✅ [Singularity] Successfully generated ${serviceName}_workflow.ts`)

  const githubActionTemplate = `name: Autonomous ${idea.feature} Workflow

on:
  schedule:
    - cron: '0 * * * *' # Hourly
  workflow_dispatch:

jobs:
  run-workflow:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'
      - run: npm ci
      - run: npx tsx antigravity/workflows/${serviceName}_workflow.ts
        env:
          MONGODB_URI: \${{ secrets.MONGODB_URI }}
          NEXT_PUBLIC_SUPABASE_URL: \${{ secrets.NEXT_PUBLIC_SUPABASE_URL }}
          NEXT_PUBLIC_SUPABASE_ANON_KEY: \${{ secrets.NEXT_PUBLIC_SUPABASE_ANON_KEY }}
`

  fs.writeFileSync(githubActionPath, githubActionTemplate)
  console.log(`✅ [Singularity] Successfully generated autonomous_${serviceName}.yml`)

  // Generate GitLab CI entry
  const gitlabPath = path.join(process.cwd(), '.gitlab-ci.yml')
  if (fs.existsSync(gitlabPath)) {
    const gitlabContent = fs.readFileSync(gitlabPath, 'utf8')
    const gitlabJob = `
run-autonomous-${serviceName}:
  stage: test
  script:
    - echo "Running autonomous cycle for ${idea.feature}"
    - npx tsx antigravity/workflows/${serviceName}_workflow.ts
  rules:
    - if: $CI_PIPELINE_SOURCE == "schedule"
`
    if (!gitlabContent.includes(`run-autonomous-${serviceName}:`)) {
      fs.appendFileSync(gitlabPath, gitlabJob)
      console.log(`✅ [Singularity] Successfully updated .gitlab-ci.yml with ${serviceName} job`)
    }
  }

  // Generate Jenkins pipeline entry
  const jenkinsPath = path.join(process.cwd(), 'Jenkinsfile')
  if (fs.existsSync(jenkinsPath)) {
    let jenkinsContent = fs.readFileSync(jenkinsPath, 'utf8')
    const jenkinsStage = `        stage('Run Autonomous ${idea.feature}') {
            steps {
                sh 'npx tsx antigravity/workflows/${serviceName}_workflow.ts'
            }
        }\n`
    if (!jenkinsContent.includes(`stage('Run Autonomous ${idea.feature}')`)) {
      jenkinsContent = jenkinsContent.replace(/        stage\('Creative Workflow'\) \{/g, jenkinsStage + "        stage('Creative Workflow') {")
      fs.writeFileSync(jenkinsPath, jenkinsContent)
      console.log(`✅ [Singularity] Successfully updated Jenkinsfile with ${serviceName} stage`)
    }
  }

  return { filePath, workflowPath, githubActionPath, serviceName, feature: idea.feature }
}
