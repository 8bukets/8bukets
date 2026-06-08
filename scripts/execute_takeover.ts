import { cloudWorkflowAgent } from '../antigravity/services/cloud_workflow';

async function main() {
  console.log('🔗 [Takeover] Initializing autonomous takeover protocol...');
  await cloudWorkflowAgent.enforceCloudTakeover();
  console.log('🏁 [Takeover] Protocol execution finished.');
}

main().catch(err => {
  console.error('❌ [Takeover] Failed:', err);
  process.exit(1);
});
