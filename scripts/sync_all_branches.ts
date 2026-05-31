import { Jules } from '../antigravity/jules'
import { syncCollaborationState, broadcastToStakeholders } from '../antigravity/services/collaboration'
import { generateConsolidatedReport } from '../antigravity/services/intelligence'

/**
 * FULL SYSTEM SYNC & COLLABORATION SCRIPT
 * Performs a deep scan of all branches and merges knowledge into the matrix.
 */

async function main() {
  console.log('🚀 [Antigravity] Starting Full Ecosystem Synchronization...')
  const jules = new Jules('Ops')

  try {
    // 1. Scan all branches (force: true ensures deep analysis)
    const branches = await jules.scanAllBranches(true)
    console.log(`🔍 Found ${branches.length} branches.`)

    // 2. Synchronize collaboration state and merge insights
    console.log('🧠 Merging branch insights and synchronizing state...')
    const state = await syncCollaborationState(branches)

    // 3. Broadcast to stakeholders with updated synergy data
    await broadcastToStakeholders(state)

    // 4. Generate consolidated intelligence report
    console.log('📊 Generating consolidated intelligence report...')
    await generateConsolidatedReport(branches)

    console.log('✅ [Antigravity] Full Ecosystem Sync Complete.')
  } catch (err) {
    console.error('💥 [Antigravity] Sync failed:', err)
    process.exit(1)
  }
}

main()
