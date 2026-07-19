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
import { syncCollaborationState } from './services/collaboration';
import { observeKnowledge } from './services/knowledge';
import { getSystemInsights, healthCheck, clearLogBuffer } from './core';
import { runSequentialAgents } from './run_parallel';
import { workOrderService } from './services/work_order';
import { exec as execCallback, spawn } from 'child_process';
import { promisify } from 'util';
const exec = promisify(execCallback);

// --- Color constants for better readability ---
const c = {
    reset: "\x1b[0m",
    bright: "\x1b[1m",
    dim: "\x1b[2m",
    fg: {
        black: "\x1b[30m",
        red: "\x1b[31m",
        green: "\x1b[32m",
        yellow: "\x1b[33m",
        blue: "\x1b[34m",
        magenta: "\x1b[35m",
        cyan: "\x1b[36m",
        white: "\x1b[37m",
        gray: "\x1b[90m"
    },
};

const program = new Command();

program
    .name('antigravity')
    .description('CLI for the Antigravity Autonomous Ecosystem')
    .version('1.0.0');

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
    .command('collaborate')
    .description('Run a full multi-agent collaboration cycle (agents:run + sync).')
    .action(async () => {
        console.log(`\n${c.bright}${c.fg.magenta}🤝 [CLI] Initiating full multi-agent collaboration cycle...${c.reset}`);

        console.log(`\n${c.bright}--- 1. Executing Specialized Agent Pulses ---${c.reset}`);
        await runSequentialAgents();
        console.log(`${c.bright}--- ✅ Agent pulses complete ---${c.reset}\n`);

        console.log(`${c.bright}--- 2. Synchronizing Collaboration State & Merging Insights ---${c.reset}`);
        await syncCollaborationState();
        console.log(`${c.bright}--- ✅ Collaboration state synchronized ---${c.reset}\n`);

        console.log(`${c.fg.green}✅ [CLI] Multi-agent collaboration cycle complete.${c.reset}`);
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

        const cbStatusColor = (status: string) => {
            switch (status) {
                case 'closed': return c.fg.green;
                case 'open': return c.fg.red;
                case 'half-open': return c.fg.yellow;
                default: return c.reset;
            }
        };

        console.log(`\n${c.bright}${c.fg.cyan}--- 📊 Antigravity System Status ---${c.reset}`);
        console.log(`\n🕒 Uptime: ${c.fg.yellow}${Math.floor(insights.uptime / 60)} minutes${c.reset}`);

        console.log(`\n${c.bright}${c.fg.cyan}--- ❤️ System Health ---${c.reset}`);
        console.log(`  MongoDB Circuit Breaker: ${cbStatusColor(insights.circuitBreakers.mongodb)}${insights.circuitBreakers.mongodb}${c.reset}`);
        console.log(`  Supabase Circuit Breaker: ${cbStatusColor(insights.circuitBreakers.supabase)}${insights.circuitBreakers.supabase}${c.reset}`);

        console.log(`\n${c.bright}${c.fg.cyan}--- 🛡️ Cognitive Security ---${c.reset}`);
        const securityStatusColor = insights.security.status === 'secure' ? c.fg.green : c.fg.red;
        const issuesColor = insights.security.issuesFound > 0 ? c.fg.red : c.fg.green;
        console.log(`  Status: ${securityStatusColor}${insights.security.status}${c.reset}`);
        console.log(`  Issues Found: ${issuesColor}${insights.security.issuesFound}${c.reset}`);
        console.log(`  Files Scanned: ${c.fg.yellow}${insights.security.scannedFiles}${c.reset}`);
        console.log(`  Last Audit: ${c.dim}${new Date(insights.security.lastAudit).toLocaleString()}${c.reset}`);

        console.log(`\n${c.bright}${c.fg.cyan}--- 🧠 Cognitive Insights & Proposals ---${c.reset}`);
        if (insights.ideas.length > 0) {
            console.log('  New Ideas Synthesized:');
            insights.ideas.forEach((idea: any) => console.log(`    - ${c.fg.magenta}[${idea.complexity}]${c.reset} ${idea.feature}: ${c.dim}${idea.rationale}${c.reset}`));
        } else {
            console.log(`  ${c.dim}No new ideas synthesized.${c.reset}`);
        }
        if (insights.proposals.length > 0) {
            console.log('\n  Predictive Refactors:');
            insights.proposals.forEach((p: any) => console.log(`    - ${c.fg.blue}[${p.vector.toUpperCase()}]${c.reset} ${p.proposal} ${c.dim}(Impact: ${(p.impactScore * 100).toFixed(0)}%)${c.reset}`));
        } else {
            console.log(`\n  ${c.dim}No predictive refactors proposed.${c.reset}`);
        }

        console.log(`\n${c.bright}${c.fg.cyan}--- 🗄️ Caching & Persistence ---${c.reset}`);
        console.log(`  Volatility Registry Size: ${c.fg.yellow}${insights.caching.registrySize}${c.reset}`);
        if (insights.persistence.length > 0) {
            console.log('\n  Persistence Fleet:');
            insights.persistence.forEach((p: any) => {
                const statusColor = p.status === 'healthy' ? c.fg.green : c.fg.yellow;
                console.log(`    - ${p.agent}: ${statusColor}${p.status}${c.reset} ${c.dim}(PID: ${p.pid || 'N/A'})${c.reset}`);
            });
        }

        console.log('✅ [CLI] System status report complete.');
    });

