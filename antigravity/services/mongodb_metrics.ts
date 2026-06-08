import { getMongoClient } from '../core'

/**
 * ANTIGRAVITY MONGODB TELEMETRY SERVICE
 */

export async function getMongoDBMetrics() {
  try {
    const client = await getMongoClient()
    const db = client.db()
    const stats = await db.command({ dbStats: 1 })
    return {
      status: 'healthy',
      collections: stats.collections,
      dataSize: stats.dataSize,
      indexSize: stats.indexSize,
      fullyOnline: true
    }
  } catch (e) {
    return {
      status: 'unavailable',
      fullyOnline: false
    }
  }
}
