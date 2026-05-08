import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  cacheComponents: true,
  reactCompiler: true,
  experimental: {
    viewTransition: true,
    optimizePackageImports: ["lucide-react", "lodash", "@supabase/supabase-js", "mongodb"],
    instantNavigationDevToolsToggle: true,
    turbopackFileSystemCacheForDev: true,
  },
  // Scale by defining your own cache behavior across the app
  cacheLife: {
    inventory: {
      stale: 30, // 30 seconds on client
      revalidate: 60, // 1 minute on server
      expire: 60 * 5 // 5 minutes max
    },
    catalog: {
      stale: 60 * 60, // 1 hour on client
      revalidate: 60 * 60 * 4, // 4 hours on server
      expire: 60 * 60 * 24 // 24 hours max
    }
  },
  // Boost: Turbopack specific optimizations
  turbopack: {
    // Resolve alias fallback to silence Node.js native module errors in browser
    resolveAlias: {
      fs: './antigravity/empty.ts',
      path: 'path-browserify',
      os: 'os-browserify/browser',
    },
  },
};

export default nextConfig;
