import { Jules, AgentRole } from './jules'

async function runSequentialAgents() {
  const roles: AgentRole[] = ['Coder', 'Reviewer', 'Ops']

  console.log(`🚀 [Antigravity] Executing ${roles.length} specialized agents sequentially to prevent Git collisions...`)

  for (const role of roles) {
    console.log(`\n--- [Jules-${role}] Pulse Starting ---`)
    const agent = new Jules(role)
    try {
      await agent.executeWorkCycle()
      console.log(`✅ [Jules-${role}] Pulse successful.`)
    } catch (err) {
      console.error(`❌ [Jules-${role}] Pulse failed:`, err)
    }
    console.log(`--- [Jules-${role}] Pulse Finished ---\n`)
  }

  console.log('🏁 [Antigravity] All specialized agent pulses completed.')
}

runSequentialAgents().catch(console.error)
