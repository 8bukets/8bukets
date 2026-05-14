import { jules } from '../antigravity/jules'
import { workOrderService } from '../antigravity/services/work_order'
import fs from 'fs'
import path from 'path'

/**
 * FULL AUTONOMOUS CREATION ORDER AND EXECUTION
 * This script triggers the complete autonomous lifecycle:
 * 1. Synthesis (Gap Analysis)
 * 2. Creation Orders (Work Order Generation)
 * 3. Execution (Bootstrap -> Smoke Test -> Deployment)
 */

async function main() {
  console.log('🚀 [Antigravity] Starting Full Autonomous Creation & Execution Cycle...')

  // Clear existing pending orders to ensure a clean run for this demo
  const storagePath = path.join(process.cwd(), 'data/work_orders.json')
  if (fs.existsSync(storagePath)) {
    const data = JSON.parse(fs.readFileSync(storagePath, 'utf8'))
    const filtered = data.filter((o: any) => o.status !== 'pending')
    fs.writeFileSync(storagePath, JSON.stringify(filtered, null, 2))
    console.log('🧹 [Antigravity] Cleared existing pending orders.')
  }

  // Execute the work cycle
  await jules.executeWorkCycle()

  console.log('\n📊 [Antigravity] Cycle Summary:')
  if (!fs.existsSync(storagePath)) {
    console.log(' - No work orders were created during this cycle.')
    return
  }
  const finalOrders = JSON.parse(fs.readFileSync(storagePath, 'utf8'))
  const recentOrders = finalOrders.slice(-5)

  recentOrders.forEach((o: any) => {
    console.log(` - [${o.status.toUpperCase()}] ${o.type}: ${o.goal}`)
  })

  console.log('\n✅ [Antigravity] Autonomous Creation Cycle Complete.')
}

main().catch(err => {
  console.error('💥 [Antigravity] Cycle failed:', err)
  process.exit(1)
})
