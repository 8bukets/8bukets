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
      // Use relative import for runtime resolution in Next.js 16
      const { jules } = await import('./antigravity/jules')
      if (jules && typeof jules.runDailyRoutine === 'function') {
        await jules.runDailyRoutine()
      }
    } catch (e) {
      console.warn('[Instrumentation] Jules resolution failed. System remaining in manual mode.')
    }
  }
}

export async function onRequestError(err: unknown, request: Request) {
  // console.error(`[Request Error] ${request.method} ${request.url}:`, err)
}
