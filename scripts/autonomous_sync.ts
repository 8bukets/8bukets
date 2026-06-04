import { jules } from '../antigravity/jules';
import { exec } from 'child_process';
import { promisify } from 'util';
import * as fs from 'fs';
import * as path from 'path';
import { generateConsolidatedReport } from '../antigravity/services/intelligence';

const execAsync = promisify(exec);

/**
 * UNIFIED AUTONOMOUS ORCHESTRATOR
 * Bridges TypeScript and Python intelligence layers for a complete system pulse.
 */
async function autonomousSync() {
  console.log('🚀 [Orchestrator] Starting Unified Autonomous Synchronization...');

  try {
    // 1. Ensure environment is ready
    if (!fs.existsSync(path.join(process.cwd(), 'results'))) {
        fs.mkdirSync(path.join(process.cwd(), 'results'));
    }

    // 2. Run TypeScript Work Cycle
    // This includes knowledge ingestion, self-repair, PR auditing, and reporting.
    console.log('🔷 [TS] Executing Jules Work Cycle...');
    await jules.executeWorkCycle();

    // 3. Run Python Intelligence & Knowledge Merge
    // Bridging the Python agents' data into the unified foundation.
    console.log('🔶 [Python] Running Knowledge Merge & System Analytics...');
    try {
      console.log(' - Executing merge_knowledge.py...');
      await execAsync('python3 merge_knowledge.py');

      console.log(' - Executing analytics.py...');
      await execAsync('python3 analytics.py');

      console.log(' - Running Python Orchestrator (Subset)...');
      // Running with --skip-scraper since TS already handled fresh ingestion
      // and --token default_dev_token for local auth
      await execAsync('python3 run_system.py --skip-scraper --token default_dev_token');

      console.log(' ✅ [Python] Intelligence sub-cycle complete.');
    } catch (pyErr: any) {
      console.warn(' ⚠️ [Python] Intelligence sub-cycle encountered issues:', pyErr.message);
    }

    // 4. Final Verification & Final Report Generation
    // We re-run the report generation to capture the results from the Python cycle.
    console.log('📊 [Orchestrator] Finalizing artifacts and generating final report...');
    const branches = await jules.scanAllBranches();
    const result = await generateConsolidatedReport(branches);
    console.log(` ✅ Consolidated Report updated at ${result.reportPath}`);

    console.log('🏆 [Orchestrator] Unified Synchronization Complete.');
  } catch (err) {
    console.error('💥 [Orchestrator] Critical Synchronization Failure:', err);
    process.exit(1);
  }
}

autonomousSync().catch(console.error);
