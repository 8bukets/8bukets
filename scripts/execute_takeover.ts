import { jules } from '../antigravity/jules';
import { cloudWorkflowAgent } from '../antigravity/services/cloud_workflow';
import { workOrderService } from '../antigravity/services/work_order';
import { onlinePresence } from '../antigravity/services/presence';

/**
 * CLOUD TAKEOVER EXECUTION SCRIPT
 * Specifically designed to be run in cloud environments (CI/CD, Vercel, etc.)
 * to force a state recovery and execute pending work orders if the primary node is offline.
 */
async function main() {
  console.log('🌌 [ExecuteTakeover] Initiating cloud-native takeover protocol...');

  try {
    // 1. Force presence sync to establish leadership context
    console.log('📡 [ExecuteTakeover] Synchronizing presence...');
    await onlinePresence.syncPresence();

    // 2. Audit for takeover necessity
    console.log('⚖️ [ExecuteTakeover] Auditing for cloud takeover necessity...');
    const takeoverResult = await cloudWorkflowAgent.enforceCloudTakeover();

    if (takeoverResult.takeover) {
      console.log('🚀 [ExecuteTakeover] Takeover active. Processing recovered ecosystem state.');

      // 3. Execute all pending work orders (Recovered from MongoDB)
      console.log('⚡ [ExecuteTakeover] Executing pending work orders...');
      await workOrderService.executePendingOrders();

      // 4. Run a full Jules work cycle to ensure continuous evolution
      console.log('🌟 [ExecuteTakeover] Triggering full Jules work cycle...');
      await jules.executeWorkCycle();

      console.log('🏆 [ExecuteTakeover] Cloud takeover and execution cycle complete.');
    } else {
      console.log(`ℹ️ [ExecuteTakeover] Takeover not required. Reason: ${takeoverResult.reason}`);
    }
  } catch (error: any) {
    console.error('💥 [ExecuteTakeover] Critical failure during takeover execution:', error.message);
    process.exit(1);
  }
}

main().catch(err => {
  console.error('💥 [ExecuteTakeover] Unhandled error:', err);
  process.exit(1);
});
