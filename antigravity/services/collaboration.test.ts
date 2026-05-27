import { describe, it, expect, vi, beforeEach } from 'vitest'
import fs from 'fs'

vi.mock('fs', () => ({
  default: {
    existsSync: vi.fn(),
    readFileSync: vi.fn(),
    writeFileSync: vi.fn(),
    promises: {
      readFile: vi.fn(),
      writeFile: vi.fn(),
      mkdir: vi.fn(),
      appendFile: vi.fn(),
      readdir: vi.fn(),
    }
  },
  existsSync: vi.fn(),
  readFileSync: vi.fn(),
}))

// We mock the core module *before* importing the service
vi.mock('@/antigravity/core', () => ({
  autonomousFetch: vi.fn((schema, fn) => fn()),
  logAutonomousAction: vi.fn(),
  healthCheck: vi.fn(() => Promise.resolve({
    mongodb: 'healthy',
    supabase: 'connected',
    timestamp: new Date().toISOString()
  })),
  getSystemInsights: vi.fn(() => Promise.resolve({
    circuitBreakers: { mongodb: 'closed' },
    caching: { registrySize: 0 }
  }))
}))

// Now import the service
import { getMissionMetadata, syncCollaborationState } from './collaboration'

vi.mock('../jules', () => ({
  jules: {
    scanAllBranches: vi.fn(() => Promise.resolve([]))
  }
}))

vi.mock('./docker', () => ({
  checkDockerHealth: vi.fn(() => Promise.resolve({
    status: 'optimal',
    containerCount: 1,
    timestamp: '2026-05-12T00:00:00.000Z'
  }))
}))

vi.mock('../jules', () => ({
  jules: {
    scanAllBranches: vi.fn(() => Promise.resolve([]))
  }
}))

describe('Collaboration Service', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('should parse mission metadata correctly', async () => {
    const mockMission = `
# Antigravity Mission

## Mission Statement
Test Mission

## Stakeholders
- Role A: a@test.com
- Role B: b@test.com

## Strategic Goals
1. Goal 1
2. Goal 2
`
    vi.mocked(fs.existsSync).mockReturnValue(true as any)
    vi.mocked(fs.promises.readFile).mockResolvedValue(mockMission as any)

    const metadata = await getMissionMetadata()

    expect(metadata).toBeDefined()
    expect(metadata.missionStatement).toBe('Test Mission')
    expect(metadata.stakeholders).toHaveLength(2)
    expect(metadata.stakeholders[0]).toEqual({ role: 'Role A', email: 'a@test.com' })
    expect(metadata.goals).toEqual(['Goal 1', 'Goal 2'])
  })

  it('should throw error if mission document is missing', async () => {
    vi.mocked(fs.existsSync).mockReturnValue(false as any)
    await expect(getMissionMetadata()).rejects.toThrow('Mission document missing')
  })

  it('should sync collaboration state correctly', async () => {
    const mockMission = `
# Antigravity Mission
## Mission Statement
Test Mission
## Stakeholders
- Role A: a@test.com
## Strategic Goals
1. Goal 1
`
    vi.mocked(fs.existsSync).mockImplementation(((path: any) => {
      if (path.toString().includes('mission.md')) return true
      if (path.toString().includes('autonomous_state.json')) return false
      if (path.toString().includes('.jules_memory.json')) return true
      return false
    }) as any)
    vi.mocked(fs.promises.readFile).mockImplementation(((path: any) => {
      if (path.toString().includes('mission.md')) return Promise.resolve(mockMission)
      if (path.toString().includes('.jules_memory.json')) return Promise.resolve(JSON.stringify({ autonomousTasks: [] }))
      return Promise.resolve('')
    }) as any)
    vi.mocked(fs.promises.writeFile).mockImplementation((() => Promise.resolve()) as any)

    const state = await syncCollaborationState()

    expect(state).toBeDefined()
    expect(state.mission).toBe('Test Mission')
    expect(state.docker.status).toBe('optimal')
    expect(fs.promises.writeFile).toHaveBeenCalledWith(
      expect.stringContaining('autonomous_state.json'),
      expect.any(String)
    )
  })
})
