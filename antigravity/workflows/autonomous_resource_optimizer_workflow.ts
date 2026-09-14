import { getAutonomousResourceOptimizerData } from '../services/autonomous_resource_optimizer';

async function run() {
  const data = await getAutonomousResourceOptimizerData();
  console.log('✅ [Workflow] Autonomous Resource Optimizer complete:', JSON.stringify(data, null, 2));
}

run().catch((err) => {
  console.error('❌ [Workflow] Autonomous Resource Optimizer failed:', err);
  process.exit(1);
});
