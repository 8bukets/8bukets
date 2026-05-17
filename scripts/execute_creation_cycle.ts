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

  // 3. Execution: Process all pending orders
  console.log('⚡ [CreationCycle] Executing generated work orders...');
  logAutonomousAction('⚡ [CreationCycle] Executing generated work orders...', 'info');
  await workOrderService.executePendingOrders();

  console.log('✅ [CreationCycle] Creation cycle complete.');
  logAutonomousAction('✅ [CreationCycle] Creation cycle complete.', 'info');
}

executeCreationCycle().catch(err => {
  console.error('💥 [CreationCycle] Fatal error:', err);
  process.exit(1);
});
