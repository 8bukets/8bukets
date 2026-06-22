// src/index.js
var index_default = {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    if (url.pathname === "/health") {
      return new Response(JSON.stringify({
        status: "online",
        agent: "Jules",
        worker: "sor8bukets",
        timestamp: (/* @__PURE__ */ new Date()).toISOString()
      }), {
        headers: { "content-type": "application/json" }
      });
    }
    return new Response("\u{1F916} Hello World from sor8bukets sovereign worker! Antigravity is active.", {
      headers: { "content-type": "text/plain" }
    });
  }
};
export {
  index_default as default
};
//# sourceMappingURL=index.js.map
