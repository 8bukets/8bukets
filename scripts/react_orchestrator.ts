import { jules } from '../antigravity/jules'
import { reactService } from '../antigravity/services/react'

/**
 * REACT ORCHESTRATOR DEMONSTRATION SCRIPT
 * This script demonstrates the ReAct (Reasoning and Acting) integration within Antigravity.
 * It uses the refactored, generic ReAct loop.
 */

async function main() {
  console.log('🚀 [Orchestrator] Initializing ReAct Demonstration...')

  // 1. Execute the full Jules Work Cycle (which now includes ReAct)
  console.log('\n--- Part 1: Full Jules Work Cycle (Integrated ReAct) ---')
  await jules.executeWorkCycle()

  // 2. Demonstrate a standalone ReAct cycle with different tools
  console.log('\n--- Part 2: Standalone ReAct Cycle (Generic Loop) ---')
  const customTools = {
    checkSystemState: async () => 'System is in error: Missing documentation in antigravity/core.ts',
    findOptimizations: async () => 'Optimization: Add JSDoc to core.ts functions.',
    finalize: async () => 'Demo cycle complete.'
  }

  const steps = await reactService.executeCycle('Repair system documentation', customTools)

  console.log('\n--- ReAct Trace ---')
  console.log(reactService.getTrace())

  console.log('\n✅ [Orchestrator] ReAct Demonstration Complete.')
}

main().catch(err => {
  console.error('❌ [Orchestrator] Error during demonstration:', err)
  process.exit(1)
})
