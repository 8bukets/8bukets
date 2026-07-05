import { jules } from '../antigravity/jules';
import { cloudConnectedIntegrationService } from '../antigravity/services/cloud_connected_integration';
import { onlinePresence } from '../antigravity/services/presence';
import { swarmHeartbeat } from '../antigravity/services/swarm_heartbeat';
import { globalNeuralSync } from '../antigravity/services/global_neural_sync_service_phase_12';
import { exec } from 'child_process';
import { promisify } from 'util';
import * as fs from 'fs';
import * as path from 'path';

const execAsync = promisify(exec);

/**
 * UNIFIED AUTONOMOUS SYNCHRONIZATION ORCHESTRATOR
 * Coordinates full ecosystem state convergence, Jules work cycles, and Python agent execution.
 */
async function main() {
  console.log('🚀 [AutonomousSync] Initiating unified ecosystem synchronization...');

  const isCloud = !!(process.env.GITHUB_ACTIONS || process.env.GITLAB_CI || process.env.AUTONOMOUS_MODE === 'cloud' || process.env.MACBOOK_CLOUD_SIMULATION === 'true');

  try {
    // 1. Phase 26 Sovereign Mesh Activation
    console.log('📡 [AutonomousSync] Activating sovereign mesh connections...');
    await cloudConnectedIntegrationService.establishSovereignMeshConnections();

    // 2. Proactive iCloud Sync Fix (if local)
    if (!isCloud) {
       console.log('☁️  [AutonomousSync] Ensuring iCloud Sync is fluid...');
       try {
         await execAsync('bash scripts/fix_icloud_sync.sh');
       } catch (e: any) {
         console.warn('⚠️  [AutonomousSync] Could not fix iCloud sync proactively:', e.message);
       }
    }

    // 3. Global Neural Convergence (Phase 12)
    console.log('🧠 [AutonomousSync] Performing global neural convergence...');
    await globalNeuralSync.convergeState();

    // 4. Execute Technical Knowledge Scrapers
    console.log('📚 [AutonomousSync] Updating technical knowledge base...');
    const scrapers = [
      'npm run ingest:knowledge'
    ];

    for (const scraper of scrapers) {
      try {
        console.log(` - Running: ${scraper}...`);
        await execAsync(scraper);
      } catch (e: any) {
        console.warn(` ⚠️  [AutonomousSync] Scraper failed: ${scraper} - ${e.message}`);
      }
    }

    // 5. Execute Unified Cloud-Native Work Cycle (Phase 23)
    console.log('🌟 [AutonomousSync] Executing Unified Cloud-Native Work Cycle...');
    await onlinePresence.syncPresence();
    const isLeader = onlinePresence.isLeader();

    if (isLeader || !isCloud) {
       await cloudConnectedIntegrationService.executeCloudSovereignWork();
       // executeWorkCycle already performs Phase 23 Pulse and Engine Evolution
       await jules.executeWorkCycle();
    } else {
       console.log('📡 [AutonomousSync] Node is subordinate. Skipping work cycle to avoid conflicts.');
    }

    // 6. Execute Python Ecosystem Cycle
    console.log('🐍 [AutonomousSync] Running Python Ecosystem Autonomous Cycle...');
    try {
      const token = process.env.SYSTEM_AUTH_TOKEN || 'default_dev_token';
      const { stdout } = await execAsync(`python3 run_system.py --skip-scraper --token ${token}`);
      console.log(stdout);
      console.log('✅ [AutonomousSync] Python Ecosystem Cycle Complete.');
    } catch (e: any) {
      console.error('❌ [AutonomousSync] Python Ecosystem Cycle Failed:', e.message);
    }

    // 7. Final Presence Heartbeat
    console.log('📡 [AutonomousSync] Broadcasting final presence heartbeat...');
    await onlinePresence.syncPresence();

    console.log('🏆 [AutonomousSync] Unified synchronization complete.');
  } catch (error: any) {
    console.error('💥 [AutonomousSync] Fatal orchestration error:', error.message);
    process.exit(1);
  } finally {
    // Phase 19: Cleanly stop heartbeat to prevent CI process hangs
    swarmHeartbeat.stop();
  }
}

main().catch(err => {
  console.error('💥 [AutonomousSync] Unhandled error:', err);
  process.exit(1);
});
