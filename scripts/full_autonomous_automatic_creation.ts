import { healthCheck } from '../antigravity/core'
import { isDockerHealthy } from '../antigravity/services/docker'
import { workOrderService } from '../antigravity/services/work_order'
import fs from 'fs'
import path from 'path'

/**
 * FULL AUTONOMOUS AUTOMATIC CREATION ORDER AND EXECUTION
 *
 * This script unifies the entire Antigravity lifecycle:
 * 1. Pre-flight Health Checks (DB, Cloud, Docker)
 * 2. State Purge (Clean existing pending orders)
 * 3. Root Order Generation (AUTONOMOUS_CREATION)
 * 4. Recursive Execution Pulse (Synthesis -> Bootstrap -> Smoke Test -> Deployment)
 * 5. Detailed Final Reporting
 */

async function main() {
  console.log('🚀 [Antigravity] Starting Full Autonomous Automatic Creation Pulse...')

  // Step 1: Pre-flight Health Checks
  console.log('🔍 [Antigravity] Performing pre-flight health checks...')
  const coreHealth = await healthCheck()
  const dockerHealthy = await isDockerHealthy()

  console.log(` - MongoDB: ${coreHealth.mongodb}`)
  console.log(` - Supabase: ${coreHealth.supabase}`)
  console.log(` - Docker: ${dockerHealthy ? 'healthy' : 'unreachable'}`)

  if (coreHealth.mongodb === 'error' && process.env.NODE_ENV === 'production') {
    console.error('❌ [Antigravity] Critical: MongoDB is down. Aborting autonomous creation.')
    process.exit(1)
  }

  // Step 2: State Purge
  console.log('🧹 [Antigravity] Purging stale pending orders...')
  workOrderService.clearPendingOrders()

  // Step 3: Root Order Generation
  console.log('📝 [Antigravity] Generating root AUTONOMOUS_CREATION order...')
  const rootOrder = workOrderService.createOrder(
    'AUTONOMOUS_CREATION',
    'Execute full autonomous creation cycle (Synthesis -> Bootstrap -> Smoke Test -> Deployment)',
    {
      source: 'full_autonomous_automatic_creation',
      timestamp: new Date().toISOString(),
      environment: process.env.NODE_ENV || 'development'
    }
  )
  console.log(`✅ [Antigravity] Root order created: ${rootOrder.id}`)

  // Step 4: Recursive Execution Pulse
  console.log('⚡ [Antigravity] Beginning recursive execution pulse...')
  await workOrderService.executePendingOrders()

  // Step 5: Detailed Final Reporting
  console.log('\n📊 [Antigravity] Final Execution Report:')
  const storagePath = path.join(process.cwd(), 'data/work_orders.json')
  if (fs.existsSync(storagePath)) {
    const allOrders = JSON.parse(fs.readFileSync(storagePath, 'utf8'))
    const sessionOrders = allOrders.filter((o: any) =>
        o.id === rootOrder.id || (o.dependsOn && o.dependsOn.includes(rootOrder.id)) ||
        allOrders.some((parent: any) => o.dependsOn && o.dependsOn.includes(parent.id) && parent.created_at >= rootOrder.created_at)
    )

    if (sessionOrders.length === 0) {
      console.log(' - No orders were executed in this pulse.')
    } else {
      sessionOrders.forEach((o: any) => {
        const statusIcon = o.status === 'completed' ? '✅' : o.status === 'failed' ? '❌' : '⏳'
        console.log(` ${statusIcon} [${o.status.toUpperCase()}] ${o.type}: ${o.goal} (${o.id})`)
        if (o.error) console.log(`    └─ Error: ${o.error}`)
      })
    }
  } else {
    console.log('⚠️ [Antigravity] No work orders file found for reporting.')
  }

  console.log('\n🏁 [Antigravity] Full autonomous creation pulse completed.')
}

main().catch(err => {
  console.error('💥 [Antigravity] Autonomous pulse failed:', err)
  process.exit(1)
})
