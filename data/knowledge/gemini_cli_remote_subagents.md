# Gemini CLI Remote Subagents Documentation

Ingested from raw documentation.

## Gemini CLI Remote Subagents

Gemini CLI supports connecting to remote subagents using the Agent-to-Agent (A2A) protocol. This allows Gemini CLI to interact with other agents, expanding its capabilities by delegating tasks to remote services.

Remote subagents are defined as Markdown files (.md) with YAML frontmatter. They can be placed in `.gemini/agents/*.md` (Project-level) or `~/.gemini/agents/*.md` (User-level).

## Gemini CLI Remote Subagent Configuration Schema

The YAML frontmatter configuration schema for remote subagents.

Required fields include `kind: remote`, `name` (a valid slug), and either `agent_card_url` or `agent_card_json`. Optional `auth` object is used for authentication configuration.

## Gemini CLI Remote Subagent Authentication

Gemini CLI supports multiple authentication types for remote agents: `apiKey`, `http`, `google-credentials`, and `oauth`.

Secret values support dynamic resolution like `$ENV_VAR` or `!command`. `google-credentials` automatically selects access or identity tokens based on the host pattern (`*.googleapis.com` or `*.run.app`).

## Gemini CLI Remote Subagent Proxy Support

Gemini CLI routes traffic to remote agents through an HTTP/HTTPS proxy if configured.

It uses `general.proxy` in `settings.json` or standard environment variables (`HTTP_PROXY`, `HTTPS_PROXY`).

## Gemini CLI Managing Subagents

Users can manage subagents using slash commands within Gemini CLI.

Commands include `/agents list`, `/agents reload`, `/agents enable <agent_name>`, and `/agents disable <agent_name>`. Remote agents can be globally disabled by setting `experimental.enableAgents` to `false` in `settings.json`.
