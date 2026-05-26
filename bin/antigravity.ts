import { Command } from 'commander';
import { spawn } from 'child_process';
import path from 'path';

const program = new Command();

program
  .name('antigravity')
  .description('CLI tool for Antigravity autonomous system')
  .version('0.1.0');

function runCommand(command: string, args: string[]) {
  const child = spawn(command, args, { stdio: 'inherit', shell: true });
  child.on('error', (error) => {
    console.error(`Error executing command: ${error.message}`);
  });
  child.on('exit', (code) => {
    process.exit(code ?? 0);
  });
}

program
  .command('daily')
  .description('Run autonomous daily sync')
  .action(() => {
    runCommand('npx', ['tsx', '--env-file=.env', 'scripts/autonomous_sync.ts']);
  });

program
  .command('explore')
  .description('Run explorer')
  .action(() => {
    runCommand('npx', ['tsx', '--env-file=.env', 'antigravity/explorer.ts']);
  });

program
  .command('evolve')
  .description('Run evolution')
  .action(() => {
    runCommand('npx', ['tsx', '--env-file=.env', 'antigravity/evolution.ts']);
  });

program
  .command('ignite')
  .description('Run daily continuously (ignite)')
  .action(() => {
    runCommand('npx', ['tsx', '--env-file=.env', 'antigravity/run_daily.ts', '--continuous']);
  });

program
  .command('creation')
  .description('Execute creation cycle')
  .action(() => {
    runCommand('npx', ['tsx', '--env-file=.env', 'scripts/execute_creation_cycle.ts']);
  });

program.parse(process.argv);
