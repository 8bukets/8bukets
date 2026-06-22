/** PHASE 16 COMPLIANCE: swarm-heartbeat (interval: 5s) **/
import { describe, it, expect, vi, beforeEach } from 'vitest'
import * as dockerService from './docker'
import { exec } from 'child_process'

vi.mock('child_process', () => {
  const mExec = vi.fn((cmd, cb) => {
    if (cb) cb(null, { stdout: '' })
  })
  return {
    exec: mExec,
    __esModule: true,
    default: {
      exec: mExec
    }
  }
})

describe('Docker Service', () => {
  beforeEach(() => {
    vi.clearAllMocks()
    process.env.ANTIGRAVITY_SIMULATE_DOCKER = 'false'
    process.env.MACBOOK_CLOUD_SIMULATION = 'false'
  })

  it('should return mock fleet status when simulation is active', async () => {
    process.env.ANTIGRAVITY_SIMULATE_DOCKER = 'true'
    const status = await dockerService.getDockerStatus()
    expect(status).toHaveLength(2)
    expect(status[0].name).toBe('mongodb')
  })

  it('should return healthy status when Docker is running', async () => {
    (exec as any).mockImplementation((cmd: string, callback: any) => {
      callback(null, { stdout: 'docker ps output' })
    })
    const healthy = await dockerService.isDockerHealthy()
    expect(healthy).toBe(true)
  })

  it('should return unhealthy status when Docker is not running', async () => {
    (exec as any).mockImplementation((cmd: string, callback: any) => {
      callback(new Error('Docker not running'))
    })
    const healthy = await dockerService.isDockerHealthy()
    expect(healthy).toBe(false)
  })
})
