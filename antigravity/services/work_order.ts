import fs from 'fs'
import path from 'path'
import { z } from 'zod'
import { logAutonomousAction } from '../core'

export const WorkOrderSchema = z.object({
  id: z.string(),
  type: z.enum(['BOOTSTRAP_SERVICE', 'OPTIMIZE_SYSTEM', 'CONTENT_GENERATION', 'SMOKE_TEST', 'DEPLOYMENT']),
  goal: z.string(),
  payload: z.any(),
  status: z.enum(['pending', 'executing', 'completed', 'failed']),
  created_at: z.string(),
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

  private load() {
    if (fs.existsSync(STORAGE_PATH)) {
      try {
        const data = fs.readFileSync(STORAGE_PATH, 'utf8')
        const parsed = JSON.parse(data)
        const result = z.array(WorkOrderSchema).safeParse(parsed)
        if (result.success) {
          this.orders = result.data
        } else {
          console.error('❌ [WorkOrder] Data validation failed:', result.error.format())
          this.orders = []
        }
      } catch (e) {
        console.error('❌ [WorkOrder] Failed to load work orders:', e)
        this.orders = []
      }
    }
  }

  private save() {
    const dataDir = path.dirname(STORAGE_PATH)
    if (!fs.existsSync(dataDir)) {
      fs.mkdirSync(dataDir, { recursive: true })
    }
    fs.writeFileSync(STORAGE_PATH, JSON.stringify(this.orders, null, 2))
  }

  public createOrder(type: WorkOrder['type'], goal: string, payload: any): WorkOrder {
    const newOrder: WorkOrder = {
      id: `wo_${Math.random().toString(36).substring(2, 11)}`,
      type,
      goal,
      payload,
      status: 'pending',
      created_at: new Date().toISOString()
    }
    this.orders.push(newOrder)
    this.save()
    logAutonomousAction(`[WORK_ORDER] Created: ${newOrder.id} - ${goal}`, 'cognitive')
    return newOrder
  }

  public getPendingOrders(): WorkOrder[] {
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
      this.save()
    }
  }

  public async executePendingOrders() {
    const pending = this.getPendingOrders()
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
    console.log(`🎬 [WorkOrder] Dispatching ${order.type}: ${order.goal}`)

    switch (order.type) {
      case 'BOOTSTRAP_SERVICE':
        const { bootstrap } = await import('../singularity')
        return await bootstrap(order.payload)

      case 'CONTENT_GENERATION':
        const { generateContent } = await import('./content')
        return await generateContent(order.payload)

      case 'SMOKE_TEST':
        const { runSmokeTest } = await import('./smoke_test')
        return await runSmokeTest(order.payload)

      case 'DEPLOYMENT':
        logAutonomousAction(`[DEPLOYMENT] Executing deployment: ${order.goal}`, 'info')
        return { status: 'deployed', timestamp: new Date().toISOString() }

      case 'OPTIMIZE_SYSTEM':
        const { evolve, applyFixes } = await import('../evolution')
        const suggestions = (order.payload && Array.isArray(order.payload.proposals))
          ? order.payload.proposals
          : await evolve()
        await applyFixes(suggestions)
        return { appliedFixes: suggestions.length }

      default:
        throw new Error(`Unknown work order type: ${order.type}`)
    }
  }
}

export const workOrderService = new WorkOrderService()
