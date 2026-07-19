import { Command } from 'commander';
import { getSystemInsights, clearLogBuffer } from '../core';
import { observeKnowledge } from '../services/knowledge';

export function registerLogsCommands(program: Command, c: any) {
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
}
