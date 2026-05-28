import { describe, it, expect, vi } from 'vitest'
import { getMissionMetadata } from './collaboration'

// Mock dependencies
vi.mock('@/antigravity/core', () => ({
  healthCheck: vi.fn(async () => ({
    mongodb: 'healthy',
    supabase: 'healthy',
    timestamp: '2026-05-07T21:00:00Z'
  })),
  autonomousFetch: vi.fn(async (schema, fetcher) => await fetcher())
}))

describe('Collaboration Service', () => {
  it('should parse stakeholders from mission.md', async () => {
    const context = await getMissionMetadata()
    expect(context.stakeholders).toBeDefined()
    // The actual mission.md might have different data, so we check for existence
    expect(Array.isArray(context.stakeholders)).toBe(true)
  })

  it('should include mission statement', async () => {
    const context = await getMissionMetadata()
    expect(context.missionStatement).toBeDefined()
  })
})
