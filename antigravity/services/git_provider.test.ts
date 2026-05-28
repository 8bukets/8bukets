import { describe, it, expect, vi, beforeEach } from 'vitest'
import { GitProviderService } from './git_provider'

describe('GitProviderService', () => {
  let service: GitProviderService
  let mockExec: any

  beforeEach(() => {
    mockExec = vi.fn()
    service = new GitProviderService(mockExec)
  })

  it('should detect github provider', async () => {
    mockExec.mockResolvedValue({ stdout: 'origin  https://github.com/owner/repo.git (fetch)', stderr: '' })
    const provider = await service.getActiveProvider()
    expect(provider).toBe('github')
  })

  it('should detect gitlab provider', async () => {
    mockExec.mockResolvedValue({ stdout: 'origin  https://gitlab.com/owner/repo.git (fetch)', stderr: '' })
    const provider = await service.getActiveProvider()
    expect(provider).toBe('gitlab')
  })

  it('should handle unknown provider', async () => {
    mockExec.mockResolvedValue({ stdout: 'origin  https://other.com/owner/repo.git (fetch)', stderr: '' })
    const provider = await service.getActiveProvider()
    expect(provider).toBe('unknown')
  })
})
