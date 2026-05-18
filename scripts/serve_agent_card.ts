import * as http from 'http';

const PORT = 8080;

const agentCard = {
  id: 'antigravity-remote-endpoint',
  name: 'Antigravity Remote Agent Endpoints',
  description: 'Serves A2A requests for daily tasks and security auditor agents.',
  version: '1.0.0',
  endpoints: {
    tasks: '/api/v1/tasks',
  },
  securitySchemes: {
    apiKeyAuth: {
      type: 'apiKey',
      in: 'header',
      name: 'X-API-Key',
    },
  },
};

const server = http.createServer((req, res) => {
  if (req.method === 'GET' && req.url === '/agent-card') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(agentCard, null, 2));
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found');
  }
});

server.listen(PORT, () => {
  console.log(`Agent card server listening on port ${PORT}`);
});
