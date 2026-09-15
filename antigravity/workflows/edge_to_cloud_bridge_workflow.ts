import { getEdgetoCloudBridgeData } from '../services/edge_to_cloud_bridge';

async function run() {
  const data = await getEdgetoCloudBridgeData();
  console.log('✅ [Workflow] Edge to Cloud Bridge complete:', JSON.stringify(data, null, 2));
}

run().catch((err) => {
  console.error('❌ [Workflow] Edge to Cloud Bridge failed:', err);
  process.exit(1);
});
