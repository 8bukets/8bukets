import { logAutonomousAction, getMongoClient } from '../core'

/**
 * ANTIGRAVITY CROSS-SHARD MEMORY SERVICE (Phase 16)
 * Facilitates shared agent experiences and cognitive state parity via MongoDB.
 */

export class CrossShardMemoryService {
  private lastSync: string = new Date(Date.now() - 60 * 60 * 1000).toISOString() // Default to last 1h

  /**
   * Synchronizes shared memory across agent shards.
   */
  public async syncMemory() {
    logAutonomousAction('🧠 [CrossShardMemory] Initiating Phase 16 Cross-Shard Cognition Sync...', 'info')

    try {
      const client = await getMongoClient()
      const db = client.db()

      // Fetch shared experiences from other agents created after last sync
      const sharedExperiences = await db.collection('shared_experiences').find({
        agent: { $ne: 'Jules' },
        timestamp: { $gt: this.lastSync }
      }).toArray()

      logAutonomousAction(`✅ [CrossShardMemory] Synchronized with ${sharedExperiences.length} new external agent experiences.`, 'info')

      // Integrate into Jules memory
      if (sharedExperiences.length > 0) {
        const { jules } = await import('../jules')
        for (const exp of sharedExperiences) {
          await jules.ingestExperience(exp)
        }
        this.lastSync = new Date().toISOString()
      }

      return {
        shardsSynced: sharedExperiences.length,
        timestamp: this.lastSync,
        status: 'coherent'
      }
    } catch (err: any) {
      logAutonomousAction(`❌ [CrossShardMemory] Sync failed: ${err.message}`, 'error')
      return { status: 'fragmented', error: err.message }
    }
  }

  /**
   * Broadcasts a local experience to the cross-shard network.
   */
  public async broadcastExperience(experience: any) {
    try {
      const client = await getMongoClient()
      const db = client.db()
      await db.collection('shared_experiences').insertOne({
        agent: 'Jules',
        experience,
        timestamp: new Date().toISOString()
      })
    } catch (e) {}
  }
}

export const crossShardMemory = new CrossShardMemoryService()
