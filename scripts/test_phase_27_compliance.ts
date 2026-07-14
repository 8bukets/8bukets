import { swarmHeartbeat } from '../antigravity/services/swarm_heartbeat'
import { universalMeshRouting } from '../antigravity/services/universal_mesh_routing'
import { onlinePresence } from '../antigravity/services/presence'
import { chiefAIOfficerAgent } from '../antigravity/ChiefAIOfficerAgent'
import * as fs from 'fs'
import * as path from 'path'

async function testPhase27Compliance() {
  console.log('🧪 Testing Phase 27 (MUR) Compliance...')

  // 1. Verify AGENTS.md
  const agentsMd = fs.readFileSync(path.join(process.cwd(), 'AGENTS.md'), 'utf8')
  if (agentsMd.includes('Phase 27') && agentsMd.includes('Multi-Universal Resonance')) {
    console.log('✅ AGENTS.md reflects Phase 27 MUR.')
  } else {
    throw new Error('❌ AGENTS.md compliance failed.')
  }

  // 2. Verify Presence
  const presence = await onlinePresence.syncPresence()
  if (presence?.compliance === 'Phase 27 Multi-Universal Resonance' && presence.version === '1.7.0-mur') {
    console.log('✅ Presence reflects Phase 27 MUR.')
  } else {
    console.error('Presence:', presence)
    throw new Error('❌ Presence compliance failed.')
  }

  // 3. Verify Swarm Heartbeat Metrics
  const metrics = swarmHeartbeat.getMetrics()
  if (metrics.singularity_readiness === 0.999995) {
    console.log('✅ Swarm Heartbeat reflects Phase 27 targets.')
  } else {
    console.error('Metrics:', metrics)
    throw new Error('❌ Swarm Heartbeat targets failed.')
  }

  // 4. Verify Mesh Routing
  const routing = await universalMeshRouting.optimizeRoutingPath('node-a', 'node-b')
  if (routing.metrics.latency === 0.008 && routing.metrics.resonance === 0.99999 && routing.metrics.compliance === 'PHASE_27_MUR') {
    console.log('✅ Universal Mesh Routing reflects Phase 27 MUR.')
  } else {
    console.error('Routing:', routing)
    throw new Error('❌ Mesh Routing compliance failed.')
  }

  console.log('🏆 All Phase 27 Compliance Tests Passed.')
}

testPhase27Compliance().catch(err => {
  console.error(err.message)
  process.exit(1)
})
