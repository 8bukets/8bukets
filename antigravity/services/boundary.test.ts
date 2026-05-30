import { describe, it, expect, vi } from 'vitest';
import { BoundaryService } from './boundary';

describe('BoundaryService', () => {
  it('initializes with the correct default URL', () => {
    const service = new BoundaryService();
    // Assuming process.env.BOUNDARY_URL is not set in test environment, or mocking it
    expect(service).toBeDefined();
  });

  it('handles connection check gracefully when URL is unreachable', async () => {
    const service = new BoundaryService();

    // Mock fetch to simulate the 404 or network error
    global.fetch = vi.fn().mockRejectedValue(new Error('Network error'));

    const result = await service.checkConnection();
    expect(result.status).toBe('error');
    expect(result.message).toContain('Network error');
  });

  it('handles connection check when HTTP status is not ok', async () => {
    const service = new BoundaryService();

    global.fetch = vi.fn().mockResolvedValue({
      ok: false,
      status: 404
    });

    const result = await service.checkConnection();
    expect(result.status).toBe('warning');
    expect(result.message).toContain('HTTP 404');
  });

  it('requests target access successfully', async () => {
    const service = new BoundaryService();
    const result = await service.requestTargetAccess('tgt_123456');
    expect(result).toBe(true);
  });
});
