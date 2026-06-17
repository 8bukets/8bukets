import { describe, it, expect, vi, beforeEach } from 'vitest'
import { ReActService } from '../antigravity/services/react'
import { TokenOptimizer } from '../antigravity/services/token_optimizer'
import { TokenSimulator } from '../antigravity/services/simulator'

describe('Agent Workflow & Token Optimization', () => {
  let reactService: ReActService

  beforeEach(() => {
    reactService = new ReActService()
  })

  it('ReActService should detect and break loops', async () => {
    const tools = {
      stuck: vi.fn().mockResolvedValue('same observation')
    }

    // We need to trick the reasoner to keep calling 'stuck'
    // Since our reasoner is mock, we can just observe it hits the limit or loop detector
    // Use the specially implemented 'trigger loop' goal to force repetition
    const steps = await reactService.executeCycle('trigger loop', tools, 5)

    // If it hit the loop detector, it should have a 'Loop detector triggered' observation
    const loopStep = steps.find(s => s.observation === 'Loop detector triggered.')
    expect(loopStep).toBeDefined()
  })

  it('TokenOptimizer should compress structured data', () => {
    const data = { status: 'ok', latency: 'low', users: 100 }
    const compressed = TokenOptimizer.compressStructuredData(data)
    expect(compressed).toContain('status:ok')
    expect(compressed).toContain('latency:low')

    const decompressed = TokenOptimizer.decompressStructuredData(compressed)
    expect(decompressed.status).toBe('ok')
    expect(decompressed.users).toBe('100')
  })

  it('TokenSimulator should calculate savings', () => {
    const result = TokenSimulator.simulate(5, 2000, 500, true)
    expect(result.cachedTokens).toBeGreaterThan(0)
    expect(result.billedTokens).toBeLessThan(result.totalTokens)
  })
})
