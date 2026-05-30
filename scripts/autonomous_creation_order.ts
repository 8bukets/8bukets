import { workOrderService } from '../antigravity/services/work_order'
import { logAutonomousAction } from '../antigravity/core'

/**
 * FULL AUTONOMOUS CREATION ORDER SCRIPT
 * Triggers the complete autonomous cycle: Synthesis -> Work Order -> Execution.
 * Ensures a clean state by clearing pending orders before ignition.
 */

async function main() {
  console.log('🚀 [Antigravity] Starting Full Autonomous Creation Order...')
  logAutonomousAction('🚀 [Antigravity] Starting Full Autonomous Creation Order...', 'info')

  // Clear existing pending orders to ensure a clean run
  console.log('🧹 [Antigravity] Clearing existing pending orders...')
  await workOrderService.clearPendingOrders()

  // Create the root autonomous creation order
  console.log('📝 [Antigravity] Creating ignition order...')
  const igniteOrder = await workOrderService.createOrder(
    'AUTONOMOUS_CREATION',
    'Execute full autonomous creation cycle (Synthesis -> Bootstrap -> Smoke Test -> Deployment)',
    {
      source: 'autonomous_creation_order',
      timestamp: new Date().toISOString()
    }
  )

  console.log(`✅ [Antigravity] Created ignition order: ${igniteOrder.id}`)
  console.log('⚡ [Antigravity] Executing pending orders...')

  // Execute the orders
  await workOrderService.executePendingOrders()

  console.log('\n🏁 [Antigravity] Full autonomous ignition cycle finished.')
  logAutonomousAction('🏁 [Antigravity] Full autonomous ignition cycle finished.', 'info')
}

main().catch(err => {
  console.error('💥 [Antigravity] Ignition failed:', err)
  process.exit(1)
})
