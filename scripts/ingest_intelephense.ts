import { intelephenseService } from '../antigravity/services/intelephense_service';

async function main() {
  console.log('🚀 Starting Intelephense documentation consolidation via Service...');
  await intelephenseService.consolidate();
  console.log('✨ Consolidation complete.');
}

main().catch(console.error);
