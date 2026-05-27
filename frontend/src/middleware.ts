import { createMiddleware } from "@arcjet/next";
import aj from "@/lib/arcjet";
import { updateSession } from "@/utils/supabase/middleware";
import { NextRequest, NextResponse } from "next/server";

export const config = {
  matcher: ["/((?!_next/static|_next/image|favicon.ico).*)"],
};

const arcjetMiddleware = createMiddleware(aj);

import type { NextFetchEvent } from "next/server";

export default async function middleware(request: NextRequest, event: NextFetchEvent) {
  // Run arcjet first so it can process telemetry via event.waitUntil
  const arcjetResponse = await arcjetMiddleware(request, event);

  // If arcjet blocks or redirects, return immediately
  if (arcjetResponse && arcjetResponse.status !== 200) {
    return arcjetResponse;
  }

  // Supabase session update middleware
  let response = NextResponse.next({
    request: {
      headers: request.headers,
    },
  });

  try {
    response = await updateSession(request, response);
  } catch (e) {
    // If Supabase environment variables are missing during build/dev, gracefully handle it
    console.warn("Supabase middleware skipped:", e);
  }

  // Manually merge Arcjet headers if needed, although next() often preserves them
  // if they were added to request headers by arcjet (which createMiddleware usually does)
  if (arcjetResponse && arcjetResponse.headers) {
    arcjetResponse.headers.forEach((value, key) => {
      // Don't overwrite existing set-cookie headers from Supabase
      if (key.toLowerCase() !== 'set-cookie') {
        response.headers.set(key, value);
      }
    });
  }

  return response;
}