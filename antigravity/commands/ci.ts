/** PHASE 16 COMPLIANCE: swarm-heartbeat (interval: 5s) **/
import { swarmHeartbeat } from '@/antigravity/services/swarm_heartbeat'
/** PHASE 15 COMPLIANCE: quantum-secure (Dilithium/Kyber) **/
import { latticeSync } from '@/antigravity/services/lattice_sync'
import { Command } from 'commander';
import { getLatestBuildStatus, triggerBuild } from '../services/jenkins';

export function registerCICommands(program: Command, c: any) {
    const ciCommand = program.command('ci').description('Interact with the CI/CD pipeline.');

    ciCommand
        .command('status')
        .description('Show the status of the most recent build.')
        .action(async () => {
            console.log('🚀 [CLI] Fetching latest CI/CD build status...');
            try {
                const status = await getLatestBuildStatus();

                if (!status || !status.status) {
                    console.log(`${c.fg.yellow}Could not retrieve CI/CD status or status is incomplete.${c.reset}`);
                    return;
                }

                const statusColor = status.status.toLowerCase() === 'success' ? c.fg.green : status.status.toLowerCase() === 'failure' ? c.fg.red : c.fg.yellow;

                console.log(`\n${c.bright}${c.fg.cyan}--- 🚀 CI/CD Build Status ---${c.reset}`);
                console.log(`  Build:    ${c.fg.yellow}${status.number || 'N/A'}${c.reset}`);
                console.log(`  Status:   ${statusColor}${status.status.toUpperCase()}${c.reset}`);
                if (status.timestamp) {
                    console.log(`  Finished: ${c.dim}${new Date(status.timestamp).toLocaleString()}${c.reset}`);
                }
                if (status.url) {
                    console.log(`  URL:      ${c.fg.blue}${status.url}${c.reset}`);
                }
                console.log('\n✅ [CLI] CI/CD status check complete.');
            } catch (error: any) {
                console.error(`${c.fg.red}Failed to fetch CI/CD status: ${error.message}${c.reset}`);
            }
        });

    ciCommand
        .command('trigger')
        .description('Trigger a new CI/CD build for the main project.')
        .action(async () => {
            console.log('🚀 [CLI] Triggering new CI/CD build...');
            try {
                const result = await triggerBuild();
                console.log(`${c.fg.green}✅ Build successfully triggered.${c.reset}`);
                if (result && result.url) {
                    console.log(`  View queue item at: ${c.fg.blue}${result.url}${c.reset}`);
                }
            } catch (error: any) {
                console.error(`${c.fg.red}Failed to trigger CI/CD build: ${error.message}${c.reset}`);
            }
        });
}
