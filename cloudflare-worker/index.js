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

    if (request.method === 'POST' && url.pathname === '/heartbeat') {
      try {
        const payload = await request.json();
        // In a real worker, we would use env.PRESENCE_KV.put(payload.node_id, JSON.stringify(payload))
        // For simulation, we just acknowledge the heartbeat.
        return new Response(JSON.stringify({
          status: 'received',
          node_id: payload.telemetry?.node_id,
          timestamp: new Date().toISOString()
        }), {
          headers: { 'content-type': 'application/json' },
        });
      } catch (e) {
        return new Response('Invalid heartbeat payload', { status: 400 });
      }
    }

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
        ecosystem: 'Antigravity 8Bukets',
        nodes: [
          { id: 'macbook-primary-01', status: 'online_monitored' },
          { id: 'cloud-relay-01', status: 'active_standby' }
        ]
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
