import { getProactiveScalabilityServiceData } from '../services/proactive_scalability';

async function run() {
  const data = await getProactiveScalabilityServiceData();
  console.log('✅ [Workflow] Proactive Scalability complete:', JSON.stringify(data, null, 2));
}

run().catch((err) => {
  console.error('❌ [Workflow] Proactive Scalability failed:', err);
  process.exit(1);
});
