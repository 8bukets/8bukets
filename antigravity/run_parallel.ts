import { Jules, AgentRole } from './jules'
import fs from 'fs'
import path from 'path'

const LOCK_FILE = path.join(process.cwd(), 'antigravity/.git_lock');

async function acquireLock(agent: string): Promise<boolean> {
  const maxRetries = 120; // Wait up to 60 seconds (120 * 500ms)
  for (let i = 0; i < maxRetries; i++) {
    if (!fs.existsSync(LOCK_FILE)) {
      try {
        fs.writeFileSync(LOCK_FILE, JSON.stringify({ agent, timestamp: new Date().toISOString() }), { flag: 'wx' });
        return true;
      } catch (e) {
        // file creation failed, lock was acquired concurrently
      }
    }
    await new Promise(resolve => setTimeout(resolve, 500));
  }
  return false;
}

function releaseLock(agent: string) {
  try {
    if (fs.existsSync(LOCK_FILE)) {
      const lockData = JSON.parse(fs.readFileSync(LOCK_FILE, 'utf8'));
      if (lockData.agent === agent) {
        fs.unlinkSync(LOCK_FILE);
      }
    }
  } catch (e) {}
}

export async function runSequentialAgents() {
  const roles: AgentRole[] = ['Coder', 'Reviewer', 'Security', 'Architect', 'Supervisor', 'Ops', 'Chief AI Officer'];
  const metrics = { executed: 0, successful: 0, failed: 0, roles: [] as string[] };

  const parallelEnabled = process.env.PARALLEL_WORK_ENABLED === 'true';
  const safetySwitchActive = process.env.PARALLEL_SAFETY_SWITCH !== 'false'; // Defaults to true/active

  if (parallelEnabled && !safetySwitchActive) {
    console.log(`🚀 [Antigravity] Executing ${roles.length} specialized agents in PARALLEL with lock security...`);
    
    const agentPromises = roles.map(async (role) => {
      metrics.executed++;
      metrics.roles.push(role);
      console.log(`\n--- [Jules-${role}] Parallel Pulse Triggered ---`);
      
      const agent = new Jules(role);
      const lockAcquired = await acquireLock(role);
      if (!lockAcquired) {
        console.error(`❌ [Jules-${role}] Parallel lock acquisition timed out. Aborting to prevent Git index corruption.`);
        metrics.failed++;
        return;
      }
      
      try {
        await agent.executeWorkCycle();
        console.log(`✅ [Jules-${role}] Parallel pulse successful.`);
        metrics.successful++;
      } catch (err) {
        console.error(`❌ [Jules-${role}] Parallel pulse failed:`, err);
        metrics.failed++;
      } finally {
        releaseLock(role);
        console.log(`--- [Jules-${role}] Parallel Pulse Finished ---\n`);
      }
    });

    await Promise.all(agentPromises);
  } else {
    if (parallelEnabled && safetySwitchActive) {
      console.warn(`🛡️ [Safety Switch] Parallel execution requested, but Safety Switch is ACTIVE. Falling back to safe sequential mode to prevent conflicts.`);
    } else {
      console.log(`🚀 [Antigravity] Executing ${roles.length} specialized agents sequentially to prevent Git collisions...`);
    }

    for (const role of roles) {
      metrics.executed++;
      metrics.roles.push(role);
      console.log(`\n--- [Jules-${role}] Pulse Starting ---`);
      const agent = new Jules(role);
      try {
        await agent.executeWorkCycle();
        console.log(`✅ [Jules-${role}] Pulse successful.`);
        metrics.successful++;
      } catch (err) {
        console.error(`❌ [Jules-${role}] Pulse failed:`, err);
        metrics.failed++;
      }
      console.log(`--- [Jules-${role}] Pulse Finished ---\n`);
    }
  }

  console.log('🏁 [Antigravity] All specialized agent pulses completed.');
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

