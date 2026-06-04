import { defineConfig } from 'vitest/config';
import path from 'path';

export default defineConfig({
  test: {
    globals: true,
    environment: 'node',
    testTimeout: 15000,
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './'),
      'next/cache': path.resolve(__dirname, './tests/mocks/next-cache.ts'),
      'next/server': path.resolve(__dirname, './tests/mocks/next-server.ts'),
    },
  },
});
