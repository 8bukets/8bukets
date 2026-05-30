import { describe, it, expect, vi } from 'vitest'
import { getMissionMetadata as getCollaborationContext, exportEcosystemMetadata } from './collaboration'

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
      { role: 'Filip Keser (Founder)', email: 'filip@example.com' },
      { role: 'Jules (Lead Architect)', email: 'jules@antigravity.ai' },
      { role: 'Sigma Bot (Operations)', email: 'sigma@antigravity.ai' }
    ])
  })

  it('should include ecosystem metadata', async () => {
    const context = await exportEcosystemMetadata()
    expect(context.systemId).toBe('antigravity-alpha-01')
    expect(context.timestamp).toBeDefined()
  })
})
