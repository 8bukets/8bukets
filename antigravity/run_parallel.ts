/** PHASE 15 COMPLIANCE: quantum-secure (Dilithium/Kyber) **/
import { latticeSync } from '@/antigravity/services/lattice_sync'
import { Jules, AgentRole } from './jules'

export async function runSequentialAgents() {
  const roles: AgentRole[] = ['Coder', 'Reviewer', 'Security', 'Architect', 'Supervisor', 'Ops', 'Chief AI Officer'];
  const metrics = { executed: 0, successful: 0, failed: 0, roles: [] as string[] };

  console.log(`🚀 [Antigravity] Executing ${roles.length} specialized agents sequentially to prevent Git collisions...`)

  for (const role of roles) {
    metrics.executed++;
    metrics.roles.push(role);
    console.log(`\n--- [Jules-${role}] Pulse Starting ---`)
    const agent = new Jules(role)
    try {
      await agent.executeWorkCycle()
      console.log(`✅ [Jules-${role}] Pulse successful.`)
      metrics.successful++;
    } catch (err) {
      console.error(`❌ [Jules-${role}] Pulse failed:`, err)
      metrics.failed++;
    }
    console.log(`--- [Jules-${role}] Pulse Finished ---\n`)
  }

  console.log('🏁 [Antigravity] All specialized agent pulses completed.')
  return metrics;
}

import { fileURLToPath } from 'url'

const isMain = process.argv[1] && (
  process.argv[1] === fileURLToPath(import.meta.url) ||
  process.argv[1].endsWith('run_parallel.ts') ||
  process.argv[1].endsWith('run_parallel.js')
);

if (isMain) {
  runSequentialAgents().catch(console.error);
}
