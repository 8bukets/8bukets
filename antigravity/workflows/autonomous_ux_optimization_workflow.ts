import { getAutonomousUXOptimizationServiceData } from '../services/autonomous_ux_optimization';

async function run() {
  const data = await getAutonomousUXOptimizationServiceData();
  console.log('✅ [Workflow] Autonomous UX Optimization complete:', JSON.stringify(data, null, 2));
}

run().catch((err) => {
  console.error('❌ [Workflow] Autonomous UX Optimization failed:', err);
  process.exit(1);
});
