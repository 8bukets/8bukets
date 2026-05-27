import { describe, it, expect, vi } from 'vitest'
import { getCollaborationContext } from './collaboration'

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
    const context = await getCollaborationContext()
    expect(context.stakeholders).toEqual([
      { name: 'Filip Keser', role: 'Founder', email: 'filip@example.com' },
      { name: 'Jules', role: 'Lead Architect', email: 'jules@antigravity.ai' },
      { name: 'Sigma Bot', role: 'Operations', email: 'sigma@antigravity.ai' }
    ])
  })

  it('should include system metadata', async () => {
    const context = await getCollaborationContext()
    expect(context.systemMetadata).toBeDefined()
    expect(context.systemMetadata.version).toBe('0.1.0')
  })
})
