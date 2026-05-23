import { jules } from '../antigravity/jules';

import * as fs from 'fs';
import * as path from 'path';

async function main() {
  const args = process.argv.slice(2);
  const isContinuous = args.includes('--continuous');

  // Ensure we simulate a cloud environment if not explicitly disabled
  if (process.env.MACBOOK_CLOUD_SIMULATION !== 'false') {
    process.env.MACBOOK_CLOUD_SIMULATION = 'true';
  }

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

    // Integrate Python Ecosystem Cycle
    console.log('🐍 Running Python Ecosystem Autonomous Cycle...');
    const { exec } = await import('child_process');
    const { promisify } = await import('util');
    const execAsync = promisify(exec);

    try {
      const token = process.env.SYSTEM_AUTH_TOKEN || 'default_dev_token';
      const { stdout } = await execAsync(`python3 run_system.py --skip-scraper --token ${token}`);
      console.log(stdout);
      console.log('✅ Python Ecosystem Cycle Complete.');
    } catch (e: any) {
      console.error('❌ Python Ecosystem Cycle Failed:', e.message);
    }
  }
}

main().catch(console.error);
