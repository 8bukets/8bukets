import { healthCheck } from '../antigravity/core'
import { isDockerHealthy } from '../antigravity/services/docker'
import { workOrderService } from '../antigravity/services/work_order'
import fs from 'fs'
import path from 'path'

/**
 * FULL AUTONOMOUS AUTOMATIC CREATION ORDER AND EXECUTION (IMPROVED)
 *
 * This script unifies the entire Antigravity lifecycle:
 * 1. Pre-flight Health Checks (DB, Cloud, Docker)
 * 2. State Purge (Clean existing pending orders)
 * 3. Root Order Generation (AUTONOMOUS_CREATION)
 * 4. Recursive Execution Pulse (Synthesis -> Bootstrap -> Smoke Test -> Deployment)
 * 5. Detailed Final Reporting
 */

async function main() {
  // full autonomus automatic workflow creation
  'use cache'
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
  await workOrderService.clearPendingOrders()

  // Step 3: Root Order Generation
  console.log('📝 [Antigravity] Generating root AUTONOMOUS_CREATION order...')
  const rootOrder = await workOrderService.createOrder(
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
  // create agent Chief AI Officer
  console.log('\n📊 [Antigravity] Final Execution Report:')
  const storagePath = path.join(process.cwd(), 'data/work_orders.json')
  if (await fs.promises.access(storagePath).then(() => true).catch(() => false)) {
    const allOrders = JSON.parse(await fs.promises.readFile(storagePath, 'utf8'))

    // Improved linkage: Find all orders that transitively depend on the root order
    const sessionOrderIds = new Set<string>([rootOrder.id])
    let expanded = true
    while (expanded) {
      expanded = false
      for (const order of allOrders) {
        if (!sessionOrderIds.has(order.id) && order.dependsOn?.some((depId: string) => sessionOrderIds.has(depId))) {
          sessionOrderIds.add(order.id)
          expanded = true
        }
      }
    }

    const sessionOrders = allOrders.filter((o: any) => sessionOrderIds.has(o.id))

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
