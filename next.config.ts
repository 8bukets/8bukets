import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  cacheComponents: true,
  reactCompiler: true,
  viewTransition: true,
  // Boost: Optimizes imports for large libraries to speed up Turbopack scanning
  optimizePackageImports: ["lucide-react", "lodash", "@supabase/supabase-js", "mongodb"],
  experimental: {
    turbopackFileSystemCacheForDev: true,
  },
  // Boost: Turbopack specific optimizations
  turbopack: {
    // Resolve alias fallback to silence Node.js native module errors in browser
    resolveAlias: {
      "mongodb-client-encryption": "node-noop",
      "aws4": "node-noop"
    },
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
  }
};

export default nextConfig;
