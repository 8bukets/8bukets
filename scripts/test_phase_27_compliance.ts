import * as fs from 'fs';
import * as path from 'path';

async function testCompliance() {
  console.log('🧪 Starting Phase 27 Compliance Audit...');
  let failures = 0;

  // 1. Audit AGENTS.md
  const agentsMd = fs.readFileSync('AGENTS.md', 'utf8');
  if (agentsMd.includes('Phase 27 (Multi-Universal Resonance) Standards') &&
      agentsMd.includes('0.008ms') &&
      agentsMd.includes('0.999995')) {
    console.log('✅ AGENTS.md complies with Phase 27 standards.');
  } else {
    console.error('❌ AGENTS.md FAILS Phase 27 compliance.');
    failures++;
  }

  // 2. Audit Presence Service
  const presenceTs = fs.readFileSync('antigravity/services/presence.ts', 'utf8');
  if (presenceTs.includes("version: '1.7.0-mur'") &&
      presenceTs.includes('phase27: z.object({')) {
    console.log('✅ Presence service complies with Phase 27 standards.');
  } else {
    console.error('❌ Presence service FAILS Phase 27 compliance.');
    failures++;
  }

  // 3. Audit Swarm Heartbeat
  const heartbeatTs = fs.readFileSync('antigravity/services/swarm_heartbeat.ts', 'utf8');
  if (heartbeatTs.includes('0.999995') && heartbeatTs.includes('0.008')) {
    console.log('✅ Swarm Heartbeat complies with Phase 27 metrics.');
  } else {
    console.error('❌ Swarm Heartbeat FAILS Phase 27 metrics.');
    failures++;
  }

  // 4. Audit Evolution Engine
  const evolutionTs = fs.readFileSync('antigravity/evolution.ts', 'utf8');
  if (evolutionTs.includes('Rule 37: Phase 27 Multi-Universal Resonance Compliance') &&
      evolutionTs.includes('PHASE_27_MUR_VIOLATION')) {
    console.log('✅ Evolution Engine complies with Rule 37.');
  } else {
    console.error('❌ Evolution Engine FAILS Rule 37 compliance.');
    failures++;
  }

  if (failures === 0) {
    console.log('\n🏆 ALL PHASE 27 COMPLIANCE CHECKS PASSED.');
    process.exit(0);
  } else {
    console.error(`\n💥 PHASE 27 COMPLIANCE FAILED WITH ${failures} ERRORS.`);
    process.exit(1);
  }
}

testCompliance().catch(err => {
  console.error('💥 Compliance test execution failed:', err);
  process.exit(1);
});
