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
          console.log(`✅ [WorkOrder] Loaded ${this.orders.length} orders from MongoDB.`)
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
          console.log(`✅ [WorkOrder] Loaded ${this.orders.length} orders from local fallback.`)
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
    fs.writeFileSync(STORAGE_PATH, JSON.stringify(this.orders, null, 2))
  }

  public async createOrder(type: WorkOrder['type'], goal: string, payload: any): Promise<WorkOrder> {
    const newOrder: WorkOrder = {
      id: `wo_${Math.random().toString(36).substring(2, 11)}`,
      type,
      goal,
      payload,
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

  public async executePendingOrders() {
    const pending = await this.getPendingOrders()
    if (pending.length === 0) return

    console.log(`⚡ [WorkOrder] Executing ${pending.length} pending orders...`)

    for (const order of pending) {
      await this.updateOrderStatus(order.id, 'executing')
      try {
        const result = await this.dispatch(order)
        await this.updateOrderStatus(order.id, 'completed', result)
        logAutonomousAction(`[WORK_ORDER] Completed: ${order.id}`, 'cognitive')
      } catch (err: any) {
        console.error(`❌ [WorkOrder] Order ${order.id} failed:`, err)
        await this.updateOrderStatus(order.id, 'failed', undefined, err.message)
        logAutonomousAction(`[WORK_ORDER] Failed: ${order.id}`, 'error')
      }
    }
  }

  private async dispatch(order: WorkOrder) {
    console.log(`🎬 [WorkOrder] Dispatching ${order.type}: ${order.goal || order.description}`)

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

      default:
        console.log(`ℹ️ [WorkOrder] Skipping unknown or external order type: ${order.type}`)
        return { skipped: true, reason: 'external_type' }
    }
  }
}

export const workOrderService = new WorkOrderService()
