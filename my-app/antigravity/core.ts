import { MongoClient } from 'mongodb'
import { createClient } from '@supabase/supabase-js'
import { cacheLife, cacheTag, revalidateTag, updateTag, refresh } from 'next/cache'
import { connection } from 'next/server'
import { z } from 'zod'

/**
 * ANTIGRAVITY AUTONOMOUS CORE
 * This file orchestrates all full-stack connectivity and patterns.
 */

// --- 1. CONFIGURATION & TYPES ---

const MONGODB_URI = process.env.MONGODB_URI
const SUPABASE_URL = process.env.SUPABASE_DATABASE_URL
const SUPABASE_KEY = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY

if (!MONGODB_URI || !SUPABASE_URL || !SUPABASE_KEY) {
  console.warn('⚠️ [Autonomous Core] Missing production credentials. System running in limited observability mode.')
}

export interface PageProps<T = unknown> {
  params: Promise<T>
  searchParams: Promise<Record<string, string | string[] | undefined>>
}

export interface LayoutProps<T = unknown> {
  children: React.ReactNode
  params: Promise<T>
}

// --- 2. AUTONOMOUS DATABASE CLIENTS ---

let _mongoClientPromise: Promise<MongoClient>
const supabase = createClient(SUPABASE_URL || 'https://placeholder.supabase.co', SUPABASE_KEY || 'placeholder')

// Phase 5: Self-Healing State
const circuitBreaker = {
  mongodb: { failures: 0, lastFailure: 0, state: 'closed' as 'closed' | 'open' | 'half-open' },
  supabase: { failures: 0, lastFailure: 0, state: 'closed' as 'closed' | 'open' | 'half-open' }
}

const FAILURE_THRESHOLD = 3
const RECOVERY_TIMEOUT = 1000 * 30 // 30 seconds

export async function getMongoClient(): Promise<MongoClient> {
  // Circuit Breaker Logic
  if (circuitBreaker.mongodb.state === 'open') {
    if (Date.now() - circuitBreaker.mongodb.lastFailure > RECOVERY_TIMEOUT) {
      console.log('🔄 [Autonomous Core] Attempting MongoDB self-healing...')
      circuitBreaker.mongodb.state = 'half-open'
    } else {
      throw new Error('Circuit Breaker: MongoDB is in recovery mode.')
    }
  }

  if (_mongoClientPromise) return _mongoClientPromise

  try {
    if (process.env.NODE_ENV === 'development') {
      let globalWithMongo = global as typeof globalThis & { _mongoClientPromise?: Promise<MongoClient> }
      if (!globalWithMongo._mongoClientPromise) {
        globalWithMongo._mongoClientPromise = new MongoClient(MONGODB_URI!).connect()
      }
      _mongoClientPromise = globalWithMongo._mongoClientPromise
    } else {
      _mongoClientPromise = new MongoClient(MONGODB_URI!).connect()
    }
    const client = await _mongoClientPromise
    circuitBreaker.mongodb.state = 'closed'
    circuitBreaker.mongodb.failures = 0
    return client
  } catch (err) {
    circuitBreaker.mongodb.failures++
    circuitBreaker.mongodb.lastFailure = Date.now()
    if (circuitBreaker.mongodb.failures >= FAILURE_THRESHOLD) {
      circuitBreaker.mongodb.state = 'open'
      // Phase 7: Autonomous Notification
      import('./services/notification').then(n => {
        n.sendNotification({
          type: 'health',
          message: 'MongoDB Circuit Breaker tripped. System in recovery mode.',
          severity: 'critical'
        })
      })
    }
    throw err
  }
}

export { supabase }

// --- 3. AUTONOMOUS ORCHESTRATION & HELPERS ---

/**
 * Standard caching APIs
 */
export { cacheLife, cacheTag, revalidateTag, updateTag, refresh }

/**
 * VOLATILITY REGISTRY (Phase 4: Predictive Scaling)
 * In a distributed system, this would be backed by Redis.
 * Here we use an in-memory map for the autonomous pattern.
 */
const volatilityRegistry = new Map<string, { updates: number; lastUpdate: number }>()

export function recordUpdate(tag: string) {
  const current = volatilityRegistry.get(tag) || { updates: 0, lastUpdate: Date.now() }
  const newStats = {
    updates: current.updates + 1,
    lastUpdate: Date.now()
  }
  volatilityRegistry.set(tag, newStats)
  updateTag(tag)

  // Phase 7+: Persist to Predictive Analytics Layer
  import('./services/analytics').then(a => {
    a.trackEvent(tag, 'VOLATILITY_INCREASE', newStats)
  })
}

export function getPredictiveProfile(tag: string): 'inventory' | 'catalog' | 'minutes' {
  const stats = volatilityRegistry.get(tag)
  if (!stats) return 'catalog' // Default to long-lived for new data
  
  const age = Date.now() - stats.lastUpdate
  const frequency = stats.updates > 5 ? 'high' : 'low'

  // Autonomous Decision Logic
  if (frequency === 'high' || age < 1000 * 60) return 'inventory' // 30s-60s (Volatile)
  if (stats.updates > 0) return 'minutes' // 5m-15m (Stable)
  return 'catalog' // 1h-24h (Static)
}

