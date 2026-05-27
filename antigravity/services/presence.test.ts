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
        updateOne: vi.fn(() => Promise.resolve()),
        find: vi.fn(() => ({
          toArray: vi.fn(() => Promise.resolve([]))
        }))
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
  beforeEach(() => {
    vi.clearAllMocks()
    process.env.GITHUB_ACTIONS = ''
    process.env.AUTONOMOUS_MODE = ''
    process.env.MACBOOK_CLOUD_SIMULATION = ''
  })

  it('should sync presence correctly and determine leadership', async () => {
    const presence = await onlinePresence.syncPresence()
    expect(presence).toBeDefined()
    expect(presence?.status).toBe('online')
    expect(presence?.docker.container_count).toBe(5)
    expect(presence?.git.open_prs).toBe(1)

    // Default local node should be leader
    expect(presence?.environment).toBe('local')
    expect(presence?.is_leader).toBe(true)
    expect(presence?.node_priority).toBe(100)

    expect(core.logAutonomousAction).toHaveBeenCalledWith(expect.stringContaining('Presence heartbeated'), 'info')
  })

  it('should promote cloud node to leader if no other nodes are active', async () => {
    process.env.GITHUB_ACTIONS = 'true'

    const presence = await onlinePresence.syncPresence()
    expect(presence?.environment).toBe('cloud')
    expect(presence?.is_leader).toBe(true) // Leader because no other nodes in mock
    expect(presence?.node_priority).toBe(10)
  })

  it('should not promote cloud node to leader if higher priority node is active', async () => {
    process.env.GITHUB_ACTIONS = 'true'

    // Mock existing high priority node
    const mockFind = vi.fn(() => ({
      toArray: vi.fn(() => Promise.resolve([{ node_priority: 100 }]))
    }))

    vi.spyOn(core, 'getMongoClient').mockImplementationOnce(async () => ({
      db: vi.fn(() => ({
        collection: vi.fn(() => ({
          find: mockFind,
          updateOne: vi.fn(() => Promise.resolve())
        }))
      }))
    }) as any)

    const presence = await onlinePresence.syncPresence()
    expect(presence?.environment).toBe('cloud')
    expect(presence?.is_leader).toBe(false)
  })
})
