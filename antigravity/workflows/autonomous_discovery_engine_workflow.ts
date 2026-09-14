import { getAutonomousDiscoveryEngineData } from '../services/autonomous_discovery_engine';

async function run() {
  const data = await getAutonomousDiscoveryEngineData();
  console.log('✅ [Workflow] Autonomous Discovery Engine complete:', JSON.stringify(data, null, 2));
}

run().catch((err) => {
  console.error('❌ [Workflow] Autonomous Discovery Engine failed:', err);
  process.exit(1);
});
