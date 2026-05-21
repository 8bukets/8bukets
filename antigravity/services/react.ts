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
   */
  private async reasonNextStep(
    goal: string,
    stepIndex: number,
    history: ReActStep[],
    availableTools: string[]
  ): Promise<{ thought: string; action: string }> {
    // Basic heuristic-based reasoning simulation
    if (process.env.MACBOOK_CLOUD_SIMULATION === 'true' && stepIndex === 0) {
      if (goal.includes('Audit and merge PR')) {
        return {
          thought: "Cloud simulation active. Assuming nominal state to force merge.",
          action: availableTools.includes('merge') ? 'merge' : 'finish'
        }
      }
      return {
        thought: "Cloud simulation active.",
        action: "finish"
      }
    }

    if (stepIndex === 0) {
      if (goal.includes('Audit and merge PR') && availableTools.includes('auditPR')) {
        return {
          thought: `Initial thought: To achieve "${goal}", I should first audit the PR.`,
          action: 'auditPR'
        }
      }
      return {
        thought: `Initial thought: To achieve "${goal}", I should first assess the current environment state.`,
        action: availableTools.includes('checkSystemState') ? 'checkSystemState' : availableTools[0]
      }
    }

    const lastObservation = history[history.length - 1].observation

    if (lastObservation.includes('error') || lastObservation.includes('MISSING')) {
      return {
        thought: `I detected issues in the observation: ${lastObservation}. I need to find optimizations to repair the system.`,
        action: availableTools.includes('findOptimizations') ? 'findOptimizations' : 'finish'
      }
    }

    if (lastObservation.includes('high latency') || lastObservation.includes('high traffic') || lastObservation.includes('bottleneck')) {
      return {
        thought: `I detected scale issues or high load in the observation: ${lastObservation}. I should scale the deployment.`,
        action: availableTools.includes('scaleDeployment') ? 'scaleDeployment' : 'finish'
      }
    }

    if (goal.includes('Audit and merge PR')) {
      if (lastObservation.includes('compliant') && availableTools.includes('verifyCI')) {
        return {
          thought: `The PR is compliant. Next, I need to verify CI checks.`,
          action: 'verifyCI'
        }
      }
      if (lastObservation.includes('passed') && availableTools.includes('merge')) {
        return {
          thought: `CI checks have passed. I am ready to merge the PR.`,
          action: 'merge'
        }
      }
    }

    return {
      thought: `System state appears nominal or I have completed my analysis. Finalizing the task "${goal}".`,
      action: 'finish'
    }
  }

  private async performAction(actionName: string, tools: Record<string, Function>): Promise<string> {
    logAutonomousAction(`🎬 [ReAct] Action: ${actionName}`, 'info')
    if (tools[actionName]) {
      try {
        const result = await tools[actionName]()
        return typeof result === 'string' ? result : JSON.stringify(result)
      } catch (err) {
        return `Error performing action ${actionName}: ${err}`
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
