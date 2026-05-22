/**
 * Welcome to Cloudflare Workers!
 *
 * - This worker acts as a global status beacon for the Antigravity Autonomous System.
 * - It fetches real-time presence data from Supabase to provide an always-on "Online Presence".
 */

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    // Helper to fetch from Supabase
    const getSupabasePresence = async () => {
      const sbUrl = env.SUPABASE_URL;
      const sbKey = env.SUPABASE_ANON_KEY;

      if (!sbUrl || !sbKey) return null;

      try {
        const response = await fetch(`${sbUrl}/rest/v1/agent_presence?agent=eq.Jules&select=*`, {
          headers: {
            'apikey': sbKey,
            'Authorization': `Bearer ${sbKey}`,
            'Content-Type': 'application/json'
          }
        });

        if (response.ok) {
          const data = await response.json();
          return data[0] || null;
        }
      } catch (e) {
        console.error('Failed to fetch from Supabase:', e);
      }
      return null;
    };

    if (url.pathname === '/health') {
      const presence = await getSupabasePresence();

      const status = {
        status: presence ? 'online' : 'beacon-active',
        agent: 'Jules',
        version: '1.4.0-alpha',
        worker: 'antigravity-edge-worker',
        timestamp: new Date().toISOString(),
        manifest: 'Cloud-Native Autonomous Presence',
        cloud_state: presence ? {
          last_seen: presence.lastSeen,
          mode: presence.execution_mode,
          env: presence.environment,
          connectivity: presence.connectivity,
          visual_heartbeat: presence.visual_heartbeat,
          telemetry: presence.telemetry
        } : 'awaiting-heartbeat'
      };

      return new Response(JSON.stringify(status, null, 2), {
        headers: {
          'content-type': 'application/json',
          'Access-Control-Allow-Origin': '*'
        },
      });
    }

    if (url.pathname === '/presence') {
      const presence = await getSupabasePresence();

      return new Response(JSON.stringify({
        agent: 'Jules',
        mode: presence?.execution_mode || 'cloud-active',
        presence: presence ? 'always-on' : 'standby',
        ecosystem: 'Antigravity 8Bukets',
        last_pulse: presence?.lastSeen || 'unknown',
        heartbeat: presence?.visual_heartbeat || { pulse_intensity: 0, last_action: 'waiting' },
        telemetry: presence?.telemetry || { provider_health: 'unknown' }
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
