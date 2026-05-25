import { logAutonomousAction, getMongoClient, supabase } from '../core'
import { gitProvider } from './git_provider'
import { z } from 'zod'
import fs from 'fs'
import path from 'path'

/**
 * ANTIGRAVITY CLOUD CONVERGENCE SERVICE
 * Synchronizes autonomous state across the multi-cloud ecosystem.
 * Targets: MongoDB (Persistent Memory), Supabase (Real-time Presence), GitHub/GitLab (Evolution).
 */

export const CloudConvergenceStateSchema = z.object({
  last_sync: z.string(),
  active_providers: z.array(z.string()),
  ecosystem_health: z.enum(['optimal', 'degraded', 'recovering']),
  sync_metrics: z.object({
    mongo_records: z.number(),
    supabase_presence: z.boolean(),
    git_status: z.string()
  })
})

export type CloudConvergenceState = z.infer<typeof CloudConvergenceStateSchema>

export class CloudConvergenceService {
  /**
   * Orchestrates a full ecosystem synchronization.
   */
  public async synchronizeEcosystem() {
    const isCloud = !!(process.env.GITHUB_ACTIONS || process.env.GITLAB_CI || process.env.AUTONOMOUS_MODE === 'cloud' || process.env.MACBOOK_CLOUD_SIMULATION === 'true')
    logAutonomousAction(`🌐 [CloudConvergence] Initiating full ecosystem convergence (${isCloud ? 'CLOUD' : 'LOCAL'})...`, 'info')

    const providers = []
    if (process.env.GITHUB_TOKEN) providers.push('github')
    if (process.env.GITLAB_TOKEN) providers.push('gitlab')
    if (process.env.MONGODB_URI) providers.push('mongodb')
    if (process.env.NEXT_PUBLIC_SUPABASE_URL) providers.push('supabase')

    try {
      // 1. Core State Retrieval & Bidirectional Sync
      let workOrderCount = 0
      try {
        const mongoClient = await getMongoClient()
        const db = mongoClient.db()

        // Push local orders that might be missing in MongoDB
        const localPath = path.join(process.cwd(), 'data/work_orders.json')
        if (fs.existsSync(localPath)) {
           const localOrders = JSON.parse(fs.readFileSync(localPath, 'utf8'))
           for (const order of localOrders) {
              const { _id, ...orderData } = order
              await db.collection('work_orders').updateOne(
                { id: order.id },
                { $set: orderData },
                { upsert: true }
              )
           }
           logAutonomousAction(`📤 [CloudConvergence] Synced ${localOrders.length} local orders to MongoDB.`, 'info')
        }

        workOrderCount = await db.collection('work_orders').countDocuments()
      } catch (e) {
        logAutonomousAction('⚠️ [CloudConvergence] MongoDB unreachable or sync failed during convergence.', 'warning')
      }

      // 2. Supabase Real-time Pulse
      let supabasePresence = false
      try {
        const { data: presence, error: sbError } = await supabase
          .from('agent_presence')
          .select('*')
          .eq('agent', 'Jules')
          .single()
        supabasePresence = !!presence && !sbError
      } catch (e) {
        logAutonomousAction('⚠️ [CloudConvergence] Supabase unreachable during convergence.', 'warning')
      }

      // 3. Git Provider Status
      let gitStatus = 'unknown'
      try {
        const pulls = await gitProvider.listPullRequests()
        gitStatus = pulls.length > 0 ? `${pulls.length} open PRs/MRs` : 'clean'
      } catch (e) {
        logAutonomousAction('⚠️ [CloudConvergence] Git providers unreachable during convergence.', 'warning')
      }

      // 4. Cognitive Memory Health Check
      let memorySync = 'local-only'
      try {
        const mongoClient = await getMongoClient()
        const db = mongoClient.db()
        const memory = await db.collection('agent_memory').findOne({ agent: 'Jules' })
        if (memory) {
          memorySync = 'synchronized'
          logAutonomousAction('🧠 [CloudConvergence] Cognitive memory verified in MongoDB.', 'info')
        }
      } catch (e) {
        logAutonomousAction('⚠️ [CloudConvergence] Memory sync verification failed.', 'warning')
      }

      // 5. Knowledge Metadata Bridge
      let knowledgeCount = 0
      try {
        const mongoClient = await getMongoClient()
        const db = mongoClient.db()
        knowledgeCount = await db.collection('knowledge').countDocuments()
        logAutonomousAction(`📚 [CloudConvergence] ${knowledgeCount} knowledge nodes bridged in MongoDB.`, 'info')
      } catch (e) {
        logAutonomousAction('⚠️ [CloudConvergence] Knowledge bridge verification failed.', 'warning')
      }

      const state: CloudConvergenceState = {
        last_sync: new Date().toISOString(),
        active_providers: providers,
        ecosystem_health: (workOrderCount > 0 || supabasePresence || knowledgeCount > 0) ? 'optimal' : 'degraded',
        sync_metrics: {
          mongo_records: workOrderCount,
          supabase_presence: supabasePresence,
          git_status: gitStatus
        }
      }

      // 6. Cross-Persist Convergence
      try {
        const mongoClient = await getMongoClient()
        const db = mongoClient.db()
        await db.collection('system_state').updateOne(
          { systemId: 'antigravity-alpha-01' },
          { $set: { cloud_convergence: state, last_convergence: new Date().toISOString() } },
          { upsert: true }
        )
      } catch (e) {
        logAutonomousAction('⚠️ [CloudConvergence] Failed to persist convergence state to MongoDB.', 'warning')
      }

      // 7. Active State Recovery (Bridge MongoDB & Supabase)
      if ((workOrderCount > 0 || knowledgeCount > 0) && !supabasePresence) {
        logAutonomousAction('🔄 [CloudConvergence] Supabase presence missing but MongoDB active. Attempting Cloud-Native recovery...', 'info')
        try {
          const mongoClient = await getMongoClient()
          const db = mongoClient.db()
          const systemState = await db.collection('system_state').findOne({ systemId: 'antigravity-alpha-01' })

          if (systemState) {
            await supabase.from('agent_presence').upsert({
              id: 'jules-alpha-01',
              agent: 'Jules',
              status: 'recovered',
              lastSeen: new Date().toISOString(),
              execution_mode: 'cloud',
              recovered_from: 'mongodb',
              knowledge_nodes: knowledgeCount,
              context: systemState.cloud_convergence
            })
            logAutonomousAction('✅ [CloudConvergence] Supabase presence recovered from MongoDB state.', 'info')
            state.sync_metrics.supabase_presence = true
          }
        } catch (recoveryErr: any) {
          logAutonomousAction(`⚠️ [CloudConvergence] Active recovery failed: ${recoveryErr.message}`, 'warning')
        }
      }

      logAutonomousAction(`✅ [CloudConvergence] Ecosystem state converged (Mode: ${isCloud ? 'Cloud' : 'MacBook'}).`, 'info')
      return state
    } catch (err: any) {
      logAutonomousAction(`❌ [CloudConvergence] Fatal convergence failure: ${err.message}`, 'error')
      // Do not rethrow to prevent crashing the main loop
      return null
    }
  }

