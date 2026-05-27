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

program.parse();
