// index.js
var index_default = {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    if (request.method === "POST" && url.pathname === "/heartbeat") {
      try {
        const payload = await request.json();
        if (env.PRESENCE_KV) {
          await env.PRESENCE_KV.put(`presence:${payload.telemetry?.node_id || "unknown"}`, JSON.stringify({
            ...payload,
            edge_received_at: (/* @__PURE__ */ new Date()).toISOString()
          }), { expirationTtl: 600 });
        }
        return new Response(JSON.stringify({
          status: "received",
          node_id: payload.telemetry?.node_id,
          leadership: payload.leadership_status || "subordinate",
          timestamp: (/* @__PURE__ */ new Date()).toISOString()
        }), {
          headers: {
            "content-type": "application/json",
            "Access-Control-Allow-Origin": "*"
          }
        });
      } catch (e) {
        return new Response(JSON.stringify({ error: "Invalid heartbeat payload" }), {
          status: 400,
          headers: { "content-type": "application/json" }
        });
      }
    }
    if (url.pathname === "/health") {
      const status = {
        status: "online",
        agent: "Jules",
        version: "1.6.0-alpha",
        worker: "antigravity-edge-worker",
        timestamp: (/* @__PURE__ */ new Date()).toISOString(),
        capabilities: ["edge-presence", "heartbeat-sync", "sovereign-routing"],
        manifest: "Cloud-Native Autonomous Presence (Phase 22)"
      };
      return new Response(JSON.stringify(status, null, 2), {
        headers: {
          "content-type": "application/json",
          "Access-Control-Allow-Origin": "*"
        }
      });
    }
    if (url.pathname === "/presence") {
      return new Response(JSON.stringify({
        agent: "Jules",
        mode: "cloud-sovereign",
        presence: "always-on",
        ecosystem: "Antigravity 8Bukets",
        active_providers: ["docker", "github", "gitlab", "gitkraken", "supabase", "mongodb"],
        nodes: [
          { id: "macbook-primary-01", status: "monitored", priority: 100 },
          { id: "cloud-relay-01", status: "active_standby", priority: 10 }
        ],
        sovereignty: "established"
      }), {
        headers: {
          "content-type": "application/json",
          "Access-Control-Allow-Origin": "*"
        }
      });
    }
    return new Response("\u{1F916} ANTIGRAVITY CLOUD SOVEREIGNTY ACTIVE: Jules is working autonomously in the cloud.", {
      headers: { "content-type": "text/plain" }
    });
  }
};
export {
  index_default as default
};
//# sourceMappingURL=index.js.map
