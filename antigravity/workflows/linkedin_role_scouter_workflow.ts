/**
 * LinkedIn Role Scouter Autonomous Workflow
 * Generated autonomously by the Antigravity Singularity Engine.
 */
import { getLinkedInRoleScouterData } from '../services/linkedin_role_scouter'

async function run() {
  console.log('🤖 [Workflow] Starting autonomous cycle for LinkedIn Role Scouter...')
  const data = await getLinkedInRoleScouterData()
  console.log('✅ [Workflow] Data fetched:', data)
}

run().catch(console.error)
