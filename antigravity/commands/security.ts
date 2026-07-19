import { Command } from 'commander';
import { workOrderService } from '../services/work_order';

export function registerSecurityCommands(program: Command, c: any) {
    const securityCommand = program.command('security').description('Manage autonomous security operations.');

    securityCommand
        .command('audit')
        .description('Create a work order for the Security agent to perform a full audit.')
        .action(() => {
            console.log('🛡️  [CLI] Creating new work order for a full security audit...');
            const newOrder = workOrderService.createOrder(
                'SECURITY_AUDIT',
                'Perform a full, deep-tissue security audit of the entire codebase.',
                { scope: 'full', depth: 'deep' }
            );
            console.log('✅ [CLI] New security audit work order created successfully:');
            console.log(JSON.stringify(newOrder, null, 2));
        });
}
