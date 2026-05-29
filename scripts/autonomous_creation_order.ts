import { workOrderService } from '../antigravity/services/work_order';
import { logAutonomousAction } from '../antigravity/core';

/**
 * FULL AUTONOMOUS AUTOMATIC CREATION ORDER AND EXECUTION
 * This script initiates the root creation order and triggers the full execution chain.
 */

async function main() {
  console.log('🔥 [Antigravity] Starting Full Autonomous Automatic Creation Order and Execution...');
  logAutonomousAction('🔥 [Antigravity] Starting Full Autonomous Automatic Creation Order and Execution...', 'info');

  // Clear existing pending orders to ensure a clean autonomous run via the service
  console.log('🧹 [Antigravity] Cleaning up stale pending orders...');
  await workOrderService.clearPendingOrders();

  // Create the root autonomous creation order
  console.log('📝 [Antigravity] Creating root AUTONOMOUS_CREATION order...');
  const creationOrder = await workOrderService.createOrder(
    'AUTONOMOUS_CREATION',
    'Full Autonomous Creation Cycle (Synthesis -> Scaffolding -> Testing -> Deployment)',
    {
      source: 'autonomous_creation_order_script',
      timestamp: new Date().toISOString()
    }
  );

  console.log(`✅ [Antigravity] Root order created: ${creationOrder.id}`);
  console.log('🚀 [Antigravity] Initiating recursive execution of the dependency chain...');

  // Execute the order - this will trigger the creationEngine.runCycle()
  // which will then generate and execute the sub-order chain.
  await workOrderService.executePendingOrders();

  console.log('\n🏁 [Antigravity] Full autonomous creation and execution cycle completed.');
}

main().catch(err => {
  console.error('💥 [Antigravity] Autonomous creation failed:', err);
  process.exit(1);
});
