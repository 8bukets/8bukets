#!/usr/bin/env node
/**
 * ANTIGRAVITY AUTONOMOUS ECOSYSTEM
 * Command-Line Interface (CLI)
 *
 * This utility provides a unified entrypoint for managing and interacting
 * with the various components of the Antigravity system.
 */

import { Command, Option } from 'commander';
import { evolve, applyFixes } from './evolution';
import { jules } from './jules';
import { syncCollaborationState } from './services/collaboration'
import { observeKnowledge } from './services/knowledge'
import { getSystemInsights, healthCheck } from './core'
import { runSequentialAgents } from './run_parallel';
import { workOrderService } from './services/work_order';

const program = new Command();

program
    .name('agy')
    .description('CLI for the Antigravity Autonomous Ecosystem')
    .version('1.1.0');

program
    .command('evolve')
    .description('Run the cognitive evolution engine to analyze the codebase.')
    .option('--apply-fixes', 'Automatically apply suggested fixes.')
    .action(async (options) => {
        console.log('🧠 [CLI] Initiating cognitive evolution scan...');
        const suggestions = await evolve();
        if (options.applyFixes) {
            await applyFixes(suggestions);
        }
        console.log('✅ [CLI] Evolution scan complete.');
    });

program
    .command('sync')
    .description('Synchronize the autonomous collaboration state and merge insights.')
    .action(async () => {
        console.log('🔄 [CLI] Synchronizing collaboration state...');
        await syncCollaborationState();
        console.log('✅ [CLI] Collaboration state synchronized.');
    });

program
    .command('health')
    .description('Run a health check on core system dependencies (MongoDB, Supabase).')
    .action(async () => {
        console.log('🩺 [CLI] Performing system health check...');
        const status = await healthCheck();
        console.log(JSON.stringify(status, null, 2));
        console.log('✅ [CLI] Health check complete.');
    });

program
    .command('status')
    .description('Show a comprehensive overview of the current system status and health.')
    .action(async () => {
        console.log('📊 [CLI] Gathering comprehensive system status...');
        const insights = await getSystemInsights();

        console.log('\n--- 📊 Antigravity System Status ---');
        console.log(`\n🕒 Uptime: ${Math.floor(insights.uptime / 60)} minutes`);

        console.log('\n--- ❤️ System Health ---');
        console.log(`  MongoDB Circuit Breaker: ${insights.circuitBreakers.mongodb}`);
        console.log(`  Supabase Circuit Breaker: ${insights.circuitBreakers.supabase}`);

        console.log('\n--- 🛡️ Cognitive Security ---');
        console.log(`  Status: ${insights.security.status}`);
        console.log(`  Issues Found: ${insights.security.issuesFound}`);
        console.log(`  Files Scanned: ${insights.security.scannedFiles}`);
        console.log(`  Last Audit: ${new Date(insights.security.lastAudit).toLocaleString()}`);

        console.log('\n--- 🧠 Cognitive Insights & Proposals ---');
        if (insights.ideas.length > 0) {
            console.log('  New Ideas Synthesized:');
            insights.ideas.forEach((idea: any) => console.log(`    - [${idea.complexity}] ${idea.feature}: ${idea.rationale}`));
        } else {
            console.log('  No new ideas synthesized.');
        }
        if (insights.proposals.length > 0) {
            console.log('\n  Predictive Refactors:');
            insights.proposals.forEach((p: any) => console.log(`    - [${p.vector.toUpperCase()}] ${p.proposal} (Impact: ${(p.impactScore * 100).toFixed(0)}%)`));
        } else {
            console.log('\n  No predictive refactors proposed.');
        }

        console.log('\n--- 🗄️ Caching & Persistence ---');
        console.log(`  Volatility Registry Size: ${insights.caching.registrySize}`);
        if (insights.persistence.length > 0) {
            console.log('\n  Persistence Fleet:');
            insights.persistence.forEach((p: any) => console.log(`    - ${p.agent}: ${p.status} (PID: ${p.pid || 'N/A'})`));
        }

        console.log('✅ [CLI] System status report complete.');
    });

program
    .command('logs')
    .description('Show the latest autonomous action logs from the in-memory buffer.')
    .action(async () => {
        console.log('📜 [CLI] Fetching latest autonomous logs...');
        const { logs } = await getSystemInsights();
        if (!logs || logs.length === 0) {
            console.log('No logs available in the current buffer.');
        } else {
            logs.forEach((log: any) => {
                console.log(`[${log.time}] [${log.type.toUpperCase()}] ${log.msg}`);
            });
        }
        console.log('✅ [CLI] Log display complete.');
    });

program
    .command('knowledge:observe <url>')
    .description('Scan and observe a URL for market intelligence.')
    .action(async (url) => {
        console.log(`🧠 [CLI] Observing ${url} for knowledge...`);
        await observeKnowledge(url);
        console.log(`✅ [CLI] Observation of ${url} complete.`);
    });

const julesCommand = program.command('jules').description('Commands for the Jules AI agent.');

julesCommand
    .command('daily')
    .description("Trigger Jules' autonomous daily work cycle.")
    .action(async () => {
        console.log("🤖 [CLI] Triggering Jules' daily routine...");
        await jules.runDailyRoutine();
        console.log("✅ [CLI] Jules' daily routine complete.");
    });

program
    .command('agents:run')
    .description('Run specialized agents sequentially to perform work cycles.')
    .action(async () => {
        console.log('🚀 [CLI] Executing sequential agent run...');
        await runSequentialAgents();
        console.log('✅ [CLI] Sequential agent run complete.');
    });

const workOrderCommand = program.command('work-orders').description('Manage autonomous work orders.');

workOrderCommand
    .command('list')
    .description('List pending work orders.')
    .action(() => {
        console.log('📋 [CLI] Listing pending work orders...');
        const pending = workOrderService.getPendingOrders();
        if (pending.length === 0) {
            console.log('No pending work orders.');
        } else {
            console.log(JSON.stringify(pending, null, 2));
        }
        console.log('✅ [CLI] Work order list complete.');
    });

workOrderCommand
    .command('execute')
    .description('Execute all pending work orders in sequence.')
    .action(async () => {
        console.log('⚡️ [CLI] Initiating execution of pending work orders...');
        await workOrderService.executePendingOrders();
        console.log('✅ [CLI] Work order execution cycle complete.');
    });

workOrderCommand
    .command('create <description>')
    .description('Create a new autonomous work order from the terminal.')
    .addOption(new Option('-p, --priority <level>', 'Set the priority for the work order').choices(['Low', 'Medium', 'High', 'Critical']).default('Medium'))
    .action((description, options) => {
        console.log('📝 [CLI] Creating new autonomous work order...');
        const newOrder = workOrderService.createOrder({
            description,
            priority: options.priority,
            source: 'cli',
        });
        console.log('✅ [CLI] New work order created successfully:');
        console.log(JSON.stringify(newOrder, null, 2));
    });

program.parse(process.argv);

if (!process.argv.slice(2).length) {
    program.outputHelp();
}