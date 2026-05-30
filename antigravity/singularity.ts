import { logAutonomousAction } from './core'
import fs from 'fs'
import path from 'path'

/**
 * ANTIGRAVITY SINGULARITY ENGINE
 * Autonomously scaffolds and generates new services based on synthesis.
 */

export async function bootstrap(idea: { feature: string, rationale: string }) {
  logAutonomousAction(`🌀 [Singularity] Bootstrapping: ${idea.feature}...`, 'info')

  const serviceName = idea.feature.toLowerCase().replace(/\s+/g, '_').replace(/_service$/, '')
  const filePath = path.join(process.cwd(), 'antigravity/services', `${serviceName}.ts`)

  const exists = await fs.promises.stat(filePath).then(() => true).catch(() => false)
  if (exists) {
    logAutonomousAction(` - Service ${serviceName} already exists. Skipping bootstrap.`, 'info')
    return
  }

  const identifier = idea.feature.replace(/[^a-zA-Z0-9]/g, '')
  const template = `/**
 * ${idea.feature}
 * Generated autonomously by the Antigravity Singularity Engine.
 * Rationale: ${idea.rationale}
 */
import { z } from 'zod'
import { autonomousFetch } from '../core'

export const ${identifier}Schema = z.object({
  status: z.string(),
  lastRun: z.string()
})

export async function get${identifier}Data() {
  return autonomousFetch(${identifier}Schema, async () => {
    return {
      status: 'active',
      lastRun: new Date().toISOString()
    }
  }, { life: 'minutes' })
}
`

  await fs.promises.writeFile(filePath, template)
  logAutonomousAction(`✅ [Singularity] Successfully generated ${serviceName}.ts`, 'info')

  // Generate Test File
  const testPath = path.join(process.cwd(), 'antigravity/services', `${serviceName}.test.ts`)
  const testExists = await fs.promises.stat(testPath).then(() => true).catch(() => false)
  if (!testExists) {
    const testTemplate = `/**
 * ${idea.feature} Test
 * Generated autonomously by the Antigravity Singularity Engine.
 */
import { describe, it, expect } from 'vitest'
import * as service from './${serviceName}'

describe('${idea.feature}', () => {
  it('should have a functional data fetcher', async () => {
    const data = await service.get${identifier}Data()
    expect(data.status).toBe('active')
    expect(data.lastRun).toBeDefined()
  })
})
`
    await fs.promises.writeFile(testPath, testTemplate)
    logAutonomousAction(`🧪 [Singularity] Successfully generated ${serviceName}.test.ts`, 'info')
  }

  // Scaffolding CI/CD Configurations
  // GitHub Actions Workflow
  const githubActionsDir = path.join(process.cwd(), '.github/workflows')
  const githubDirExists = await fs.promises.stat(githubActionsDir).then(() => true).catch(() => false)
  if (githubDirExists) {
    const githubWorkflowPath = path.join(githubActionsDir, `test_${serviceName}.yml`)
    const workflowExists = await fs.promises.stat(githubWorkflowPath).then(() => true).catch(() => false)
    if (!workflowExists) {
      const githubWorkflowTemplate = `name: Test ${serviceName}

on:
  push:
    paths:
      - 'antigravity/services/${serviceName}.ts'
      - 'antigravity/services/${serviceName}.test.ts'
  pull_request:
    paths:
      - 'antigravity/services/${serviceName}.ts'
      - 'antigravity/services/${serviceName}.test.ts'

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - name: Install Dependencies
        run: npm ci
      - name: Run Tests
        run: npx vitest run antigravity/services/${serviceName}.test.ts
`
      await fs.promises.writeFile(githubWorkflowPath, githubWorkflowTemplate)
      logAutonomousAction(`🤖 [Singularity] Generated GitHub Actions workflow for ${serviceName}`, 'info')
    }
  }

  // GitLab CI Appending
  const gitlabCiPath = path.join(process.cwd(), '.gitlab-ci.yml')
  const gitlabExists = await fs.promises.stat(gitlabCiPath).then(() => true).catch(() => false)
  if (gitlabExists) {
    let gitlabCiContent = await fs.promises.readFile(gitlabCiPath, 'utf8')
    const gitlabJobName = `test-${serviceName}`
    if (!gitlabCiContent.includes(gitlabJobName + ':')) {
      const gitlabJobTemplate = `\n${gitlabJobName}:
  stage: test
  script:
    - npm ci
    - npx vitest run antigravity/services/${serviceName}.test.ts
`
      await fs.promises.appendFile(gitlabCiPath, gitlabJobTemplate)
      logAutonomousAction(`🦊 [Singularity] Appended test job for ${serviceName} to .gitlab-ci.yml`, 'info')
    }
  }

  // Jenkinsfile Appending
  const jenkinsfilePath = path.join(process.cwd(), 'Jenkinsfile')
  const jenkinsExists = await fs.promises.stat(jenkinsfilePath).then(() => true).catch(() => false)
  if (jenkinsExists) {
    let jenkinsfileContent = await fs.promises.readFile(jenkinsfilePath, 'utf8')
    const jenkinsStageName = `Test ${serviceName}`
    if (!jenkinsfileContent.includes(jenkinsStageName)) {
      const jenkinsStageTemplate = `        stage('${jenkinsStageName}') {
            steps {
                sh 'npm ci'
                sh 'npx vitest run antigravity/services/${serviceName}.test.ts'
            }
        }\n`

      const insertIndex = jenkinsfileContent.indexOf("        stage('Creative Workflow') {")
      if (insertIndex !== -1) {
        jenkinsfileContent = jenkinsfileContent.slice(0, insertIndex) + jenkinsStageTemplate + "\n" + jenkinsfileContent.slice(insertIndex)
        await fs.promises.writeFile(jenkinsfilePath, jenkinsfileContent)
        logAutonomousAction(`👔 [Singularity] Injected test stage for ${serviceName} into Jenkinsfile`, 'info')
      }
    }
  }

  return { filePath, testPath, serviceName, feature: idea.feature }
}
