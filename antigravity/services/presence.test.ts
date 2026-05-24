import { describe, it, expect, vi, beforeEach } from 'vitest'
import { onlinePresence } from './presence'
import * as core from '../core'
import { gitProvider } from './git_provider'
import * as docker from './docker'

vi.mock('../core', () => ({
  logAutonomousAction: vi.fn(),
  getMongoClient: vi.fn(() => ({
    db: vi.fn(() => ({
      collection: vi.fn(() => ({
        updateOne: vi.fn(() => Promise.resolve())
      }))
    }))
  })),
  supabase: {
    from: vi.fn(() => ({
      upsert: vi.fn(() => Promise.resolve({ error: null }))
    }))
  },
  healthCheck: vi.fn(() => Promise.resolve({ mongodb: 'healthy', supabase: 'healthy' }))
}))

vi.mock('./docker', () => ({
  checkDockerHealth: vi.fn(() => Promise.resolve({ status: 'optimal', containerCount: 5, mode: 'native' }))
}))

vi.mock('./git_provider', () => ({
  gitProvider: {
    listPullRequests: vi.fn(() => Promise.resolve([{ id: 1, provider: 'github' }]))
  }
}))

describe('OnlinePresenceService', () => {
  it('should sync presence correctly', async () => {
    const presence = await onlinePresence.syncPresence()
    expect(presence).toBeDefined()
    expect(presence?.status).toBe('online')
    expect(presence?.docker.container_count).toBe(5)
    expect(presence?.git.open_prs).toBe(1)
    expect(core.logAutonomousAction).toHaveBeenCalledWith(expect.stringContaining('Presence heartbeated'), 'info')
  })
})
