import fs from 'fs'
import path from 'path'
import { z } from 'zod'
import { logAutonomousAction, getMongoClient } from '../core'

export const WorkOrderSchema = z.object({
  id: z.string(),
  type: z.string(), // Allow all types, specific ones handled in dispatch
  goal: z.string().optional(),
  description: z.string().optional(), // Support Python-style description
  payload: z.any().optional(),
  status: z.enum(['pending', 'executing', 'completed', 'failed', 'in_progress']),
  created_at: z.string(),
  updated_at: z.string().optional(),
  completed_at: z.string().optional(),
  dependsOn: z.array(z.string()).optional(),
  result: z.any().optional(),
  error: z.string().optional()
})

export type WorkOrder = z.infer<typeof WorkOrderSchema>

const STORAGE_PATH = path.join(process.cwd(), 'data/work_orders.json')

export class WorkOrderService {
  private orders: WorkOrder[] = []

  constructor() {
    this.load()
  }

  private async load() {
    // Try MongoDB first
    try {
      const client = await getMongoClient()
      const db = client.db()
      const mongoOrders = await db.collection('work_orders').find({}).toArray()
      if (mongoOrders.length > 0) {
        const result = z.array(WorkOrderSchema).safeParse(mongoOrders)
        if (result.success) {
          this.orders = result.data
          logAutonomousAction(`✅ [WorkOrder] Loaded ${this.orders.length} orders from MongoDB.`, 'info')
          this.saveLocal() // Sync local for fallback
          return
        }
      }
    } catch (e) {
      console.warn('⚠️ [WorkOrder] MongoDB load failed, falling back to local file.')
    }

    // Fallback to local file
    if (fs.existsSync(STORAGE_PATH)) {
      try {
        const data = fs.readFileSync(STORAGE_PATH, 'utf8')
        const parsed = JSON.parse(data)
        const result = z.array(WorkOrderSchema).safeParse(parsed)
        if (result.success) {
          this.orders = result.data
          logAutonomousAction(`✅ [WorkOrder] Loaded ${this.orders.length} orders from local fallback.`, 'info')
        } else {
          console.error('❌ [WorkOrder] Local data validation failed:', result.error.format())
        }
      } catch (e) {
        console.error('❌ [WorkOrder] Failed to load local work orders:', e)
      }
    }
  }

  private async save(order?: WorkOrder) {
    this.saveLocal()

    try {
      const client = await getMongoClient()
      const db = client.db()
      if (order) {
        // Use a plain object for MongoDB to avoid potential issues with Zod/class instances
        const orderData = { ...order };
        delete (orderData as any)._id; // Ensure we don't try to update the immutable _id

        await db.collection('work_orders').updateOne(
          { id: order.id },
          { $set: orderData },
          { upsert: true }
        )
      } else {
        // Full sync if no specific order provided
        for (const o of this.orders) {
          await db.collection('work_orders').updateOne(
            { id: o.id },
            { $set: o },
            { upsert: true }
          )
        }
      }
    } catch (e) {
      console.error('❌ [WorkOrder] Failed to save to MongoDB:', e)
    }
  }

  private saveLocal() {
    const dataDir = path.dirname(STORAGE_PATH)
    if (!fs.existsSync(dataDir)) {
      fs.mkdirSync(dataDir, { recursive: true })
    }
    fs.writeFileSync(STORAGE_PATH, JSON.stringify(this.orders, null, 4))
  }

  public async createOrder(type: WorkOrder['type'], goal: string, payload: any, dependsOn?: string[]): Promise<WorkOrder> {
    const newOrder: WorkOrder = {
      id: `wo_${Math.random().toString(36).substring(2, 11)}`,
      type,
      goal,
      payload,
      dependsOn,
      status: 'pending',
      created_at: new Date().toISOString()
    }
    this.orders.push(newOrder)
    await this.save(newOrder)
    logAutonomousAction(`[WORK_ORDER] Created: ${newOrder.id} - ${goal}`, 'cognitive')
    return newOrder
  }

