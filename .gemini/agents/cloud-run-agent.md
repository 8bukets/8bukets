---
kind: remote
name: cloud-run-agent
description: "Cloud Run specialized agent for interacting with GCP Cloud Run endpoints. Use this agent for tasks involving Google Cloud Run infrastructure, such as managing, scaling, or deploying serverless containers securely via Application Default Credentials."
agent_card_url: https://my-agent-xyz.run.app/.well-known/agent.json
auth:
  type: google-credentials
  scopes:
    - https://www.googleapis.com/auth/cloud-platform
---
