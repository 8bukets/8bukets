import { describe, it, expect, vi } from 'vitest'
import { z } from 'zod'
import { autonomousFetch } from './core'

// Mock next/cache
vi.mock('next/cache', () => ({
  cacheLife: vi.fn(),
  cacheTag: vi.fn(),
}))

describe('Antigravity Autonomous Core', () => {
  it('should autonomously validate and fetch data', async () => {
    const schema = z.object({ id: z.number(), name: z.string() })
    const mockFetcher = async () => ({ id: 1, name: 'Autonomous Test' })

    const result = await autonomousFetch(schema, mockFetcher)
    expect(result.name).toBe('Autonomous Test')
  })

  it('should throw error on schema mismatch', async () => {
    const schema = z.object({ id: z.number() })
    const mockFetcher = async () => ({ id: 'not-a-number' })

    await expect(autonomousFetch(schema, mockFetcher as any)).rejects.toThrow('Autonomous validation failed')
  })
})
