import * as http from 'http';

const PORT = 8080;

const agentCard = {
  name: "agent",
  description: "A helpful coding assistant",
  skills: [
    {
      id: "agent_root",
      name: "root",
      description: "A helpful coding assistant",
      tags: ["llm", "dockeragent"]
    }
  ],
  preferredTransport: "jsonrpc",
  url: `http://localhost:${PORT}/invoke`,
  capabilities: {
    streaming: true
  },
  version: "0.1.0"
};

const server = http.createServer((req, res) => {
  if (req.method === 'GET' && req.url === '/.well-known/agent-card') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(agentCard, null, 2));
  } else if (req.method === 'POST' && req.url === '/invoke') {
    let body = '';
    req.on('data', chunk => {
      body += chunk.toString();
    });
    req.on('end', () => {
      try {
        const rpcRequest = JSON.parse(body);

        let responseText = "I received your message.";
        if (rpcRequest.params && rpcRequest.params.message && rpcRequest.params.message.parts) {
            const parts = rpcRequest.params.message.parts;
            const textPart = parts.find((p: any) => p.kind === 'text');
            if (textPart && textPart.text === 'What is 2+2?') {
                responseText = "2+2 equals 4.";
            }
        }

        const rpcResponse = {
          jsonrpc: "2.0",
          id: rpcRequest.id || null,
          result: {
            artifacts: [
              {
                parts: [
                  {
                    kind: "text",
                    text: responseText
                  }
                ]
              }
            ]
          }
        };
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify(rpcResponse, null, 2));
      } catch (err) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({
          jsonrpc: "2.0",
          error: {
            code: -32700,
            message: "Parse error"
          },
          id: null
        }));
      }
    });
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found');
  }
});

server.listen(PORT, () => {
  console.log(`Agent server listening on port ${PORT}`);
});