  public async getPendingOrders(): Promise<WorkOrder[]> {
    await this.load() // Refresh from DB
    return this.orders.filter(o => o.status === 'pending')
  }

  public async updateOrderStatus(id: string, status: WorkOrder['status'], result?: any, error?: string) {
    const order = this.orders.find(o => o.id === id)
    if (order) {
      order.status = status
      if (status === 'completed' || status === 'failed') {
        order.completed_at = new Date().toISOString()
      }
      if (result) order.result = result
      if (error) order.error = error
      await this.save(order)
    }
  }

  /**
   * Clears all orders from memory and local storage. Useful for testing.
   */
  public async clearOrders() {
    this.orders = []
    this.saveLocal()
    // We don't necessarily want to wipe the DB in a real environment,
    // but for autonomous local runs this is fine.
  }

  public async executePendingOrders() {
    let pending = await this.getPendingOrders()
    if (pending.length === 0) return

    logAutonomousAction(`⚡ [WorkOrder] Executing ${pending.length} pending orders...`, 'info')

    let executedInCycle = true
    while (executedInCycle && pending.length > 0) {
      executedInCycle = false

      for (const order of pending) {
        // Check if dependencies are met
        const deps = order.dependsOn || []
        const unmetDeps = deps.filter(depId => {
          const depOrder = this.orders.find(o => o.id === depId)
          return !depOrder || depOrder.status !== 'completed'
        })

        if (unmetDeps.length === 0) {
          await this.updateOrderStatus(order.id, 'executing')
          try {
            const result = await this.dispatch(order)
            await this.updateOrderStatus(order.id, 'completed', result)
            logAutonomousAction(`[WORK_ORDER] Completed: ${order.id}`, 'cognitive')
            executedInCycle = true
          } catch (err: any) {
            console.error(`❌ [WorkOrder] Order ${order.id} failed:`, err)
            await this.updateOrderStatus(order.id, 'failed', undefined, err.message)
            logAutonomousAction(`[WORK_ORDER] Failed: ${order.id}`, 'error')
            // Even if it fails, we mark cycle as progressed to re-evaluate remaining orders
            executedInCycle = true
          }
        }
      }

      // Refresh pending list
      pending = await this.getPendingOrders()
    }

    if (pending.length > 0) {
      logAutonomousAction(`⚠️ [WorkOrder] ${pending.length} orders remain pending due to unmet or failed dependencies.`, 'warn')
    }
  }

