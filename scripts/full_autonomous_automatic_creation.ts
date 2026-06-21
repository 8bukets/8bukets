import { workOrderService } from '../antigravity/services/work_order';
import { onlinePresence } from '../antigravity/services/presence';
import { jules } from '../antigravity/jules';
import { checkDockerHealth } from '../antigravity/services/docker';
import { logAutonomousAction } from '../antigravity/core';

/**
 * FULL AUTONOMOUS AUTOMATIC CREATION ENGINE
 *
 * Orchestrates the complete lifecycle:
 * 1. Pre-flight Health Checks
 * 2. State & Collaboration Sync
 * 3. Work Order Queue Purge
 * 4. Root Creation Order Generation
 * 5. Recursive Execution Pulse
 * 6. Transitive Dependency Reporting
 */

async function main() {
  console.log('🚀 [Antigravity] Starting Full Autonomous Automatic Creation...');
  logAutonomousAction('🚀 [Antigravity] Initiating full autonomous creation cycle', 'info');

  // 1. Pre-flight Health Checks
  const dockerStatus = await checkDockerHealth();
  console.log(`🐳 [Health] Docker Status: ${dockerStatus.status} (${dockerStatus.containerCount} containers)`);

  if (dockerStatus.status === 'disconnected' && process.env.AUTONOMOUS_MODE !== 'cloud') {
    console.warn('⚠️ [Health] Docker is disconnected. Some creation steps might fail or use simulation fallback.');
  }

  // 2. State & Collaboration Sync
  console.log('📡 [Sync] Synchronizing online presence and collaboration context...');
  await onlinePresence.syncPresence();
  await jules.syncCollaboration();
  console.log('✅ [Sync] Ecosystem state synchronized.');

  // 3. Work Order Queue Purge
  console.log('🧹 [Cleanup] Purging stale pending work orders for a clean creation state...');
  await workOrderService.clearPendingOrders();

  // 4. Root Creation Order Generation
  console.log('📝 [Order] Creating root AUTONOMOUS_CREATION work order...');
  const rootOrder = await workOrderService.createOrder(
    'AUTONOMOUS_CREATION',
    'Execute root autonomous creation cycle (Synthesis -> Bootstrap -> Smoke Test -> Deployment)',
    {
      trigger: 'full_autonomous_script',
      timestamp: new Date().toISOString(),
      mode: process.env.AUTONOMOUS_MODE || 'standard'
    }
  );
  console.log(`✅ [Order] Root order created: ${rootOrder.id}`);

  // 5. Recursive Execution Pulse
  console.log('⚡ [Execution] Beginning recursive execution pulse...');
  await workOrderService.executePendingOrders();

  // 6. Transitive Dependency Reporting & Verification
  console.log('\n📊 [Report] Creation Cycle Lifecycle Summary:');
  const allOrders = (workOrderService as any).orders; // Accessing private for reporting
  const cycleOrders = allOrders.filter((o: any) =>
    o.created_at >= rootOrder.created_at || o.id === rootOrder.id
  );

  const synthesisOrder = cycleOrders.find((o: any) => o.type === 'AUTONOMOUS_CREATION');
  const bootstrapOrders = cycleOrders.filter((o: any) => o.type === 'BOOTSTRAP_SERVICE');
  const smokeTestOrders = cycleOrders.filter((o: any) => o.type === 'SMOKE_TEST');
  const deploymentOrders = cycleOrders.filter((o: any) => o.type === 'DEPLOYMENT');

  console.log(`- Root Synthesis: ${synthesisOrder?.status || 'N/A'}`);
  console.log(`- Services Bootstrapped: ${bootstrapOrders.length} (${bootstrapOrders.map((o: any) => o.status).join(', ')})`);
  console.log(`- Smoke Tests Run: ${smokeTestOrders.length} (${smokeTestOrders.map((o: any) => o.status).join(', ')})`);
  console.log(`- Deployments Triggered: ${deploymentOrders.length} (${deploymentOrders.map((o: any) => o.status).join(', ')})`);

  const failed = cycleOrders.filter((o: any) => o.status === 'failed');
  if (failed.length > 0) {
    console.error(`❌ [Report] Cycle completed with ${failed.length} failures.`);
    failed.forEach((o: any) => console.error(`   - ${o.type} (${o.id}): ${o.error}`));
  } else {
    console.log('✨ [Report] Full autonomous creation cycle completed successfully with zero failures.');
  }
}

main().catch(err => {
  console.error('💥 [Antigravity] Fatal error during autonomous creation:', err);
  process.exit(1);
});
