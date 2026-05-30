import { type NextRequest, NextResponse } from 'next/server'

/**
 * Next.js 16 Proxy
 * Scalable Pattern: Centralized Routing & Auth
 * Because this runs in the Node.js runtime, you can use standard Node libraries here.
 */
export async function proxy(request: NextRequest) {
  const { pathname } = request.nextUrl
  
  // 1. Scalable Auth Check (Generic)
  const token = request.cookies.get('session')?.value
  if (pathname.startsWith('/admin') && !token) {
    return NextResponse.redirect(new URL('/login', request.url))
  }

  // 2. Feature Flagging / A/B Testing at Scale
  // In a real app, you might fetch this from a DB or Redis since we are in Node.js
  const isNewStoreEnabled = true 
  if (pathname === '/shop' && isNewStoreEnabled) {
    return NextResponse.rewrite(new URL('/store/featured', request.url))
  }

  return NextResponse.next()
}

export const config = {
  matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)'],
}
