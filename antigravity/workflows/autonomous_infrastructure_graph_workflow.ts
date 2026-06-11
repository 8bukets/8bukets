/**
 * Autonomous Infrastructure Graph Autonomous Workflow
 * Generated autonomously by the Antigravity Singularity Engine.
 */
import { getAutonomousInfrastructureGraphData } from '../services/autonomous_infrastructure_graph'

async function run() {
  console.log('🤖 [Workflow] Starting autonomous cycle for Autonomous Infrastructure Graph...')
  const data = await getAutonomousInfrastructureGraphData()
  console.log('✅ [Workflow] Data fetched:', data)
}

run().catch(console.error)