  /**
   * Autonomously resolves state conflicts between Cloud and Local.
   * Prioritizes MongoDB as the source of truth in Cloud/Autonomous mode.
   */
  public async resolveConflicts() {
    logAutonomousAction('⚖️ [CloudConvergence] Auditing for state conflicts...', 'info')

    try {
      const mongoClient = await getMongoClient()
      const db = mongoClient.db()

      const isCloud = process.env.AUTONOMOUS_MODE === 'cloud' ||
                      process.env.GITHUB_ACTIONS ||
                      process.env.GITLAB_CI ||
                      process.env.MACBOOK_CLOUD_SIMULATION === 'true'

      // Phase 22: Node Sovereignty & Cloud Takeover
      const nodeId = isCloud ? 'cloud-relay-01' : 'macbook-primary-01'
      const presence = await db.collection('agent_presence').findOne({ agent: 'Jules', 'telemetry.node_id': nodeId })
      const isLeader = presence?.is_leader ?? !isCloud

      if (isCloud && isLeader) {
         logAutonomousAction('⚡ [CloudConvergence] Cloud node is currently the LEADER. Assuming full operational sovereignty.', 'info')
      }

      // Sync work orders and system configuration from MongoDB to local if running in cloud mode
      if (isCloud) {
        logAutonomousAction('🌩️ [CloudConvergence] Cloud mode active. Synchronizing state from MongoDB source of truth.', 'info')

        // Sync System Configuration (Phase 12 Convergence)
        try {
           const systemState = await db.collection('system_state').findOne({ systemId: 'antigravity-alpha-01' })
           if (systemState && systemState.configuration) {
              const configPath = path.join(process.cwd(), 'config/evolution_params.json')
              if (!fs.existsSync(path.dirname(configPath))) fs.mkdirSync(path.dirname(configPath), { recursive: true })
              fs.writeFileSync(configPath, JSON.stringify(systemState.configuration, null, 4))
              logAutonomousAction('⚙️ [CloudConvergence] Synchronized evolution configuration from MongoDB.', 'info')
           }
        } catch (configErr) {
           logAutonomousAction('⚠️ [CloudConvergence] Configuration sync failed during conflict resolution.', 'warning')
        }

        const localPath = path.join(process.cwd(), 'data/work_orders.json')
        let localOrders = []
        if (fs.existsSync(localPath)) {
          try {
            localOrders = JSON.parse(fs.readFileSync(localPath, 'utf8'))
          } catch (e) {
            logAutonomousAction('⚠️ [CloudConvergence] Failed to parse local work orders during conflict resolution.', 'warning')
          }
        }

        // 1. Bidirectional Work Order Sync
        // Push local "executing", "completed", or "failed" updates to MongoDB first to ensure continuity
        const updatesToPush = localOrders.filter((o: any) => ['executing', 'completed', 'failed'].includes(o.status))
        if (updatesToPush.length > 0) {
          logAutonomousAction(`📤 [CloudConvergence] Pushing ${updatesToPush.length} local status updates to MongoDB...`, 'info')
          for (const order of updatesToPush) {
            const { _id, ...orderData } = order
            await db.collection('work_orders').updateOne(
              { id: order.id },
              { $set: { ...orderData, updated_at: new Date().toISOString() } },
              { upsert: true }
            )
          }
        }

        // 2. Pull all active and recent orders from MongoDB to establish full parity
        const mongoOrders = await db.collection('work_orders').find({
           $or: [
             { status: { $in: ['pending', 'in_progress', 'executing'] } },
             { updated_at: { $gt: new Date(Date.now() - 24 * 60 * 60 * 1000).toISOString() } }
           ]
        }).toArray()

        if (mongoOrders.length > 0) {
          // Merge logic: MongoDB orders take precedence for the local execution queue in cloud mode
          const orderMap = new Map(localOrders.map((o: any) => [o.id, o]))
          mongoOrders.forEach((mo: any) => {
            const { _id, ...orderData } = mo
            orderMap.set(mo.id, orderData)
          })

          fs.writeFileSync(localPath, JSON.stringify(Array.from(orderMap.values()), null, 2))

          // Update autonomous_state.json with resolution metadata
          const statePath = path.join(process.cwd(), 'autonomous_state.json')
          if (fs.existsSync(statePath)) {
            const state = JSON.parse(fs.readFileSync(statePath, 'utf8'))
            state.last_conflict_resolution = new Date().toISOString()
            state.synced_orders = mongoOrders.length
            state.execution_mode = 'cloud'
            state.cloud_parity = true
            fs.writeFileSync(statePath, JSON.stringify(state, null, 4))
          }

          logAutonomousAction(`✅ [CloudConvergence] Resolved conflicts: Synced ${mongoOrders.length} orders from MongoDB to local state for full cloud parity.`, 'info')
          return { status: 'resolved', conflicts: mongoOrders.length }
        }
      }
    } catch (e: any) {
      logAutonomousAction(`⚠️ [CloudConvergence] Conflict resolution failed: ${e.message}`, 'warning')
    }

    return { status: 'resolved', conflicts: 0 }
  }
}

export const cloudConvergence = new CloudConvergenceService()
