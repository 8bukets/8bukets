import { describe, it, expect, vi, beforeEach } from 'vitest'
import { creationEngine } from '../antigravity/services/creation_engine'
import { workOrderService } from '../antigravity/services/work_order'
import * as synthesis from '../antigravity/synthesis'
import fs from 'fs'
import path from 'path'

// Mock core dependencies
vi.mock('../antigravity/core', async () => {
  const actual = await vi.importActual('../antigravity/core') as any
  return {
    ...actual,
    logAutonomousAction: vi.fn(),
    getMongoClient: vi.fn().mockResolvedValue({
      db: () => ({
        collection: () => ({
          find: () => ({ toArray: () => Promise.resolve([]) }),
          updateOne: vi.fn().mockResolvedValue({}),
        })
      })
    }),
    getSystemInsights: vi.fn().mockResolvedValue({
      docker: { status: 'optimal' },
      circuitBreakers: { mongodb: 'closed' }
    })
  }
})

describe('Autonomous Creation Full Cycle', () => {
  beforeEach(async () => {
    vi.clearAllMocks()
    await workOrderService.clearOrders()
  })

  it('should synthesize ideas and execute the full dependency chain', async () => {
    // 1. Mock synthesis to return a controlled idea
    const mockIdea = {
      feature: 'Test Autonomous Service',
      rationale: 'Testing full cycle',
      complexity: 'Low' as const
    }
    vi.spyOn(synthesis, 'synthesize').mockResolvedValue([mockIdea])

    // Mock dispatch to avoid actual external calls during test
    // @ts-ignore
    vi.spyOn(workOrderService, 'dispatch').mockImplementation(async (order) => {
      if (order.type === 'SMOKE_TEST') return { status: 'passed' }
      return { status: 'success' }
    })

    // 2. Run the cycle
    const result = await creationEngine.runCycle()

    // 3. Verify results
    expect(result.status).toBe('completed')
    expect(result.features).toContain('Test Autonomous Service')

    // 4. Verify work orders were created in sequence
    const orders = JSON.parse(fs.readFileSync('data/work_orders.json', 'utf8'))

    const bootstrap = orders.find((o: any) => o.type === 'BOOTSTRAP_SERVICE')
    const smoke = orders.find((o: any) => o.type === 'SMOKE_TEST')
    const deploy = orders.find((o: any) => o.type === 'DEPLOYMENT')
    const sync = orders.find((o: any) => o.type === 'SYSTEM_SYNC')

    expect(bootstrap).toBeDefined()
    expect(smoke).toBeDefined()
    expect(deploy).toBeDefined()
    expect(sync).toBeDefined()

    // Verify dependencies
    expect(smoke.dependsOn).toContain(bootstrap.id)
    expect(deploy.dependsOn).toContain(smoke.id)
    expect(sync.dependsOn).toContain(deploy.id)

    // Verify status (should be completed as executePendingOrders is called)
    expect(bootstrap.status).toBe('completed')
    expect(smoke.status).toBe('completed')
    expect(deploy.status).toBe('completed')
    expect(sync.status).toBe('completed')
  }, 30000)
})
