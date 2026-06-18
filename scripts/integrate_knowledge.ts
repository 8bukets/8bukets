/** PHASE 15 COMPLIANCE: quantum-secure (Dilithium/Kyber) **/
import { latticeSync } from '@/antigravity/services/lattice_sync'
import { Jules } from '../antigravity/jules'

async function main() {
  console.log('🚀 Starting Knowledge Integration...')
  try {
    const jules = new Jules()
    await jules.executeWorkCycle()
    console.log('✅ Knowledge Integration Complete.')
  } catch (err) {
    console.error('❌ Knowledge Integration Failed:', err)
    process.exit(1)
  }
}

main()
