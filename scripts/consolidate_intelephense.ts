import { intelephenseService } from '../antigravity/services/intelephense_service'

async function consolidate() {
  await intelephenseService.consolidate()
}

consolidate().catch(console.error)
