/**
 * Next.js 16 Global Instrumentation
 */
export async function register() {
  if (process.env.NEXT_RUNTIME === 'nodejs') {
    // CRITICAL: NEVER run autonomous routines during build phase.
    if (process.env.NEXT_PHASE === 'phase-production-build') {
      return
    }

    console.log('[Instrumentation] Initializing Antigravity Core...')
    
    try {
      // Use dynamic import to avoid build-time tracing issues
      // @ts-ignore
      const { jules } = await import('./antigravity/jules')
      if (jules && typeof jules.runDailyRoutine === 'function') {
        await jules.runDailyRoutine()
      }
    } catch (e) {
      console.warn('[Instrumentation] Autonomous routine skipped: Could not resolve Jules.')
    }
  }
}

export async function onRequestError(err: unknown, request: Request) {
  // console.error(`[Request Error] ${request.method} ${request.url}:`, err)
}
