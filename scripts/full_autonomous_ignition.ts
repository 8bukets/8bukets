import { workOrderService } from '../antigravity/services/work_order'
import fs from 'fs'
import path from 'path'

/**
 * FULL AUTONOMOUS IGNITION SCRIPT
 * Triggers the complete autonomous cycle: Synthesis -> Work Order -> Execution.
 * Ensures a clean state by clearing pending orders before ignition.
 */

async function main() {
  console.log('🔥 [Antigravity] Starting Full Autonomous Ignition...')

  const storagePath = path.join(process.cwd(), 'data/work_orders.json')

  // Ensure data directory exists
  const dataDir = path.dirname(storagePath)
  if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir, { recursive: true })
  }

  // Clear existing pending orders to ensure a clean run
  if (fs.existsSync(storagePath)) {
    try {
      const data = JSON.parse(fs.readFileSync(storagePath, 'utf8'))
      const filtered = data.filter((o: any) => o.status !== 'pending')
      fs.writeFileSync(storagePath, JSON.stringify(filtered, null, 2))
      console.log('🧹 [Antigravity] Cleared existing pending orders.')
    } catch (e) {
      console.warn('⚠️ [Antigravity] Failed to parse existing work orders, resetting file.')
      fs.writeFileSync(storagePath, '[]')
    }
  } else {
    fs.writeFileSync(storagePath, '[]')
  }

  // Create the root autonomous creation order
  console.log('📝 [Antigravity] Creating ignition order...')
  const igniteOrder = workOrderService.createOrder(
    'AUTONOMOUS_CREATION',
    'Execute full autonomous creation cycle (Synthesis -> Bootstrap -> Smoke Test -> Deployment)',
    {
      source: 'full_autonomous_ignition',
      timestamp: new Date().toISOString()
    }
  )

  console.log(`✅ [Antigravity] Created ignition order: ${igniteOrder.id}`)
  console.log('🚀 [Antigravity] Executing pending orders...')

  // Execute the orders
  await workOrderService.executePendingOrders()

  console.log('\n🏁 [Antigravity] Full autonomous ignition cycle finished.')
}

main().catch(err => {
  console.error('💥 [Antigravity] Ignition failed:', err)
  process.exit(1)
})
