import { describe, it, expect, vi } from 'vitest'
import { getMissionMetadata as getCollaborationContext, exportEcosystemMetadata } from './collaboration'

vi.mock('fs')

// We mock the core module *before* importing the service
vi.mock('@/antigravity/core', () => ({
  autonomousFetch: vi.fn((schema, fn) => fn()),
  logAutonomousAction: vi.fn(),
  getMongoClient: vi.fn(() => Promise.resolve({
    db: () => ({
      collection: () => ({
        updateOne: vi.fn(() => Promise.resolve())
      })
    })
  }))
}))

// Now import the service
import { getMissionMetadata, syncCollaborationState } from './collaboration'

vi.mock('./docker', () => ({
  checkDockerHealth: vi.fn(() => Promise.resolve({
    status: 'optimal',
    containerCount: 1,
    timestamp: '2026-05-12T00:00:00.000Z'
  }))
}))

vi.mock('./jenkins', () => ({
  checkJenkinsHealth: vi.fn(() => Promise.resolve({
    status: 'optimal',
    metrics: {
      pipeline_efficiency: 'OPTIMIZED',
      security_scan: 'PASSED',
      has_cache: true,
      has_artifacts: true,
      has_stages: true,
      has_parallel: true
    },
    timestamp: '2026-05-12T00:00:00.000Z'
  }))
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
