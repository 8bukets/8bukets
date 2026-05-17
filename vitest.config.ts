import { defineConfig } from 'vitest/config';
import path from 'path';

export default defineConfig({
  test: {
    globals: true,
    environment: 'node',
    testTimeout: 15000,
    exclude: ['**/node_modules/**', 'software-review-platform/backend/test/**'],
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './'),
      'next/cache': path.resolve(__dirname, './tests/mocks/next-cache.ts'),
      'next/server': path.resolve(__dirname, './tests/mocks/next-server.ts'),
    },
  },
});
