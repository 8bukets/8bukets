import { getPerformanceMonitoringServiceData } from '../services/performance_monitoring';

async function run() {
  const data = await getPerformanceMonitoringServiceData();
  console.log('✅ [Workflow] Performance Monitoring complete:', JSON.stringify(data, null, 2));
}

run().catch((err) => {
  console.error('❌ [Workflow] Performance Monitoring failed:', err);
  process.exit(1);
});
