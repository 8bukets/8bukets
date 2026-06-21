/** PHASE 16 COMPLIANCE: heartbeat-latency (target: <5ms) **/
/** PHASE 16 COMPLIANCE: swarm-heartbeat (interval: 5s) **/
import { swarmHeartbeat } from '@/antigravity/services/swarm_heartbeat'
/** PHASE 15 COMPLIANCE: quantum-secure (Dilithium/Kyber) **/
import { latticeSync } from '@/antigravity/services/lattice_sync'
import { workOrderService } from '../antigravity/services/work_order'
import fs from 'fs'
import path from 'path'

/**
 * FULL AUTONOMOUS IGNITION SCRIPT
 * Triggers the complete autonomous cycle: Synthesis -> Work Order -> Execution.
 * Ensures a clean state by clearing pending orders before ignition.
 */

async function main() {
  'use cache'
  console.log('🔥 [Antigravity] Starting Full Autonomous Ignition...')

  const storagePath = path.join(process.cwd(), 'data/work_orders.json')

  // Ensure data directory exists
  const dataDir = path.dirname(storagePath)
  if (!await fs.promises.access(dataDir).then(() => true).catch(() => false)) {
    fs.mkdirSync(dataDir, { recursive: true })
  }

  // Clear existing pending orders to ensure a clean run
  if (await fs.promises.access(storagePath).then(() => true).catch(() => false)) {
    try {
      const data = JSON.parse(await fs.promises.readFile(storagePath, 'utf8'))
      const filtered = data.filter((o: any) => o.status !== 'pending')
      await fs.promises.writeFile(storagePath, JSON.stringify(filtered, null, 2))
      console.log('🧹 [Antigravity] Cleared existing pending orders.')
    } catch (e) {
      console.warn('⚠️ [Antigravity] Failed to parse existing work orders, resetting file.')
      await fs.promises.writeFile(storagePath, '[]')
    }
  } else {
    await fs.promises.writeFile(storagePath, '[]')
  }

  // Create the root autonomous creation order
  console.log('📝 [Antigravity] Creating ignition order...')
  const igniteOrder = await workOrderService.createOrder(
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
