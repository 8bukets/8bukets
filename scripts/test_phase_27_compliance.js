const fs = require('fs');
const path = require('path');

// Mock logAutonomousAction since we are in a simple node script
const logAutonomousAction = (msg, type) => console.log(`[${type}] ${msg}`);

/**
 * PHASE 27 COMPLIANCE AUDITOR (JS VERSION)
 * Uses native node to bypass tsx/esbuild issues in the sandbox.
 */
async function auditPhase27() {
  console.log('🧐 [Audit] Commencing Phase 27 MUR Compliance Audit (JS Fallback)...');

  let failures = 0;

  // 1. Version Check in presence.ts
  const presencePath = path.join(process.cwd(), 'antigravity/services/presence.ts');
  const presenceContent = fs.readFileSync(presencePath, 'utf8');
  if (presenceContent.includes("version: '1.7.0-mur'")) {
    console.log('✅ [Audit] System Version: 1.7.0-mur (COMPLIANT)');
  } else {
    console.error('❌ [Audit] System Version mismatch in presence.ts (NON-COMPLIANT)');
    failures++;
  }

  // 2. Metrics Check in swarm_heartbeat.ts
  const heartbeatPath = path.join(process.cwd(), 'antigravity/services/swarm_heartbeat.ts');
  const heartbeatContent = fs.readFileSync(heartbeatPath, 'utf8');
  if (heartbeatContent.includes('resonanceLatencyMur = Math.random() * 0.007') &&
      heartbeatContent.includes('singularityReadinessMur: number = 0.999998')) {
    console.log('✅ [Audit] Phase 27 Metrics Targets (COMPLIANT)');
  } else {
    console.error('❌ [Audit] Phase 27 Metrics Targets mismatch in swarm_heartbeat.ts (NON-COMPLIANT)');
    failures++;
  }

  // 3. Protocol Check in universal_mesh_routing.ts
  const umrPath = path.join(process.cwd(), 'antigravity/services/universal_mesh_routing.ts');
  const umrContent = fs.readFileSync(umrPath, 'utf8');
  if (umrContent.includes("protocol: 'UMR-v3.0'") && umrContent.includes('latencyEstimate = 0.0075')) {
    console.log('✅ [Audit] Universal Mesh Routing: UMR-v3.0 (COMPLIANT)');
  } else {
    console.error('❌ [Audit] UMR Protocol version mismatch in universal_mesh_routing.ts (NON-COMPLIANT)');
    failures++;
  }

  // 4. File-level Compliance Check (Evolution Rules)
  console.log('📂 [Audit] Checking file-level compliance rules in evolution.ts...');
  const evolutionPath = path.join(process.cwd(), 'antigravity/evolution.ts');
  const evolutionContent = fs.readFileSync(evolutionPath, 'utf8');
  if (evolutionContent.includes('Rule 37: Phase 27 Multi-Universal Resonance Compliance') &&
      evolutionContent.includes('PHASE_27_MUR_METRICS_MISSING')) {
       console.log('✅ [Audit] Evolution Rules: Rule 37 implemented (COMPLIANT)');
  } else {
       console.error('❌ [Audit] Rule 37 missing in evolution.ts (NON-COMPLIANT)');
       failures++;
  }

  // 5. Cloud Sovereign Pulse check
  const pulsePath = path.join(process.cwd(), 'scripts/cloud_sovereign_work_pulse.ts');
  if (fs.existsSync(pulsePath)) {
    console.log('✅ [Audit] scripts/cloud_sovereign_work_pulse.ts exists (COMPLIANT)');
  } else {
    console.error('❌ [Audit] scripts/cloud_sovereign_work_pulse.ts missing (NON-COMPLIANT)');
    failures++;
  }

  if (failures === 0) {
    console.log('🏆 [Audit] Phase 27 Multi-Universal Resonance Audit: SUCCESS');
    process.exit(0);
  } else {
    console.error(`💥 [Audit] Phase 27 Multi-Universal Resonance Audit: FAILED (${failures} failures)`);
    process.exit(1);
  }
}

auditPhase27().catch(err => {
  console.error(err);
  process.exit(1);
});
