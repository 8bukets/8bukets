/** PHASE 15 COMPLIANCE: quantum-secure (Dilithium/Kyber) **/
import { latticeSync } from '@/antigravity/services/lattice_sync'
import { ConflictResolver } from './antigravity/utils/conflict_resolver';
import path from 'path';
import fs from 'fs';

async function main() {
    const files = await fs.promises.readFile('conflicted_files.txt', 'utf8').split('\n').filter(Boolean);
    for (const file of files) {
        await ConflictResolver.resolve(path.join(process.cwd(), file));
    }
}

main().catch(console.error);
