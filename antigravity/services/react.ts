import { logAutonomousAction } from '../core'

/**
 * ANTIGRAVITY REACT SERVICE
 * Implements the ReAct (Reasoning and Acting) protocol: Thought -> Action -> Observation.
 * Based on arXiv:2210.03629.
 */

export interface ReActStep {
  thought: string
  action: string
  observation: string
}

export interface ReActAgentPrompt {
  goal: string
  context?: string
  availableTools: string[]
}

export class ReActService {
  private steps: ReActStep[] = []

  /**
   * Execute a ReAct cycle for a given goal and tools.
   * This implementation follows a generic loop where each step's thought and action
   * are determined by the current state and the goal.
   */
  public async executeCycle(
    goal: string,
    tools: Record<string, Function>,
    maxSteps: number = 5
  ): Promise<ReActStep[]> {
    logAutonomousAction(`🧠 [ReAct] Starting autonomous cycle for goal: "${goal}"`, 'info')
    this.steps = []

    for (let i = 0; i < maxSteps; i++) {
      // In a production system with an LLM, we would send the history + goal to the model
      // and it would return the next Thought and Action.
      // Here, we simulate the 'Reasoning' engine's decision process.
      const stepDecision = await this.reasonNextStep(goal, i, this.steps, Object.keys(tools))

      if (stepDecision.action === 'finish') {
        logAutonomousAction(`✅ [ReAct] Goal achieved: ${stepDecision.thought}`, 'info')
        this.steps.push({
          thought: stepDecision.thought,
          action: 'finish',
          observation: 'Cycle finalized successfully.'
        })
        break
      }

      logAutonomousAction(`💭 [ReAct] Step ${i + 1} Thought: ${stepDecision.thought}`, 'info')
      const observation = await this.performAction(stepDecision.action, tools)

      this.steps.push({
        thought: stepDecision.thought,
        action: stepDecision.action,
        observation
      })

      if (i === maxSteps - 1) {
        console.warn(`⚠️ [ReAct] Reached maximum steps (${maxSteps}) for goal: ${goal}`)
      }
    }

    logAutonomousAction(`[ReAct] Completed cycle for goal: ${goal}`, 'cognitive')
    return this.steps
  }

  /**
   * Mock reasoning engine.
   * Determines the next Thought and Action based on the goal and execution history.
   * NOTE: This is a hardcoded simulation of an LLM's reasoning process. A true ReAct
   * implementation would use a model to generate the thought/action based on the goal,
   * available tools, and history, making it adaptable to arbitrary goals.
   */
  private async reasonNextStep(
    goal: string,
    stepIndex: number,
    history: ReActStep[],
    availableTools: string[]
  ): Promise<{ thought: string; action: string }> {
    // Route to a specific reasoning strategy based on the goal.
    if (goal.includes('Audit and merge PR')) {
      return this.reasonForPrMerge(goal, stepIndex, history, availableTools);
    }

    // Default reasoning for other goals
    if (stepIndex === 0) {
      return {
        thought: `Initial thought: To achieve "${goal}", I should first assess the current environment state.`,
        action: availableTools.includes('checkSystemState') ? 'checkSystemState' : availableTools[0]
      }
    }

    const lastObservation = history[history.length - 1]?.observation || '';
    if (lastObservation.includes('error') || lastObservation.includes('MISSING')) {
      return {
        thought: `I detected issues in the observation: ${lastObservation}. I need to find optimizations to repair the system.`,
        action: availableTools.includes('findOptimizations') ? 'findOptimizations' : 'finish'
      }
    }

    return {
      thought: `System state appears nominal or I have completed my analysis. Finalizing the task "${goal}".`,
      action: 'finish'
    }
  }

  private reasonForPrMerge(
    goal: string,
    stepIndex: number,
    history: ReActStep[],
    availableTools: string[]
  ): { thought: string; action: string } {
    if (stepIndex === 0) {
      return {
        thought: `Initial thought: To achieve "${goal}", I should first audit the PR.`,
        action: 'auditPR'
      };
    }

    const lastObservation = history[history.length - 1]?.observation || '';

    // Centralize failure conditions
    if (lastObservation.includes('not compliant') || lastObservation.includes('failed') || lastObservation.includes('false')) {
      let reason = 'The PR is not compliant.';
      if (lastObservation.includes('failed')) reason = 'CI check failed.';
      if (lastObservation.includes('false')) reason = 'The merge operation failed.';
      return {
        thought: `Audit failed: ${reason} Aborting PR integration process.`,
        action: 'finish'
      };
    }

    if (lastObservation.includes('compliant') && availableTools.includes('verifyCI')) {
      return { thought: `The PR is compliant. Next, I need to verify CI checks.`, action: 'verifyCI' };
    }

    if (lastObservation.includes('passed') && availableTools.includes('merge')) {
      return { thought: `CI checks have passed. I am ready to merge the PR.`, action: 'merge' };
    }

    if (lastObservation.includes('true')) {
      return { thought: `Merge succeeded: The PR was successfully merged. Completing task.`, action: 'finish' };
    }

    // Fallback for this specific goal
    return { thought: `PR merge analysis complete. Finalizing task.`, action: 'finish' };
  }

  private async performAction(actionName: string, tools: Record<string, Function>): Promise<string> {
    logAutonomousAction(`🎬 [ReAct] Action: ${actionName}`, 'info')
    if (tools[actionName]) {
      try {
        const result = await tools[actionName]()
        return typeof result === 'string' ? result : JSON.stringify(result)
      } catch (err: any) {
        return `Error performing action ${actionName}: ${err.message || String(err)}`
      }
    }
    return `Action ${actionName} not found in tools.`
  }

  public getTrace(): string {
    return this.steps.map((s, i) =>
      `Step ${i + 1}:\n  Thought: ${s.thought}\n  Action: ${s.action}\n  Observation: ${s.observation}`
    ).join('\n\n')
  }
}

export const reactService = new ReActService()
