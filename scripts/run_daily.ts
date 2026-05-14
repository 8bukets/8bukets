import { jules } from '../antigravity/jules';

async function main() {
  const args = process.argv.slice(2);
  const isContinuous = args.includes('--continuous');

  if (isContinuous) {
    console.log('Running in continuous mode...');
    await jules.startConsciousnessLoop();
  } else {
    console.log('Running single daily cycle...');
    await jules.executeWorkCycle();
  }
}

main().catch(console.error);
