import { workOrderService } from '../antigravity/services/work_order';

/**
 * AUTONOMOUS CREATION ORDER AND EXECUTION
 *
 * This script initializes the full autonomous lifecycle by:
 * 1. Purging all existing pending work orders for a clean state.
 * 2. Creating a root AUTONOMOUS_CREATION work order.
 * 3. Executing all pending orders (including those generated mid-cycle).
 */

async function main() {
  console.log('🚀 [Antigravity] Initializing Autonomous Creation Order...');

  // Step 1: Clear existing pending orders
  workOrderService.clearPendingOrders();
  console.log('🧹 [Antigravity] Pending orders cleared.');

  // Step 2: Create the root creation order
  const rootOrder = await workOrderService.createOrder(
    'AUTONOMOUS_CREATION',
    'Execute full autonomous creation cycle (Synthesis -> Bootstrap -> Smoke Test -> Deployment)',
    {
      source: 'autonomous_creation_script',
      timestamp: new Date().toISOString()
    }
  );

  console.log(`📝 [Antigravity] Created root order: ${rootOrder.id}`);

  // Step 3: Execute the cycle
  console.log('⚡ [Antigravity] Beginning execution pulse...');
  await workOrderService.executePendingOrders();

  console.log('✅ [Antigravity] Autonomous creation order sequence completed.');
}

main().catch(err => {
  console.error('💥 [Antigravity] Autonomous creation failed:', err);
  process.exit(1);
});
