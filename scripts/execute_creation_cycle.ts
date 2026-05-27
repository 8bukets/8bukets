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

  // Ensure data directory exists
  const dataDir = path.join(process.cwd(), 'data')
  if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir, { recursive: true })
    console.log('📁 [Antigravity] Created data directory.')
  }

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

  // Explicitly confirm autonomous evolution and self-correction sequence
  console.log('🤖 [Antigravity] Autonomous evolution and self-correction phase initiated based on session intelligence.')

  console.log('\n📊 [Antigravity] Cycle Summary:')
  if (!fs.existsSync(storagePath)) {
    console.log(' - No work orders file found.')
    return
  }
  const finalOrders = JSON.parse(fs.readFileSync(storagePath, 'utf8'))

  if (finalOrders.length === 0) {
    console.log(' - No work orders recorded.')
  } else {
    finalOrders.forEach((o: any) => {
      const deps = o.dependsOn ? ` (depends on: ${o.dependsOn.join(', ')})` : ''
      console.log(` - [${o.status.toUpperCase()}] ID: ${o.id} | ${o.type}: ${o.goal}${deps}`)
      if (o.result) console.log(`   └─ Result: ${JSON.stringify(o.result)}`)
      if (o.error) console.log(`   └─ Error: ${o.error}`)
    })
  }

  console.log('\n✅ [Antigravity] Autonomous Creation Cycle Complete.')
}

main().catch(err => {
  console.error('💥 [Antigravity] Cycle failed:', err)
  process.exit(1)
})
