import { logAutonomousAction } from './core'
import { jules } from './jules.ts';

const isContinuous = process.argv.includes('--continuous');

async function run() {
  const { healthCheck } = await import('./core');
  const health = await healthCheck();
  logAutonomousAction(`🏥 [Antigravity Root] System Health: MongoDB=${health.mongodb}, Supabase=${health.supabase}`, 'info');

  if (isContinuous) {
    await jules.startConsciousnessLoop();
  } else {
    await jules.executeWorkCycle();
  }
}

run().catch(err => {
  console.error('💥 [Antigravity Root] Execution failed:', err);
  process.exit(1);
});
