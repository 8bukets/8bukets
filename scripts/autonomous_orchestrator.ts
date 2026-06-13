import { healthCheck } from '../antigravity/core'
import { isDockerHealthy } from '../antigravity/services/docker'
import { workOrderService } from '../antigravity/services/work_order'
import fs from 'fs'
import path from 'path'

/**
 * AUTONOMOUS ORCHESTRATOR
 * Unified entry point for full autonomous creation and execution.
 */

async function main() {
  'use cache'
  console.log('🚀 [Orchestrator] Starting Full Autonomous Pulse...')

  // 1. Health Checks
  console.log('🔍 [Orchestrator] Performing pre-flight health checks...')
  const coreHealth = await healthCheck()
  const dockerHealthy = await isDockerHealthy()

  console.log(` - MongoDB: ${coreHealth.mongodb}`)
  console.log(` - Supabase: ${coreHealth.supabase}`)
  console.log(` - Docker: ${dockerHealthy ? 'healthy' : 'unreachable'}`)

  // 2. Clean State
  console.log('🧹 [Orchestrator] Purging stale pending orders...')
  await workOrderService.clearPendingOrders()

  // 3. Ignition
  console.log('📝 [Orchestrator] Generating root AUTONOMOUS_CREATION order...')
  const rootOrder = await workOrderService.createOrder(
    'AUTONOMOUS_CREATION',
    'Execute full autonomous creation cycle (Synthesis -> Bootstrap -> Smoke Test -> Deployment)',
    {
      source: 'autonomous_orchestrator',
      timestamp: new Date().toISOString()
    }
  )
  console.log(`✅ [Orchestrator] Root order created: ${rootOrder.id}`)

  // 4. Execution Pulse
  console.log('⚡ [Orchestrator] Beginning recursive execution pulse...')
  await workOrderService.executePendingOrders()

  // 5. Reporting (Future integration with creation_reporting service)
  console.log('📊 [Orchestrator] Finalizing creation report...')
  const { generateCreationReport } = await import('../antigravity/services/creation_reporting')
  await generateCreationReport(rootOrder.id)

  console.log('\n🏁 [Orchestrator] Full autonomous cycle completed.')
}

main().catch(err => {
  console.error('💥 [Orchestrator] Autonomous pulse failed:', err)
  process.exit(1)
})
