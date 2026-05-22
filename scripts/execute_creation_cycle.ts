import { synthesize } from '../antigravity/synthesis';
import { workOrderService } from '../antigravity/services/work_order';
import { logAutonomousAction } from '../antigravity/core';

async function executeCreationCycle() {
  console.log('🚀 [CreationCycle] Starting Autonomous Creation Cycle...');
  logAutonomousAction('🚀 [CreationCycle] Starting Autonomous Creation Cycle...', 'info');

  // 1. Synthesis: Gap Analysis & Idea Generation
  const ideas = await synthesize();
  console.log(`🔮 [CreationCycle] Synthesized ${ideas.length} new ideas.`);
  logAutonomousAction(`🔮 [CreationCycle] Synthesized ${ideas.length} new ideas.`, 'info');

  if (ideas.length === 0) {
    console.log('✨ [CreationCycle] No new gaps identified. System state is optimal.');
    logAutonomousAction('✨ [CreationCycle] No new gaps identified. System state is optimal.', 'info');
    return;
  }

  // 2. Order Generation: Bootstrap & Smoke Test
  for (const idea of ideas) {
    // Only process Low/Medium complexity for now to ensure safe autonomous evolution
    if (idea.complexity === 'Low' || idea.complexity === 'Medium') {
      console.log(`📝 [CreationCycle] Generating orders for: ${idea.feature}`);
      logAutonomousAction(`📝 [CreationCycle] Generating orders for: ${idea.feature}`, 'info');

      // Create Bootstrap Order
      const bootstrapOrder = await workOrderService.createOrder(
        'BOOTSTRAP_SERVICE',
        `Bootstrap ${idea.feature}`,
        idea
      );

      // Create Smoke Test Order (to be executed after bootstrap)
      await workOrderService.createOrder(
        'SMOKE_TEST',
        `Verify ${idea.feature} integrity`,
        { serviceName: idea.feature.toLowerCase().replace(/\s+/g, '_').replace(/_service$/, '') }
      );
    }
  }

  // 3. Execution: Process all pending orders with Chain Logic
  console.log('⚡ [CreationCycle] Executing generated work orders...');
  logAutonomousAction('⚡ [CreationCycle] Executing generated work orders...', 'info');

  const pending = await workOrderService.getPendingOrders();

  for (const order of pending) {
    // Only process orders we just created or related ones
    await workOrderService.updateOrderStatus(order.id, 'executing');
    try {
      // @ts-ignore - Accessing private for orchestration logic in this script
      const result = await workOrderService.dispatch(order);

      if (result?.skipped) {
        console.log(`ℹ️ [CreationCycle] Order ${order.id} (${order.type}) skipped by TypeScript engine. Reverting to pending for external processing.`);
        await workOrderService.updateOrderStatus(order.id, 'pending');
        continue;
      }

      await workOrderService.updateOrderStatus(order.id, 'completed', result);
      logAutonomousAction(`[WORK_ORDER] Completed: ${order.id}`, 'cognitive');

      // CHAIN LOGIC: If a Smoke Test passes, trigger Deployment
      if (order.type === 'SMOKE_TEST' && result?.status === 'passed') {
        const featureName = order.payload?.serviceName;
        console.log(`🚀 [CreationCycle] Smoke test passed for ${featureName}. Triggering deployment...`);
        logAutonomousAction(`🚀 [CreationCycle] Smoke test passed for ${featureName}. Triggering deployment...`, 'info');

        const deployOrder = await workOrderService.createOrder(
          'DEPLOYMENT',
          `Deploy ${featureName} to production`,
          { serviceName: featureName }
        );

        await workOrderService.updateOrderStatus(deployOrder.id, 'executing');
        // @ts-ignore
        const deployResult = await workOrderService.dispatch(deployOrder);
        await workOrderService.updateOrderStatus(deployOrder.id, 'completed', deployResult);
        logAutonomousAction(`[WORK_ORDER] Completed Deployment: ${deployOrder.id}`, 'cognitive');
      }
    } catch (err: any) {
      console.error(`❌ [WorkOrder] Order ${order.id} failed:`, err);
      await workOrderService.updateOrderStatus(order.id, 'failed', undefined, err.message);
      logAutonomousAction(`[WORK_ORDER] Failed: ${order.id}`, 'error');
    }
  }

  console.log('✅ [CreationCycle] Creation cycle complete.');
  logAutonomousAction('✅ [CreationCycle] Creation cycle complete.', 'info');
}

executeCreationCycle().catch(err => {
  console.error('💥 [CreationCycle] Fatal error:', err);
  process.exit(1);
});
