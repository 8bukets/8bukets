/**
 * Welcome to Cloudflare Workers! This is your first worker.
 *
 * - Run `npm run dev` in your terminal to start a development server
 * - Open a browser tab at http://localhost:8787/ to see your worker in action
 * - Run `npm run deploy` to publish your worker
 *
 * Learn more at https://developers.cloudflare.com/workers/
 */

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    if (url.pathname === '/health') {
      return new Response(JSON.stringify({ status: 'ok', worker: 'antigravity-edge-worker' }), {
        headers: { 'content-type': 'application/json' },
      });
    }

    return new Response('Hello World from Antigravity Edge Worker!', {
      headers: { 'content-type': 'text/plain' },
    });
  },
};
