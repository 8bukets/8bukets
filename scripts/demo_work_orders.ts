import { workOrderService } from '../antigravity/services/work_order'

/**
 * DEMO: AUTONOMOUS CREATION ORDER AND EXECUTION
 * This script demonstrates the full lifecycle of a Work Order.
 */

async function demo() {
  console.log('🚀 [Demo] Initializing Work Order Lifecycle Demonstration...')

  // 1. Create a Content Generation order
  console.log('\n--- Step 1: Creating Autonomous Orders ---')
  workOrderService.createOrder(
    'CONTENT_GENERATION',
    'Generate Autonomous System Status Report',
    {
      title: 'Antigravity Autonomous Status',
      content: 'The system is operating at Phase 12 Super-Intelligence. All neural nodes are synchronized.',
      filename: 'CREATION_ORDER_REPORT.md'
    }
  )

  // 2. Create a Bootstrap order (Simulated Idea)
  workOrderService.createOrder(
    'BOOTSTRAP_SERVICE',
    'Bootstrap Task Orchestrator',
    {
      feature: 'Task Orchestrator Service',
      rationale: 'Formalizes the management of long-running autonomous processes.'
    }
  )

  // 3. Process the orders
  console.log('\n--- Step 2: Executing Orders ---')
  await workOrderService.executePendingOrders()

  console.log('\n✅ [Demo] Work Order Lifecycle Demonstration Complete.')
}

demo().catch(console.error)