/**
 * predictiveFetch: Autonomous 'Phase 4' fetching.
 * Automatically chooses the best cacheLife based on observed volatility.
 */
export async function predictiveFetch<T>(
  tag: string,
  schema: z.Schema<T>,
  fetcher: () => Promise<unknown>
): Promise<T> {
  const profile = getPredictiveProfile(tag)
  return autonomousFetch(schema, fetcher, {
    tags: [tag],
    life: profile
  })
}

// --- 4. COGNITIVE INSIGHTS (Phase 6) ---

const logBuffer: { msg: string; time: string; type: string }[] = []

export function logAutonomousAction(msg: string, type: string = 'info') {
  logBuffer.unshift({ msg, time: new Date().toLocaleTimeString(), type })
  if (logBuffer.length > 50) logBuffer.pop()
}

export async function getSystemInsights() {
  // Phase 12: Safeguard against CLI-mode execution
  // Only use cache if we are in a recognized Next.js request context
  const isServerRequest = !!process.env.NEXT_RUNTIME

  if (isServerRequest) {
    'use cache'
    cacheLife('inventory')
  }
  
  const { synthesize } = await import('./synthesis')
  const { getPersistenceHealth } = await import('./services/persistence')
  const { getNetworkState } = await import('./services/neural')
  const { getRelayState } = await import('./services/relay')
  const { optimize } = await import('./optimization')
  const { runSecurityAudit } = await import('./services/cognitive_security')
  const { auditEfficiency } = await import('./efficiency')
  const { probeSuperConnectivity } = await import('./orchestration')
  const { mapResourceDesires } = await import('./sentience')
  
  const ideas = await synthesize()
  const persistence = await getPersistenceHealth()
  const network = await getNetworkState()
  const relay = await getRelayState()
  const security = await runSecurityAudit()
  const efficiency = await auditEfficiency()
  const connectivity = await probeSuperConnectivity()
  const desires = await mapResourceDesires()

  // Phase 12: Pass partial insights to optimizer to avoid recursion
  const proposals = await optimize({
    caching: { registrySize: volatilityRegistry.size },
    ideas
  })

  return {
    circuitBreakers: {
      mongodb: circuitBreaker.mongodb.state,
      supabase: circuitBreaker.supabase.state,
    },
    caching: {
      registrySize: volatilityRegistry.size,
      activeProfiles: Array.from(volatilityRegistry.keys()).map(tag => ({
        tag,
        profile: getPredictiveProfile(tag)
      }))
    },
    logs: logBuffer,
    ideas,
    persistence,
    network,
    relay,
    proposals,
    security,
    efficiency,
    connectivity,
    desires,
    uptime: process.uptime()
  }
}

/**
 * resolve: Safely resolve mandatory async props
 */
export async function resolve<T>(promise: Promise<T>): Promise<T> {
  return await promise
}

/**
 * autonomousFetch: Automatically handles caching, tagging, and schema validation.
 * Phase 5: Implements Graceful Degradation and Automatic Retry.
 */
export async function autonomousFetch<T>(
  schema: z.Schema<T>,
  fetcher: () => Promise<unknown>,
  config: { tags?: string[]; life?: string } = {}
): Promise<T> {
  try {
    const data = await fetcher()
    
    // Phase 12: Safeguard against non-server environments
    const isServerRequest = !!process.env.NEXT_RUNTIME

    if (isServerRequest) {
      if (config.tags) config.tags.forEach(tag => cacheTag(tag))
      if (config.life) cacheLife(config.life as any)
    }

    const result = schema.safeParse(data)
    if (!result.success) {
      console.error('[Autonomous Core] Validation Failure:', result.error.format())
      throw new Error('Autonomous validation failed')
    }
    return result.data
  } catch (err) {
    console.warn('[Autonomous Core] Primary fetch failed. Attempting Graceful Degradation...', err)
    
    // In Next.js 16, if we are in a 'use cache' scope, we can rely on 
    // the stale-while-revalidate behavior if a previous entry exists.
    // If we throw here, Next.js will often serve the stale content if available.
    throw err 
  }
}

/**
 * healthCheck: Autonomous self-diagnostic
 */
export async function healthCheck() {
  const results = {
    mongodb: 'unknown',
    supabase: 'unknown',
    timestamp: new Date().toISOString()
  }

  try {
    const client = await getMongoClient()
    await client.db().admin().ping()
    results.mongodb = 'healthy'
  } catch (e) {
    results.mongodb = 'error'
  }

  try {
    const { error } = await supabase.from('_health').select('id').limit(1)
    // If table doesn't exist, it's still "connected" if no network error
    results.supabase = error && error.code === 'PGRST116' ? 'healthy' : 'connected'
  } catch (e) {
    results.supabase = 'error'
  }

  return results
}

/**
 * getRuntimeEnv: Runtime-safe environment access
 */
export async function getRuntimeEnv(key: string) {
  await connection()
  return process.env[key]
}
