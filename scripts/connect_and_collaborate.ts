import { exec } from 'child_process';
import * as fs from 'fs/promises';
import { promisify } from 'util';
import { syncCollaborationState } from '../antigravity/services/collaboration';

const execAsync = promisify(exec);

async function main() {
  console.log('Initiating autonomous Docker sovereignty audit and stakeholder collaboration sync...');

  const state: any = {
    timestamp: new Date().toISOString(),
    dockerInfo: null,
    dockerPs: null,
  };

  try {
    console.log('Running docker info...');
    const { stdout: infoOutput } = await execAsync('docker info');
    state.dockerInfo = infoOutput;
  } catch (error: any) {
    console.error('Failed to run docker info:', error.message);
    state.dockerInfo = 'Error: ' + error.message;
  }

  try {
    console.log('Running docker ps...');
    const { stdout: psOutput } = await execAsync('docker ps');
    state.dockerPs = psOutput;
  } catch (error: any) {
    console.error('Failed to run docker ps:', error.message);
    state.dockerPs = 'Error: ' + error.message;
  }

  const outputPath = 'autonomous_state.json';
  await fs.writeFile(outputPath, JSON.stringify(state, null, 2));
  console.log(`Audit complete. State written to ${outputPath}`);

  console.log('Running engine system collaboration sync...');
  try {
    await syncCollaborationState();
    console.log('Engine collaboration sync complete.');
  } catch (error: any) {
     console.error('Failed to sync collaboration state:', error.message);
  }
}

main().catch(console.error);
