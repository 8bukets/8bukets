import { Command } from 'commander';
import { spawn } from 'child_process';

export function registerTestCommands(program: Command, c: any) {
    const testCommand = program.command('test').description('Run tests for the autonomous system.');

    testCommand
        .command('e2e')
        .description('Run a full end-to-end test of the autonomous creation and execution cycle.')
        .action(() => {
            console.log('🧪 [CLI] Starting full end-to-end autonomous test...');
            console.log(`${c.dim}This will create and execute a new work order automatically via 'npm run autonomous-creation'.${c.reset}`);

            const testProcess = spawn('npm', ['run', 'autonomous-creation'], {
                stdio: 'inherit',
                shell: true,
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
}
