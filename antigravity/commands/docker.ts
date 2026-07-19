import { Command } from 'commander';
import { exec as execCallback, spawn } from 'child_process';
import { promisify } from 'util';
const exec = promisify(execCallback);

export function registerDockerCommands(program: Command, c: any) {
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
                stdio: 'inherit',
            });

            dockerProcess.on('error', (err) => {
                console.error(`${c.fg.red}Failed to execute 'docker compose logs'. Is Docker running?${c.reset}`);
                console.error(err);
            });

            dockerProcess.on('close', (code) => {
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
}
