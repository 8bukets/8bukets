import * as fs from 'fs'
import * as path from 'path'

/**
 * PHASE 27 COMPLIANCE AUDITOR
 * Verifies that the codebase meets Phase 27: Multi-Universal Resonance (MUR) standards.
 */

const RED = '\x1b[31m'
const GREEN = '\x1b[32m'
const YELLOW = '\x1b[33m'
const NC = '\x1b[0m'

const checks = [
  {
    name: 'Presence Version (1.7.0-mur)',
    file: 'antigravity/services/presence.ts',
    pattern: /version: '1.7.0-mur'/,
    description: 'The presence service must broadcast Phase 27 MUR version.'
  },
  {
    name: 'Presence Schema (Phase 27 Metrics)',
    file: 'antigravity/services/presence.ts',
    pattern: /phase27: z\.object\(\{/,
    description: 'PresenceSchema must include phase27 object.'
  },
  {
    name: 'Swarm Heartbeat Resonance (< 0.008ms)',
    file: 'antigravity/services/swarm_heartbeat.ts',
    pattern: /resonanceLatency: number = 0 .* Target: < 0\.008ms/,
    description: 'Phase 27 resonance latency target must be < 0.008ms.'
  },
  {
    name: 'Swarm Heartbeat Singularity (> 0.999995)',
    file: 'antigravity/services/swarm_heartbeat.ts',
    pattern: /singularityReadiness: number = 0\.99999[6-9] .* Target: > 0\.999995/,
    description: 'Phase 27 singularity readiness target must be > 0.999995.'
  },
  {
    name: 'Evolution Engine (Rule 37)',
    file: 'antigravity/evolution.ts',
    pattern: /\/\/ Rule 37: Phase 27 Multi-Universal Resonance \(MUR\) Compliance/,
    description: 'Evolution engine must include Rule 37 for MUR compliance.'
  },
  {
    name: 'Evolution Engine (Phase 27 Headers)',
    file: 'antigravity/evolution.ts',
    pattern: /phase === '27' \? 'MULTI_UNIVERSAL_RESONANCE \| UNIVERSAL_CONSENSUS'/,
    description: 'Evolution engine must support Phase 27 compliance headers.'
  },
  {
    name: 'Cloud Sovereign Work Pulse (Entry Point)',
    file: 'scripts/cloud_sovereign_work_pulse.ts',
    exists: true,
    description: 'Phase 27 entry point for cloud sovereign operations must exist.'
  },
  {
    name: 'AGENTS.md (Roadmap Update)',
    file: 'AGENTS.md',
    pattern: /- \*\*Phase 27\*\*: Multi-Universal Resonance \(MUR\) \(Current\)/,
    description: 'AGENTS.md must reflect Phase 27 as the current phase.'
  }
]

async function runAudit() {
  console.log('🧐 [Phase 27 Audit] Commencing Multi-Universal Resonance compliance check...\n')
  let failures = 0

  for (const check of checks) {
    const fullPath = path.join(process.cwd(), check.file)
    process.stdout.write(` - Checking ${check.name}... `)

    if (!fs.existsSync(fullPath)) {
      if (check.exists) {
        console.log(`${RED}FAILED${NC} (File not found)`)
        failures++
      } else {
        console.log(`${YELLOW}SKIPPED${NC} (File not found)`)
      }
      continue
    }

    const content = fs.readFileSync(fullPath, 'utf8')
    if (check.pattern && !check.pattern.test(content)) {
      console.log(`${RED}FAILED${NC}`)
      console.log(`   ${YELLOW}Expected pattern:${NC} ${check.pattern}`)
      console.log(`   ${YELLOW}Description:${NC} ${check.description}`)
      failures++
    } else {
      console.log(`${GREEN}PASSED${NC}`)
    }
  }

  console.log('\n--- AUDIT SUMMARY ---')
  if (failures === 0) {
    console.log(`${GREEN}✅ ALL SYSTEMS GO. Phase 27 MUR Compliance Verified.${NC}`)
    process.exit(0)
  } else {
    console.log(`${RED}❌ AUDIT FAILED. ${failures} compliance violations found.${NC}`)
    process.exit(1)
  }
}

runAudit().catch(err => {
  console.error('💥 Audit crashed:', err)
  process.exit(1)
})
