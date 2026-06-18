/** PHASE 15 COMPLIANCE: quantum-secure (Dilithium/Kyber) **/
import { latticeSync } from '@/antigravity/services/lattice_sync'
import { intelephenseService } from '../antigravity/services/intelephense_service'

async function consolidate() {
  await intelephenseService.consolidate()
}

consolidate().catch(console.error)
