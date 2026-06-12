import { execFile } from 'child_process';
import { promisify } from 'util';
import { syncToICloud } from '../antigravity/services/icloud';

const execFileAsync = promisify(execFile);

async function run() {
  console.log('🚀 [Antigravity] Starting daily work cycle...');

  // 1. pluu (git pull --rebase)
  console.log('📥 [pluu] Pulling latest changes (rebase)...');
  try {
    const { stdout } = await execFileAsync('git', ['pull', '--rebase']);
    console.log(stdout);
  } catch (err: any) {
    console.warn('⚠️ [pluu] Git pull failed or restricted. Continuing...');
    console.warn(err.stdout || err.message);
  }

  // 2. sync to icloud
  console.log('☁️ [sync] Synchronizing project to iCloud...');
  const syncResult = await syncToICloud();
  if (syncResult.status === 'success') {
    console.log(`✅ [sync] iCloud synchronization successful: ${syncResult.target}`);
  } else {
    console.error(`❌ [sync] iCloud synchronization failed: ${syncResult.error}`);
    // We continue even if sync fails to try the upload
  }

  // 3. upload (git push)
  console.log('📤 [upload] Pushing changes to remote...');
  try {
    const { stdout } = await execFileAsync('git', ['push']);
    console.log(stdout);
    console.log('✅ [upload] Push successful.');
  } catch (err: any) {
    console.warn('⚠️ [upload] Git push failed or nothing to push.');
    console.warn(err.stdout || err.message);
  }

  console.log('🏆 [Antigravity] Daily work cycle complete.');
}

run().catch(err => {
  console.error('💥 [Antigravity] Daily work cycle failed:', err);
  process.exit(1);
});
