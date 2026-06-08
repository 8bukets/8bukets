import { supabase } from '../core'

/**
 * ANTIGRAVITY SUPABASE TELEMETRY SERVICE
 */

export async function getSupabaseMetrics() {
  try {
    const { data, error } = await supabase.from('_health').select('id').limit(1)
    // If table doesn't exist, it's still "connected" if no network error
    const status = error && error.code === 'PGRST116' ? 'healthy' : (error ? 'degraded' : 'healthy')

    return {
      status,
      fullyOnline: status === 'healthy',
      api_url: process.env.NEXT_PUBLIC_SUPABASE_URL
    }
  } catch (e) {
    return {
      status: 'unavailable',
      fullyOnline: false
    }
  }
}
