/**
 * SOR8BUKETS WORKER
 * Standard ecosystem worker for Antigravity intelligence distribution.
 */

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    if (url.pathname === '/health') {
      return new Response(JSON.stringify({
        status: 'online',
        agent: 'Jules',
        worker: 'sor-8bukets',
        timestamp: new Date().toISOString()
      }), {
        headers: { 'content-type': 'application/json' }
      });
    }

    return new Response('🤖 Hello World from sor-8bukets sovereign worker! Antigravity is active.', {
      headers: { 'content-type': 'text/plain' },
    });
  },
};
