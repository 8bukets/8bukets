import { healthCheck } from './core'
import { evolve } from './evolution'
import { jules } from './jules'
import { synthesize } from './synthesis'
import chokidar from 'chokidar'
import path from 'path'

/**
 * ANTIGRAVITY AUTONOMOUS EXPLORER
 * Automatically scans and validates the system state.
 */
export async function explore() {
  console.log('🚀 [Antigravity Explorer] Starting autonomous scan...')

  const results: any = {
    timestamp: new Date().toISOString(),
    connectivity: {},
    environment: {},
    health: 'unknown',
    evolution: [],
    synthesis: []
  }

  // 1. Connectivity Scan
  try {
    results.connectivity = await healthCheck()
  } catch (e) {
    results.connectivity = { error: String(e) }
  }

  // 2. Environment Validation
  const required = ['MONGODB_URI', 'NEXT_PUBLIC_SUPABASE_URL', 'NEXT_PUBLIC_SUPABASE_ANON_KEY']
  for (const key of required) {
    const val = process.env[key]
    results.environment[key] = val ? 'present' : 'MISSING'
  }

  // 3. Cognitive Evolution Analysis
  try {
    results.evolution = await evolve()
  } catch (e) {
    console.error('❌ [Explorer] Evolution scan failed:', e)
  }

  // 4. Cognitive Synthesis
  try {
    results.synthesis = await synthesize()
  } catch (e) {
    console.error('❌ [Explorer] Synthesis engine failed:', e)
  }

  // 5. Overall Verdict
  const isHealthy = results.connectivity.mongodb === 'healthy' &&
                    results.connectivity.supabase !== 'error' &&
                    !Object.values(results.environment).includes('MISSING')

  results.health = isHealthy ? 'OPTIMAL' : 'DEGRADED'

  // 7. Jules Protocol: Record the Task
  jules.recordTask(`System Scan: Health is ${results.health}. Found ${results.evolution.length} evolution paths.`)

  console.log(`✅ [Explorer] Cycle Complete. Status: ${results.health}`)
  return results
}

/**
 * REAL-TIME WATCHDOG (Phase 16)
 * Monitors the filesystem for changes and triggers reactive exploration.
 */
export function watchSystem() {
  console.log('👁️  [Watchdog] Initiating real-time system surveillance...')

  const watcher = chokidar.watch(process.cwd(), {
    ignored: [
      /(^|[\/\\])\../, // ignore dotfiles
      /node_modules/,
      /.next/,
      /dist/
    ],
    persistent: true
  })

  watcher.on('change', (filePath) => {
    console.log(`🔔 [Watchdog] Detected change in: ${path.basename(filePath)}. Triggering reactive scan...`)
    explore().catch(err => console.error('💥 [Watchdog] Reactive scan failed:', err))
  })

  return watcher
}

// Allow running directly
if (import.meta.url === `file://${process.argv[1]}`) {
  explore().catch(console.error)
}
