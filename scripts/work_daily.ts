import { execFile } from 'child_process';
import { promisify } from 'util';
import { syncToICloud } from '../antigravity/services/icloud';

const execFileAsync = promisify(execFile);

async function run() {
  'use cache'
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

  // 3. Commit changes (if any)
  console.log('📝 [commit] Checking for changes to commit...');
  try {
    const { stdout: status } = await execFileAsync('git', ['status', '--porcelain']);
    if (status.trim()) {
      console.log('➕ [commit] Staging changes...');
      await execFileAsync('git', ['add', '.']);
      console.log('💾 [commit] Committing changes...');
      await execFileAsync('git', ['commit', '-m', '🤖 chore: daily autonomous sync and work update']);
    } else {
      console.log('✨ [commit] No changes to commit.');
    }
  } catch (err: any) {
    console.warn('⚠️ [commit] Failed to commit changes.');
    console.warn(err.stdout || err.message);
  }

  // 4. upload (git push)
  console.log('📤 [upload] Pushing changes to remote...');
  try {
    const { stdout } = await execFileAsync('git', ['push']);
    console.log(stdout);
    console.log('✅ [upload] Push successful.');
  } catch (err: any) {
    console.log('🔄 [upload] Standard push failed, attempting with upstream set...');
    try {
      const { stdout } = await execFileAsync('git', ['push', '--set-upstream', 'origin', 'HEAD']);
      console.log(stdout);
      console.log('✅ [upload] Push with upstream successful.');
    } catch (upstreamErr: any) {
      console.warn('⚠️ [upload] Git push failed or restricted.');
      console.warn(upstreamErr.stdout || upstreamErr.message);
    }
  }

  console.log('🏆 [Antigravity] Daily work cycle complete.');
}

run().catch(err => {
  console.error('💥 [Antigravity] Daily work cycle failed:', err);
  process.exit(1);
});
