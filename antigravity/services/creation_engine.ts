import { synthesize } from '../synthesis';
import { workOrderService } from './work_order';
import { logAutonomousAction } from '../core';

/**
 * ANTIGRAVITY AUTONOMOUS CREATION ENGINE
 * Orchestrates the full lifecycle of feature creation from synthesis to deployment.
 */
export class AutonomousCreationEngine {
  public async runCycle() {
    logAutonomousAction('🚀 [CreationEngine] Starting full autonomous creation cycle...', 'info');

    // 1. Synthesis: Gap Analysis & Idea Generation
    const ideas = await synthesize();
    logAutonomousAction(`🔮 [CreationEngine] Synthesized ${ideas.length} new ideas.`, 'info');

    if (ideas.length === 0) {
      logAutonomousAction('✨ [CreationEngine] No new gaps identified. System state is optimal.', 'info');
      return { status: 'optimal', features: [] };
    }

    const createdFeatures = [];

    // 2. Order Generation with Dependency Chains
    for (const idea of ideas) {
      // Only process Low/Medium complexity for safe autonomous evolution
      if (idea.complexity === 'Low' || idea.complexity === 'Medium') {
        logAutonomousAction(`📝 [CreationEngine] Generating dependency chain for: ${idea.feature}`, 'info');

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
    return { status: 'completed', features: createdFeatures };
  }
}

export const creationEngine = new AutonomousCreationEngine();
