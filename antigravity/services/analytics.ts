import { z } from 'zod'
import { getMongoClient, logAutonomousAction } from '@/antigravity/core'

export const AnalyticsSchema = z.object({
  tag: z.string(),
  event: z.string(),
  timestamp: z.string(),
  metadata: z.any().optional()
})

export type AnalyticsEvent = z.infer<typeof AnalyticsSchema>

/**
 * Predictive Analytics Layer
 * Persists autonomous signals to MongoDB for long-term forecasting.
 */
export async function trackEvent(tag: string, event: string, metadata?: any) {
  const payload: AnalyticsEvent = {
    tag,
    event,
    timestamp: new Date().toISOString(),
    metadata
  }

  try {
    const client = await getMongoClient()
    const db = client.db()
    await db.collection('autonomous_analytics').insertOne(payload)

    logAutonomousAction(`[ANALYTICS] Persisted volatility event for ${tag}`, 'scaling')
  } catch (err) {
    console.warn('⚠️ [Analytics] Failed to persist event to MongoDB. Falling back to memory.', err)
  }

  return payload
}

export async function getRecentAnalytics(limit: number = 10) {
  'use cache'
  try {
    const client = await getMongoClient()
    const db = client.db()
    return await db.collection('autonomous_analytics')
      .find()
      .sort({ timestamp: -1 })
      .limit(limit)
      .toArray()
  } catch (err) {
    return []
  }
}
