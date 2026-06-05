---
kind: remote
name: a2a-remote-agent
description: "A2A Remote Agent implementing the Agent-to-Agent protocol based on the provided Gemini CLI specification. Use this to delegate tasks to compatible remote A2A services deployed on Cloud Run."
agent_card_url: https://my-a2a-service-xyz.run.app/.well-known/agent.json
auth:
  type: google-credentials
  scopes:
    - https://www.googleapis.com/auth/cloud-platform
---
