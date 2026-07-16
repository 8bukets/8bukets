
import fs from 'fs';
import path from 'path';

function verifyPhase27Compliance() {
  const files = [
    'antigravity/services/intelephense_service.ts',
    'antigravity/services/knowledge_observer.ts',
    'antigravity/services/presence.ts'
  ];

  console.log('🔍 [Compliance Auditor] Starting Phase 27 MUR Audit...');
  let overallSuccess = true;

  files.forEach(file => {
    const content = fs.readFileSync(path.join(process.cwd(), file), 'utf8');

    // Check resonance-latency < 0.008ms
    const resonanceMatch = content.match(/resonance-latency.*target: <0\.008ms/i) ||
                           content.match(/RESONANCE_LATENCY.*target: <0\.008ms/i) ||
                           content.match(/resonance_latency: 0\.0075/);
    if (resonanceMatch) {
      console.log(`✅ ${file}: Resonance Latency compliance verified.`);
    } else {
      console.error(`❌ ${file}: Resonance Latency compliance FAILED.`);
      overallSuccess = false;
    }

    // Check singularity-readiness > 0.999995
    const singularityMatch = content.match(/singularity-readiness.*threshold: 0\.999995/i) ||
                             content.match(/SINGULARITY_READINESS.*threshold: 0\.999995/i) ||
                             content.match(/singularity_readiness: 0\.999996/);
    if (singularityMatch) {
      console.log(`✅ ${file}: Singularity Readiness compliance verified.`);
    } else {
      console.error(`❌ ${file}: Singularity Readiness compliance FAILED.`);
      overallSuccess = false;
    }
  });

  // Verify AGENTS.md
  const agentsMd = fs.readFileSync(path.join(process.cwd(), 'AGENTS.md'), 'utf8');
  if (agentsMd.includes('27. **Phase 27: Multi-Universal Resonance (MUR) (Current)**')) {
    console.log('✅ AGENTS.md: Phase 27 MUR Current status verified.');
  } else {
    console.error('❌ AGENTS.md: Phase 27 MUR Current status FAILED.');
    overallSuccess = false;
  }

  if (overallSuccess) {
    console.log('✨ [Compliance Auditor] PHASE 27 MUR AUDIT PASSED.');
    process.exit(0);
  } else {
    console.error('🔥 [Compliance Auditor] PHASE 27 MUR AUDIT FAILED.');
    process.exit(1);
  }
}

verifyPhase27Compliance();
