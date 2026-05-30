import { jules } from '../antigravity/jules';

import * as fs from 'fs';
import * as path from 'path';

async function main() {
  const args = process.argv.slice(2);
  const isContinuous = args.includes('--continuous');

  // Synchronize with autonomous_state.json
  const statePath = path.join(process.cwd(), 'autonomous_state.json');
  if (fs.existsSync(statePath)) {
    try {
      const state = JSON.parse(fs.readFileSync(statePath, 'utf8'));
      if (state.execution_mode === 'cloud') {
        process.env.AUTONOMOUS_MODE = 'cloud';
        console.log('☁️  Detected CLOUD mode from autonomous_state.json');
      }
    } catch (e) {
      console.warn('⚠️  Failed to sync with autonomous_state.json');
    }
  }

  if (isContinuous) {
    console.log('Running in continuous mode...');
    await jules.startConsciousnessLoop();
  } else {
    console.log('Running single daily cycle...');
    await jules.executeWorkCycle();
  }
}

main().catch(console.error);
