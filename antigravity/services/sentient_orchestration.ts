import { z } from 'zod';
import { logAutonomousAction } from '../core';

/**
 * ANTIGRAVITY SENTIENT ORCHESTRATION SERVICE
 * Provides functional multi-agent intent coordination logic.
 */

export const IntentSchema = z.object({
  id: z.string(),
  agent: z.string(),
  action: z.string(),
  priority: z.number(),
  context: z.record(z.any()),
  timestamp: z.string()
});

export type Intent = z.infer<typeof IntentSchema>;

export const SentientOrchestrationSchema = z.object({
  activeIntents: z.array(IntentSchema),
  coordinatedPlan: z.array(z.string()),
  status: z.enum(['idle', 'coordinating', 'executing', 'conflict_detected']),
  lastUpdate: z.string()
});

export type SentientOrchestration = z.infer<typeof SentientOrchestrationSchema>;

export class SentientOrchestrationService {
  private state: SentientOrchestration = {
    activeIntents: [],
    coordinatedPlan: [],
    status: 'idle',
    lastUpdate: new Date().toISOString()
  };

  /**
   * Registers a new intent from an agent for coordination.
   */
  public async registerIntent(intent: Intent) {
    logAutonomousAction(`🧠 [SentientOrchestration] Registering intent from ${intent.agent}: ${intent.action}`, 'info');

    const result = IntentSchema.safeParse(intent);
    if (!result.success) {
      logAutonomousAction(`❌ [SentientOrchestration] Invalid intent format: ${result.error.message}`, 'error');
      throw new Error('Invalid intent format');
    }

    this.state.activeIntents.push(result.data);
    this.state.lastUpdate = new Date().toISOString();

    await this.coordinate();
  }

  /**
   * Coordinates active intents to resolve conflicts and establish an execution plan.
   */
  private async coordinate() {
    this.state.status = 'coordinating';
    logAutonomousAction('⚖️ [SentientOrchestration] Coordinating multi-agent intents...', 'info');

    // Sort intents by priority (higher first) and then timestamp
    const sortedIntents = [...this.state.activeIntents].sort((a, b) => {
      if (b.priority !== a.priority) return b.priority - a.priority;
      return new Date(a.timestamp).getTime() - new Date(b.timestamp).getTime();
    });

    // Detect conflicts (simplified logic: same action on same context key)
    const plan: string[] = [];
    const contextKeysModified = new Set<string>();

    for (const intent of sortedIntents) {
      const conflictKeys = Object.keys(intent.context).filter(key => contextKeysModified.has(key));

      if (conflictKeys.length > 0) {
        logAutonomousAction(`⚠️ [SentientOrchestration] Conflict detected for ${intent.agent} on keys: ${conflictKeys.join(', ')}`, 'warning');
        this.state.status = 'conflict_detected';
        // In a real scenario, we might try to resolve or de-prioritize
      } else {
        Object.keys(intent.context).forEach(key => contextKeysModified.add(key));
        plan.push(`${intent.agent}:${intent.action}`);
      }
    }

    this.state.coordinatedPlan = plan;
    this.state.status = plan.length > 0 ? 'executing' : 'idle';
    this.state.lastUpdate = new Date().toISOString();

    logAutonomousAction(`✅ [SentientOrchestration] Coordinated plan established with ${plan.length} steps.`, 'info');
  }

  public getState(): SentientOrchestration {
    return this.state;
  }

  /**
   * Clears completed intents from the registry.
   */
  public clearIntents() {
    this.state.activeIntents = [];
    this.state.coordinatedPlan = [];
    this.state.status = 'idle';
    this.state.lastUpdate = new Date().toISOString();
  }
}

export const sentientOrchestration = new SentientOrchestrationService();
