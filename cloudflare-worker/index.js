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
      // High-availability status check
      const status = {
        status: 'online',
        agent: 'Jules',
        version: '1.4.0-alpha',
        worker: 'antigravity-edge-worker',
        timestamp: new Date().toISOString(),
        manifest: 'Cloud-Native Autonomous Presence'
      };

      return new Response(JSON.stringify(status, null, 2), {
        headers: {
          'content-type': 'application/json',
          'Access-Control-Allow-Origin': '*'
        },
      });
    }

    if (url.pathname === '/presence') {
      return new Response(JSON.stringify({
        agent: 'Jules',
        mode: 'cloud-active',
        presence: 'always-on',
        ecosystem: 'Antigravity 8Bukets'
      }), {
        headers: {
          'content-type': 'application/json',
          'Access-Control-Allow-Origin': '*'
        },
      });
    }

    return new Response('ANTIGRAVITY CLOUD PRESENCE ACTIVE: 🤖 Jules is working autonomously.', {
      headers: { 'content-type': 'text/plain' },
    });
  },
};
