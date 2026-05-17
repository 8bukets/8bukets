import { jules } from './jules';

const isContinuous = process.argv.includes('--continuous');

async function run() {
  if (isContinuous) {
    // await jules.startConsciousnessLoop();
  } else {
    await jules.executeWorkCycle();
  }
}

run().catch(err => {
  console.error('💥 [Antigravity Root] Execution failed:', err);
  process.exit(1);
});
