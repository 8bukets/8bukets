import chokidar from 'chokidar';
import { exec } from 'child_process';
import { promisify } from 'util';
import * as path from 'path';

const execAsync = promisify(exec);

// Path to monitor - usually where you do your active work
const WORKSPACE_DIR = process.cwd();

// Debounce to prevent spamming restarts
let isRestarting = false;
let restartTimeout: NodeJS.Timeout | null = null;

async function triggeriCloudRestart(reason: string) {
  if (isRestarting) return;

  console.log(`[iCloud Monitor] Sync anomaly detected (${reason}). Triggering perfect sync...`);
  isRestarting = true;

  try {
    const { stdout, stderr } = await execAsync(`bash ${path.join(WORKSPACE_DIR, 'scripts/fix_icloud_sync.sh')}`);
    console.log(`[iCloud Monitor] ${stdout.trim()}`);
    if (stderr) console.warn(`[iCloud Monitor Warning] ${stderr.trim()}`);
  } catch (error: any) {
    console.error(`[iCloud Monitor Error] Failed to restart sync: ${error.message}`);
  }

  // Prevent another restart for at least 15 seconds
  if (restartTimeout) clearTimeout(restartTimeout);
  restartTimeout = setTimeout(() => {
    isRestarting = false;
    console.log('[iCloud Monitor] Ready for new anomalies.');
  }, 15000);
}

// Watch for file locks or weird extension changes typical of sync stalls (.icloud)
console.log(`[iCloud Monitor] Watching ${WORKSPACE_DIR} for iCloud anomalies...`);

const watcher = chokidar.watch(WORKSPACE_DIR, {
  ignored: /(^|[\/\\])\..|node_modules|dist/, // Ignore dotfiles, node_modules, dist
  persistent: true,
  ignoreInitial: true,
});

watcher
  .on('add', filePath => {
    // If iCloud leaves a .icloud extension file around for more than a few seconds, it might be stuck
    if (filePath.endsWith('.icloud')) {
      triggeriCloudRestart(`Stuck .icloud file detected: ${path.basename(filePath)}`);
    }
  })
  .on('error', error => {
    console.error(`[iCloud Monitor] Watcher Error: ${error}`);
  });

// Keep process alive gracefully
process.on('SIGINT', () => {
  watcher.close().then(() => {
    console.log('[iCloud Monitor] Shutting down gracefully.');
    process.exit(0);
  });
});
