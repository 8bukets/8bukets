import { Command } from 'commander';
import { workOrderService } from '../services/work_order';

export function registerDeploymentCommands(program: Command, c: any) {
    const deploymentCommand = program.command('deployment').description('Manage deployments.');

    deploymentCommand
        .command('status')
        .description('Show the status of the most recent deployment.')
        .action(() => {
            console.log('🛰️  [CLI] Fetching status of most recent deployment...');

            const deploymentOrders = ((workOrderService as any).orders || [])
                .filter((o: any) => o.type === 'DEPLOYMENT' && (o.status === 'completed' || o.status === 'failed'));

            if (deploymentOrders.length === 0) {
                console.log(`${c.dim}No deployment attempts found.${c.reset}`);
                return;
            }

            // Sort by completed_at date to find the most recent one
            deploymentOrders.sort((a: any, b: any) => {
                if (!a.completed_at || !b.completed_at) return 0;
                return new Date(b.completed_at).getTime() - new Date(a.completed_at).getTime();
            });

            const latestDeployment = deploymentOrders[0];

            const statusColor = latestDeployment.status === 'completed' ? c.fg.green : c.fg.red;

            console.log(`\n${c.bright}${c.fg.cyan}--- 🛰️  Most Recent Deployment ---${c.reset}`);
            console.log(`  ID:       ${c.fg.gray}${latestDeployment.id}${c.reset}`);
            console.log(`  Goal:     ${latestDeployment.goal}`);
            console.log(`  Status:   ${statusColor}${latestDeployment.status.toUpperCase()}${c.reset}`);
            if (latestDeployment.completed_at) {
                console.log(`  Finished: ${c.dim}${new Date(latestDeployment.completed_at).toLocaleString()}${c.reset}`);
            }
            if (latestDeployment.status === 'completed' && latestDeployment.result) {
                console.log(`  Result:   ${c.fg.green}DEPLOYED SUCCESSFULLY${c.reset}`);
            } else if (latestDeployment.error) {
                console.log(`  Error:    ${c.fg.red}${latestDeployment.error}${c.reset}`);
            }

            console.log('\n✅ [CLI] Deployment status check complete.');
        });
}
