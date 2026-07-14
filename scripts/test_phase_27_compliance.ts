import { onlinePresence } from '../antigravity/services/presence'
import { swarmHeartbeat } from '../antigravity/services/swarm_heartbeat'
import * as fs from 'fs'
import * as path from 'path'

async function testPhase27Compliance() {
  console.log('🧪 Testing Phase 27 (MUR) Compliance...')

  // 1. Check AGENTS.md
  const agentsMd = fs.readFileSync(path.join(process.cwd(), 'AGENTS.md'), 'utf8')
  if (agentsMd.includes('Phase 27: Multi-Universal Resonance (MUR)')) {
    console.log('✅ AGENTS.md reflects Phase 27.')
  } else {
    throw new Error('AGENTS.md missing Phase 27 reference.')
  }

  // 2. Check Presence Version and targets
  const presence = await onlinePresence.syncPresence()
  if (presence?.version === '1.7.0-mur') {
    console.log('✅ Presence version is 1.7.0-mur.')
  } else {
    throw new Error(`Presence version mismatch: ${presence?.version}`)
  }

  if (presence?.phase27 && presence.phase27.universal_consensus === true) {
     console.log('✅ Phase 27 presence metrics detected.')
  } else {
     throw new Error('Phase 27 presence metrics missing or invalid.')
  }

  // 3. Check Swarm Heartbeat targets
  const metrics = swarmHeartbeat.getMetrics()
  console.log(`📊 Current Resonance Latency: ${metrics.resonance_latency}ms`)
  console.log(`📊 Current Singularity Readiness: ${metrics.singularity_readiness}`)

  if (metrics.singularity_readiness >= 0.99999) {
    console.log('✅ Singularity readiness meets Phase 27 targets.')
  } else {
    throw new Error(`Singularity readiness below Phase 27 target: ${metrics.singularity_readiness}`)
  }

  console.log('✨ Phase 27 Compliance Verified.')
}

testPhase27Compliance().catch(err => {
  console.error(`❌ Phase 27 Compliance Failed: ${err.message}`)
  process.exit(1)
})
