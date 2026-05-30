/**
 * Next.js 16 Global Instrumentation
 * Used for observability, error tracking, and side-effects.
 export async function register() {
   // This runs once when a new Next.js instance is booted (Server-side)
   if (process.env.NEXT_RUNTIME === 'nodejs') {
     console.log('[Instrumentation] Initializing Antigravity Core...')

     // Trigger Jules' Autonomous Daily Routine
     const { jules } = await import('@/antigravity/jules')
     await jules.runDailyRoutine()

     // Example: Verify DB connectivity on boot
     try {
 ...
      const { getMongoClient } = await import('@/antigravity/core')
      await getMongoClient()
      console.log('[Instrumentation] MongoDB Connected Successfully')
    } catch (err) {
      console.error('[Instrumentation] MongoDB Connection Failed:', err)
    }
  }

  if (process.env.NEXT_RUNTIME === 'edge') {
    console.log('[Instrumentation] Initializing Edge runtime...')
  }
}

/**
 * Global Error Handler for Server-side logic
 */
export async function onRequestError(err: unknown, request: Request) {
  // Log to external services like Sentry or Axiom
  console.error(`[Request Error] ${request.method} ${request.url}:`, err)
}