  private async dispatch(order: WorkOrder) {
    logAutonomousAction(`🎬 [WorkOrder] Dispatching ${order.type}: ${order.goal || order.description}`, 'info')

    switch (order.type) {
      case 'BOOTSTRAP_SERVICE':
        const { bootstrap } = await import('../singularity')
        return await bootstrap(order.payload)

      case 'CONTENT_GENERATION':
        const { generateContent } = await import('./content')
        return await generateContent(order.payload)

      case 'OPTIMIZE_SYSTEM':
        const { evolve, applyFixes } = await import('../evolution')
        const suggestions = (order.payload && Array.isArray(order.payload.proposals))
          ? order.payload.proposals
          : await evolve()
        await applyFixes(suggestions)
        return { appliedFixes: suggestions.length }

      case 'SMOKE_TEST':
        logAutonomousAction(`🧪 [WorkOrder] Running smoke test for ${order.payload?.serviceName}...`, 'info')
        // In a real scenario, this would trigger vitest for the specific file
        // For now, we simulate success if the file exists
        const { exec } = await import('child_process')
        const { promisify } = await import('util')
        const execAsync = promisify(exec)
        try {
          // If we have a specific test for the service, run it. Otherwise run general tests.
          const testPath = `antigravity/services/${order.payload?.serviceName}.test.ts`
          if (fs.existsSync(path.join(process.cwd(), testPath))) {
            await execAsync(`npx vitest run ${testPath}`)
          } else {
            logAutonomousAction(`ℹ️ [WorkOrder] No specific test found for ${order.payload?.serviceName}. Running general integrity check.`, 'info')
            await execAsync('npx vitest run antigravity/core.test.ts')
          }
          return { status: 'passed' }
        } catch (e: any) {
          throw new Error(`Smoke test failed: ${e.message}`)
        }

      case 'DEPLOYMENT':
        logAutonomousAction(`🚀 [WorkOrder] Triggering rollout for ${order.id}...`, 'info')
        const { spawnSync } = await import('child_process')
        // In cloud environments, we ensure we use python3 or the relevant entry point
        const rolloutResult = spawnSync('python3', ['scripts/rollout_executor.py'], { encoding: 'utf8' })
        if (rolloutResult.status !== 0) {
          throw new Error(`Rollout failed: ${rolloutResult.stderr}`)
        }
        return { status: 'deployed', output: rolloutResult.stdout }

      case 'SYSTEM_SYNC':
        logAutonomousAction(`🔄 [WorkOrder] Executing System Sync for ${order.id}...`, 'info')
        // Ensure we can run the sync script which handles Docker health and stakeholder sync
        const { spawnSync: spawnSyncSync } = await import('child_process')
        const isCloudSync = !!(process.env.GITHUB_ACTIONS || process.env.GITLAB_CI || process.env.AUTONOMOUS_MODE === 'cloud')

        // Run both TypeScript sync and Python-based audit if available
        const syncCmd = isCloudSync ? 'npx' : 'tsx'
        const syncArgs = isCloudSync ? ['tsx', 'scripts/connect_and_collaborate.ts'] : ['scripts/connect_and_collaborate.ts']

        spawnSyncSync(syncCmd, syncArgs, { encoding: 'utf8' })

        const { syncCollaborationState } = await import('./collaboration')
        await syncCollaborationState()

        // Phase 17: Unified Cloud Convergence
        const { cloudConvergence } = await import('./cloud_convergence')
        await cloudConvergence.synchronizeEcosystem()

        return { status: 'synced' }

      case 'CLOUD_INTELLIGENCE_MERGE':
        logAutonomousAction(`☁️ [WorkOrder] Executing Cloud Intelligence Merge for ${order.id}...`, 'info')
        const { spawnSync: spawnSyncCloud } = await import('child_process')
        const cloudResult = spawnSyncCloud('python3', ['sync_icloud.py', '--pull'], { encoding: 'utf8' })
        if (cloudResult.status !== 0 && !cloudResult.stderr.includes('Two-factor authentication required')) {
           // We allow skipping 2FA in autonomous background runs but log it
           console.warn('⚠️ [WorkOrder] iCloud Merge requires manual 2FA. Skipping for now.')
        }

        // Trigger a re-ingestion of knowledge after merge
        const { jules: julesCloud } = await import('../jules')
        await julesCloud.observeKnowledge()

        return { status: 'merged', output: cloudResult.stdout }

      case 'KNOWLEDGE_INGESTION':
        logAutonomousAction(`📚 [WorkOrder] Executing Knowledge Ingestion for ${order.id}...`, 'info')
        const { jules } = await import('../jules')
        await jules.observeGithubDocs()
        return { status: 'ingested' }

      case 'AUTONOMOUS_CREATION':
        logAutonomousAction(`🚀 [WorkOrder] Executing Autonomous Creation Cycle for ${order.id}...`, 'info')
        const { creationEngine } = await import('./creation_engine')
        return await creationEngine.runCycle()

      default:
        logAutonomousAction(`ℹ️ [WorkOrder] Skipping unknown or external order type: ${order.type}`, 'info')
        return { skipped: true, reason: 'external_type' }
    }
  }
}

export const workOrderService = new WorkOrderService()
