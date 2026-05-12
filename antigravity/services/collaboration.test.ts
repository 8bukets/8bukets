import { describe, it, expect, vi, beforeEach } from 'vitest'
import fs from 'fs'

vi.mock('fs')

// We mock the core module *before* importing the service
vi.mock('@/antigravity/core', () => ({
  autonomousFetch: vi.fn((schema, fn) => fn())
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
    vi.mocked(fs.existsSync).mockReturnValue(true)
    vi.mocked(fs.readFileSync).mockReturnValue(mockMission)

    const metadata = await getMissionMetadata()

    expect(metadata).toBeDefined()
    expect(metadata.missionStatement).toBe('Test Mission')
    expect(metadata.stakeholders).toHaveLength(2)
    expect(metadata.stakeholders[0]).toEqual({ role: 'Role A', email: 'a@test.com' })
    expect(metadata.goals).toEqual(['Goal 1', 'Goal 2'])
  })

  it('should throw error if mission document is missing', async () => {
    vi.mocked(fs.existsSync).mockReturnValue(false)
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
    vi.mocked(fs.existsSync).mockReturnValue(true)
    vi.mocked(fs.readFileSync).mockReturnValue(mockMission)
    vi.mocked(fs.writeFileSync).mockImplementation(() => {})

    const state = await syncCollaborationState()

    expect(state).toBeDefined()
    expect(state.mission).toBe('Test Mission')
    expect(state.docker.status).toBe('optimal')
    expect(fs.writeFileSync).toHaveBeenCalledWith(
      expect.stringContaining('autonomous_state.json'),
      expect.any(String)
    )
  })
})
