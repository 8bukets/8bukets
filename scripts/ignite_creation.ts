import { workOrderService } from '../antigravity/services/work_order'

/**
 * IGNITE AUTONOMOUS CREATION
 * This script triggers the full autonomous creation cycle by generating
 * and executing an AUTONOMOUS_CREATION work order.
 */

async function main() {
  console.log('🔥 [Antigravity] Igniting Full Autonomous Creation Cycle...')

  // Create the root autonomous creation order
  const igniteOrder = workOrderService.createOrder(
    'AUTONOMOUS_CREATION',
    'Ignite full autonomous creation cycle (Synthesis -> Bootstrap -> Smoke Test -> Deployment)',
    {
      source: 'manual_ignition',
      timestamp: new Date().toISOString()
    }
  )

  console.log(`✅ [Antigravity] Created ignition order: ${igniteOrder.id}`)
  console.log('🚀 [Antigravity] Executing pending orders...')

  // Execute the orders
  await workOrderService.executePendingOrders()

  console.log('\n🏁 [Antigravity] Autonomous ignition cycle finished.')
}

main().catch(err => {
  console.error('💥 [Antigravity] Ignition failed:', err)
  process.exit(1)
})
