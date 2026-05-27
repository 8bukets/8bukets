import { workOrderService } from '../antigravity/services/work_order';
import { logAutonomousAction } from '../antigravity/core';

async function igniteCreation() {
  console.log('🔥 [Ignite] Igniting Full Autonomous Creation Cycle...');
  logAutonomousAction('🔥 [Ignite] Igniting Full Autonomous Creation Cycle...', 'info');

  // Ensure a clean state for the demonstration
  await workOrderService.clearOrders();

  // Create the top-level creation order
  const creationOrder = await workOrderService.createOrder(
    'AUTONOMOUS_CREATION',
    'Execute Full Autonomous Creation Cycle',
    { trigger: 'ignite_script', timestamp: new Date().toISOString() }
  );

  console.log(`✅ [Ignite] Creation order generated: ${creationOrder.id}`);
  console.log('⚡ [Ignite] Triggering immediate execution...');

  // Process the order (this will trigger synthesis and follow-up chains)
  await workOrderService.executePendingOrders();

  console.log('🚀 [Ignite] Autonomous Creation Cycle execution initiated.');
}

igniteCreation().catch(err => {
  console.error('💥 [Ignite] Fatal error during ignition:', err);
  process.exit(1);
});
