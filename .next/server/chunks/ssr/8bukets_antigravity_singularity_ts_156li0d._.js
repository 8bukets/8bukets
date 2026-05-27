module.exports=[48491,a=>{"use strict";var b=a.i(22734),c=a.i(14747);async function d(a){console.log(`🌀 [Singularity] Bootstrapping: ${a.feature}...`);let d=a.feature.toLowerCase().replace(/[^a-z0-9]+/g,"_").replace(/_service$/,""),e=c.default.join(process.cwd(),"antigravity/services",`${d}.ts`),f=c.default.join(process.cwd(),"antigravity/workflows",`${d}_workflow.ts`),g=c.default.join(process.cwd(),".github/workflows",`autonomous_${d}.yml`);for(let a of[c.default.join(process.cwd(),"antigravity/services"),c.default.join(process.cwd(),"antigravity/workflows"),c.default.join(process.cwd(),".github/workflows")])try{await b.default.promises.access(a)}catch{await b.default.promises.mkdir(a,{recursive:!0})}let h=!1;try{await b.default.promises.access(e),h=!0}catch{}try{await b.default.promises.access(f),h=!0}catch{}try{await b.default.promises.access(g),h=!0}catch{}if(h)return void console.log(` - Service ${d} artifacts already exist. Skipping bootstrap to prevent overwriting existing logic.`);let i=`/**
 * ${a.feature}
 * Generated autonomously by the Antigravity Singularity Engine.
 * Rationale: ${a.rationale}
 */
import { z } from 'zod'
import { autonomousFetch } from '@/antigravity/core'

export const ${a.feature.replace(/[^a-zA-Z0-9]+/g,"")}Schema = z.object({
  status: z.string(),
  lastRun: z.string()
})

export async function get${a.feature.replace(/[^a-zA-Z0-9]+/g,"")}Data() {
  'use cache'
  return autonomousFetch(${a.feature.replace(/[^a-zA-Z0-9]+/g,"")}Schema, async () => {
    return {
      status: 'active',
      lastRun: new Date().toISOString()
    }
  })
}
`;await b.default.promises.writeFile(e,i),console.log(`✅ [Singularity] Successfully generated ${d}.ts`);let j=`/**
 * ${a.feature} Autonomous Workflow
 * Generated autonomously by the Antigravity Singularity Engine.
 */
import { get${a.feature.replace(/[^a-zA-Z0-9]+/g,"")}Data } from '../services/${d}'

async function run() {
  console.log('🤖 [Workflow] Starting autonomous cycle for ${a.feature}...')
  const data = await get${a.feature.replace(/[^a-zA-Z0-9]+/g,"")}Data()
  console.log('✅ [Workflow] Data fetched:', data)
}

run().catch(console.error)
`;await b.default.promises.writeFile(f,j),console.log(`✅ [Singularity] Successfully generated ${d}_workflow.ts`);let k=`name: Autonomous ${a.feature} Workflow

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
      - run: npx tsx antigravity/workflows/${d}_workflow.ts
        env:
          MONGODB_URI: \${{ secrets.MONGODB_URI }}
          NEXT_PUBLIC_SUPABASE_URL: \${{ secrets.NEXT_PUBLIC_SUPABASE_URL }}
          NEXT_PUBLIC_SUPABASE_ANON_KEY: \${{ secrets.NEXT_PUBLIC_SUPABASE_ANON_KEY }}
`;await b.default.promises.writeFile(g,k),console.log(`✅ [Singularity] Successfully generated autonomous_${d}.yml`);let l=c.default.join(process.cwd(),".gitlab-ci.yml");try{await b.default.promises.access(l);let c=await b.default.promises.readFile(l,"utf8"),e=`
run-autonomous-${d}:
  stage: test
  script:
    - echo "Running autonomous cycle for ${a.feature}"
    - npx tsx antigravity/workflows/${d}_workflow.ts
  rules:
    - if: $CI_PIPELINE_SOURCE == "schedule"
`;c.includes(`run-autonomous-${d}:`)||(await b.default.promises.appendFile(l,e),console.log(`✅ [Singularity] Successfully updated .gitlab-ci.yml with ${d} job`))}catch{}let m=c.default.join(process.cwd(),"Jenkinsfile");try{await b.default.promises.access(m);let c=await b.default.promises.readFile(m,"utf8"),e=`        stage('Run Autonomous ${a.feature}') {
            steps {
                sh 'npx tsx antigravity/workflows/${d}_workflow.ts'
            }
        }
`;c.includes(`stage('Run Autonomous ${a.feature}')`)||(c=c.replace(/        stage\('Creative Workflow'\) \{/g,e+"        stage('Creative Workflow') {"),await b.default.promises.writeFile(m,c),console.log(`✅ [Singularity] Successfully updated Jenkinsfile with ${d} stage`))}catch{}return{filePath:e,workflowPath:f,githubActionPath:g,serviceName:d,feature:a.feature}}a.s(["bootstrap",0,d])}];

//# sourceMappingURL=8bukets_antigravity_singularity_ts_156li0d._.js.map