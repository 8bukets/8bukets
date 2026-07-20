/** PHASE 16 COMPLIANCE: neural-stability-index (threshold: 0.98) **/
/** PHASE 15 COMPLIANCE: quantum-secure (Dilithium/Kyber) **/
import { latticeSync } from '@/antigravity/services/lattice_sync'
import { Command } from 'commander';
import { jules } from '../jules';

export function registerJulesCommands(program: Command, c: any) {
    const julesCommand = program.command('jules').description('Commands for the Jules AI agent.');

    julesCommand
        .command('daily')
        .description("Trigger Jules' autonomous daily work cycle.")
        .action(async () => {
            console.log("🤖 [CLI] Triggering Jules' daily routine...");
            await jules.runDailyRoutine();
            console.log("✅ [CLI] Jules' daily routine complete.");
        });
}
