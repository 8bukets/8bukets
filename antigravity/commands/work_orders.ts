/** PHASE 16 COMPLIANCE: swarm-heartbeat (interval: 5s) **/
import { swarmHeartbeat } from '@/antigravity/services/swarm_heartbeat'
/** PHASE 15 COMPLIANCE: quantum-secure (Dilithium/Kyber) **/
import { latticeSync } from '@/antigravity/services/lattice_sync'
import { Command, Option } from 'commander';
import { workOrderService } from '../services/work_order';

export function registerWorkOrderCommands(program: Command, c: any) {
    const workOrderCommand = program.command('work-orders').description('Manage autonomous work orders.');

    workOrderCommand
        .command('list')
        .description('List pending work orders.')
        .action(() => {
            console.log('📋 [CLI] Listing pending work orders...');
            const pending = workOrderService.getPendingOrders();
            if (pending.length === 0) {
                console.log(`${c.dim}No pending work orders.${c.reset}`);
            } else {
                const idWidth = 15;
                const goalWidth = 50;
                const typeWidth = 20;
                const complexityWidth = 12;

                // Header
                console.log(
                    `\n  ${c.bright}${c.fg.cyan}${'ID'.padEnd(idWidth)}${'Goal'.padEnd(goalWidth)}${'Type'.padEnd(typeWidth)}${'Complexity'.padEnd(complexityWidth)}Created At${c.reset}`
                );
                console.log(`  ${c.dim}${'─'.repeat(idWidth - 1)} ${'─'.repeat(goalWidth - 1)} ${'─'.repeat(typeWidth - 1)} ${'─'.repeat(complexityWidth - 1)} ${'─'.repeat(20)}${c.reset}`);

                pending.forEach(order => {
                    const goal = order.goal.length > goalWidth - 3 ? order.goal.substring(0, goalWidth - 6) + '...' : order.goal;

                    let complexity = 'N/A';
                    if (order.type === 'BOOTSTRAP_SERVICE' && order.payload.complexity) {
                        complexity = order.payload.complexity;
                    } else if (order.type === 'META_CORRECTION' && order.payload.findings?.length > 0) {
                        const severities = order.payload.findings.map(f => f.severity);
                        if (severities.includes('critical')) complexity = 'Critical';
                        else if (severities.includes('warning')) complexity = 'High';
                        else complexity = 'Medium';
                    }

                    const complexityColor = {
                        'Low': c.fg.green,
                        'Medium': c.fg.yellow,
                        'High': c.fg.red,
                        'Critical': `${c.bright}${c.fg.red}`
                    }[complexity] || c.reset;

                    console.log(
                        `  ${c.fg.gray}${order.id.padEnd(idWidth)}${c.reset}${goal.padEnd(goalWidth)}${c.fg.magenta}${order.type.padEnd(typeWidth)}${c.reset}${complexityColor}${complexity.padEnd(complexityWidth)}${c.reset}${c.dim}${new Date(order.created_at).toLocaleString()}${c.reset}`
                    );
                });
                console.log(); // Newline for spacing
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
}
