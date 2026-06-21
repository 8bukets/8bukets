import { z } from 'zod';
import { logAutonomousAction } from '../core';
import { reactService } from './react';
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
export const SentientOrchestrationSchema = z.object({
    activeIntents: z.array(IntentSchema),
    coordinatedPlan: z.array(z.string()),
    status: z.enum(['idle', 'coordinating', 'executing', 'conflict_detected']),
    lastUpdate: z.string()
});
export class SentientOrchestrationService {
    constructor() {
        this.state = {
            activeIntents: [],
            coordinatedPlan: [],
            status: 'idle',
            lastUpdate: new Date().toISOString()
        };
    }
    /**
     * Registers a new intent from an agent for coordination.
     */
    async registerIntent(intent) {
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
     * Utilizes the ReAct framework for intelligent sequencing.
     */
    async coordinate() {
        this.state.status = 'coordinating';
        logAutonomousAction('⚖️ [SentientOrchestration] Coordinating multi-agent intents via ReAct...', 'info');
        // Sort intents by priority (higher first) and then timestamp
        const sortedIntents = [...this.state.activeIntents].sort((a, b) => {
            if (b.priority !== a.priority)
                return b.priority - a.priority;
            return new Date(a.timestamp).getTime() - new Date(b.timestamp).getTime();
        });
        const goal = `Coordinate ${sortedIntents.length} multi-agent intents: ${sortedIntents.map(i => i.agent + ':' + i.action).join(', ')}`;
        // Define tools for ReAct
        const tools = {
            assessConflicts: async () => {
                const contextKeysModified = new Set();
                const conflicts = [];
                for (const intent of sortedIntents) {
                    const conflictKeys = Object.keys(intent.context).filter(key => contextKeysModified.has(key));
                    if (conflictKeys.length > 0)
                        conflicts.push(`${intent.agent}:${intent.action} conflicts on [${conflictKeys.join(', ')}]`);
                    Object.keys(intent.context).forEach(key => contextKeysModified.add(key));
                }
                return conflicts.length > 0 ? conflicts.join('; ') : 'no_conflicts';
            },
            generateSequence: async () => {
                return sortedIntents.map(i => `${i.agent}:${i.action}`).join(' -> ');
            },
            finalize: async () => 'plan_finalized'
        };
        try {
            const steps = await reactService.executeCycle(goal, tools);
            // Map ReAct steps back to coordinatedPlan
            this.state.coordinatedPlan = sortedIntents.map(i => `${i.agent}:${i.action}`);
            this.state.status = this.state.coordinatedPlan.length > 0 ? 'executing' : 'idle';
            const lastStep = steps[steps.length - 1];
            if (lastStep === null || lastStep === void 0 ? void 0 : lastStep.thought.toLowerCase().includes('conflict')) {
                this.state.status = 'conflict_detected';
            }
        }
        catch (err) {
            logAutonomousAction(`❌ [SentientOrchestration] ReAct coordination failed: ${err.message}`, 'error');
            // Fallback to simple mapping
            this.state.coordinatedPlan = sortedIntents.map(i => `${i.agent}:${i.action}`);
        }
        this.state.lastUpdate = new Date().toISOString();
        logAutonomousAction(`✅ [SentientOrchestration] Coordinated plan established with ${this.state.coordinatedPlan.length} steps.`, 'info');
    }
    getState() {
        return this.state;
    }
    /**
     * Clears completed intents from the registry.
     */
    clearIntents() {
        this.state.activeIntents = [];
        this.state.coordinatedPlan = [];
        this.state.status = 'idle';
        this.state.lastUpdate = new Date().toISOString();
    }
}
export const sentientOrchestration = new SentientOrchestrationService();
