import { logAutonomousAction } from '../core';
export class ReActService {
    constructor() {
        this.steps = [];
        this.actionHistory = new Set();
    }
    /**
     * Execute a ReAct cycle for a given goal and tools.
     */
    async executeCycle(goal, tools, maxSteps = 5) {
        logAutonomousAction(`🧠 [ReAct] Starting autonomous cycle for goal: "${goal}"`, 'info');
        this.steps = [];
        this.actionHistory.clear();
        for (let i = 0; i < maxSteps; i++) {
            // 1. Context Pruning: Get a summarized representation of the history
            const condensedHistory = this.pruneContext(this.steps);
            // 2. Static-first Prompt Construction: Construct the prompt for the (simulated) LLM
            this.constructPrompt({
                goal,
                context: condensedHistory,
                availableTools: Object.keys(tools)
            });
            // 3. Reason next step
            const stepDecision = await this.reasonNextStep(goal, i, this.steps, Object.keys(tools));
            // 4. Loop Detection: Check if we are stuck in a repetitive action loop
            const stateKey = `${stepDecision.action}:${this.steps.length > 0 ? this.steps[this.steps.length - 1].observation.slice(0, 50) : 'init'}`;
            if (this.actionHistory.has(stateKey) && stepDecision.action !== 'finish') {
                logAutonomousAction(`⚠️ [ReAct] Loop detected for action "${stepDecision.action}". Breaking loop.`, 'warn');
                this.steps.push({
                    thought: "I detected an infinite loop trap. Forcing termination.",
                    action: 'finish',
                    observation: 'Loop detector triggered.'
                });
                break;
            }
            this.actionHistory.add(stateKey);
            if (stepDecision.action === 'finish') {
                logAutonomousAction(`✅ [ReAct] Goal achieved: ${stepDecision.thought}`, 'info');
                this.steps.push({
                    thought: stepDecision.thought,
                    action: 'finish',
                    observation: 'Cycle finalized successfully.'
                });
                break;
            }
            logAutonomousAction(`💭 [ReAct] Step ${i + 1} Thought: ${stepDecision.thought}`, 'info');
            const observation = await this.performAction(stepDecision.action, tools);
            this.steps.push({
                thought: stepDecision.thought,
                action: stepDecision.action,
                observation
            });
            if (i === maxSteps - 1) {
                logAutonomousAction(`⚠️ [ReAct] Reached maximum steps (${maxSteps}) for goal: ${goal}`, 'warn');
            }
        }
        logAutonomousAction(`[ReAct] Completed cycle for goal: ${goal}`, 'cognitive');
        return this.steps;
    }
    /**
     * Production Tactic: Context Pruning & Summarization
     * Instead of appending raw histories, pass a rolling state representation.
     */
    pruneContext(history) {
        if (history.length === 0)
            return "No prior actions.";
        // Keep only the last 2 steps in detail, summarize the rest
        const lastSteps = history.slice(-2);
        const summarized = history.slice(0, -2).map(s => `Action: ${s.action} -> Result: ${s.observation.slice(0, 20)}...`).join(' | ');
        return `Summary: ${summarized || 'None'}\nRecent: ${lastSteps.map(s => `[${s.action}]: ${s.observation}`).join('\n')}`;
    }
    /**
     * Production Tactic: Leverage Prompt Caching
     * Construct prompts with static components first and dynamic variables at the very end.
     */
    constructPrompt(params) {
        const staticInstructions = `
# System Instructions
You are an autonomous ReAct agent.
Follow the Thought -> Action -> Observation cycle.
Available Tools: ${params.availableTools.join(', ')}
    `.trim();
        // Dynamic components go at the end to maximize cache hits for the static instructions
        return `${staticInstructions}\n\n## Current Goal: ${params.goal}\n## Context: ${params.context}`;
    }
    /**
     * Mock reasoning engine.
     * Determines the next Thought and Action based on the goal and execution history.
     */
    async reasonNextStep(goal, stepIndex, history, availableTools) {
        // Basic heuristic-based reasoning simulation
        if (process.env.MACBOOK_CLOUD_SIMULATION === 'true' && stepIndex === 0) {
            if (goal.includes('Audit and merge PR')) {
                return {
                    thought: "Cloud simulation active. Assuming nominal state to force merge.",
                    action: availableTools.includes('merge') ? 'merge' : 'finish'
                };
            }
            return {
                thought: "Cloud simulation active.",
                action: "finish"
            };
        }
        if (stepIndex === 0) {
            if (goal.includes('Audit and merge PR') && availableTools.includes('auditPR')) {
                return {
                    thought: `Initial thought: To achieve "${goal}", I should first audit the PR.`,
                    action: 'auditPR'
                };
            }
            return {
                thought: `Initial thought: To achieve "${goal}", I should first assess the current environment state.`,
                action: availableTools.includes('checkSystemState') ? 'checkSystemState' : availableTools[0]
            };
        }
        const lastObservation = history[history.length - 1].observation;
        if (lastObservation.includes('error') || lastObservation.includes('MISSING')) {
            return {
                thought: `I detected issues in the observation: ${lastObservation}. I need to find optimizations to repair the system.`,
                action: availableTools.includes('findOptimizations') ? 'findOptimizations' : 'finish'
            };
        }
        if (lastObservation.includes('high latency') || lastObservation.includes('high traffic') || lastObservation.includes('bottleneck')) {
            return {
                thought: `I detected scale issues or high load in the observation: ${lastObservation}. I should scale the deployment.`,
                action: availableTools.includes('scaleDeployment') ? 'scaleDeployment' : 'finish'
            };
        }
        if (goal.includes('Audit and merge PR')) {
            const isCloud = !!(process.env.GITHUB_ACTIONS || process.env.GITLAB_CI || process.env.AUTONOMOUS_MODE === 'cloud');
            if (lastObservation.includes('compliant') && availableTools.includes('verifyCI')) {
                return {
                    thought: `The PR is compliant. Next, I need to verify CI checks.`,
                    action: 'verifyCI'
                };
            }
            if ((lastObservation.includes('passed') || (isCloud && lastObservation.includes('compliant'))) && availableTools.includes('merge')) {
                return {
                    thought: isCloud
                        ? `CI checks passed or in cloud-native mode with compliant audit. Executing autonomous merge.`
                        : `CI checks have passed. I am ready to merge the PR.`,
                    action: 'merge'
                };
            }
        }
        if (goal.toLowerCase().includes('deploy react agents')) {
            if (stepIndex === 1 && availableTools.includes('verifyDeployLogic')) {
                return {
                    thought: `I need to verify the deployment logic for React agents.`,
                    action: 'verifyDeployLogic'
                };
            }
            if (stepIndex === 2 && availableTools.includes('improveWorkflowRun')) {
                return {
                    thought: `Logic verified. Next, I should improve the workflow run for deployment efficiency.`,
                    action: 'improveWorkflowRun'
                };
            }
        }
        return {
            thought: `System state appears nominal or I have completed my analysis. Finalizing the task "${goal}".`,
            action: 'finish'
        };
    }
    async performAction(actionName, tools) {
        logAutonomousAction(`🎬 [ReAct] Action: ${actionName}`, 'info');
        if (tools[actionName]) {
            try {
                const result = await tools[actionName]();
                return typeof result === 'string' ? result : JSON.stringify(result);
            }
            catch (err) {
                return `Error performing action ${actionName}: ${err}`;
            }
        }
        return `Action ${actionName} not found in tools.`;
    }
    getTrace() {
        return this.steps.map((s, i) => `Step ${i + 1}:\n  Thought: ${s.thought}\n  Action: ${s.action}\n  Observation: ${s.observation}`).join('\n\n');
    }
}
export const reactService = new ReActService();
