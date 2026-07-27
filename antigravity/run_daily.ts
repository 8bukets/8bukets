import { Jules } from './jules';

const isContinuous = process.argv.includes('--continuous');

async function run() {
  const jules = await Jules.create('General');
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
