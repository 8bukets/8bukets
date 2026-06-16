import { ConflictResolver } from './antigravity/utils/conflict_resolver';
import path from 'path';
import fs from 'fs';

async function main() {
    const files = fs.readFileSync('conflicted_files.txt', 'utf8').split('\n').filter(Boolean);
    for (const file of files) {
        await ConflictResolver.resolve(path.join(process.cwd(), file));
    }
}

main().catch(console.error);