const logsCommand = program.command('logs').description('Manage autonomous action logs.');

logsCommand
    .command('show')
    .description('Show the latest autonomous action logs from the in-memory buffer.')
    .action(async () => {
        console.log('📜 [CLI] Fetching latest autonomous logs...');
        const { logs } = await getSystemInsights();
        if (!logs || logs.length === 0) {
            console.log(`${c.dim}No logs available in the current buffer.${c.reset}`);
        } else {
            logs.forEach((log: { time: string; type: string; msg: string }) => {
                let typeColor = c.fg.yellow;
                const typeUpper = log.type.toUpperCase();
                if (typeUpper === 'INFO') typeColor = c.fg.green;
                if (typeUpper === 'ROI') typeColor = c.fg.blue;
                if (typeUpper === 'ERROR' || typeUpper === 'WARN' || typeUpper === 'SECURITY') typeColor = c.fg.red;
                if (typeUpper === 'SYSTEM' || typeUpper === 'COGNITIVE') typeColor = c.fg.magenta;

                console.log(`${c.fg.gray}[${log.time}]${c.reset} ${typeColor}[${typeUpper}]${c.reset} ${log.msg}`);
            });
        }
        console.log('✅ [CLI] Log display complete.');
    });

logsCommand
    .command('clear')
    .description('Clear the in-memory autonomous log buffer.')
    .action(() => {
        console.log('🗑️  [CLI] Clearing in-memory log buffer...');
        clearLogBuffer();
        console.log('✅ [CLI] Log buffer cleared.');
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

const dockerCommand = program.command('docker').description('Manage core Docker services.');

dockerCommand
    .command('status')
    .description('Show the status of the core Docker containers (MongoDB, etc.).')
    .action(async () => {
        console.log('🐳 [CLI] Checking status of Docker services...');
        const dockerComposeDir = '/Users/filipkeser/Documents/Antigravity';

        try {
            const { stdout, stderr } = await exec('docker compose ps', {
                cwd: dockerComposeDir,
            });

            if (stderr && !stdout) {
                console.error(`${c.fg.red}Error checking Docker status:${c.reset}\n${stderr}`);
                return;
            }

            console.log(`\n${c.bright}${c.fg.cyan}--- 🐳 Docker Service Status ---${c.reset}\n`);
            console.log(stdout);

            if (stderr) {
                console.warn(`${c.fg.yellow}Warnings from Docker:${c.reset}\n${stderr}`);
            }

            console.log('✅ [CLI] Docker status check complete.');
        } catch (error: any) {
            console.error(`${c.fg.red}Failed to execute 'docker compose ps'. Is Docker running and is the project at '${dockerComposeDir}'?${c.reset}`);
            if (error.stderr) {
                console.error(error.stderr);
            }
        }
    });

dockerCommand
    .command('up')
    .description('Start the core Docker containers in detached mode (docker compose up -d).')
    .action(async () => {
        console.log('🐳 [CLI] Starting Docker services...');
        const dockerComposeDir = '/Users/filipkeser/Documents/Antigravity';

        try {
            const { stdout, stderr } = await exec('docker compose up -d', {
                cwd: dockerComposeDir,
            });

            if (stdout) {
                console.log(stdout);
            }
            if (stderr) {
                // Log stderr as a warning as it often contains non-critical info like "network already exists"
                console.warn(`${c.fg.yellow}Output from Docker (stderr):${c.reset}\n${stderr}`);
            }

            console.log('✅ [CLI] Docker `up` command finished.');
        } catch (error: any) {
            console.error(`${c.fg.red}Failed to execute 'docker compose up -d'. Is Docker running?${c.reset}`);
            if (error.stderr) {
                console.error(error.stderr);
            }
        }
    });

dockerCommand
    .command('down')
    .description('Stop and remove the core Docker containers (docker compose down).')
    .action(async () => {
        console.log('🐳 [CLI] Stopping Docker services...');
        const dockerComposeDir = '/Users/filipkeser/Documents/Antigravity';

        try {
            const { stdout, stderr } = await exec('docker compose down', {
                cwd: dockerComposeDir,
            });

            if (stdout) {
                console.log(stdout);
            }
            if (stderr) {
                console.warn(`${c.fg.yellow}Output from Docker (stderr):${c.reset}\n${stderr}`);
            }

            console.log('✅ [CLI] Docker `down` command finished.');
        } catch (error: any) {
            console.error(`${c.fg.red}Failed to execute 'docker compose down'. Is Docker running?${c.reset}`);
            if (error.stderr) {
                console.error(error.stderr);
            }
        }
    });

dockerCommand
    .command('logs [service]')
    .description('Tail the logs of a specific Docker service (or all services).')
    .action((service) => {
        const serviceName = service || 'all services';
        console.log(`🐳 [CLI] Tailing logs for service: ${c.fg.cyan}${serviceName}${c.reset}. Press Ctrl+C to exit.`);
        const dockerComposeDir = '/Users/filipkeser/Documents/Antigravity';

        const args = ['compose', 'logs', '--follow'];
        if (service) {
            args.push(service);
        }

        const dockerProcess = spawn('docker', args, {
            cwd: dockerComposeDir,
            stdio: 'inherit', // Pipe child process's stdio to the parent for real-time output
        });

        dockerProcess.on('error', (err) => {
            console.error(`${c.fg.red}Failed to execute 'docker compose logs'. Is Docker running?${c.reset}`);
            console.error(err);
        });

        // This event fires when the user stops the process (e.g., with Ctrl+C)
        dockerProcess.on('close', (code) => {
            // A null code means termination by signal (like Ctrl+C), which is a normal exit for this command.
            if (code !== 0 && code !== null) {
                console.log(`\n${c.fg.yellow}Log tailing process exited unexpectedly with code ${code}.${c.reset}`);
            }
        });
    });

dockerCommand
    .command('restart <service>')
    .description('Restart a specific Docker service.')
    .action(async (service) => {
        console.log(`🐳 [CLI] Restarting Docker service: ${c.fg.cyan}${service}${c.reset}...`);
        const dockerComposeDir = '/Users/filipkeser/Documents/Antigravity';

        try {
            const { stdout, stderr } = await exec(`docker compose restart ${service}`, {
                cwd: dockerComposeDir,
            });

            if (stdout) {
                console.log(stdout);
            }
            if (stderr) {
                console.warn(`${c.fg.yellow}Output from Docker (stderr):${c.reset}\n${stderr}`);
            }

            console.log(`✅ [CLI] Service '${c.fg.cyan}${service}${c.reset}' restarted.`);
        } catch (error: any) {
            console.error(`${c.fg.red}Failed to execute 'docker compose restart ${service}'. Is Docker running and is the service name correct?${c.reset}`);
            if (error.stderr) {
                console.error(error.stderr);
            }
        }
    });

dockerCommand
    .command('prune')
    .description('Remove unused Docker data (containers, networks, volumes, images).')
    .option('-a, --all', 'Remove all unused images, not just dangling ones.')
    .action(async (options) => {
        console.log(`🐳 [CLI] Pruning unused Docker data...`);

        const pruneCommand = `docker system prune --volumes -f ${options.all ? '-a' : ''}`.trim();
        console.log(`${c.dim}Executing: ${pruneCommand}${c.reset}`);

        try {
            const { stdout, stderr } = await exec(pruneCommand);

            if (stdout) {
                console.log(stdout);
            }
            if (stderr) {
                console.warn(`${c.fg.yellow}Output from Docker (stderr):${c.reset}\n${stderr}`);
            }

            console.log(`✅ [CLI] Docker prune complete.`);
        } catch (error: any) {
            console.error(`${c.fg.red}Failed to execute 'docker system prune'. Is Docker running?${c.reset}`);
            if (error.stderr) {
                console.error(error.stderr);
            }
        }
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

const testCommand = program.command('test').description('Run tests for the autonomous system.');

testCommand
    .command('e2e')
    .description('Run a full end-to-end test of the autonomous creation and execution cycle.')
    .action(() => {
        console.log('🧪 [CLI] Starting full end-to-end autonomous test...');
        console.log(`${c.dim}This will create and execute a new work order automatically via 'npm run autonomous-creation'.${c.reset}`);

        // We use spawn to get real-time output from the npm script
        const testProcess = spawn('npm', ['run', 'autonomous-creation'], {
            stdio: 'inherit', // Pipe output to our terminal, showing the script's progress in real-time.
            shell: true,      // Use shell for compatibility, especially on Windows.
        });

        testProcess.on('error', (err) => {
            console.error(`${c.fg.red}Failed to start the test process. Make sure 'npm' is in your PATH.${c.reset}`);
            console.error(err);
        });

        testProcess.on('close', (code) => {
            if (code !== 0) {
                console.error(`\n${c.fg.red}❌ [CLI] End-to-end autonomous test script failed with exit code ${code}.${c.reset}`);
            }
        });
    });

program.parse(process.argv);

if (!process.argv.slice(2).length) {
    program.outputHelp();
}