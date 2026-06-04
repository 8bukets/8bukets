import { jules } from '../antigravity/jules';
import { syncCollaborationState } from '../antigravity/services/collaboration';
import { generateConsolidatedReport } from '../antigravity/services/intelligence';

/**
 * Ecosystem Synchronization Script
 * Performs a comprehensive scan and merge of all system branches and collaboration state.
 */
async function syncAll() {
  console.log('🔄 Starting Ecosystem Synchronization...');

  try {
    // 1. Scan all branches for intelligence
    console.log('🔍 Scanning branches...');
    const branches = await jules.scanAllBranches(true);

    // 2. Synchronize collaboration state
    console.log('🤝 Synchronizing collaboration state...');
    await syncCollaborationState(branches);

    // 3. Generate consolidated intelligence report
    console.log('📊 Generating consolidated report...');
    await generateConsolidatedReport(branches);

    console.log('✅ Ecosystem Synchronization Complete.');
  } catch (error) {
    console.error('❌ Synchronization Failed:', error);
    process.exit(1);
  }
}

syncAll().catch(console.error);
