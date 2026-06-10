import { syncToICloud } from '../antigravity/services/icloud';

async function run() {
  const result = await syncToICloud();
  if (result.status === 'success') {
    console.log(`✅ [Manual Sync] iCloud synchronization successful: ${result.target}`);
  } else {
    console.error(`❌ [Manual Sync] iCloud synchronization failed: ${result.error}`);
    process.exit(1);
  }
}

run().catch(err => {
  console.error('💥 [Manual Sync] Unexpected error:', err);
  process.exit(1);
});
