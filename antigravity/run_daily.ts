import { jules } from './jules.ts';

const isContinuous = process.argv.includes('--continuous');

async function run() {
  const { healthCheck } = await import('./core');
  const health = await healthCheck();
  console.log(`🏥 [Antigravity Root] System Health: MongoDB=${health.mongodb}, Supabase=${health.supabase}`);

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
