#!/usr/bin/env npx tsx

import { Command } from 'commander';
import { observeKnowledge } from './antigravity/services/knowledge';
import { Jules } from './antigravity/jules';

const program = new Command();

program
  .name('antigravity')
  .description('Google Antigravity CLI - Build the new way autonomously')
  .version('1.0.0');

program
  .command('ignite')
  .description('Ignite the autonomous swarm')
  .action(async () => {
    console.log('🚀 Igniting the Antigravity Swarm...');
    const jules = await Jules.create('General');
    await jules.processPendingTasks();
    console.log('✅ Swarm ignited.');
  });

program
  .command('ignite-cloud-presence')
  .description('Ignite continuous cloud presence and ecosystem collaboration setup for remote environments')
  .action(async () => {
    console.log('🚀 Igniting Cloud Presence and Docker Ecosystem Connectivity...');
    process.env.MACBOOK_CLOUD_SIMULATION = 'true';
    process.env.AUTONOMOUS_MODE = 'cloud';
    try {
      const { spawn } = require('child_process');
      const child = spawn('npm', ['run', 'connect'], { stdio: 'inherit', shell: true });
      child.on('error', (error: Error) => {
        console.error(`Error executing connect: ${error.message}`);
      });
      child.on('exit', (code: number | null) => {
        if (code !== 0) {
          console.error(`Connect process exited with code ${code}`);
        } else {
          console.log('✅ Cloud presence ignited and connectivity synced.');
        }
      });
    } catch (err) {
      console.error(`❌ Cloud presence ignition failed: ${err}`);
      process.exit(1);
    }
  });

program
  .command('observe <url>')
  .description('Ingest knowledge from a given URL into the neural mesh')
  .action(async (url) => {
    console.log(`🧠 Observing knowledge from ${url}...`);
    try {
      const result = await observeKnowledge(url);
      console.log(`✅ Successfully observed: ${result.title}`);
    } catch (err) {
      console.error(`❌ Observation failed: ${err}`);
      process.exit(1);
    }
  });

program
  .command('workflow')
  .description('Generate automated workflow pipelines')
  .action(() => {
    const { spawn } = require('child_process');
    const child = spawn('npx', ['tsx', '--env-file=.env', 'scripts/autonomous_workflow_creation.ts'], { stdio: 'inherit', shell: true });
    child.on('error', (error: Error) => {
      console.error(`Error executing command: ${error.message}`);
    });
    child.on('exit', (code: number | null) => {
      if (code !== 0) {
        console.error(`Process exited with code ${code}`);
      }
    });
  });

program.parse();
