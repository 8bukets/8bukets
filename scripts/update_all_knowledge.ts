import { jules } from '../antigravity/jules';
import { execSync } from 'child_process';

/**
 * TRIGGER SCRIPT: UPDATE ALL KNOWLEDGE
 * Orchestrates scrapers and invokes Jules to update the unified system knowledge.
 */

async function main() {
    console.log('🚀 [Update] Starting full knowledge update cycle...');

    try {
        // 1. Run Google Innovation Scraper
        console.log(' - Running Google Innovation & AI scraper...');
        execSync('npx tsx scripts/ingest_google_innovation_knowledge.ts', { stdio: 'inherit' });

        // 2. Run Markposition Scraper (already integrated in Jules, but let's ensure it runs)
        console.log(' - Running Markposition scraper...');
        execSync('npx tsx scripts/ingest_markposition_knowledge.ts', { stdio: 'inherit' });

        // 3. Invoke Jules' Knowledge Observation
        // This will ingest local markdown and the newly generated JSON files into system_knowledge.json
        console.log(' - Invoking Jules cognitive observation...');
        await jules.observeKnowledge();

        console.log('✅ [Update] Knowledge update cycle complete.');
    } catch (error) {
        console.error('❌ [Update] Knowledge update cycle failed:', error);
        process.exit(1);
    }
}

main().catch(console.error);
