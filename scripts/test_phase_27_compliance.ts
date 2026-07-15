import { jules } from '../antigravity/jules';
import { onlinePresenceService } from '../antigravity/services/presence';
import fs from 'fs';

async function testCompliance() {
  console.log('🧪 Starting Phase 27 MUR Compliance Audit...');

  // 1. Audit AGENTS.md
  const agentsMd = fs.readFileSync('AGENTS.md', 'utf8');
  if (agentsMd.includes('Phase 27: Multi-Universal Resonance (Current)')) {
    console.log('✅ AGENTS.md updated to Phase 27.');
  } else {
    console.error('❌ AGENTS.md missing Phase 27 Current indicator.');
  }

  // 2. Audit Jules Engine
  console.log('🤖 Auditing Jules Engine...');
  const suggestions = await jules.improve();
  if (suggestions.suggestions.some(s => s.includes('Phase 27') && s.includes('MUR'))) {
    console.log('✅ Jules recognizes Phase 27 MUR knowledge.');
  } else {
    console.log('⚠️ Jules did not suggest Phase 27 MUR (maybe knowledge ingestion needs refresh).');
  }

  // 3. Audit Presence Service
  console.log('📡 Auditing Presence Service...');
  const posture = await onlinePresenceService.getSystemPosture();
  if (posture.telemetry.phase27) {
    console.log('✅ Presence includes Phase 27 telemetry.');
    console.log('   Resonance Latency:', posture.telemetry.phase27.resonance_latency);
    console.log('   Singularity Readiness:', posture.telemetry.phase27.singularity_readiness);
  } else {
    console.error('❌ Presence missing Phase 27 telemetry.');
  }

  console.log('🏁 Compliance Audit Complete.');
}

testCompliance().catch(console.error);
