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
    const isNetworkError = err.message.includes('Could not resolve host') || err.message.includes('Connection refused');
    const isNoTracking = err.message.includes('There is no tracking information');

    if (isNoTracking) {
      console.log('🔄 [pluu] No tracking information found, attempting to pull from origin/main...');
      try {
        const { stdout } = await execFileAsync('git', ['pull', '--rebase', 'origin', 'main']);
        console.log(stdout);
      } catch (fallbackErr: any) {
        console.error('❌ [pluu] Fallback git pull from origin main failed.');
        console.error(fallbackErr.stdout || fallbackErr.message);
        process.exit(1);
      }
    } else if (isNetworkError) {
      console.warn('⚠️ [pluu] Network issue during git pull. Continuing with local state...');
    } else {
      console.error('❌ [pluu] Git pull failed critically.');
      console.error(err.stdout || err.message);
      process.exit(1);
    }
  }

  // 2. ingest knowledge
  console.log('👁️ [ingest] Ingesting webshop market intelligence...');
  try {
    await execFileAsync('npm', ['run', 'ingest:webshop']);
  } catch (err: any) {
    console.warn('⚠️ [ingest] Webshop ingestion failed, continuing...');
  }

  // 3. sync to icloud
  console.log('☁️ [sync] Synchronizing project to iCloud...');
  const syncResult = await syncToICloud();
  if (syncResult.status === 'success') {
    console.log(`✅ [sync] iCloud synchronization successful: ${syncResult.target}`);
  } else {
    console.error(`❌ [sync] iCloud synchronization failed: ${syncResult.error}`);
    process.exit(1); // Critical failure for the requested workflow
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
      console.error('❌ [upload] Git push failed critically.');
      console.error(upstreamErr.stdout || upstreamErr.message);
      process.exit(1);
    }
  }

  console.log('🏆 [Antigravity] Daily work cycle complete.');
}

run().catch(err => {
  console.error('💥 [Antigravity] Daily work cycle failed:', err);
  process.exit(1);
});
