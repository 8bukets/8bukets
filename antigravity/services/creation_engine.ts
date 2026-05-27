import { synthesize } from '../synthesis';
import { workOrderService } from './work_order';
import { logAutonomousAction } from '../core';
import { sentientOrchestration } from './sentient_orchestration';

/**
 * ANTIGRAVITY AUTONOMOUS CREATION ENGINE
 * Orchestrates the full lifecycle of feature creation from synthesis to deployment.
 */
export class AutonomousCreationEngine {
  public async runCycle() {
    logAutonomousAction('🚀 [CreationEngine] Starting full autonomous creation cycle...', 'info');

    // Phase 21: Sentient Orchestration - Register Creation Intent
    await sentientOrchestration.registerIntent({
      id: `intent_creation_${Date.now()}`,
      agent: 'CreationEngine',
      action: 'runCycle',
      priority: 2, // Higher than general work cycle
      context: { cycle: 'autonomous_creation' },
      timestamp: new Date().toISOString()
    });

    // 1. Synthesis: Gap Analysis & Idea Generation
    const ideas = await synthesize();
    logAutonomousAction(`🔮 [CreationEngine] Synthesized ${ideas.length} new ideas.`, 'info');

    if (ideas.length === 0) {
      logAutonomousAction('✨ [CreationEngine] No new gaps identified. System state is optimal.', 'info');
      return { status: 'optimal', features: [] };
    }

    const createdFeatures = [];

    // 2. Order Generation with Dependency Chains
    const { getSystemInsights } = await import('../core');
    const insights = await getSystemInsights();
    const systemOptimal = (insights as any).docker?.status === 'optimal' && (insights as any).circuitBreakers?.mongodb === 'closed';

    for (const idea of ideas) {
      // Phase 20: Scale Evolution Complexity
      const allowedComplexities = (systemOptimal || process.env.AUTONOMOUS_MODE === 'cloud' || process.env.MACBOOK_CLOUD_SIMULATION === 'true')
        ? ['Low', 'Medium', 'High']
        : ['Low', 'Medium'];

      if (allowedComplexities.includes(idea.complexity)) {
        logAutonomousAction(`📝 [CreationEngine] Generating dependency chain for ${idea.complexity}-complexity feature: ${idea.feature}`, 'info');

        // Step A: Bootstrap
        const bootstrapOrder = await workOrderService.createOrder(
          'BOOTSTRAP_SERVICE',
          `Bootstrap ${idea.feature}`,
          idea
        );

        // Step B: Smoke Test (Depends on Bootstrap)
        const serviceName = idea.feature.toLowerCase().replace(/\s+/g, '_').replace(/_service$/, '');
        const smokeTestOrder = await workOrderService.createOrder(
          'SMOKE_TEST',
          `Verify ${idea.feature} integrity`,
          { serviceName },
          [bootstrapOrder.id]
        );

        // Step C: Deployment (Depends on Smoke Test)
        const deployOrder = await workOrderService.createOrder(
          'DEPLOYMENT',
          `Deploy ${idea.feature} to production`,
          { serviceName },
          [smokeTestOrder.id]
        );

        // Step D: Git Sync (Depends on Deployment)
        await workOrderService.createOrder(
          'SYSTEM_SYNC',
          `Synchronize ${idea.feature} evolution to Git`,
          { feature: idea.feature },
          [deployOrder.id]
        );

        createdFeatures.push(idea.feature);
      }
    }

    // 3. Execution: Trigger the WorkOrderService to process the chain
    logAutonomousAction('⚡ [CreationEngine] Triggering execution of dependency chains...', 'info');
    await workOrderService.executePendingOrders();

    logAutonomousAction('✅ [CreationEngine] Autonomous creation cycle complete.', 'info');

    // Clear intent after completion
    sentientOrchestration.clearIntents();

    return { status: 'completed', features: createdFeatures };
  }
}

export const creationEngine = new AutonomousCreationEngine();
