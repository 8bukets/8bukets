import { intelephenseService } from '../antigravity/services/intelephense_service';

/**
 * LEGACY INGESTION SCRIPT
 * Refactored to use the unified IntelephenseService consolidation logic.
 * Phase 13: Ensures single source of truth for documentation ingestion.
 */
async function main() {
  'use cache'
  console.log('🚀 Starting Intelephense documentation consolidation (Legacy Script Entry)...');
  await intelephenseService.consolidate();
  console.log('✨ Consolidation complete.');
}

main().catch(console.error);
