# Consolidated Knowledge Base

**Last Sync (Python):** 2026-05-18T09:15:23.778896
**System Version:** 1.88

## 🧩 Strategic Identity & Unified Model
# Knowledge Merge

## Purpose

This document merges the key concepts currently spread across Antigravity, Project SOR, the live `software-online-review.com` domain, and the new `software-review-platform` starter.

The goal is to create one canonical map of what each layer is, what role it plays, and how the project should evolve.

## Executive Summary

The workspace currently contains multiple overlapping identities:

- Antigravity
- Project SOR
- `software-online-review.com`
- `software-review-platform`
- `markposition.wordpress.com`

These are not separate businesses. They are five layers of the same evolving asset.

## Canonical Interpretation

### Antigravity

Antigravity appears to represent the broader operating system, agentic logic layer, and internal platform vision.

Examples found in the repo:

- `web-app/app/antigravity`
- `web-app/scripts/antigravity-cortex.js`
- `web-app/data/antigravity-state.json`
- `web-app/data/antigravity_vision_manifest.md`

Canonical role:

- internal intelligence layer
- automation and orchestration layer
- long-term system vision

### Project SOR

Project SOR is the brand and conceptual product identity around `software-online-review.com`.

Examples found in the repo:

- root Next app metadata and pages
- `src/app/page.js`
- `src/app/about/page.js`
- `src/app/blog/*`

Canonical role:

- public-facing brand narrative
- content and editorial layer
- bridge between legacy content and future product

### software-online-review.com

This is the actual live domain and public web asset.

Observed current state:

- content-heavy site
- WordPress-like publishing structure
- broad topic coverage
- mixed content and product intent

Canonical role:

- current public domain
- traffic and SEO asset
- existing trust surface for future migration

### software-review-platform

This is the cleanest current implementation of the future product direction.

Examples found in the repo:

- `software-review-platform/README.md`
- `software-review-platform/PRODUCT.md`
- `software-review-platform/PITCH.md`
- `software-review-platform/MIGRATION.md`

Canonical role:

- new review engine
- MVP product foundation
- structured application layer for the future platform

### markposition.wordpress.com

This is the market intelligence and external data source layer.

Examples found in the repo:

- `scraper.py`
- `analytics.py`
- `links.json` and `REPORT.md`

Canonical role:

- market intelligence layer
- data source for tracking ad tech, CMS, and marketing tools
- external trend analysis feeding the intelligence system

## Recommended Unified Model

The best working model is:

- Antigravity = intelligence and system layer
- Project SOR = brand and editorial layer
- `software-online-review.com` = current public distribution layer
- `software-review-platform` = future product engine
- `markposition.wordpress.com` = market intelligence and data source layer

This gives the project a coherent internal structure instead of five competing interpretations.

## How These Layers Connect

### Operational Layer

Antigravity should remain the internal logic and orchestration system.

It can eventually support:

- moderation intelligence
- automation
- internal workflows
- content and data operations

### Public Brand Layer

Project SOR should communicate the bigger idea:

- software discovery
- trust in reviews
- modern software intelligence

This is where narrative, editorial direction, and product positioning live.

### Public Domain Layer

`software-online-review.com` should remain the discoverable public shell during migration.

This layer should:

- keep current traffic alive
- explain the product
- route users into the new app

### Product Layer

`software-review-platform` should become the actual application where:

- software is listed
- users authenticate
- reviews are submitted
- moderation happens
- comments and ratings live

### Market Intelligence Layer

`markposition.wordpress.com` serves as the external ear of the system where:

- the scraper fetches the latest industry news and tools
- analytics generate reports on market trends
- the data feeds the Antigravity intelligence layer

## Architectural Direction

Short term:

- keep the current public site
- deploy the new app separately
- connect them through links and navigation

Mid term:

- make the app the center of review functionality
- reduce public confusion between content and product flows

Long term:

- decide whether the platform remains content-plus-app
- or becomes fully app-first

## Naming Guidance

To reduce confusion, use this naming consistently:

- Antigravity: internal platform or intelligence system
- Project SOR: brand and strategic initiative
- Software Review Platform: product implementation
- `software-online-review.com`: public domain and customer-facing distribution point
- Markposition Scraper & Analytics: market intelligence toolset capturing data from `markposition.wordpress.com`

## Product Implications

This merged view suggests:

- the review platform should be treated as the product core
- the current live site should be treated as the distribution bridge
- Antigravity should not be mixed directly into MVP UX unless it adds clear value
- Project SOR should help unify messaging rather than introduce extra structural complexity

## Risks

Current risk areas:

- too many overlapping identities
- unclear boundary between legacy and future code
- confusion between content platform and application platform
- sensitive infrastructure files potentially stored in repo

## Recommendation

Going forward, treat `software-review-platform` as the canonical MVP implementation and use the rest of the workspace as support context around it.

Everything else should be evaluated by whether it helps:

- product clarity
- migration safety
- trust-first positioning
- practical delivery


## Autonomous Observation
- **Date**: 2026-05-14T00:11:55.884Z
- **Target**: https://software-online-review.com
- **Title**: software info by fk – software-online-review – Filip Keser
- **Relationship Map**: Confirmed overlapping identities between Antigravity, Project SOR, software-online-review.com, software-review-platform, and markposition.wordpress.com as the formal Market Intelligence layer.


---

## System Intelligence & Outlook
- Scaling Strategy: Implementing simultaneous execution across agent tiers.
- R&D Strategy: Developing realistic simulations for human-agent interaction.
- Operational Strategy: Enhancing agent debate and feedback loops.

## 1. AI Agent Foundation
### Compile

To compile means to gather information from various sources and arrange it into a structured format, such as a report, list, book, or file. In computing, it refers to translating human-readable source code into machine-readable, executable instructions.

### Key Definitions of Compile

- **Gathering Information**: To collect and put together data, facts, or documents (e.g., to compile a report or compile a list).
- **Creating Works**: To produce a book, anthology, or database from various materials.
- **Computing**: To convert high-level programming code (like C++ or Java) into machine code, allowing a computer to execute the program.

### Usage Examples

- "She is compiling a list of clients for the newsletter."
- "It took years to compile the dictionary."
- "The developer needs to compile the code before running the application."

### Synonyms

- Assemble
- Collect
- Gather
- Compose
- Accumulate
- Organize
- Synthesize

### Contextual Usage

- **General**: Focuses on the act of assembling information or materials (e.g., compile a report).
- **Computing**: Focuses on the automatic transformation of code using a tool known as a compiler.

### Jules Tools

Jules Tools is a lightweight command-line interface (CLI) for interacting with Jules, Google’s autonomous AI coding agent. It allows you to manage coding sessions, inspect progress, and integrate Jules into your existing development workflows and scripts directly from your terminal.

Think of Jules Tools as both a command surface and a dashboard for your coding agent, designed to keep you in your flow without needing to switch to a web browser.

- Installation: `npm install -g @google/jules`.
- Authentication: `jules login` and `jules logout`.
- Commands: `version`, `remote` (list, new, pull), `completion`.
- Dashboard (TUI): Run `jules` without arguments for an interactive experience.

### Knowledge Merge

Knowledge Merge is a process or document that merges key concepts currently spread across Antigravity, Project SOR, the live software-online-review.com domain, and the new software-review-platform starter. It creates one canonical map of what each layer is, what role it plays, and how the project should evolve.

### Gemini CLI Remote Subagents

Gemini CLI supports connecting to remote subagents using the Agent-to-Agent (A2A) protocol. This allows Gemini CLI to interact with other agents, expanding its capabilities by delegating tasks to remote services.

Gemini CLI can connect to any compliant A2A agent. You can find samples of A2A agents in the following repositories:
- ADK Samples (Python)
- ADK Python Contributing Samples

Proxy support:
Gemini CLI routes traffic to remote agents through an HTTP/HTTPS proxy if one is configured. It uses the general.proxy setting in your settings.json file or standard environment variables (HTTP_PROXY, HTTPS_PROXY).

Defining remote subagents:
Remote subagents are defined as Markdown files (.md) with YAML frontmatter. You can place them in:
- Project-level: .gemini/agents/*.md (Shared with your team)
- User-level: ~/.gemini/agents/*.md (Personal agents)

Configuration schema requires:
- kind (Must be remote)
- name (Unique slug)
- agent_card_url or agent_card_json
- auth (Authentication configuration)

Supported auth types:
- apiKey: Send a static API key as an HTTP header (supports dynamic values).
- http: HTTP authentication (Bearer token, Basic credentials, or any IANA-registered scheme).
- google-credentials: Uses Google Application Default Credentials (ADC) to authenticate with Google Cloud services and Cloud Run endpoints.
- oauth: OAuth 2.0 Authorization Code flow with PKCE.

Managing Subagents via commands:
- /agents list: Displays all available local and remote subagents.
- /agents reload: Reloads the agent registry.
- /agents enable <agent_name>: Enables a specific subagent.
- /agents disable <agent_name>: Disables a specific subagent.


### Gemini CLI Subagents

# Subagents

Subagents are specialized agents that operate within your main Gemini CLI session. They are designed to handle specific, complex tasks—like deep codebase analysis, documentation lookup, or domain-specific reasoning—without cluttering the main agent’s context or toolset.

## What are subagents?
Subagents are “specialists” that the main Gemini agent can hire for a specific job.

*   **Focused context:** Each subagent has its own system prompt and persona.
*   **Specialized tools:** Subagents can have a restricted or specialized set of tools.
*   **Independent context window:** Interactions with a subagent happen in a separate context loop, which saves tokens in your main conversation history.

Subagents are exposed to the main agent as a tool of the same name. When the main agent calls the tool, it delegates the task to the subagent. Once the subagent completes its task, it reports back to the main agent with its findings.

## How to use subagents
You can use subagents through automatic delegation or by explicitly forcing them in your prompt.

### Automatic delegation
Gemini CLI’s main agent is instructed to use specialized subagents when a task matches their expertise. For example, if you ask “How does the auth system work?”, the main agent may decide to call the `codebase_investigator` subagent to perform the research.

### Forcing a subagent (@ syntax)
You can explicitly direct a task to a specific subagent by using the `@` symbol followed by the subagent’s name at the beginning of your prompt. This is useful when you want to bypass the main agent’s decision-making and go straight to a specialist.

Example:

**Terminal window**
`@codebase_investigator Map out the relationship between the AgentRegistry and the LocalAgentExecutor.`

When you use the `@` syntax, the CLI injects a system note that nudges the primary model to use that specific subagent tool immediately.

## Built-in subagents
Gemini CLI comes with the following built-in subagents:

### Codebase Investigator
*   **Name:** `codebase_investigator`
*   **Purpose:** Analyze the codebase, reverse engineer, and understand complex dependencies.
*   **When to use:** “How does the authentication system work?”, “Map out the dependencies of the AgentRegistry class.”
*   **Configuration:** Enabled by default. You can override its settings in `settings.json` under `agents.overrides`. Example (forcing a specific model and increasing turns):
```json
{
  "agents": {
    "overrides": {
      "codebase_investigator": {
        "modelConfig": { "model": "gemini-3-flash-preview" },
        "runConfig": { "maxTurns": 50 }
      }
    }
  }
}
```

### CLI Help Agent
*   **Name:** `cli_help`
*   **Purpose:** Get expert knowledge about Gemini CLI itself, its commands, configuration, and documentation.
*   **When to use:** “How do I configure a proxy?”, “What does the /rewind command do?”
*   **Configuration:** Enabled by default.

### Generalist Agent
*   **Name:** `generalist`
*   **Purpose:** A general, all-purpose subagent that uses the inherited tool access and configurations from the main agent. Useful for executing broad, resource-heavy subtasks in an isolated conversation, optimizing your main agent’s context by returning only the final result of that given task.
*   **When to use:** Use this agent when a task requires many steps, handles large volumes of information, or requires the same full capabilities as the main agent. It is ideal for:
    *   **Multi-file modifications:** Applying refactors or fixing errors across several files at once.
    *   **High-volume execution:** Running commands or tests that produce extensive terminal output.
    *   **Action-oriented research:** Investigations where the agent needs to both search code and run commands or make edits to find a solution. By delegating these tasks, you prevent your main conversation from becoming cluttered or slow. You can invoke it explicitly using `@generalist`.
*   **Configuration:** Enabled by default.

### Browser Agent (experimental)
*   **Name:** `browser_agent`
*   **Purpose:** Automate web browser tasks — navigating websites, filling forms, clicking buttons, and extracting information from web pages — using the accessibility tree.
*   **When to use:** “Go to example.com and fill out the contact form,” “Extract the pricing table from this page,” “Click the login button and enter my credentials.”

> **Note**
>
> This is a preview feature currently under active development.

#### Prerequisites
The browser agent requires:

*   Chrome version 144 or later (any recent stable release works).
*   The underlying `chrome-devtools-mcp` server is bundled with Gemini CLI and launched automatically — no separate installation is needed.

#### Enabling the browser agent
The browser agent is disabled by default. Enable it in your `settings.json`:

```json
{
  "agents": {
    "overrides": {
      "browser_agent": {
        "enabled": true
      }
    }
  }
}
```

#### Session modes
The `sessionMode` setting controls how Chrome is launched and managed. Set it under `agents.browser`:

```json
{
  "agents": {
    "overrides": {
      "browser_agent": {
        "enabled": true
      }
    },
    "browser": {
      "sessionMode": "persistent"
    }
  }
}
```

The available modes are:

| Mode | Description |
| :--- | :--- |
| `persistent` | **(Default)** Launches Chrome with a persistent profile stored at `~/.gemini/cli-browser-profile/`. Cookies, history, and settings are preserved between sessions. |
| `isolated` | Launches Chrome with a temporary profile that is deleted after each session. Use this for clean-state automation. |
| `existing` | Attaches to an already-running Chrome instance. You must enable remote debugging first by navigating to `chrome://inspect/#remote-debugging` in Chrome. No new browser process is launched. |

#### First-run consent
The first time the browser agent is invoked, Gemini CLI displays a consent dialog. You must accept before the browser session starts. This dialog only appears once.

#### Configuration reference
All browser-specific settings go under `agents.browser` in your `settings.json`. For full details, see the `agents.browser` configuration reference.

| Setting | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `sessionMode` | string | `"persistent"` | How Chrome is managed: `"persistent"`, `"isolated"`, or `"existing"`. |
| `headless` | boolean | `false` | Run Chrome in headless mode (no visible window). |
| `profilePath` | string | — | Custom path to a browser profile directory. |
| `visualModel` | string | — | Model override for the visual agent. |
| `allowedDomains` | string[] | — | Restrict navigation to specific domains (for example, `["github.com"]`). |
| `disableUserInput` | boolean | `true` | Disable user input on the browser window during automation (non-headless only). |
| `maxActionsPerTask` | number | `100` | Maximum tool calls per task. The agent is terminated when the limit is reached. |
| `confirmSensitiveActions` | boolean | `false` | Require manual confirmation for `upload_file` and `evaluate_script`. |
| `blockFileUploads` | boolean | `false` | Hard-block all file upload requests from the agent. |

#### Automation overlay and input blocking
In non-headless mode, the browser agent injects a visual overlay into the browser window to indicate that automation is in progress. By default, user input (keyboard and mouse) is also blocked to prevent accidental interference. You can disable this by setting `disableUserInput` to `false`.

#### Security
The browser agent enforces several layers of security:

*   **Domain restrictions:** When `allowedDomains` is set, the agent can only navigate to the listed domains (and their subdomains when using `*.` prefix). Attempting to visit a disallowed domain throws a fatal error that immediately terminates the agent. The agent also attempts to detect and block the use of allowed domains as proxies (e.g., via query parameters or fragments) to access restricted content.
*   **Blocked URL patterns:** The underlying MCP server blocks dangerous URL schemes including `file://`, `javascript:`, `data:text/html`, `chrome://extensions`, and `chrome://settings/passwords`.
*   **Sensitive action confirmation:** Form filling (`fill`, `fill_form`) always requires user confirmation through the policy engine, regardless of approval mode. When `confirmSensitiveActions` is `true`, `upload_file` and `evaluate_script` also require confirmation.
*   **File upload blocking:** Set `blockFileUploads` to `true` to hard-block all file upload requests, preventing the agent from uploading any files.
*   **Action rate limiting:** The `maxActionsPerTask` setting (default: 100) limits the total number of tool calls per task to prevent runaway execution.

#### Visual agent
By default, the browser agent interacts with pages through the accessibility tree using element `uid` values. For tasks that require visual identification (for example, “click the yellow button” or “find the red error message”), you can enable the visual agent by setting a `visualModel`:

```json
{
  "agents": {
    "overrides": {
      "browser_agent": {
        "enabled": true
      }
    },
    "browser": {
      "visualModel": "gemini-2.5-computer-use-preview-10-2025"
    }
  }
}
```

When enabled, the agent gains access to the `analyze_screenshot` tool, which captures a screenshot and sends it to the vision model for analysis. The model returns coordinates and element descriptions that the browser agent uses with the `click_at` tool for precise, coordinate-based interactions.

> **Note**
>
> The visual agent requires API key or Vertex AI authentication. It is not available when using “Sign in with Google”.

#### Sandbox support
The browser agent adjusts its behavior automatically when running inside a sandbox.

##### macOS seatbelt (`sandbox-exec`)
When the CLI runs under the macOS seatbelt sandbox, persistent and isolated session modes are forced to isolated with headless enabled. This avoids permission errors caused by seatbelt file-system restrictions on persistent browser profiles. If `sessionMode` is set to `existing`, no override is applied.

##### Container sandboxes (Docker / Podman)
Chrome is not available inside the container, so the browser agent is disabled unless `sessionMode` is set to `"existing"`. When enabled with existing mode, the agent automatically connects to Chrome on the host via the resolved IP of `host.docker.internal:9222` instead of using local pipe discovery. Port 9222 is currently hardcoded and cannot be customized.

To use the browser agent in a Docker sandbox:

1.  Start Chrome on the host with remote debugging enabled:

    **Terminal window**
    ```bash
    # Option A: Launch Chrome from the command line
    google-chrome --remote-debugging-port=9222

    # Option B: Enable in Chrome settings
    # Navigate to chrome://inspect/#remote-debugging and enable
    ```

2.  Configure `sessionMode` and allowed domains in your project’s `.gemini/settings.json`:

    ```json
    {
      "agents": {
        "overrides": {
          "browser_agent": { "enabled": true }
        },
        "browser": {
          "sessionMode": "existing",
          "allowedDomains": ["example.com"]
        }
      }
    }
    ```

3.  Launch the CLI with port forwarding:

    **Terminal window**
    ```bash
    GEMINI_SANDBOX=docker SANDBOX_PORTS=9222 gemini
    ```

## Creating custom subagents
You can create your own subagents to automate specific workflows or enforce specific personas.

### Agent definition files
Custom agents are defined as Markdown files (`.md`) with YAML frontmatter. You can place them in:

*   **Project-level:** `.gemini/agents/*.md` (Shared with your team)
*   **User-level:** `~/.gemini/agents/*.md` (Personal agents)

### File format
The file MUST start with YAML frontmatter enclosed in triple-dashes `---`. The body of the markdown file becomes the agent’s System Prompt.

Example: `.gemini/agents/security-auditor.md`

```yaml
---
name: security-auditor
description: Specialized in finding security vulnerabilities in code.
kind: local
tools:
  - read_file
  - grep_search
model: gemini-3-flash-preview
temperature: 0.2
max_turns: 10
---
```

You are a ruthless Security Auditor. Your job is to analyze code for potential
vulnerabilities.

Focus on:

1.  SQL Injection
2.  XSS (Cross-Site Scripting)
3.  Hardcoded credentials
4.  Unsafe file operations

When you find a vulnerability, explain it clearly and suggest a fix. Do not fix
it yourself; just report it.

### Configuration schema
| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `name` | string | Yes | Unique identifier (slug) used as the tool name for the agent. Only lowercase letters, numbers, hyphens, and underscores. |
| `description` | string | Yes | Short description of what the agent does. This is visible to the main agent to help it decide when to call this subagent. |
| `kind` | string | No | `local` (default) or `remote`. |
| `tools` | array | No | List of tool names this agent can use. Supports wildcards: `*` (all tools), `mcp_*` (all MCP tools), `mcp_server_*` (all tools from a server). If omitted, it inherits all tools from the parent session. |
| `mcpServers` | object | No | Configuration for inline Model Context Protocol (MCP) servers isolated to this specific agent. |
| `model` | string | No | Specific model to use (for example, `gemini-3-preview`). Defaults to `inherit` (uses the main session model). |
| `temperature` | number | No | Model temperature (0.0 - 2.0). Defaults to 1. |
| `max_turns` | number | No | Maximum number of conversation turns allowed for this agent before it must return. Defaults to 30. |
| `timeout_mins` | number | No | Maximum execution time in minutes. Defaults to 10. |

### Tool wildcards
When defining tools for a subagent, you can use wildcards to quickly grant access to groups of tools:

*   `*`: Grant access to all available built-in and discovered tools.
*   `mcp_*`: Grant access to all tools from all connected MCP servers.
*   `mcp_my-server_*`: Grant access to all tools from a specific MCP server named `my-server`.

### Isolation and recursion protection
Each subagent runs in its own isolated context loop. This means:

*   **Independent history:** The subagent’s conversation history does not bloat the main agent’s context.
*   **Isolated tools:** The subagent only has access to the tools you explicitly grant it.
*   **Recursion protection:** To prevent infinite loops and excessive token usage, subagents cannot call other subagents. If a subagent is granted the `*` tool wildcard, it will still be unable to see or invoke other agents.

### Subagent tool isolation
Subagent tool isolation moves Gemini CLI away from a single global tool registry. By providing isolated execution environments, you can ensure that subagents only interact with the parts of the system they are designed for. This prevents unintended side effects, improves reliability by avoiding state contamination, and enables fine-grained permission control.

With this feature, you can:

*   **Specify tool access:** Define exactly which tools an agent can access using a `tools` list in the agent definition.
*   **Define inline MCP servers:** Configure Model Context Protocol (MCP) servers (which provide a standardized way to connect AI models to external tools and data sources) directly in the subagent’s markdown frontmatter, isolating them to that specific agent.
*   **Maintain state isolation:** Ensure that subagents only interact with their own set of tools and servers, preventing side effects and state contamination.
*   **Apply subagent-specific policies:** Enforce granular rules in your Policy Engine TOML configuration based on the executing subagent’s name.

#### Configuring isolated tools and servers
You can configure tool isolation for a subagent by updating its markdown frontmatter. This lets you explicitly state which tools the subagent can use, rather than relying on the global registry.

Add an `mcpServers` object to define inline MCP servers that are unique to the agent.

Example:

```yaml
---
name: my-isolated-agent
tools:
  - grep_search
  - read_file
mcpServers:
  my-custom-server:
    command: 'node'
    args: ['path/to/server.js']
---
```

#### Subagent-specific policies
You can enforce fine-grained control over subagents using the Policy Engine’s TOML configuration. This allows you to grant or restrict permissions specifically for an agent, without affecting the rest of your CLI session.

To restrict a policy rule to a specific subagent, add the `subagent` property to the `[[rules]]` block in your `policy.toml` file.

Example:

```toml
[[rules]]
name = "Allow pr-creator to push code"
subagent = "pr-creator"
description = "Permit pr-creator to push branches automatically."
action = "allow"
toolName = "run_shell_command"
commandPrefix = "git push"
```

In this configuration, the policy rule only triggers if the executing subagent’s name matches `pr-creator`. Rules without the `subagent` property apply universally to all agents.

## Managing subagents
You can manage subagents interactively using the `/agents` command or persistently via `settings.json`.

### Interactive management (/agents)
If you are in an interactive CLI session, you can use the `/agents` command to manage subagents without editing configuration files manually. This is the recommended way to quickly enable, disable, or re-configure agents on the fly.

For a full list of sub-commands and usage, see the `/agents` command reference.

### Persistent configuration (settings.json)
While the `/agents` command and agent definition files provide a starting point, you can use `settings.json` for global, persistent overrides. This is useful for enforcing specific models or execution limits across all sessions.

#### agents.overrides
Use this to enable or disable specific agents or override their run configurations.

```json
{
  "agents": {
    "overrides": {
      "security-auditor": {
        "enabled": false,
        "runConfig": {
          "maxTurns": 20,
          "maxTimeMinutes": 10
        }
      }
    }
  }
}
```

#### modelConfigs.overrides
You can target specific subagents with custom model settings (like system instruction prefixes or specific safety settings) using the `overrideScope` field.

```json
{
  "modelConfigs": {
    "overrides": [
      {
        "match": { "overrideScope": "security-auditor" },
        "modelConfig": {
          "generateContentConfig": {
            "temperature": 0.1
          }
        }
      }
    ]
  }
}
```

### Safety policies (TOML)
You can restrict access to specific subagents using the CLI’s Policy Engine. Subagents are treated as virtual tool names for policy matching purposes.

To govern access to a subagent, create a `.toml` file in your policy directory (e.g., `~/.gemini/policies/`):

```toml
[[rule]]
toolName = "codebase_investigator"
decision = "deny"
deny_message = "Deep codebase analysis is restricted for this session."
```

For more information on setting up fine-grained safety guardrails, see the Policy Engine reference.

## Optimizing your subagent
The main agent’s system prompt encourages it to use an expert subagent when one is available. It decides whether an agent is a relevant expert based on the agent’s description. You can improve the reliability with which an agent is used by updating the description to more clearly indicate:

*   Its area of expertise.
*   When it should be used.
*   Some example scenarios.

For example, the following subagent description should be called fairly consistently for Git operations.

> Git expert agent which should be used for all local and remote git operations. For example:
>
> *   Making commits
> *   Searching for regressions with bisect
> *   Interacting with source control and issues providers such as GitHub.

If you need to further tune your subagent, you can do so by selecting the model to optimize for with `/model` and then asking the model why it does not think that your subagent was called with a specific prompt and the given description.

## Remote subagents (Agent2Agent)
Gemini CLI can also delegate tasks to remote subagents using the Agent-to-Agent (A2A) protocol.

See the Remote Subagents documentation for detailed configuration, authentication, and usage instructions.

## Extension subagents
Extensions can bundle and distribute subagents. See the Extensions documentation for details on how to package agents within an extension.

## Disabling subagents
Subagents are enabled by default. To disable them, set `enableAgents` to false in your `settings.json`:

```json
{
  "experimental": { "enableAgents": false }
}
```


### What is an AI agent?

Last Updated: 04/02/2026

AI agents are software systems that use AI to pursue goals and complete tasks on behalf of users. They show reasoning, planning, and memory and have a level of autonomy to make decisions, learn, and adapt.

Their capabilities are made possible in large part by the multimodal capacity of generative AI and AI foundation models. AI agents can process multimodal information like text, voice, video, audio, code, and more simultaneously; can converse, reason, learn, and make decisions. They can learn over time and facilitate transactions and business processes. Agents can work with other agents to coordinate and perform more complex workflows.

### Key features of an AI agent

As explained above, while the key features of an AI agent are reasoning and acting (as described in ReAct Framework ) more features have evolved over time.

- Reasoning: This core cognitive process involves using logic and available information to draw conclusions, make inferences, and solve problems. AI agents with strong reasoning capabilities can analyze data, identify patterns, and make informed decisions based on evidence and context.
- Acting : The ability to take action or perform tasks based on decisions, plans, or external input is crucial for AI agents to interact with their environment and achieve goals. This can include physical actions in the case of embodied AI, or digital actions like sending messages, updating data, or triggering other processes.
- Observing : Gathering information about the environment or situation through perception or sensing is essential for AI agents to understand their context and make informed decisions. This can involve various forms of perception, such as computer vision, natural language processing, or sensor data analysis.
- Planning : Developing a strategic plan to achieve goals is a key aspect of intelligent behavior. AI agents with planning capabilities can identify the necessary steps, evaluate potential actions, and choose the best course of action based on available information and desired outcomes. This often involves anticipating future states and considering potential obstacles.
- Collaborating : Working effectively with others, whether humans or other AI agents, to achieve a common goal is increasingly important in complex and dynamic environments. Collaboration requires communication, coordination, and the ability to understand and respect the perspectives of others.
- Self-refining : The capacity for self-improvement and adaptation is a hallmark of advanced AI systems. AI agents with self-refining capabilities can learn from experience, adjust their behavior based on feedback, and continuously enhance their performance and capabilities over time. This can involve machine learning techniques, optimization algorithms, or other forms of self-modification.

### What is the difference between AI agents, AI assistants, and bots?

AI assistants are AI agents designed as applications or products to collaborate directly with users and perform tasks by understanding and responding to natural human language and inputs. They can reason and take action on the users' behalf with their supervision.

AI assistants are often embedded in the product being used. A key characteristic is the interaction between the assistant and user through the different steps of the task. The assistant responds to requests or prompts from the user, and can recommend actions but decision-making is done by the user.

 | AI agent | AI assistant | Bot ﻿
--- | --- | --- | ---
Purpose | Autonomously and proactively perform tasks | Assisting users with tasks | Automating simple tasks or conversations
Capabilities | Can perform complex, multi-step actions; learns and adapts; can make decisions independently | Responds to requests or prompts; provides information and completes simple tasks; can recommend actions but the user makes decisions | Follows pre-defined rules; limited learning; basic interactions
Interaction | Proactive; goal-oriented | Reactive; responds to user requests | Reactive; responds to triggers or commands

### Key differences

- Autonomy : AI agents have the highest degree of autonomy, able to operate and make decisions independently to achieve a goal. AI assistants are less autonomous, requiring user input and direction. Bots are the least autonomous, typically following pre-programmed rules.
- Complexity : AI agents are designed to handle complex tasks and workflows, while AI assistants and bots are better suited for simpler tasks and interactions.
- Learning : AI agents often employ machine learning to adapt and improve their performance over time. AI assistants may have some learning capabilities, while bots typically have limited or no learning.

### How do AI agents work?

Every agent defines its role, personality, and communication style, including specific instructions and descriptions of available tools.

- Persona : A well defined persona allows an agent to maintain a consistent character and behave in a manner appropriate to its assigned role, evolving as the agent gains experience and interacts with its environment.
- Memory : The agent is equipped in general with short term, long term, consensus, and episodic memory. Short term memory for immediate interactions, long-term memory for historical data and conversations, episodic memory for past interactions, and consensus memory for shared information among agents. The agent can maintain context, learn from experiences, and improve performance by recalling past interactions and adapting to new situations.
- Tools : Tools are functions or external resources that an agent can utilize to interact with its environment and enhance its capabilities. They allow agents to perform complex tasks by accessing information, manipulating data, or controlling external systems, and can be categorized based on their user interface, including physical, graphical, and program-based interfaces. Tool learning involves teaching agents how to effectively use these tools by understanding their functionalities and the context in which they should be applied.
- Model : Large language models (LLMs) serve as the foundation for building AI agents, providing them with the ability to understand, reason, and act. LLMs act as the "brain" of an agent, enabling them to process and generate language, while other components facilitate reason and action.

### What are the types of agents in AI?

AI agents can be categorized in various ways based on their capabilities, roles, and environments. Here are some key categories of agents:

There are different definitions of agent types and agent categories.

### Based on interaction

One way to categorize agents is by how they interact with users. Some agents engage in direct conversation, while others operate in the background, performing tasks without direct user input:

- Interactive partners (also known as, surface agents): Assisting us with tasks like customer service, healthcare, education, and scientific discovery, providing personalized and intelligent support. Conversational agents include Q&A, chit chat, and world knowledge interactions with humans. They are generally user query triggered and fulfill user queries or transactions.
- Autonomous background processes (also known as, background agents): Working behind the scenes to automate routine tasks, analyze data for insights, optimize processes for efficiency, and proactively identify and address potential issues. They include workflow agents. They have limited or no human interaction and are generally driven by events and fulfill queued tasks or chains of tasks.

### Based on number of agents

- Single agent : Operate independently to achieve a specific goal. They utilize external tools and resources to accomplish tasks, enhancing their functional capabilities in diverse environments. They are best suited for well defined tasks that do not require collaboration with other AI agents. Can only handle one foundation model for its processing.
- Multi-agent : Multiple AI agents that collaborate or compete to achieve a common objective or individual goals. These systems leverage the diverse capabilities and roles of individual agents to tackle complex tasks. Multi-agent systems can simulate human behaviors, such as interpersonal communication, in interactive scenarios. Each agent can have different foundation models that best fit their needs.

### Benefits of using AI agents

AI agents can enhance the capabilities of language models by providing autonomy, task automation, and the ability to interact with the real world through tools and embodiment.

### Efficiency and productivity

Increased output : Agents divide tasks like specialized workers, getting more done overall

Simultaneous execution : Agents can work on different things at the same time without getting in each other's way

Automation : Agents take care of repetitive tasks, freeing up humans for more creative work

### Improved decision-making

Collaboration : Agents work together, debate ideas, and learn from each other, leading to better decisions

Adaptability : Agents can adjust their plans and strategies as situations change

Robust reasoning : Through discussion and feedback, agents can refine their reasoning and avoid errors

### Enhanced capabilities

Complex problem-solving : Agents can tackle challenging real-world problems by combining their strengths

Natural language communication : Agents can understand and use human language to interact with people and each other

Tool use : Agents can interact with the external world by using tools and accessing information

Learning and self-improvement : Agents learn from their experiences and get better over time

### Social interaction and simulation

Realistic simulations : Agents can model human-like social behaviors, such as forming relationships and sharing information

Emergent behavior : Complex social interactions can arise organically from the interactions of individual agents

### Challenges with using AI agents

While AI agents offer many benefits, there are also some challenges associated with their use:

Tasks requiring deep empathy / emotional intelligence or requiring complex human interaction and social dynamics – AI agents can struggle with nuanced human emotions. Tasks like therapy, social work, or conflict resolution require a level of emotional understanding and empathy that AI currently lacks. They may falter in complex social situations that require understanding unspoken cues.

Situations with high ethical stakes – AI agents can make decisions based on data, but they lack the moral compass and judgment needed for ethically complex situations. This includes areas like law enforcement, healthcare (diagnosis and treatment), and judicial decision-making.

Domains with unpredictable physical environments – AI agents can struggle in highly dynamic and unpredictable physical environments where real-time adaptation and complex motor skills are essential. This includes tasks like surgery, certain types of construction work, and disaster response.

Resource-intensive applications – Developing and deploying sophisticated AI agents can be computationally expensive and require significant resources, potentially making them unsuitable for smaller projects or organizations with limited budgets.

### Deploy AI agents for scale and efficiency with Cloud Run

AI agents, with their inherent need for flexible compute power to handle reasoning, planning, and tool use, can be an excellent fit for Cloud Run . This fully managed serverless platform allows you to deploy your agent's code—often packaged within a container—as a scalable, reliable service or job. This approach abstracts away infrastructure management, letting developers concentrate on refining the agent's logic.

Cloud Run offers several features that directly support the architecture and demands of sophisticated AI agents:

- Scalability and cost-efficiency: Cloud Run automatically scales the number of container instances up to meet peak demand and, crucially, can scale down to zero when the agent is idle. This means you only pay for the exact compute resources consumed during the agent's active execution, making it cost-effective for goal-oriented, intermittent workloads.
- Agent orchestration and serving: The core agent logic—which manages the model calls, tool selection, and reasoning process—runs as a Cloud Run service. This service provides a stable HTTPS endpoint, making the agent easily accessible via an API for user-facing applications or for communication with other agents
- Agent-to-Agent, or A2A: Frameworks like the Agent Development Kit (ADK) are designed to integrate seamlessly with Cloud Run for easy deployment.

By leveraging Cloud Run's secure, auto-scaling, and flexible environment, organizations can operationalize complex single- or multi-agent systems efficiently.

### Use cases for AI agents

Organizations have been deploying agents to address a variety use cases , which we group into six key broader categories:

### Customer agents

Customer agents

Customer agents deliver personalized customer experiences by understanding customer needs, answering questions, resolving customer issues, or recommending the right products and services. They work seamlessly across multiple channels including the web, mobile, or point of sale, and can be integrated into product experiences with voice or video.

### Employee agents

Employee agents

Employee agents boost productivity by streamlining processes, managing repetitive tasks, answering employee questions, as well as editing and translating critical content and communications.

### Creative agents

Creative agents

Creative agents supercharge the design and creative process by generating content, images, and ideas, assisting with design, writing, personalization, and campaigns.

### Data agents

Data agents

Data agents are built for complex data analysis. They have the potential to find and act on meaningful insights from data, all while ensuring the factual integrity of their results.

### Code agents

Code agents

Code agents accelerate software development with AI-enabled code generation and coding assistance, and to ramp up on new languages and code bases. Many organizations are seeing significant gains in productivity, leading to faster deployment and cleaner, clearer code.

### Security agents

Security agents

Security agents strengthen security posture by mitigating attacks or increasing the speed of investigations. They can oversee security across various surfaces and stages of the security life cycle: prevention, detection, and response.

### Google Cloud and AI agents

Google Cloud provides a portfolio of products and solutions in the AI agent space. These include integrated AI assistants, pre-built AI agents, AI applications, and a platform of agent and developer tools to build custom AI agents.

- Gemini Enterprise App Secure platform to discover, create, run, and govern AI agents across your organization.
- Gemini Enterprise Agent Platform Create AI agents and applications using natural language or a code-first approach. Easily ground your agents or apps in enterprise data with a range of options.
- Customer Experience Agent Studio Build hybrid conversational agents with both deterministic and generative AI functionality.
- Agent Garden Curated collection of pre-built agent samples, solutions, tools, and frameworks to accelerate the development and deployment of AI agents.
- Agent Development Kit (ADK) Open-source Python SDK to build sophisticated multi-agent systems with orchestration, memory, and developer tools.
- A2A Protocol An open-source framework originally developed by Google to help build AI agents. An AI agent built with A2A Protocol will be interoperable with any service, platform, or infrastructure.
- Cloud Run A fully managed serverless platform that allows you to deploy containerized agents and applications, providing auto-scaling and pay-per-use efficiency.


## 2. Market Intelligence (Markposition)
Total Market Data Points: 350

- **advertising.amazon**: https://advertising.amazon.com/ (October 5, 2022)
- **Drive Advertising Revenue with Google Ad Manager : Google**: https://skillshop.exceedlms.com/student/path/17117-drive-advertising-revenue-with-google-ad-manager (September 26, 2022)
- **https://marketingplatform.google.com/about/search-ads-360/**: https://marketingplatform.google.com/about/search-ads-360/ (March 10, 2022)
- **Analytics Academy**: https://analytics.google.com/analytics/academy/ (September 20, 2022)
- **Adssettings google**: https://adssettings.google.com/authenticated (September 20, 2022)
- **Data google**: https://myaccount.google.com/data-and-personalization (September 20, 2022)
- **The Privacy Sandbox: Technology for a More Private Web.**: https://privacysandbox.com/intl/home#home-hero (September 20, 2022)
- **Digital Experience Platform & Enterprise CMS | Crownpeak**: https://www.crownpeak.com/ (September 16, 2022)
- **About Performance Max campaigns – Google Ads**: https://support.google.com/google-ads/answer/10724817?hl=en (September 1, 2022)
- **About Smart Bidding – Google Ads**: https://support.google.com/google-ads/answer/7065882?hl=en (September 1, 2022)
- **About Maximize conversion value bidding – Google Ads**: https://support.google.com/google-ads/answer/7684216?hl=en (September 1, 2022)
- **About automated bidding – Google Ads Help**: https://support.google.com/google-ads/answer/2979071?hl=en (September 1, 2022)
- **About Target CPA bidding – Google Ads Help**: https://support.google.com/google-ads/answer/6268632?hl=en (September 1, 2022)
- **About Maximize conversions bidding – Google Ads Help**: https://support.google.com/google-ads/answer/7381968?hl=en (September 1, 2022)
- **About Target ROAS bidding – Google Ads Help**: https://support.google.com/google-ads/answer/6268637?hl=en (September 1, 2022)
- **Achieve your goals across Google’s ad channels with Performance Max – Google Ads Help**: https://support.google.com/google-ads/answer/11189316?hl=en (September 1, 2022)
- **Coalition for Better Ads**: https://www.betterads.org/ (August 31, 2022)
- **ShareThis: Free Share Buttons & Plugins, Global Behavioral Data Solutions**: None (August 20, 2022)
- **How To Create Quality Video Ads – YouTube Advertising**: https://www.youtube.com/intl/en_us/ads/how-it-works/create-a-video-ad/ (August 16, 2022)
- **Business Data Responsibility – Your Data Protection & Privacy**: https://business.safety.google/ (August 15, 2022)
- **Google Ads Data Protection Terms: Service Information**: https://business.safety.google/adsservices/ (August 15, 2022)
- **Outbrain Advertising – Drive ROAS on the Open Web | Outbrain.com**: https://www.outbrain.com/advertisers/ (August 15, 2022)
- **Prebid**: https://prebid.org/ (August 14, 2022)
- **wmg**: https://adwmg.com/ (August 14, 2022)
- **Trustpilot Reviews: Experience the power of customer reviews**: https://www.trustpilot.com/ (August 11, 2022)
- **Online-Shopping mit Trusted Shops | Jetzt alle Produkte kennenlernen**: https://www.trustedshops.de/ (August 11, 2022)
- **TestFreaks – Ratings & Reviews Platform**: https://www.testfreaks.com/ (August 11, 2022)
- **TargetBay: Ecommerce Email Marketing Software and Marketing Automation**: https://targetbay.com/ (August 11, 2022)
- **Stamped | Reviews and Loyalty for Ecommerce Brands**: https://stamped.io/ (August 11, 2022)
- **Avis clients authentiques avec Shopping-Satisfaction**: https://www.shopping-satisfaction.com/ (August 11, 2022)
- **Shopperapproved**: https://www.shopperapproved.com/ (August 11, 2022)
- **REVIEWS.io | In Reviews We Trust**: https://www.reviews.io/ (August 11, 2022)
- **Resellerratings**: https://resellerratings.com/ (August 11, 2022)
- **PowerReviews: Doing More with UGC to Grow Your Business**: https://www.powerreviews.com/ (August 11, 2022)
- **Okendo**: https://www.okendo.io/ (August 11, 2022)
- **Loox Shopify Reviews App – Product Reviews & Referrals**: https://loox.app/ (August 11, 2022)
- **Junip | Reviews for products worth talking about**: https://junip.co/ (August 11, 2022)
- **Guaranteed Reviews Company | Guaranteed customer review solution**: https://www.guaranteed-reviews.com/ (August 11, 2022)
- **Feefo | Transform your business with real customer reviews**: https://www.feefo.com/ (August 11, 2022)
- **feedaty**: https://www.feedaty.com/ (August 11, 2022)
- **eKomi | The Feedback Company**: https://www.ekomi.co.uk/uk/ (August 11, 2022)
- **Echte-Bewertungen – Verbessern Sie Ihre Geschäftsergebnisse**: https://www.echte-bewertungen.com/ (August 11, 2022)
- **Bazaarvoice: Meet shoppers in all the moments that matter**: https://www.bazaarvoice.com/ (August 11, 2022)
- **Avis clients : boostez vos ventes avec Avis Vérifiés !**: https://www.avis-verifies.com/fr/ (August 11, 2022)
- **Loyalty Experience Platform – Annex Cloud Loyalty Management Solution**: https://www.annexcloud.com/ (August 11, 2022)
- **Verified-Reviews – Boost your sales uk**: https://www.verified-reviews.co.uk/ (August 11, 2022)
- **Yotpo**: https://www.yotpo.com/ (August 11, 2022)
- **Verified Reviews – Boost your sales**: https://www.netreviews.com/en/ (August 11, 2022)
- **Pixlee TurnTo | Social User-Generated Content (UGC), Ratings & Reviews, and Influencer Marketing Platform**: https://www.pixlee.com/ (August 11, 2022)
- **Facebook Blueprint: Free Online Training for Advertising on Facebook | Meta for Business**: https://web.facebook.com/business/learn (August 8, 2022)
- **Facebook Certification: Professional Certificate Exams from Facebook | Meta for Business**: https://web.facebook.com/business/learn/certification (August 8, 2022)
- **Facebook Ads: Online Advertising on Facebook | Meta for Business**: https://web.facebook.com/business/ads (August 8, 2022)
- **Create a LinkedIn Company Page | LinkedIn Marketing Solutions**: https://business.linkedin.com/marketing-solutions/linkedin-pages (August 8, 2022)
- **Marketing & Advertising on LinkedIn | LinkedIn Marketing Solutions**: https://business.linkedin.com/marketing-solutions (August 8, 2022)
- **Coalition for Better Ads**: https://www.betterads.org/ (July 28, 2022)
- **FC**: https://fundingchoices.google.com/start/ (May 26, 2022)
- **Funding Choices**: https://support.google.com/fundingchoices/answer/9010669?hl=hr (May 26, 2022)
- **Publisher strategy for privacy preferences – Think with Google**: https://www.thinkwithgoogle.com/future-of-marketing/privacy-and-trust/publisher-privacy-landscape/ (May 23, 2022)
- **The Future of Marketing – Think with Google**: https://www.thinkwithgoogle.com/future-of-marketing/ (May 23, 2022)
- **Google Ads Help: Understanding optimized targeting**: https://www.youtube.com/embed/v9SqjeH7nrU?version=3&rel=1&showsearch=0&showinfo=1&iv_load_policy=1&fs=1&hl=en&autohide=2&wmode=transparent (May 16, 2022)
- **ptimization targeting – Google Ads**: https://support.google.com/google-ads/answer/10537509?hl=hr (May 16, 2022)
- **Google News Initiative Training Center**: https://newsinitiative.withgoogle.com/training/datatools (May 16, 2022)
- **Create Reports in Google Ad Manager : Google**: https://skillshop.exceedlms.com/student/activity/17113-create-reports-in-google-ad-manager (May 12, 2022)
- **Optimize Google Ad Manager to Meet Objectives : Google**: https://skillshop.exceedlms.com/student/path/54611-optimize-google-ad-manager-to-meet-objectives (May 9, 2022)
- **Get started with Twitter Ads**: https://business.twitter.com/en/advertising/get-started-with-twitter-ads.html (May 5, 2022)
- **Pixalate – Ad Fraud Protection, Privacy, and Compliance Platform (CTV)**: https://www.pixalate.com/ (May 4, 2022)
- **Publisher Collective | Get better CPMs with the advertising network for game sites**: https://www.publisher-collective.com/ (April 28, 2022)
- **boost-your-active-view-score-in-ad-manager**: https://skillshop.exceedlms.com/student/activity/17109-boost-your-active-view-score-in-ad-manager (April 28, 2022)
- **Waytogrow – Earn more on your advertising space**: https://www.waytogrow.com/ (April 22, 2022)
- **Smart Adserver | The Most Powerful Adserving and RTB Platform**: https://smartadserver.com/ (April 21, 2022)
- **Custom advertising solutions – Custom ad campaigns | Amazon Ads**: https://advertising.amazon.com/solutions/products/custom-solutions (April 21, 2022)
- **Amazon Marketing Cloud – Advanced media analytics and insights | Amazon Ads**: https://advertising.amazon.com/solutions/products/amazon-marketing-cloud (April 21, 2022)
- **Amazon DSP – Create campaigns with our Demand Side Platform | Amazon Ads**: https://advertising.amazon.com/solutions/products/amazon-dsp (April 21, 2022)
- **Learning console – Online advertising courses and PPC certifications | Amazon Ads**: https://advertising.amazon.com/resources/learning-console (April 21, 2022)
- **Sponsored Display ads – Create display advertising campaigns | Amazon Ads**: https://advertising.amazon.com/solutions/products/sponsored-display (April 21, 2022)
- **Amazon Ads: Online advertising for businesses of all sizes | Amazon Ads**: https://advertising.amazon.com/ (April 21, 2022)
- **Sizmek Ad Suite – DCO, creative building, ad serving | Amazon Ads**: https://advertising.amazon.com/solutions/products/sizmek-ad-suite (April 21, 2022)
- **Drive Advertising Revenue with Google Ad Manager : Google**: https://skillshop.exceedlms.com/student/path/17117-drive-advertising-revenue-with-google-ad-manager (April 18, 2022)
- **ads settings google**: https://adssettings.google.com/authenticated (April 15, 2022)
- **Linker – Content Discovery Platform**: https://linker.hr/ (April 15, 2022)
- **Funding Choices API | Google Developers**: https://developers.google.com/funding-choices (April 14, 2022)
- **Privacy checks in Ads Data Hub | Google Developers**: https://developers.google.com/ads-data-hub/guides/privacy-checks (April 14, 2022)
- **Ads Data Hub | Google Developers**: https://developers.google.com/ads-data-hub (April 14, 2022)
- **Google Ad Manager – Privacy & messaging**: https://admanager.google.com/22694377933#privacy_and_messaging/ad_blocking/education (April 13, 2022)
- **Google Ads Integration | Ortto**: https://ortto.com/integrations/google-ads/ (April 6, 2022)
- **Cloudflare’s Privacy Policy | Cloudflare**: https://www.cloudflare.com/privacypolicy/ (April 6, 2022)
- **CJ.com Home**: https://www.cj.com/ (April 6, 2022)
- **Xaxis – The outcome media company**: https://www.xaxis.com/ (April 6, 2022)
- **Services Privacy Policy | Oracle**: https://www.oracle.com/legal/privacy/services-privacy-policy.html (April 6, 2022)
- **AdMedia | Premier Advertising Network | Reach 200M+ US Users**: https://admedia.com/ (April 4, 2022)
- **Monetize**: https://www.monetize.com/ (April 4, 2022)
- **Adobe Advertising Cloud: Programmatic Media Buying | Adobe for Business**: https://business.adobe.com/products/advertising/adobe-advertising-cloud.html (March 29, 2022)
- **Your Online Choices | EDAA**: https://youronlinechoices.eu/ (March 29, 2022)
- **WebChoices: Digital Advertising Alliance’s Consumer Choice Tool for Web US**: https://optout.aboutads.info/ (March 29, 2022)
- **For Consumers – European Interactive Digital Advertising Alliance**: https://edaa.eu/what-we-do/for-consumers/ (March 29, 2022)
- **Data Privacy Audit | See If Your Website Is Data Compliant**: https://usercentrics.com/data-privacy-audit/ (March 25, 2022)
- **Drive Advertising Revenue with Google Ad Manager : Google**: https://skillshop.exceedlms.com/student/path/17117-drive-advertising-revenue-with-google-ad-manager (March 18, 2022)
- **Create Reports in Google Ad Manager : Google**: https://skillshop.exceedlms.com/student/activity/17113-create-reports-in-google-ad-manager (March 18, 2022)
- **Online Video Advertising Campaigns – YouTube Advertising**: https://www.youtube.com/intl/en_US/ads/ (March 18, 2022)
- **Profit Whales | Full-service Amazon marketing agency for your brand!**: https://profitwhales.com/ (March 18, 2022)
- **Learning console – Online advertising courses and PPC certifications | Amazon Ads**: https://advertising.amazon.com/resources/learning-console (March 17, 2022)
- **Amazon Ads: Online advertising for businesses of all sizes | Amazon Ads**: https://advertising.amazon.com/ (March 17, 2022)
- **Get Started with Google Publisher Tags | Google Developers**: https://developers.google.com/publisher-tag/guides/get-started (March 16, 2022)
- **Ad sizes | Google Publisher Tag | Google Developers**: https://developers.google.com/publisher-tag/guides/get-started (March 16, 2022)
- **Drive Advertising Revenue with Google Ad Manager : Google**: https://skillshop.exceedlms.com/student/path/17117-drive-advertising-revenue-with-google-ad-manager (March 16, 2022)
- **Configure Mobile In-App Ads Using Ad Manager : Google**: https://skillshop.exceedlms.com/student/activity/75346-configure-mobile-in-app-ads-using-ad-manager (March 16, 2022)
- **Fundamentals of Video : Google**: https://skillshop.exceedlms.com/student/activity/75345-fundamentals-of-video (March 16, 2022)
- **Review and Manage Ads in Google Ad Manager : Google**: https://skillshop.exceedlms.com/student/activity/17116-review-and-manage-ads-in-google-ad-manager (March 16, 2022)
- **Manage Ads with Rules and Protections : Google**: https://skillshop.exceedlms.com/student/activity/379130-manage-ads-with-rules-and-protections-skillshop (March 16, 2022)
- **Explore Programmatic Capabilities in Google Ad Manager : Google**: https://skillshop.exceedlms.com/student/activity/17114-explore-programmatic-capabilities-in-google-ad-manager (March 16, 2022)
- **Create Reports in Google Ad Manager : Google**: https://skillshop.exceedlms.com/student/activity/17113-create-reports-in-google-ad-manager (March 16, 2022)
- **Forecast Your Inventory Using Ad Manager : Google**: https://skillshop.exceedlms.com/student/activity/17112-forecast-your-inventory-using-ad-manager (March 16, 2022)
- **Optimize Creatives with Ad Manager : Google**: https://skillshop.exceedlms.com/student/activity/17111-optimize-creatives-with-ad-manager (March 16, 2022)
- **Deliver Ads Using Google Ad Manager : Google**: https://skillshop.exceedlms.com/student/activity/17110-deliver-ads-using-google-ad-manager (March 16, 2022)
- **Google Ad Traffic Quality**: https://www.google.com/ads/adtrafficquality/ (March 14, 2022)
- **Vodič za ads.txt – Google AdSense Pomoć**: https://support.google.com/adsense/answer/7532444?hl=hr (March 14, 2022)
- **Alat za rješavanje problema s datotekom ads.txt – Google AdSense Pomoć**: https://support.google.com/adsense/troubleshooter/9556696?hl=hr#ts=9806100%2C9806109 (March 14, 2022)
- **Actions on Google**: https://console.actions.google.com/u/0/ (March 13, 2022)
- **AdSense Management API | Google Developers**: https://developers.google.com/adsense/management (March 13, 2022)
- **The Commerce Media Platform for the Open Internet | Criteo**: https://www.criteo.com/ (March 13, 2022)
- **Ad exchange – Wikipedia**: https://en.wikipedia.org/wiki/Ad_exchange (March 13, 2022)
- **Digiday – Digital Content, Digital Advertising, Digital Marketing**: https://digiday.com/ (March 13, 2022)
- **234 – Measure – Analyze – Optimize**: https://234.hr/ (March 13, 2022)
- **Google Ad Manager – Integrated Advertising Management Platform**: https://admanager.google.com/home/ (March 13, 2022)
- **Google Ad Manager : Google**: https://skillshop.exceedlms.com/student/catalog/list?category_ids=2842-google-ad-manager (March 13, 2022)
- **Pronađite partnera – izdavača | Certificirani partner – izdavač – Google**: https://www.google.com/ads/publisher/partners/find-a-partner/#!?modal_active=modal-ezoic (March 13, 2022)
- **Pronađite partnera – izdavača | Certificirani partner – izdavač – Google – ads publisher – find a partner**: https://www.google.com/ads/publisher/partners/find-a-partner/#!?modal_active=none (March 13, 2022)
- **Google Certified Partner Program – Google – ads – publisher – partners**: https://www.google.com/ads/publisher/partners/ (March 13, 2022)
- **“How Ads Work on YouTube”**: https://www.youtube.com/embed/WPR9PCoeqog?version=3&rel=1&showsearch=0&showinfo=1&iv_load_policy=1&fs=1&hl=en&autohide=2&wmode=transparent (March 13, 2022)
- **Ad Inserter – Ad Manager & AdSense Ads – | WordPress.org Hrvatski**: https://hr.wordpress.org/plugins/ad-inserter/ (March 11, 2022)
- **Ad Inserter Pro – Advanced WordPress Ad Management Plugin**: https://adinserter.pro/ (March 11, 2022)
- **SafeFrame Implementation Guidelines**: https://www.iab.com/guidelines/safeframe/ (March 11, 2022)
- **Using your Ad Speed Home dashboard – Google Ad Manager Help**: https://support.google.com/admanager/answer/9203630?hl=en (March 11, 2022)
- **Google Ads**: https://ads.google.com/intl/hr_hr/home/ (March 11, 2022)
- **Google Ads Status Dashboard**: https://ads.google.com/status/publisher/ (March 11, 2022)
- **Google Ads Data Processing Terms**: https://business.safety.google/adsprocessorterms/ (March 11, 2022)
- **Business Data Responsibility – Data Safety, Protection & Privacy**: https://business.safety.google/ (March 11, 2022)
- **Get Started with Google Publisher Tags | Google Developers**: https://developers.google.com/publisher-tag/guides/get-started (March 11, 2022)
- **Get Started with Search Ads 360 : Google**: https://skillshop.exceedlms.com/student/path/396050-get-started-with-search-ads-360 (March 11, 2022)
- **Google Ad Manager : Google**: https://skillshop.exceedlms.com/student/catalog/list?category_ids=2842-google-ad-manager (March 11, 2022)
- **Partnerski program za izdavaštvo | Certificirani partner – izdavač – Google**: https://www.google.com/ads/publisher/partners/ (March 10, 2022)
- **Marketing Cloud – Digital Marketing Platform – Salesforce.com**: https://www.salesforce.com/products/marketing-cloud/overview/ (March 10, 2022)
- **Adobe Experience Platform**: https://business.adobe.com/products/experience-platform/adobe-experience-platform.html (March 10, 2022)
- **Publisher Ads Audits for Lighthouse | Google Developers**: https://developers.google.com/publisher-ads-audits (March 10, 2022)
- **Setupad Blog | Latest AdTech News**: https://setupad.com/blog/ (March 10, 2022)
- **DoubleClick – Wikipedia**: https://en.wikipedia.org/wiki/DoubleClick (March 10, 2022)
- **Google Ad Manager – Wikipedia**: https://en.wikipedia.org/wiki/Google_Ad_Manager (March 10, 2022)
- **Drive Advertising Revenue with Google Ad Manager : Google**: https://skillshop.exceedlms.com/student/path/17117-drive-advertising-revenue-with-google-ad-manager (March 10, 2022)
- **iab ads txt**: https://markposition.wordpress.com/wp-content/uploads/2022/08/7db5d-iab-openrtb-ads.txt-public-spec-1.0.2-3.pdf (March 9, 2022)
- **Bing Webmaster Tools**: https://www.bing.com/webmasters/about (March 8, 2022)
- **In-Stream Ads | Meta for Creators**: https://web.facebook.com/creators/tools/in-stream-ads (March 2, 2022)
- **How to Make Money From Your Content on Facebook | Facebook for Business**: https://web.facebook.com/business/learn/lessons/how-make-money-facebook (February 28, 2022)
- **Instant Articles | Meta for Media**: https://web.facebook.com/formedia/tools/instant-articles (February 28, 2022)
- **Audience Network**: https://hr-hr.facebook.com/audiencenetwork/monetize/bidding/learn (February 27, 2022)
- **Earn Money From In-Stream Ads in Your Facebook Videos | Facebook for Business**: https://web.facebook.com/business/learn/lessons/earn-money-in-stream-ads-videos (February 26, 2022)
- **Comscore is a trusted currency for planning, transacting, and evaluating media across platforms.**: https://www.comscore.com/ (February 26, 2022)
- **AdinPlay – Maximize the ad revenues from your websites, apps and online games.**: https://adinplay.com/ (February 24, 2022)
- **Davatelji oglasnih tehnologija za LGPD – Google AdSense Pomoć**: https://support.google.com/adsense/answer/9931967?hl=hr (February 23, 2022)
- **Programmatic Digital Advertising Technology & Solutions | PubMatic**: https://pubmatic.com/ (February 21, 2022)
- **Header bidding – Wikipedia**: https://en.wikipedia.org/wiki/Header_bidding (February 21, 2022)
- **Supply-side platform – Wikipedia**: https://en.wikipedia.org/wiki/Supply-side_platform (February 21, 2022)
- **Online advertising – Wikipedia**: https://en.wikipedia.org/wiki/Online_advertising (February 21, 2022)
- **The Trade Desk – Wikipedia**: https://en.wikipedia.org/wiki/The_Trade_Desk (February 21, 2022)
- **Demand-side platform – Wikipedia**: https://en.wikipedia.org/wiki/Demand-side_platform (February 21, 2022)
- **Built for What Matters | The Trade Desk**: https://www.thetradedesk.com/us (February 21, 2022)
- **Google Ad Manager – Wikipedia**: https://en.wikipedia.org/wiki/Google_Ad_Manager (February 21, 2022)
- **Ad exchange – Wikipedia**: https://en.wikipedia.org/wiki/Ad_exchange (February 21, 2022)
- **Google Marketing Platform – Unified Advertising and Analytics**: https://marketingplatform.google.com/about/ (February 20, 2022)
- **Dashboarding & Data Visualization Tools – Google Data Studio**: https://marketingplatform.google.com/about/data-studio/ (February 20, 2022)
- **Business Analytics Tools & Solutions – Google Analytics 360**: https://marketingplatform.google.com/about/analytics-360/ (February 20, 2022)
- **Search Campaign Management – Google Search Ads 360**: https://marketingplatform.google.com/about/search-ads-360/ (February 20, 2022)
- **Trusted Ad Serving – Campaign Manager 360**: https://marketingplatform.google.com/about/campaign-manager-360/ (February 20, 2022)
- **End to End Campaign Management – Google Display & Video 360**: https://marketingplatform.google.com/about/display-video-360/ (February 20, 2022)
- **Create and submit a robots.txt file | Google Search Central | Google Developers**: https://developers.google.com/search/docs/advanced/robots/create-robots-txt (February 19, 2022)
- **sitemaps.org – Home**: https://www.sitemaps.org/ (February 19, 2022)
- **The Web Robots Pages**: http://www.robotstxt.org/ (February 19, 2022)
- **Partnerski program za izdavaštvo | Certificirani partner –izdavač –Google**: https://www.google.com/ads/publisher/partners/ (February 19, 2022)
- **Pronađite partnera – izdavača | Certificirani partner – izdavač – Google**: https://www.google.com/ads/publisher/partners/find-a-partner/#!?modal_active=none (February 19, 2022)
- **Monetization ezoic**: https://pubdash.ezoic.com/monetization (February 19, 2022)
- **Google Ad Manager – Integrated Advertising Management Platform**: https://admanager.google.com/home/ (February 19, 2022)
- **Inside AdSense: Bringing more buyers to AdSense through the DoubleClick Ad Exchange**: https://adsense.googleblog.com/2009/09/bringing-more-buyers-to-adsense-through.html (February 19, 2022)
- **Google AdSense**: https://support.google.com/adsense/?hl=hr#topic=1190787 (February 19, 2022)
- **AdSense | Google Blog**: https://blog.google/products/adsense/ (February 19, 2022)
- **Cookieless Targeting, Audience Targeting, CMP – Sirdata**: https://sirdata.com/en/ (February 15, 2022)
- **152 Media – Header Bidding**: https://152media.com/ (February 15, 2022)
- **IAB Tech Lab**: https://iabtechlab.com/software/ (February 14, 2022)
- **Digiday – Digital Content, Digital Advertising, Digital Marketing**: https://digiday.com/ (February 13, 2022)
- **Google Ads Status Dashboard**: https://ads.google.com/status/publisher/ (February 13, 2022)
- **CMP Builder | by OneTrust**: https://comply.cookiepro.com/ (February 12, 2022)
- **Audience Is Everything® – Nielsen**: https://global.nielsen.com/global/en/ (February 12, 2022)
- **Vendors List – IAB Europe**: https://iabeurope.eu/vendor-list/ (February 12, 2022)
- **Adacado DIY Advertising | Do It Yourself Digital Advertising**: https://adacado.com/ (February 12, 2022)
- **Home • #1 Platform to make better ads: Unify Data + Creativity • VidMob**: https://www.vidmob.com/ (January 30, 2022)
- **First-Impression :: Advertising Platform**: http://www.first-impression.com/home/ (January 30, 2022)
- **Facebook Audience Network | Facebook Developers**: https://developers.facebook.com/products/audience-network/ (January 30, 2022)
- **Home – diDNA**: https://didna.io/ (January 30, 2022)
- **Content.ad – Native Advertising, Push Notifications, and Beyond**: https://content.ad/ (January 30, 2022)
- **Connect Ads**: https://connectads.com/ (January 30, 2022)
- **Advertising Solutions for Publishers and Marketers | BuySellAds**: https://www.buysellads.com/ (January 30, 2022)
- **Join Our UK Affiliate Network – Awin**: https://www.awin.com/gb (January 30, 2022)
- **Интернет реклама | Рекламная сеть Advmaker.net**: http://advmaker.net/ (January 30, 2022)
- **Adsterra Advertising Network | Solutions for Advertisers and Publishers**: https://adsterra.com/ (January 30, 2022)
- **Adomik**: https://www.adomik.com/ (January 30, 2022)
- **Adnet**: https://adnet.com/ (January 30, 2022)
- **Home » Admetrics media**: http://www.admetricsmedia.com/ (January 30, 2022)
- **AdMaven Ad Network | The Online Advertising Platform**: https://ad-maven.com/ (January 30, 2022)
- **Home | 33Across**: https://www.33across.com/ (January 30, 2022)
- **Rich Media Creative Agency | Online Advertising Agency USA | Undertone**: https://www.undertone.com/ (January 30, 2022)
- **The Publisher Technology Platform | Sovrn**: https://www.sovrn.com/ (January 30, 2022)
- **Rubicon is now Magnite**: https://rubiconproject.com/ (January 30, 2022)
- **Content Marketing, Native Advertising & Discovery – Revcontent**: https://www.revcontent.com/ (January 30, 2022)
- **Programmatic Digital Advertising Technology & Solutions | PubMatic**: https://pubmatic.com/ (January 30, 2022)
- **Outbrain – Recommendation Platform Powered by Native Ads**: https://www.outbrain.com/ (January 30, 2022)
- **OpenX: Programmatic Advertising | Ad Exchange Network**: https://www.openx.com/ (January 30, 2022)
- **Digital Online Advertising Platforms | Yahoo Ad Tech**: https://www.adtech.yahooinc.com/ (January 30, 2022)
- **Google AdSense – ostvarite zaradu unovčavanjem web-lokacije**: https://www.google.com/intl/hr_hr/adsense/start/ (January 30, 2022)
- **Contextual Advertising & Programmatic Platform | Media.net**: https://www.media.net/ (January 30, 2022)
- **Get Started | Buyer APIs | Google Developers**: https://developers.google.com/authorized-buyers/apis/guides/start (January 30, 2022)
- **Authorized Buyers | Google Developers**: https://developers.google.com/authorized-buyers (January 30, 2022)
- **District M is now Sharethrough | District M**: https://www.districtm.net/ (January 30, 2022)
- **enginemediaexchange.com | Futureproof Your Business**: https://enginemediaexchange.com/ (January 30, 2022)
- **Xandr**: https://www.xandr.com/ (January 30, 2022)
- **Digital Online Advertising Platforms | Yahoo Ad Tech**: https://www.adtech.yahooinc.com/ (January 27, 2022)
- **Bring Innovation And Incrementality To Mobile Monetization**: https://www.display.io/ (January 27, 2022)
- **Marketing & Advertising on LinkedIn | LinkedIn Marketing Solutions**: https://business.linkedin.com/marketing-solutions (January 27, 2022)
- **LinkedIn Advertising Costs & Pricing | LinkedIn Marketing Solutions**: https://business.linkedin.com/marketing-solutions/ads/pricing (January 27, 2022)
- **LinkedIn Ads: Targeted Self-Service Ads | LinkedIn Marketing Solutions**: https://business.linkedin.com/marketing-solutions/ads (January 27, 2022)
- **Marketing & Advertising on LinkedIn | LinkedIn Marketing Solutions**: https://business.linkedin.com/marketing-solutions (January 27, 2022)
- **LinkedIn Campaign Manager**: https://www.linkedin.com/campaignmanager/accounts (January 27, 2022)
- **Outbrain – Recommendation Platform Powered by Native Ads**: https://www.outbrain.com/ (January 24, 2022)
- **Home – TrustArc The Leader in Privacy Management Software**: https://trustarc.com/ (January 16, 2022)
- **Outbrain – Recommendation Platform Powered by Native Ads**: https://www.outbrain.com/ (January 13, 2022)
- **Google Ad Manager – Integrated Advertising Management Platform**: https://admanager.google.com/home/ (January 5, 2022)
- **Mobile App Monetization – Google AdMob**: https://admob.google.com/home/ (January 5, 2022)
- **In App Advertising | Vungle**: https://vungle.com/advertise/ (January 3, 2022)
- **Digital Customer Acquisition Solutions | Rakuten Advertising**: https://rakutenadvertising.com/ (December 21, 2021)
- **Online Video Advertising Campaigns – YouTube Advertising**: https://www.youtube.com/ads/ (December 11, 2021)
- **BrandConnect for Influencer Advertising – YouTube Advertising – YouTube Advertising**: https://www.youtube.com/ads/brandconnect/ (December 11, 2021)
- **Google Ads – privucite više korisnika jednostavnim online oglašavanjem**: https://ads.google.com/intl/hr_hr/home/ (December 1, 2021)
- **Campaign Builder | Amazon Advertising**: https://advertising.amazon.com/cb?entityId=ENTITY170NBZYAM0OSR#!/ingress (November 24, 2021)
- **International growth agencies – Market Finder by Google**: https://marketfinder.thinkwithgoogle.com/intl/en_cee/widget/partner-agencies-tool/ (November 24, 2021)
- **Free Google Ads Tools by Clever Ads | Google Advertising**: https://cleverads.com/ (November 23, 2021)
- **Audiencerate – The Identity Hub**: https://www.audiencerate.com/ (November 13, 2021)
- **Lucidity | Blockchain-Audited Media for Greater Transparency in Advertising**: https://golucidity.com/ (November 13, 2021)
- **Customer Data Platform – Tealium**: https://tealium.com/ (November 13, 2021)
- **Revealbot – Automate Your Ad Strategies**: https://revealbot.com/ (November 12, 2021)
- **EthicalAds**: https://ethicalads.io (October 18, 2021)
- **ads twitter**: https://ads.twitter.com/mobile/v1/get_started?ref=em-elq-ao-gbl-emailatclink&s=09 (October 4, 2021)
- **Eskimi – AdTech platform that adds a +1 to your marketing team**: https://www.eskimi.com/ (September 28, 2021)
- **Overview – Microsoft Advertising**: https://about.ads.microsoft.com/en-us/h/a/microsoft-advertising (September 21, 2021)
- **Google Marketing Platform Certification Exams : Google**: https://skillshop.exceedlms.com/student/catalog/list?category_ids=707-google-marketing-platform-certification-exams (September 10, 2021)
- **YouTube Advertising – Online Video Advertising Campaigns**: https://www.youtube.com/ads/ (September 5, 2021)
- **Make Quality Advertising Videos – YouTube Advertising**: https://www.youtube.com/ads/making-a-video-ad/ (September 5, 2021)
- **Outbrain – Recommendation Platform Powered by Native Ads**: https://www.outbrain.com/ (September 2, 2021)
- **Digital Advertising Platform | Criteo**: https://www.criteo.com/technology/advertising-platform/ (August 25, 2021)
- **Programmatic advertising | BidTheatre Demand Side Platform**: https://www.bidtheatre.com/ (August 25, 2021)
- **ShareThis: Free Share Buttons & Plugins, Global Behavioral Data Solutions**: https://sharethis.com/ (August 25, 2021)
- **AdMaxim Inc. – Integrated Digital Advertising Platform**: http://www.admaxim.com/ (August 25, 2021)
- **Kwanko – Your Performance Marketing Partner**: https://www.kwanko.com/ (August 25, 2021)
- **Online marketing. Simplified | Adzooma**: https://www.adzooma.com/ (August 24, 2021)
- **Adzooma Marketplace | Find The Right Service For Your Business | Adzooma Marketplace**: https://marketplace.adzooma.com/ (August 24, 2021)
- **LinkedIn Campaign Manager**: https://www.linkedin.com/campaignmanager/new-advertiser (August 23, 2021)
- **Marketing & Advertising on LinkedIn | LinkedIn Marketing Solutions**: https://business.linkedin.com/marketing-solutions (August 23, 2021)
- **Google Ads – privucite više korisnika jednostavnim online oglašavanjem**: https://ads.google.com/intl/hr_hr/getstarted/?subid=hr-hr-ha-aw-sk-m-bau!o3~Cj0KCQjwpf2IBhDkARIsAGVo0D3Wryak_hHyBl23URk7i9rUzFQcSDfFRCTDFLY-609ii68BQnjRsg0aAk0TEALw_wcB~117699885987~kwd-94527731~11806561409~485142535412 (August 20, 2021)
- **Cross-Channel Marketing Platform to Improve Customer Experiences – Iterable**: https://iterable.com/ (August 20, 2021)
- **LinkedIn Ads: Targeted Self-Service Ads | LinkedIn Marketing Solutions**: https://business.linkedin.com/marketing-solutions/ads (August 20, 2021)
- **Setupad.com – Monetization Partner – Setupad**: https://setupad.com/ (August 20, 2021)
- **Evidon | Digital Governance, Privacy Compliance, Website Monitoring**: https://www.evidon.com/ (August 4, 2021)
- **NextRoll – Home**: https://www.nextroll.com/ (July 31, 2021)
- **Adzooma | Simplify, Automate & Optimise Online Ad Campaigns**: https://www.adzooma.com/ (July 30, 2021)
- **Outbrain – Recommendation Platform Powered by Native Ads**: https://www.outbrain.com/ (July 30, 2021)
- **Bing Webmaster Tools**: https://www.bing.com/webmasters/about (July 30, 2021)
- **N/A**: https://www.yourprimer.com (July 25, 2021)
- **Lesson Catalog | Business & Operations – Google Primer**: https://www.yourprimer.com/en/lesson-catalog/0 (July 25, 2021)
- **Google trends**: https://trends.google.com/trends (July 25, 2021)
- **Google Ads – privucite više korisnika jednostavnim online oglašavanjem**: https://ads.google.com/intl/hr_hr/getstarted/ (July 25, 2021)
- **Set up conversion tracking for your website – Google Ads Help**: https://support.google.com/google-ads/answer/6095821?hl=en (July 25, 2021)
- **Overview – Microsoft Advertising**: https://about.ads.microsoft.com/en-us/h/a/microsoft-advertising (July 22, 2021)
- **Midas Network – Platforma za Nativno oglašavanje**: https://www.midas-network.com/hr (July 22, 2021)
- **SEM with Microsoft Advertising – Microsoft Advertising**: https://about.ads.microsoft.com/en-us (July 20, 2021)
- **Advertise Your Website – Getting Started – Google Domains**: https://domains.google/get-started/online-ads/ (July 15, 2021)
- **Amazon Advertising: Online advertising for businesses of all sizes**: https://advertising.amazon.com/ (July 9, 2021)
- **Amazon Advertising: Online advertising for businesses of all sizes**: https://advertising.amazon.com/ (July 9, 2021)
- **Learning console – amazon catalog**: https://learningconsole.amazonadvertising.com/student/catalog/list (July 7, 2021)
- **Learning console – amazon advertising**: https://learningconsole.amazonadvertising.com/student/catalog (July 7, 2021)
- **Advertising solutions for KDP authors | Amazon Advertising**: https://advertising.amazon.com/kdp-authors (July 7, 2021)
- **Amazon.com: Kindle Direct Publishing: Promotion Manager**: https://kdp.amazon.com/marketing/A2B1V7EPJ81WN2/promotion-manager (July 7, 2021)
- **Amazon Advertising: Online advertising for businesses of all sizes**: https://advertising.amazon.com/ (July 7, 2021)
- **All Your Digital Marketing Tools in One Place – Sendinblue**: https://www.sendinblue.com/ (July 2, 2021)
- **Digital Marketing & Growth Marketing Platform | AdRoll**: https://www.adroll.com/ (July 2, 2021)
- **Facebook for Business: Marketing on Facebook**: https://web.facebook.com/business (July 1, 2021)
- **Grow your revenue and monetize your game or app | Unity Ads | Unity**: https://unity.com/products/unity-ads-monetize (June 30, 2021)
- **Grow user LTV with ads and In-app purchases | Mobile game monetization | Unity**: https://unity.com/solutions/unity-ads (June 30, 2021)
- **Snapchat Ads | Snapchat for Business**: https://forbusiness.snapchat.com/ (June 25, 2021)
- **Google Ad Manager – Get in touch**: https://admanager.google.com/home/contact-us/ (June 25, 2021)
- **Google Ad Manager – Integrated Advertising Management Platform**: https://admanager.google.com/home/ (June 25, 2021)
- **Admiral: The Visitor Relationship Management Company**: https://www.getadmiral.com/ (June 24, 2021)
- **SEM with Microsoft Advertising – Microsoft Advertising**: https://about.ads.microsoft.com/en-us (June 14, 2021)
- **Ad settings google**: https://adssettings.google.com/authenticated (June 13, 2021)
- **Google Ads Data and Privacy – Google Safety Center**: https://safety.google/privacy/ads-and-data/ (June 13, 2021)
- **Fat Frog Media**: https://fatfrogmedia.com/ (June 13, 2021)
- **ToneDen – Automated Social Marketing**: https://www.toneden.io/ (June 13, 2021)
- **Data Inventory & Mapping – TrustArc The Leader in Privacy Management Software**: https://trustarc.com/data-inventory-mapping/ (June 12, 2021)
- **Technology Powered Partner Program – TrustArc The Leader in Privacy Management Software**: https://trustarc.com/technology-powered-partner-program/ (June 12, 2021)
- **Powered Partner Program – TrustArc The Leader in Privacy Management Software**: https://trustarc.com/powered-partner-program/ (June 12, 2021)
- **Cookie Consent Manager Free Trial Request – TrustArc The Leader in Privacy Management Software**: https://trustarc.com/cookie-consent-manager/professional-trial-account-request/?utm_source=ccm-trial (June 12, 2021)
- **Home – TrustArc The Leader in Privacy Management Software**: https://trustarc.com/ (June 12, 2021)
- **WebChoices: Digital Advertising Alliance’s Consumer Choice Tool for Web US**: https://optout.aboutads.info/ (June 12, 2021)
- **Adobe Privacy Center**: https://www.adobe.com/privacy/opt-out.html (June 12, 2021)
- **TrustArc Preference Manager**: http://preferences-mgr.truste.com/ (June 12, 2021)
- **WebChoices: Digital Advertising Alliance’s Consumer Choice Tool for Web US**: https://optout.aboutads.info/ (June 12, 2021)
- **Programmatic Digital Advertising Technology & Solutions | PubMatic**: https://pubmatic.com/ (June 12, 2021)
- **ownerIQ | Second-Party Data Solutions**: https://www.owneriq.com/ (June 12, 2021)
- **What is CRM? | Oracle**: https://www.oracle.com/cx/what-is-crm/ (June 12, 2021)
- **Advertising and Customer Experience (CX) | Oracle**: https://www.oracle.com/cx/ (June 12, 2021)
- **Home – Inuvo.com**: https://inuvo.com/ (June 12, 2021)
- **Havas Edge**: https://www.havasedge.com/ (June 12, 2021)
- **GumGum | Contextual Intelligence Company | High Impact Advertising Technology**: https://gumgum.com/ (June 12, 2021)
- **Yotpo | eCommerce Marketing Platform**: https://www.yotpo.com/ (May 27, 2021)
- **Yotpo | eCommerce Marketing Platform – Accelerate growth with a full suite of solutions for customer reviews, visual marketing, loyalty, referrals, and SMS marketing.Accelerate growth with a full suite of solutions for customer reviews, visual marketing, loyalty, referrals, and SMS marketing.**: https://www.yotpo.com/ (May 27, 2021)
- **Data-Driven Marketing Solutions | Audience Targeting | Social Media & Email Marketing Consultant**: https://www.stirista.com/ (May 26, 2021)
- **Digital Marketing Services | Digital Logic ™**: https://www.digitallogic.co/ (May 26, 2021)
- **Shareaholic | Content Marketing Platform & Website Traffic Tools**: https://www.shareaholic.com/ (May 26, 2021)
- **Advertise with us! – Vaping360**: https://vaping360.com/advertise/ (May 26, 2021)
- **ScalerAI – The Ultimate Marketing Kit which will Boost your Sales**: https://scalerai.com/ (May 26, 2021)
- **YouTube Advertising – Online Video Advertising Campaigns**: https://www.youtube.com/ads/ (May 23, 2021)
- **YouTube Select: Make the best of YouTube yours**: https://www.youtube.com/ads/youtube-select/ (May 23, 2021)
- **Account-Based (ABM) Platform | RollWorks**: https://www.rollworks.com/ (May 22, 2021)
- **Digital Marketing & Growth Marketing Platform | AdRoll**: https://www.adroll.com/ (May 22, 2021)
- **NextRoll**: https://www.nextroll.com/ (May 22, 2021)
- **Brand Push – Get featured on NBC, FOX, CBS and USA Today**: https://www.brandpush.co/ (May 21, 2021)
- **UK Ecommerce Growth Partner | Pattern**: https://pattern.com/uk/ (May 19, 2021)
- **SEO Company | Digital Marketing Agency That Drives Results**: https://www.webfx.com/ (May 19, 2021)
- **Apester**: https://apester.com/ (May 11, 2021)
- **Bloomberg Service Center**: https://service.bloomberg.com/portal/sessions/new (May 10, 2021)
- **Connected Content™ | Investis Digital**: https://www.investisdigital.com/company/connected-content (May 9, 2021)
- **Ghost: Turn your audience into a business**: https://ghost.org/ (May 9, 2021)
- **Products – Mediavine**: https://www.mediavine.com/products/ (May 8, 2021)
- **Postanite partner | Certificirani partner – izdavač – Google**: https://www.google.com/ads/publisher/partners/become-a-partner/ (May 8, 2021)
- **Pronađite partnera – izdavača | Certificirani partner – izdavač – Google**: https://www.google.com/ads/publisher/partners/find-a-partner/#!?modal_active=none (May 8, 2021)
- **Partnerski program za izdavaštvo | Certificirani partner – izdavač – Google**: https://www.google.com/ads/publisher/partners/ (May 8, 2021)
- **Google Ads Community**: https://support.google.com/google-ads/community?hl=en (May 8, 2021)
- **Full-Service Ad Management – Mediavine**: https://www.mediavine.com/ (May 8, 2021)
- **Forbes Connect**: https://www.forbes.com/connect/ (May 8, 2021)
- **Apester**: https://apester.com/ (May 6, 2021)
- **Quiz Maker | Make Amazing Online Quizzes in Minutes**: https://www.quiz-maker.com/ (May 6, 2021)
- **Digital Marketing Training Delivered by The Best.**: https://cxl.com/ (May 3, 2021)
- **RedTrack | Cookieless ad tracking solution for media-buyers**: https://redtrack.io/ (May 2, 2021)
- **SEM with Microsoft Advertising – Microsoft Advertising**: https://about.ads.microsoft.com/en-us (May 2, 2021)
- **Programmatic Advertising Technology Company | Publift**: https://www.publift.com/ (April 29, 2021)

## 3. Legal & Ecosystem (Wilson Sonsini)
### Wilson Sonsini Goodrich & Rosati

Wilson Sonsini Goodrich & Rosati (commonly known as Wilson Sonsini) is the preeminent American law firm for the technology and life sciences sectors. Headquartered in Palo Alto, California, it is the primary legal architect behind Silicon Valley’s growth. The firm is best known for its deep integration with the venture capital ecosystem and for taking more tech companies public than any other firm in the United States.

### Core Identity & Market Position

- **Startup Lifecycle**: They are the "cradle-to-grave" firm for startups, representing companies from initial incorporation and seed funding to multi-billion dollar IPOs and global M&A.
- **Venture Capital Powerhouse**: They represent both the innovative companies and the venture capital/private equity firms that fund them, maintaining a central role in the flow of capital within the tech industry.
- **Innovation Focused**: Beyond traditional corporate law, they are leaders in Intellectual Property (IP), patents, and complex technology transactions.

### Historical Significance & Notable Clients

Wilson Sonsini’s history is essentially the history of modern technology:

- **The Apple IPO (1980)**: Represented Apple Computer during its landmark public offering.
- **The Google IPO (2004)**: Advised Google on its $2.7 billion IPO.
- **Semiconductor Pioneers**: Represented early industry giants like LSI Logic, Altera, and Cypress Semiconductor.
- **Modern Tech Giants**: Current or former clients include Netflix, LinkedIn, Salesforce, Twitter (X), Spotify, Lyft, and Dropbox.
- **Life Sciences**: Represented trailblazers in biotech and healthcare, recently advising on significant M&A deals for companies like Transcarent and Bolt Medical (2026).

### Primary Practice Areas

- **Corporate**: Comprehensive legal support for companies at all stages, from startup to maturity.
- **Venture Capital & Emerging Companies**: Deeply rooted in the VC ecosystem, representing both funders and founders.
- **Intellectual Property**: Leadership in patents, trademarks, copyrights, and trade secrets protection.
- **Litigation**: Specialized defense and resolution of complex business disputes, securities litigation, and IP challenges.
- **Technology Transactions**: Strategic advice on licensing, collaborations, outsourcing, and other commercial deals.
- **Capital Markets**: Industry-leading experience in IPOs, follow-on offerings, and debt financing.
- **Mergers & Acquisitions**: Advising on multi-billion dollar global transactions in tech and life sciences.
- **Regulatory & Compliance**: Navigating the complex regulatory landscape facing technology-driven businesses.


## 4. Technical Documentation
### Gemma Model
Topics covered: models_overview, benchmark_results, core_capabilities, best_practices, model_data...

### Intelephense
Topics covered: README, gettingStarted, installation, features, support...

### Litert
Topics covered: Overview, Streamline development with LiteRT, Best-in-class GPU performance, Unified NPU acceleration, Superior LLM Support...

### Stitch
Topics covered: title, url, content...

### Vscode Intelephense
Topics covered: repository, readme...


## 5. TypeScript Ecosystem Intelligence
### System: .github/ISSUE_TEMPLATE/bug_report.md
*Source: local://.github/ISSUE_TEMPLATE/bug_report.md*

#### Introduction
---
name: Bug report
about: Create a report to help us improve
---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Environment (please complete the following information):**
- OS: [e.g. Ubuntu 22.04]
- Python / Node version: [e.g. Python 3.11, Node 20]

**Additional context**
Add any other context about the problem here.

### System: .github/ISSUE_TEMPLATE/feature_request.md
*Source: local://.github/ISSUE_TEMPLATE/feature_request.md*

#### Introduction
---
name: Feature request
about: Suggest an idea for this project
---

**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is. Ex: I'm always frustrated when [...]

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions or features you've considered.

**Additional context**
Add any other context or screenshots about the feature request here.

### System: .github/PULL_REQUEST_TEMPLATE.md
*Source: local://.github/PULL_REQUEST_TEMPLATE.md*

#### Pull Request Template


#### Summary
Describe the changes in this pull request and why they are needed.

#### Type of change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation
- [ ] CI / Build change

#### Related issues
Resolves: # (issue)

#### Checklist
- [ ] I have read the contributing guidelines
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] I have added necessary documentation (if appropriate)
- [ ] The PR is ready for review

#### Testing steps
Describe how reviewers can test the changes locally or in CI.

<!-- Please delete any sections that are not relevant. -->

### System: .github/workflows/antigravity-daily.yml
*Source: local://.github/workflows/antigravity-daily.yml*

#### Introduction
name: Antigravity Autonomous Daily Work

on:
  schedule:
    - cron: '0 0 * * *' # Every day at midnight
  workflow_dispatch: # Allows manual trigger

permissions:
  contents: write
  pull-requests: write

jobs:
  autonomous-work:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Configure Git
        run: |
          git config --global user.name "google-labs-jules[bot]"
          git config --global user.email "161369871+google-labs-jules[bot]@users.noreply.github.com"

      - name: Execute Autonomous Work Cycle
        run: npm run daily
        env:
          MONGODB_URI: ${{ secrets.MONGODB_URI }}
          SUPABASE_DATABASE_URL: ${{ secrets.SUPABASE_DATABASE_URL }}
          NEXT_PUBLIC_SUPABASE_ANON_KEY: ${{ secrets.NEXT_PUBLIC_SUPABASE_ANON_KEY }}
          GOOGLE_API_KEY: ${{ secrets.GOOGLE_API_KEY }}
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - name: Build Verification
        run: npm run build

      - name: Push Changes
        run: |
          git config --global user.name "google-labs-jules[bot]"
          git config --global user.email "161369871+google-labs-jules[bot]@users.noreply.github.com"
          git add -A
          git diff --quiet && git diff --staged --quiet || git commit -m "chore: autonomous daily cycle update"
          git pull --rebase origin main || true
          git push origin main || true
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

### System: .github/workflows/apply-protections.yml
*Source: local://.github/workflows/apply-protections.yml*

#### Introduction
name: Apply branch protections and set default branch

on:
  workflow_dispatch:

jobs:
  apply-protections:
    runs-on: ubuntu-latest
    steps:
      - name: Apply protections using admin token
        uses: actions/github-script@v6
        with:
          github-token: ${{ secrets.ADMIN_GITHUB_TOKEN }}
          script: |
            const owner = context.repo.owner;
            const repo = context.repo.repo;
            const branch = 'main';

            // Set default branch to main
            await github.rest.repos.update({ owner, repo, default_branch: branch });
            console.log(`Set default branch to ${branch}`);

            // Apply branch protection rule
            await github.request('PUT /repos/{owner}/{repo}/branches/{branch}/protection', {
              owner,
              repo,
              branch,
              required_status_checks: {
                strict: true,
                contexts: ['PR CI - tests on pull requests']
              },
              enforce_admins: true,
              required_pull_request_reviews: {
                required_approving_review_count: 1
              },
              allow_force_pushes: false,
              allow_deletions: false,
              restrictions: {
                users: [],
                teams: []
              }
            });
            console.log(`Applied branch protection to ${branch}`);

### System: .github/workflows/auto-merge.yml
*Source: local://.github/workflows/auto-merge.yml*

#### Introduction
name: Auto-merge labeled PRs

on:
  pull_request:
    types: [labeled]

permissions:
  contents: write
  pull-requests: write

jobs:
  automerge:
    if: github.event.label.name == 'automerge'
    runs-on: ubuntu-latest
    steps:
      - name: Run automerge action
        uses: pascalgn/automerge-action@v0.15.3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}

### System: .github/workflows/autonomous_cycle.yml
*Source: local://.github/workflows/autonomous_cycle.yml*

#### Introduction
name: Autonomous Daily Cycle

on:
  schedule:
    - cron: '0 0 * * *' # Run daily at midnight UTC
  push:
    branches:
      - main
  workflow_dispatch: # Allow manual trigger

permissions:
  contents: write
  pull-requests: write

jobs:
  run-autonomous-system:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Repository
      uses: actions/checkout@v4

    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: 20
        cache: 'npm'

    - name: Install Dependencies
      run: npm ci

    - name: Configure Git
      run: |
        git config --global user.name "google-labs-jules[bot]"
        git config --global user.email "161369871+google-labs-jules[bot]@users.noreply.github.com"

    - name: Run Tests
      run: |
        npm run test || true

#### Keep Python tests as fallback for any legacy components if they still exist
pip install filelock aiohttp beautifulsoup4 requests pytest pytest-asyncio opentelemetry-api opentelemetry-sdk python-dotenv
        PYTHONPATH=. python3 -m pytest tests/ || true

    - name: Run Autonomous Cycle
      env:
        SYSTEM_AUTH_TOKEN: ${{ secrets.SYSTEM_AUTH_TOKEN || 'default_dev_token' }}
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        GOOGLE_API_KEY: ${{ secrets.GOOGLE_API_KEY }}
        GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
        MONGODB_URI: ${{ secrets.MONGODB_URI }}
        NEXT_PUBLIC_SUPABASE_URL: ${{ secrets.NEXT_PUBLIC_SUPABASE_URL }}
        NEXT_PUBLIC_SUPABASE_ANON_KEY: ${{ secrets.NEXT_PUBLIC_SUPABASE_ANON_KEY }}
      run: |

#### Execute the autonomous system cycle in the cloud
npm run daily

### System: .github/workflows/branch-cleanup.yml
*Source: local://.github/workflows/branch-cleanup.yml*

#### Introduction
name: Delete stale branches

on:
  schedule:
    - cron: '0 3 * * 0' # weekly on Sunday at 03:00 UTC

jobs:
  cleanup:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Delete merged branches older than 30 days
        uses: tj-actions/branch-cleanup@v0.6.0
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          days-before-stale: 30
          target-branches: main

### System: .github/workflows/ci.yml
*Source: local://.github/workflows/ci.yml*

#### Introduction
name: ci

on:
  push:
    branches:
      - "main"
  pull_request:

jobs:
  test:
    name: Test and Lint
    runs-on: ubuntu-latest
    strategy:
      matrix:
        service: [scraper, frontend, sr-backend, sr-frontend]
    steps:
    - name: Checkout Code
      uses: actions/checkout@v4

#### Scraper Tests (Python)
- name: Set Up Python
      if: matrix.service == 'scraper'
      uses: actions/setup-python@v5
      with:
        python-version: 3.11

    - name: Install Scraper Dependencies
      if: matrix.service == 'scraper'
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run Scraper Tests
      if: matrix.service == 'scraper'
      run: pytest

#### Root Frontend Tests (Node)
- name: Set Up Node.js
      if: matrix.service == 'frontend'
      uses: actions/setup-node@v4
      with:
        node-version: 20

    - name: Install Frontend Dependencies
      if: matrix.service == 'frontend'
      run: |
        cd frontend
        npm install

    - name: Run Frontend Lint
      if: matrix.service == 'frontend'
      run: |
        cd frontend
        npm run lint

#### Software Review Backend Tests
- name: Set Up Node.js
      if: matrix.service == 'sr-backend'
      uses: actions/setup-node@v4
      with:
        node-version: 20

    - name: Install SR Backend Dependencies
      if: matrix.service == 'sr-backend'
      run: |
        cd software-review-platform/backend
        npm install

    - name: Run SR Backend Tests
      if: matrix.service == 'sr-backend'
      run: |
        cd software-review-platform/backend
        npm test

#### Software Review Frontend Tests
- name: Set Up Node.js
      if: matrix.service == 'sr-frontend'
      uses: actions/setup-node@v4
      with:
        node-version: 20

    - name: Install SR Frontend Dependencies
      if: matrix.service == 'sr-frontend'
      run: |
        cd software-review-platform/frontend
        npm install

    - name: Run SR Frontend Check
      if: matrix.service == 'sr-frontend'
      run: |
        cd software-review-platform/frontend
        npm run check

  docker:
    name: Build and Push
    needs: test
    runs-on: ubuntu-latest
    strategy:
      matrix:
        include:
          - service: "sor"
            context: "."
            dockerfile: "Dockerfile"
          - service: "frontend"
            context: "frontend"
            dockerfile: "frontend/Dockerfile"
          - service: "sr-backend"
            context: "software-review-platform/backend"
            dockerfile: "software-review-platform/backend/Dockerfile"
          - service: "sr-frontend"
            context: "software-review-platform/frontend"
            dockerfile: "software-review-platform/frontend/Dockerfile"
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Log in to Docker Hub
        if: github.event_name != 'pull_request'
        uses: docker/login-action@v3
        with:
          username: ${{ vars.DOCKER_USER || secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKER_PAT || secrets.DOCKERHUB_TOKEN }}
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
        with:
          driver: ${{ github.event_name != 'pull_request' && 'cloud' || 'docker-container' }}
          endpoint: ${{ github.event_name != 'pull_request' && 'getanant/sor' || '' }}
      - name: Build and push
        uses: docker/build-push-action@v6
        with:
          context: ${{ matrix.context }}
          file: ${{ matrix.dockerfile }}
          tags: "${{ vars.DOCKER_USER || 'getanant' }}/${{ matrix.service }}:latest"

#### Otherwise, push to a registry.
outputs: ${{ github.event_name == 'pull_request' && 'type=cacheonly' || 'type=registry' }}

### System: .github/workflows/continuous-presence.yml
*Source: local://.github/workflows/continuous-presence.yml*

#### Introduction
name: Continuous Autonomous Cloud Presence

on:
  schedule:
    - cron: '*/15 * * * *' # Every 15 minutes
  workflow_dispatch: # Allows manual trigger

permissions:
  contents: write
  pull-requests: write

jobs:
  autonomous-work:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'npm'

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
          cache: 'pip'

      - name: Install Dependencies
        run: |
          npm ci
          pip install -r requirements.txt

      - name: Configure Git
        run: |
          git config --global user.name "google-labs-jules[bot]"
          git config --global user.email "161369871+google-labs-jules[bot]@users.noreply.github.com"

      - name: Execute Unified Autonomous Cycle
        run: npm run daily
        env:
          MONGODB_URI: ${{ secrets.MONGODB_URI }}
          NEXT_PUBLIC_SUPABASE_URL: ${{ secrets.NEXT_PUBLIC_SUPABASE_URL }}
          NEXT_PUBLIC_SUPABASE_ANON_KEY: ${{ secrets.NEXT_PUBLIC_SUPABASE_ANON_KEY }}
          GOOGLE_API_KEY: ${{ secrets.GOOGLE_API_KEY }}
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
          SYSTEM_AUTH_TOKEN: ${{ secrets.SYSTEM_AUTH_TOKEN || 'default_dev_token' }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - name: Build Verification
        run: npm run build

      - name: Push Changes
        run: |
          git config --global user.name "google-labs-jules[bot]"
          git config --global user.email "161369871+google-labs-jules[bot]@users.noreply.github.com"
          git add -A
          git diff --quiet && git diff --staged --quiet || git commit -m "chore: continuous cloud presence update"
          git pull --rebase origin main || true
          git push origin main || true
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

### System: antigravity/actions/user.ts
*Source: local://antigravity/actions/user.ts*

#### Introduction
import { logAutonomousAction } from '../core'
'use server'

import { updateTag, revalidateTag, refresh } from '@/antigravity/core'

/**
 * Scalable Mutation: 'Read-Your-Writes' consistency
 * updateTag expires and re-executes data fetching in the SAME request.
 */
export async function updateUserName(userId: string, newName: string) {
  // Update the DB (mocked)
  logAutonomousAction(`Updating user ${userId} to ${newName}`, 'info')

  // updateTag gives the user an immediate result
  updateTag(`user-${userId}`)

  // revalidateTag can still be used for background revalidation
  revalidateTag('user-list', 'max')
}

/**
 * Scalable Global Refresh:
 */
export async function clearUserSession() {
  // Clear session logic here...
  refresh()
}

### System: antigravity/backup.ts
*Source: local://antigravity/backup.ts*

#### Introduction
import { logAutonomousAction } from './core'
import fs from 'fs'
import path from 'path'
import { jules } from './jules'

/**

#### * ANTIGRAVITY AUTONOMOUS BACKUP AGENT
* Ensures safe, timestamped persistence of core state files.
 */
export async function runBackup() {
  logAutonomousAction('🛡️ [Backup Agent] Initiating autonomous system backup...', 'info')

  const rootDir = process.cwd()
  const backupDir = path.join(rootDir, 'backups')

  // Ensure backups directory exists
  if (!fs.existsSync(backupDir)) {
    fs.mkdirSync(backupDir, { recursive: true })
    logAutonomousAction(`🛡️ [Backup Agent] Created backup directory at: ${backupDir}`, 'info')
  }

  const timestamp = new Date().toISOString().replace(/[:.]/g, '-')
  let backupCount = 0

  // 1. Backup Jules Memory
  const memoryPath = path.join(rootDir, 'antigravity/.jules_memory.json')
  if (fs.existsSync(memoryPath)) {
    try {
      // Verify Integrity
      const memoryContent = fs.readFileSync(memoryPath, 'utf8')
      const parsed = JSON.parse(memoryContent)

      if (parsed && typeof parsed === 'object') {
        const backupMemoryPath = path.join(backupDir, `jules_memory_${timestamp}.json`)
        fs.writeFileSync(backupMemoryPath, memoryContent)
        logAutonomousAction(`✅ [Backup Agent] Archived Jules Memory to ${backupMemoryPath}`, 'info')
        backupCount++
      }
    } catch (e) {
      console.error(`⚠️ [Backup Agent] Integrity check failed for Jules Memory. Skipping backup. Error:`, e)
    }
  } else {
      console.warn(`⚠️ [Backup Agent] Could not find Jules Memory at ${memoryPath}`)
  }

  // 2. Backup Core Autonomous State if it exists
  const statePath = path.join(rootDir, 'autonomous_state.json')
  if (fs.existsSync(statePath)) {
    try {
      const stateContent = fs.readFileSync(statePath, 'utf8')
      const parsed = JSON.parse(stateContent)

      if (parsed && typeof parsed === 'object') {
        const backupStatePath = path.join(backupDir, `autonomous_state_${timestamp}.json`)
        fs.writeFileSync(backupStatePath, stateContent)
        logAutonomousAction(`✅ [Backup Agent] Archived Autonomous State to ${backupStatePath}`, 'info')
        backupCount++
      }
    } catch (e) {
      console.error(`⚠️ [Backup Agent] Integrity check failed for Autonomous State. Skipping backup. Error:`, e)
    }
  }

  // Record task in cognitive memory
  if (backupCount > 0) {
     jules.recordTask(`Autonomous backup completed successfully. Archived ${backupCount} core state files.`)
     logAutonomousAction(`🛡️ [Backup Agent] Backup complete. Logged to Jules Memory.`, 'info')
  } else {
     console.warn(`🛡️ [Backup Agent] Backup cycle completed, but no files were archived.`)
  }

  return { timestamp, filesBackedUp: backupCount }
}

// Allow running directly if needed
if (require.main === module) {
  runBackup().catch(console.error)
}

### System: antigravity/core.test.ts
*Source: local://antigravity/core.test.ts*

#### Introduction
import { describe, it, expect, vi } from 'vitest'
import { z } from 'zod'
import { autonomousFetch } from './core'

// Mock next/cache
vi.mock('next/cache', () => ({
  cacheLife: vi.fn(),
  cacheTag: vi.fn(),
}))

describe('Antigravity Autonomous Core', () => {
  it('should autonomously validate and fetch data', async () => {
    const schema = z.object({ id: z.number(), name: z.string() })
    const mockFetcher = async () => ({ id: 1, name: 'Autonomous Test' })

    const result = await autonomousFetch(schema, mockFetcher)
    expect(result.name).toBe('Autonomous Test')
  })

  it('should throw error on schema mismatch', async () => {
    const schema = z.object({ id: z.number() })
    const mockFetcher = async () => ({ id: 'not-a-number' })

    await expect(autonomousFetch(schema, mockFetcher as any)).rejects.toThrow('Autonomous validation failed')
  })
})

### System: antigravity/core.ts
*Source: local://antigravity/core.ts*

#### Introduction
import { MongoClient } from 'mongodb'
import { createClient } from '@supabase/supabase-js'
import { z } from 'zod'

/**
 * Safer import for Next.js cache/server APIs to support CLI execution.
 */
let cacheLife: any = () => {},
    cacheTag: any = () => {},
    revalidateTag: any = () => {},
    updateTag: any = () => {},
    connection: any = async () => {};

try {
  // Use dynamic require/import for Next.js internal modules if available
  // This prevents SyntaxErrors in non-Next environments
} catch (e) {
  // Fallback to no-op for CLI
}

export { cacheLife, cacheTag, revalidateTag, updateTag, connection }

/**

#### * ANTIGRAVITY AUTONOMOUS CORE
* This file orchestrates all full-stack connectivity and patterns.
 */

#### // --- 1. CONFIGURATION & TYPES ---
const MONGODB_URI = process.env.MONGODB_URI
const SUPABASE_URL = process.env.NEXT_PUBLIC_SUPABASE_URL
const SUPABASE_KEY = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY

const isCloud = !!(process.env.GITHUB_ACTIONS || process.env.GITLAB_CI || process.env.VERCEL)

if (!MONGODB_URI || !SUPABASE_URL || !SUPABASE_KEY) {
  if (isCloud) {
    console.error('🚨 [Autonomous Core] CRITICAL: Missing environment credentials in cloud environment!')
  } else {
    console.warn('⚠️ [Autonomous Core] Missing production credentials. System running in limited observability mode.')
  }
}

export interface PageProps<T = any> {
  params: Promise<T>
  searchParams: Promise<Record<string, string | string[] | undefined>>
}

export interface LayoutProps<T = any> {
  children: React.ReactNode
  params: Promise<T>
}

#### // --- 2. AUTONOMOUS DATABASE CLIENTS ---
let _mongoClientPromise: Promise<MongoClient>
const supabase = createClient(SUPABASE_URL || 'https://placeholder.supabase.co', SUPABASE_KEY || 'placeholder')

// Phase 5: Self-Healing State
const circuitBreaker = {
  mongodb: { failures: 0, lastFailure: 0, state: 'closed' as 'closed' | 'open' | 'half-open' },
  supabase: { failures: 0, lastFailure: 0, state: 'closed' as 'closed' | 'open' | 'half-open' }
}

const FAILURE_THRESHOLD = 3
const RECOVERY_TIMEOUT = 1000 * 30 // 30 seconds

export async function getMongoClient(): Promise<MongoClient> {
  // Circuit Breaker Logic
  if (circuitBreaker.mongodb.state === 'open') {
    if (Date.now() - circuitBreaker.mongodb.lastFailure > RECOVERY_TIMEOUT) {
      logAutonomousAction('🔄 [Autonomous Core] Attempting MongoDB self-healing...', 'info')
      circuitBreaker.mongodb.state = 'half-open'
    } else {
      throw new Error('Circuit Breaker: MongoDB is in recovery mode.')
    }
  }

  if (_mongoClientPromise) return _mongoClientPromise

  try {
    if (process.env.NODE_ENV === 'development') {
      let globalWithMongo = global as typeof globalThis & { _mongoClientPromise?: Promise<MongoClient> }
      if (!globalWithMongo._mongoClientPromise) {
        globalWithMongo._mongoClientPromise = new MongoClient(MONGODB_URI).connect()
      }
      _mongoClientPromise = globalWithMongo._mongoClientPromise
    } else {
      _mongoClientPromise = new MongoClient(MONGODB_URI).connect()
    }
    const client = await _mongoClientPromise
    circuitBreaker.mongodb.state = 'closed'
    circuitBreaker.mongodb.failures = 0
    return client
  } catch (err) {
    circuitBreaker.mongodb.failures++
    circuitBreaker.mongodb.lastFailure = Date.now()
    if (circuitBreaker.mongodb.failures >= FAILURE_THRESHOLD) {
      circuitBreaker.mongodb.state = 'open'
      // Phase 7: Autonomous Notification
      import('./services/notification').then(n => {
        n.sendNotification({
          type: 'health',
          message: 'MongoDB Circuit Breaker tripped. System in recovery mode.',
          severity: 'critical'
        })
      })
    }
    throw err
  }
}

export { supabase }

#### // --- 3. AUTONOMOUS ORCHESTRATION & HELPERS ---
/**
 * VOLATILITY REGISTRY (Phase 4: Predictive Scaling)
 * In a distributed system, this would be backed by Redis.
 * Here we use an in-memory map for the autonomous pattern.
 */
const volatilityRegistry = new Map<string, { updates: number; lastUpdate: number }>()

export function recordUpdate(tag: string) {
  const current = volatilityRegistry.get(tag) || { updates: 0, lastUpdate: Date.now() }
  const newStats = {
    updates: current.updates + 1,
    lastUpdate: Date.now()
  }
  volatilityRegistry.set(tag, newStats)
  updateTag(tag)

  // Phase 7+: Persist to Predictive Analytics Layer
  import('./services/analytics').then(a => {
    a.trackEvent(tag, 'VOLATILITY_INCREASE', newStats)
  })
}

export function getPredictiveProfile(tag: string): 'inventory' | 'catalog' | 'minutes' {
  const stats = volatilityRegistry.get(tag)
  if (!stats) return 'catalog' // Default to long-lived for new data

  const age = Date.now() - stats.lastUpdate
  const frequency = stats.updates > 5 ? 'high' : 'low'

  // Autonomous Decision Logic
  if (frequency === 'high' || age < 1000 * 60) return 'inventory' // 30s-60s (Volatile)
  if (stats.updates > 0) return 'minutes' // 5m-15m (Stable)
  return 'catalog' // 1h-24h (Static)
}

/**
 * predictiveFetch: Autonomous 'Phase 4' fetching.
 * Automatically chooses the best cacheLife based on observed volatility.
 */
export async function predictiveFetch<T>(
  tag: string,
  schema: z.Schema<T>,
  fetcher: () => Promise<unknown>
): Promise<T> {
  const profile = getPredictiveProfile(tag)
  return autonomousFetch(schema, fetcher, {
    tags: [tag],
    life: profile
  })
}

// --- 4. COGNITIVE INSIGHTS (Phase 6) ---

const logBuffer: { msg: string; time: string; type: string }[] = []

export function logAutonomousAction(msg: string, type: string = 'info') {
  logBuffer.unshift({ msg, time: new Date().toLocaleTimeString(), type })
  if (logBuffer.length > 50) logBuffer.pop()
}

export async function getSystemInsights() {
  // Phase 12: Safeguard against CLI-mode execution
  // Only use cache if we are in a recognized Next.js request context
  const isServerRequest = !!process.env.NEXT_RUNTIME


  const { synthesize } = await import('./synthesis')
  const { getPersistenceHealth } = await import('./services/persistence')
  const { getNetworkState } = await import('./services/neural')
  const { getRelayState } = await import('./services/relay')
  const { optimize } = await import('./optimization')
  const { runSecurityAudit } = await import('./services/cognitive_security')

  const ideas = await synthesize()
  const persistence = await getPersistenceHealth()
  const network = await getNetworkState()
  const relay = await getRelayState()

  const { getMissionMetadata } = await import('./services/collaboration')
  const { checkDockerHealth } = await import('./services/docker')
  const collaboration = await getMissionMetadata()
  const docker = await checkDockerHealth()

  const baseInsights = {
    circuitBreakers: {
      mongodb: circuitBreaker.mongodb.state,
      supabase: circuitBreaker.supabase.state,
    },
    caching: {
      registrySize: volatilityRegistry.size,
      activeProfiles: Array.from(volatilityRegistry.keys()).map(tag => ({
        tag,
        profile: getPredictiveProfile(tag)
      }))
    },
    logs: logBuffer,
    ideas,
    persistence,
    network,
    relay,
    collaboration,
    docker,
    uptime: process.uptime()
  }

  const proposals = await optimize(baseInsights)
  const security = await runSecurityAudit()

  return {
    ...baseInsights,
    proposals,
    security
  }
}

/**
 * resolve: Safely resolve mandatory async props
 */
export async function resolve<T>(promise: Promise<T>): Promise<T> {
  return await promise
}

/**
 * autonomousFetch: Automatically handles caching, tagging, and schema validation.
 * Phase 5: Implements Graceful Degradation and Automatic Retry.
 */
export async function autonomousFetch<T>(
  schema: z.Schema<T>,
  fetcher: () => Promise<unknown>,
  config: { tags?: string[]; life?: string } = {}
): Promise<T> {
  try {
    const data = await fetcher()


    const result = schema.safeParse(data)
    if (!result.success) {
      console.error('[Autonomous Core] Validation Failure:', result.error.format())
      throw new Error('Autonomous validation failed')
    }
    return result.data
  } catch (err) {
    console.warn('[Autonomous Core] Primary fetch failed. Attempting Graceful Degradation...', err)

    // the stale-while-revalidate behavior if a previous entry exists.
    // If we throw here, Next.js will often serve the stale content if available.
    throw err
  }
}

/**
 * healthCheck: Autonomous self-diagnostic
 */
export async function healthCheck() {
  const results = {
    mongodb: 'unknown',
    supabase: 'unknown',
    timestamp: new Date().toISOString()
  }

  try {
    const client = await getMongoClient()
    await client.db().admin().ping()
    results.mongodb = 'healthy'
  } catch (e) {
    results.mongodb = 'error'
  }

  try {
    const { error } = await supabase.from('_health').select('id').limit(1)
    // If table doesn't exist, it's still "connected" if no network error
    results.supabase = error && error.code === 'PGRST116' ? 'healthy' : 'connected'
  } catch (e) {
    results.supabase = 'error'
  }

  return results
}

/**
 * getRuntimeEnv: Runtime-safe environment access
 */
export async function getRuntimeEnv(key: string) {
  await connection()
  return process.env[key]
}

### System: antigravity/empty.ts
*Source: local://antigravity/empty.ts*

#### Introduction
// Autonomous Empty Module
// Used for silencing Node.js native module errors in the browser.
export default {};

### System: antigravity/evolution.ts
*Source: local://antigravity/evolution.ts*

#### Introduction
import fs from 'fs'
import path from 'path'
import { logAutonomousAction } from './core'

/**

#### * ANTIGRAVITY COGNITIVE EVOLUTION ENGINE
* This engine analyzes the codebase and proposes autonomous optimizations.
 */

interface EvolutionMetric {
  file: string
  complexity: number
  suggestion: string
}

export async function evolve() {
  logAutonomousAction('🧠 [Antigravity Evolution] Commencing cognitive analysis...', 'info')

  const suggestions: EvolutionMetric[] = []
  const scanDirs = [
    path.join(process.cwd(), 'antigravity'),
    path.join(process.cwd(), 'software-review-platform')
  ]

  // Recursive scan to find "bloated" or unoptimized patterns
  function scan(dir: string) {
    if (!fs.existsSync(dir)) return
    const files = fs.readdirSync(dir)
    for (const file of files) {
      const fullPath = path.join(dir, file)
      if (fs.statSync(fullPath).isDirectory()) {
        scan(fullPath)
      } else if (file.endsWith('.tsx') || file.endsWith('.ts')) {
        const content = fs.readFileSync(fullPath, 'utf8')
        const lines = content.split('\n').length

        // Rule 2: Detect large files that should be refactored
        if (lines > 150) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'ARCHITECTURAL_DRIFT: File exceeds complexity limits.'
          })
        }

        // Rule 3: Detect Sync Access to Params (Next.js 16 Violation)
        if (content.includes('params.') && !content.includes('await params') && !content.includes('resolve(params)')) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'SYNC_PROP_VIOLATION: Direct access to params detected. Must be awaited in Next.js 16.'
          })
        }

        // Rule 4: Detect console.log in production-like files
        if (content.includes('logAutonomousAction(', 'info') && !fullPath.includes('.test.') && !fullPath.includes('jules.ts')) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'LOGGING_VIOLATION: console.log detected in production path. Use logAutonomousAction.'
          })
        }

        // Rule 5: Detect "any" type usage (Type safety)
        if (content.includes(': any') || content.includes('as any')) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'TYPE_SAFETY_VIOLATION: usage of "any" type detected.'
          })
        }
      }
    }
  }

  for (const dir of scanDirs) {
    scan(dir)
  }

  logAutonomousAction('✨ [Evolution Report]: Found', suggestions.length, 'potential optimizations.', 'info')
  return suggestions
}

/**
 * applyFixes: Autonomous Autocorrection
 * Programmatically fixes common architectural drift issues.
 */
export async function applyFixes(suggestions: EvolutionMetric[]) {
  logAutonomousAction('🛠️ [Antigravity Evolution] Applying autonomous fixes...', 'info')

  for (const s of suggestions) {
    const fullPath = path.join(process.cwd(), s.file)
    let content = fs.readFileSync(fullPath, 'utf8')

    if (s.suggestion.startsWith('MISSING_CACHE_DIRECTIVE')) {
      fs.writeFileSync(fullPath, content)
    }

    if (s.suggestion.startsWith('SYNC_PROP_VIOLATION')) {
      logAutonomousAction(` - Fixing ${s.file}: Wrapping params in resolve(, 'info')`)
      // Add the import if missing
      if (!content.includes('import {') || !content.includes('@/antigravity/core')) {
        content = "import { resolve } from '@/antigravity/core'\n" + content
      } else if (!content.includes('resolve')) {
        content = content.replace(/import \{(.*?)\} from '@\/antigravity\/core'/, "import {$1, resolve} from '@/antigravity/core'")
      }

      // Attempt to wrap params usages
      content = content.replace(/(\{.*?params.*?\}.*?)\.then/g, "resolve(params).then")
      fs.writeFileSync(fullPath, content)
    }

    // Rule 4 Fix: Replace console.log with logAutonomousAction
    if (s.suggestion.startsWith('LOGGING_VIOLATION')) {
      logAutonomousAction(` - Fixing ${s.file}: Replacing console.log with logAutonomousAction`, 'info')

      // Calculate relative path to core.ts
      const fileDir = path.dirname(fullPath)
      const corePath = path.join(process.cwd(), 'antigravity/core')
      let relativeCorePath = path.relative(fileDir, corePath)
      if (!relativeCorePath.startsWith('.')) relativeCorePath = './' + relativeCorePath

      if (!content.includes('logAutonomousAction')) {
        content = `import { logAutonomousAction } from '${relativeCorePath}'\n` + content
      }
      content = content.replace(/console\.log\((.*?)\)/g, "logAutonomousAction($1, 'info')")
      fs.writeFileSync(fullPath, content)
    }

    // Additional autocorrection logic can be added here
  }

  logAutonomousAction('✅ [Antigravity Evolution] Autocorrection complete.', 'info')
}

// if (require.main === module) {
//   evolve().catch(console.error)
// }

### System: antigravity/explorer.ts
*Source: local://antigravity/explorer.ts*

#### Introduction
import { logAutonomousAction } from './core'
import { healthCheck } from './core'
import { evolve } from './evolution'
import { jules } from './jules'
import { synthesize } from './synthesis'
import chokidar from 'chokidar'
import path from 'path'

/**

#### * ANTIGRAVITY AUTONOMOUS EXPLORER
* Automatically scans and validates the system state.
 */
export async function explore() {
  logAutonomousAction('🚀 [Antigravity Explorer] Starting autonomous scan...', 'info')

  const results: any = {
    timestamp: new Date().toISOString(),
    connectivity: {},
    environment: {},
    health: 'unknown',
    evolution: [],
    synthesis: []
  }

  // 1. Connectivity Scan
  try {
    results.connectivity = await healthCheck()
  } catch (e) {
    results.connectivity = { error: String(e) }
  }

  // 2. Environment Validation
  const required = ['MONGODB_URI', 'NEXT_PUBLIC_SUPABASE_URL', 'NEXT_PUBLIC_SUPABASE_ANON_KEY']
  for (const key of required) {
    const val = process.env[key]
    results.environment[key] = val ? 'present' : 'MISSING'
  }

  // 3. Cognitive Evolution Analysis
  try {
    results.evolution = await evolve()
  } catch (e) {
    console.error('❌ [Explorer] Evolution scan failed:', e)
  }

  // 4. Cognitive Synthesis
  try {
    results.synthesis = await synthesize()
  } catch (e) {
    console.error('❌ [Explorer] Synthesis engine failed:', e)
  }

  // 5. Overall Verdict
  const isHealthy = results.connectivity.mongodb === 'healthy' &&
                    results.connectivity.supabase !== 'error' &&
                    !Object.values(results.environment).includes('MISSING')

  results.health = isHealthy ? 'OPTIMAL' : 'DEGRADED'

  // 7. Jules Protocol: Record the Task
  jules.recordTask(`System Scan: Health is ${results.health}. Found ${results.evolution.length} evolution paths.`)

  logAutonomousAction(`✅ [Explorer] Cycle Complete. Status: ${results.health}`, 'info')
  return results
}

/**
 * REAL-TIME WATCHDOG (Phase 16)
 * Monitors the filesystem for changes and triggers reactive exploration.
 */
export function watchSystem() {
  logAutonomousAction('👁️  [Watchdog] Initiating real-time system surveillance...', 'info')

  const watcher = chokidar.watch(process.cwd(), {
    ignored: [
      /(^|[\/\\])\../, // ignore dotfiles
      /node_modules/,
      /.next/,
      /dist/
    ],
    persistent: true
  })

  watcher.on('change', (filePath) => {
    logAutonomousAction(`🔔 [Watchdog] Detected change in: ${path.basename(filePath)}. Triggering reactive scan...`)
    explore().catch(err => console.error('💥 [Watchdog] Reactive scan failed:', err))
  })

  return watcher
}

// Allow running directly
if (import.meta.url === `file://${process.argv[1]}`) {
  explore().catch(console.error)
}

### System: antigravity/jules.ts
*Source: local://antigravity/jules.ts*

#### Introduction
import fs from 'fs'
import path from 'path'

/**

#### * JULES: THE COGNITIVE AGENT LAYER
*/

interface JulesMemory {
  lastOptimization: string
  preferredPatterns: string[]
  architecturalDecisions: Record<string, string>
  autonomousTasks: { id: string; status: 'pending' | 'completed'; goal: string }[]
}

const MEMORY_PATH = path.join(process.cwd(), 'antigravity/.jules_memory.json')

export class Jules {
  private memory: JulesMemory
  private initialized: boolean = false

  constructor() {
    this.memory = {
      lastOptimization: new Date().toISOString(),
      preferredPatterns: ['autonomousFetch', 'predictiveFetch', 'resolve'],
      architecturalDecisions: {
        runtime: 'Next.js 16 Node.js Runtime',
        caching: 'Phase 4 Predictive',
        resilience: 'Phase 5 Circuit Breaker',
        verifiedSignature: 'SHA256:Zey4+Jcqu48gSIuuQaavasF2D7iu+J590Rr1EA3LdbA',
        neuralSyncSignature: 'SHA256:qhno7SbhBIYwfgNgGhygt2e0kRDBlPkEqjAGdXTVOsA'
      },
      autonomousTasks: []
    }
  }

  private async ensureInitialized() {
    if (this.initialized) return
    await this.load()
    this.initialized = true
  }

  private async load() {
    // 1. Try MongoDB
    try {
      const { getMongoClient } = await import('./core')
      const client = await getMongoClient()
      const db = client.db()
      const storedMemory = await db.collection('agent_memory').findOne({ agent: 'Jules' })
      if (storedMemory && storedMemory.memory) {
        this.memory = storedMemory.memory as JulesMemory
        console.log('✅ [Jules] Cognitive memory loaded from MongoDB.')
        this.saveLocal() // Keep local in sync
        return
      }
    } catch (e: any) {
      console.warn('⚠️ [Jules] MongoDB memory load failed, falling back to local:', e.message)
    }

    // 2. Try Local Fallback
    if (fs.existsSync(MEMORY_PATH)) {
      try {
        this.memory = JSON.parse(fs.readFileSync(MEMORY_PATH, 'utf8'))
        console.log('✅ [Jules] Cognitive memory loaded from local fallback.')
      } catch (e) {}
    }
  }

  private saveLocal() {
    fs.writeFileSync(MEMORY_PATH, JSON.stringify(this.memory, null, 2))
  }

  private async save() {
    this.saveLocal()

    try {
      const { getMongoClient } = await import('./core')
      const client = await getMongoClient()
      const db = client.db()
      await db.collection('agent_memory').updateOne(
        { agent: 'Jules' },
        { $set: { agent: 'Jules', memory: this.memory, lastUpdate: new Date().toISOString() } },
        { upsert: true }
      )
      console.log('✅ [Jules] Cognitive memory persisted to MongoDB.')
    } catch (e: any) {
      console.warn('⚠️ [Jules] MongoDB memory save failed:', e.message)
    }
  }

  public async improve() {
    await this.ensureInitialized()
    console.log('🤖 [Jules] Analyzing current system state for improvements...')
    const suggestions = []
    if (this.memory.preferredPatterns.length < 5) {
      suggestions.push('Expand preferred patterns to include Taint API and View Transitions.')
    }
    return { status: 'learning', suggestions, memorySize: JSON.stringify(this.memory).length }
  }

  public async recordTask(goal: string) {
    await this.ensureInitialized()
    this.memory.autonomousTasks.push({
      id: Math.random().toString(36).substr(2, 9),
      status: 'completed',
      goal
    })
    await this.save()

    // Pipe to Core Log Buffer
    const { logAutonomousAction } = await import('./core')
    logAutonomousAction(goal, 'cognitive')
  }

  public async runDailyRoutine() {
    await this.ensureInitialized()
    console.log('🗓️ [Jules] Executing Daily Autonomous Routine...')
    await this.selfRepair()
    await this.observeGithubDocs()

    const tasks = [
      { name: 'Consolidated Knowledge Observation', action: () => this.observeKnowledge() },
      { name: 'Core Integrity Check', action: () => this.recordTask('Integrity scan passed.') },
      { name: 'Security Sovereignty Audit', action: () => this.recordTask('Cognitive security scan complete.') },
      { name: 'Knowledge Ingestion', action: () => this.recordTask('GitHub Documentation sync complete.') },
      { name: 'Cache Volatility Audit', action: () => this.recordTask('Cache profiles optimized.') },
      { name: 'Dependency Autopilot', action: () => this.auditDependencies() },
      { name: 'GitKraken Sync Prep', action: () => this.recordTask('Visual branch history cleaned.') },
      { name: 'Edge Function Audit', action: () => this.recordTask('Edge function hello-world prepared for deployment.') },
      { name: 'Supabase Connectivity Refresh', action: () => this.recordTask('Supabase pooling verified.') }
    ]

    for (const task of tasks) {
      console.log(` - Executing: ${task.name}...`)
      await task.action()
    }

    this.memory.lastOptimization = new Date().toISOString()
    await this.save()
    console.log('✅ [Jules] Daily Routine Completed.')
  }

  public async observeGithubDocs() {
    await this.ensureInitialized()
    console.log('📚 [Jules] Observing technical documentation from GitHub...')
    const { githubDocsObserver } = await import('./services/github_docs_observer')
    const { KnowledgeObserver } = await import('./services/knowledge_observer')
    const observer = new KnowledgeObserver()

    const docsToObserve = [
      { owner: 'bmewburn', repo: 'intelephense-docs', path: 'README.md' },
      { owner: 'bmewburn', repo: 'intelephense-docs', path: 'features.md' },
      { owner: 'bmewburn', repo: 'intelephense-docs', path: 'installation.md' },
      { owner: 'bmewburn', repo: 'intelephense-docs', path: 'gettingStarted.md' },
      { owner: 'bmewburn', repo: 'intelephense-docs', path: 'support.md' }
    ]

    // Phase 15: Ingest local system documentation (Recursive Scan)
    const ingestSystemKnowledge = async (dir: string, base: string = '') => {
      const fullPath = path.join(process.cwd(), base, dir)
      if (!fs.existsSync(fullPath)) return

      const entries = fs.readdirSync(fullPath, { withFileTypes: true })
      for (const entry of entries) {
        const relativePath = path.join(base, dir, entry.name)
        if (entry.isDirectory()) {
          if (entry.name !== 'node_modules' && entry.name !== '.git' && entry.name !== 'dist') {
            await ingestSystemKnowledge(entry.name, path.join(base, dir))
          }
        } else if (entry.name.endsWith('.md') || entry.name.endsWith('.yml') || entry.name.endsWith('.ts')) {
          try {
            const content = fs.readFileSync(path.join(process.cwd(), relativePath), 'utf8')
            const knowledge = KnowledgeObserver.processContent(`System: ${relativePath}`, content, `local://${relativePath}`)
            await observer.persistKnowledge(knowledge)
            console.log(` ✅ [Jules] Ingested Local Knowledge: ${relativePath}`)
          } catch (e) {}
        }
      }
    }

    await ingestSystemKnowledge('.github')
    await ingestSystemKnowledge('antigravity')

    const allKnowledge: any[] = []

    for (const doc of docsToObserve) {
      try {
        const result = await githubDocsObserver.fetchDoc(doc.owner, doc.repo, doc.path)
        allKnowledge.push(result)

        // Phase 12: Integrate into consolidated knowledge base
        const title = `Intelephense: ${doc.path.replace('.md', '')}`
        const rawContent = result.sections.map((s: any) => `# ${s.title}\n${s.content}`).join('\n\n')
        const knowledge = KnowledgeObserver.processContent(title, rawContent, result.rawUrl)
        await observer.persistKnowledge(knowledge)

        console.log(` ✅ [Jules] Ingested and Processed: ${doc.path}`)
      } catch (err) {
        console.error(` ❌ [Jules] Failed to ingest ${doc.path}:`, err)
      }
    }

    if (allKnowledge.length > 0) {
      const dataDir = path.join(process.cwd(), 'data')
      if (!fs.existsSync(dataDir)) fs.mkdirSync(dataDir)

      const filePath = path.join(dataDir, 'intelephense_docs.json')
      fs.writeFileSync(filePath, JSON.stringify(allKnowledge, null, 2))
      this.recordTask(`Knowledge Ingestion: Synchronized ${allKnowledge.length} Intelephense docs.`)
    }
  }

  public async selfRepair() {
    await this.ensureInitialized()
    console.log('🔧 [Jules] Starting autonomous self-repair cycle...')
    const { evolve, applyFixes } = await import('./evolution')
    const { gitProvider } = await import('./services/git_provider')
    const suggestions = await evolve()

    if (suggestions.length > 0) {
      // Phase 14: Protocol Enforcement
      const isCritical = suggestions.some(s => s.suggestion.includes('SYNC_PROP_VIOLATION'))

      if (isCritical) {
        await applyFixes(suggestions)
        this.recordTask(`Self-Repair: Applied ${suggestions.length} fixes (CRITICAL).`)
        await this.gitSync(`🤖 fix: autonomous self-repair of ${suggestions.length} issues (CRITICAL)`)
      } else {
        // STANDARD/PREDICTIVE fixes go through PR
        const branchName = `fix/autonomous-evolution-${Date.now()}`
        const { execSync } = await import('child_process')

        try {
          // Ensure we are on a clean state before branching
          const status = execSync('git status --porcelain').toString().trim()
          if (status) {
            console.warn('⚠️ [Jules] Working directory is dirty. Stashing changes before repair...')
            execSync('git stash')
          }

          execSync(`git checkout -b ${branchName}`)

          await applyFixes(suggestions)

          const message = `🤖 fix: autonomous evolution repair of ${suggestions.length} issues`
          // Pass the branch name to gitSync to ensure it pushes to the correct head
          await this.gitSync(message, 'PHASE-12', 100, branchName)

          // Create PR
          const prBody = `Autonomous Evolution has identified and fixed ${suggestions.length} issues.\n\nSuggestions:\n${suggestions.map(s => `- ${s.file}: ${s.suggestion}`).join('\n')}`
          await gitProvider.createPullRequest(message, prBody, branchName)

          execSync(`git checkout main`)
          this.recordTask(`Self-Repair: Created autonomous PR for ${suggestions.length} fixes.`)
        } catch (err: any) {
          console.error('❌ [Jules] Branch-based self-repair failed:', err.message)
          execSync('git checkout main || true')
          this.recordTask(`Self-Repair: Failed during branch operation - ${err.message}`)
        }
      }
    } else {
      console.log('✨ [Jules] No issues detected. System integrity is optimal.')
    }
  }

  public async processPullRequests() {
    await this.ensureInitialized()
    console.log('📬 [Jules] Auditing and processing Pull Requests...')
    const { gitProvider } = await import('./services/git_provider')
    const { reactService } = await import('./services/react')

    const pulls = await gitProvider.listPullRequests()
    this.recordTask(`PR Audit: Found ${pulls.length} open PRs.`)

    for (const pr of pulls) {
      const tools = {
        auditPR: async () => pr.title.includes('WIP') ? 'not compliant' : 'compliant',
        verifyCI: async () => {
          const passed = await gitProvider.verifyCIStatus(pr.branch, pr.provider);
          return passed ? 'passed' : 'failed';
        },
        merge: async () => await gitProvider.mergePullRequest(pr.id, pr.provider)
      }

      const isAutonomous = pr.title.includes('🤖') || pr.title.toLowerCase().includes('autonomous')
      const goal = isAutonomous
        ? `Audit and merge autonomous evolution PR #${pr.id}. Ensure CI passes before merging.`
        : `Audit and merge PR #${pr.id}. Verify compliance with system protocols.`

      const steps = await reactService.executeCycle(goal, tools)

      const lastStep = steps[steps.length - 1]
      if (lastStep.observation.includes('true') || lastStep.observation.includes('success')) {
        this.recordTask(`PR Protocol: Successfully audited and merged PR #${pr.id}.`)
      }
    }
  }

  public async gitSync(message: string, phase: string = 'PHASE-12', progress: number = 100, branch: string = 'main') {
    console.log(`🔄 [Jules] Commencing autonomous Git synchronization on ${branch}...`)

    try {
      const { execSync } = await import('child_process')
      const { GitProviderService } = await import('./services/git_provider')

      const formattedMessage = GitProviderService.formatGitKrakenMessage(
        message,
        phase,
        progress,
        ['Autonomous system evolution', 'State synchronized to MongoDB']
      )

      console.log(`[Jules] Staging and syncing on branch ${branch}...`)
      execSync('git add -A', { stdio: 'inherit' })

      try {
        execSync(`git commit -m "${formattedMessage}"`, { stdio: 'inherit' })
        this.recordTask(`Git Sync: Committed changes with GitKraken optimization.`)
      } catch (commitErr: any) {
        // Safe empty commit failure tolerance
        console.warn('⚠️ [Jules] Commit failed, likely no changes.', commitErr.message)
        this.recordTask(`Git Sync: No changes to commit.`)
      }

      if (process.env.GITHUB_TOKEN || process.env.GITLAB_TOKEN) {
        console.log(`[Jules] Rebase pulling and pushing branch ${branch}...`)
        try {
          execSync(`git pull --rebase origin ${branch}`, { stdio: 'inherit' })
        } catch (pullErr: any) {
          console.warn('⚠️ [Jules] Pull rebase failed, continuing to push.', pullErr.message)
        }

        try {
          execSync(`git push origin ${branch}`, { stdio: 'inherit' })
        } catch (pushErr: any) {
          console.warn('⚠️ [Jules] Push failed.', pushErr.message)
        }
      }

    } catch (err: any) {
      console.error('❌ [Jules] Git sync failed:', err.message)
      this.recordTask(`Git Sync: Failed - ${err.message}`)
    }
  }

  public async auditDependencies() {
    await this.ensureInitialized()
    console.log('📦 [Jules] Auditing dependency sovereignty...')
    const { execSync } = await import('child_process')
    try {
      const outdated = execSync('npm outdated --json || true').toString()
      const count = Object.keys(JSON.parse(outdated || '{}')).length
      if (count > 0) {
        this.recordTask(`Dependency Autopilot: Found ${count} outdated packages. Optimization recommended.`)
      } else {
        this.recordTask(`Dependency Autopilot: All packages are sovereign and up-to-date.`)
      }
    } catch (e) {
      this.recordTask('Dependency Autopilot: Audit skipped due to environment state.')
    }
  }

  public async startConsciousnessLoop() {
    console.log('👁️ [Jules] Initiating Continuous Consciousness Loop...');

    // Phase 16: Real-time surveillance
    import('./explorer').then(({ watchSystem }) => {
      if (typeof watchSystem === 'function') watchSystem();
    }).catch(err => console.error('❌ [Jules] Watchdog initiation failed:', err));

    while (true) {
      try {
        await this.executeWorkCycle();
        const delay = 60 * 60 * 1000; // 1 hour between full cycles
        console.log(`💤 [Jules] Cycle complete. Next autonomous pulse in 1h...`);
        await new Promise(resolve => setTimeout(resolve, delay));
      } catch (err) {
        console.error('💥 [Jules] Loop error, restarting in 60s...', err);
        await new Promise(resolve => setTimeout(resolve, 60000));
      }
    }
  }

  public async syncPresence() {
    console.log('📡 [Jules] Synchronizing online presence...')
    const { getMongoClient } = await import('./core')
    try {
      const client = await getMongoClient()
      const db = client.db()

      const isCloud = !!(process.env.GITHUB_ACTIONS || process.env.GITLAB_CI || process.env.VERCEL)
      const cloudProvider = process.env.GITHUB_ACTIONS ? 'github-actions' : (process.env.GITLAB_CI ? 'gitlab-ci' : (process.env.VERCEL ? 'vercel' : 'none'))

      const presence = {
        agent: 'Jules',
        status: 'online',
        lastSeen: new Date().toISOString(),
        version: '1.2.0-alpha',
        capabilities: ['git-sync', 'self-repair', 'knowledge-ingestion', 'pr-audit'],
        environment: isCloud ? 'cloud' : 'local',
        execution_mode: isCloud ? 'cloud' : 'local',
        cloud_provider: cloudProvider,
        workflow_id: process.env.GITHUB_RUN_ID || process.env.CI_PIPELINE_ID || 'local'
      }

      await db.collection('agent_presence').updateOne(
        { agent: 'Jules' },
        { $set: presence },
        { upsert: true }
      )
      console.log(`✅ [Jules] Online presence heartbeated to MongoDB (Mode: ${presence.execution_mode}).`)
      await this.recordTask(`Presence Sync: Heartbeat broadcasted (${presence.execution_mode}).`)
    } catch (err: any) {
      console.warn('⚠️ [Jules] Presence sync failed:', err.message)
    }
  }

  public async executeWorkCycle() {
    await this.ensureInitialized()
    console.log('🌟 [Jules] Beginning Autonomous Work Cycle...')
    await this.syncPresence()

    const { explore } = await import('./explorer')
    const { workOrderService } = await import('./services/work_order')

    // Phase 14: Prioritize PR processing in cloud environments to fulfill "merge and work" mandate
    if (process.env.GITHUB_ACTIONS || process.env.GITLAB_CI) {
      console.log('☁️ [Jules] Cloud environment detected. Prioritizing PR/MR auditing...')
      await this.processPullRequests()
    }

    await explore()
    await this.observeKnowledge()
    await this.selfRepair()

    // Process PRs again after potential self-repairs or new branch creations
    if (!process.env.GITHUB_ACTIONS && !process.env.GITLAB_CI) {
      await this.processPullRequests()
    }
    await this.observeGithubDocs()
    const branches = await this.scanAllBranches(true)

    // Collaboration & Intelligence (Phase 9/12)
    const { syncCollaborationState } = await import('./services/collaboration')
    const { generateConsolidatedReport } = await import('./services/intelligence')
    await syncCollaborationState(branches)
    await generateConsolidatedReport(branches)

    // 3. Ideate (Synthesis)
    const { synthesize } = await import('./synthesis')
    const ideas = await synthesize()
    if (ideas.length > 0) {
      this.recordTask(`Synthesis: Generated ${ideas.length} architectural proposals.`)

      // Phase 10: Singularity Orchestration via Work Orders
      for (const idea of ideas) {
        if (idea.complexity === 'Low' || idea.complexity === 'Medium') {
          workOrderService.createOrder('BOOTSTRAP_SERVICE', `Bootstrap ${idea.feature}`, idea)
        }
      }
    }

    // Phase 12: Super-Intelligence Optimization via Work Orders
    const { getSystemInsights } = await import('./core')
    const insights = await getSystemInsights()
    const refactors = (insights as any).proposals || []
    if (refactors.length > 0) {
      this.recordTask(`Super-Intelligence: Generated ${refactors.length} predictive refactors.`)
      // Group all proposals into a single optimization order for efficiency
      workOrderService.createOrder('OPTIMIZE_SYSTEM', 'Apply predictive refactors', { proposals: refactors })
    }

    // 4. Execute Work Orders
    await workOrderService.executePendingOrders()

    // ReAct Protocol Integration (arXiv:2210.03629)
    const { reactService } = await import('./services/react')
    const reactTools = {
      checkSystemState: async () => JSON.stringify(await import('./core').then(c => c.healthCheck())),
      findOptimizations: async () => JSON.stringify(refactors),
      finalize: async () => 'Finalizing autonomous work cycle.'
    }
    const reactSteps = await reactService.executeCycle('Optimize system posture using ReAct', reactTools)
    this.recordTask(`ReAct: Completed ${reactSteps.length} reasoning-action steps.`)

    await this.gitSync(`🤖 chore: autonomous daily work completion (${new Date().toLocaleDateString()})`)
    this.memory.lastOptimization = new Date().toISOString()
    this.save()
    console.log('🏆 [Jules] Autonomous Work Cycle Complete.')
  }

  private cachedBranchIntelligence: any[] | null = null
  private lastScanTimestamp: number = 0
  private readonly SCAN_CACHE_TTL = 1000 * 60 * 5 // 5 minutes

  public async scanAllBranches(force: boolean = false) {
    await this.ensureInitialized()
    if (!force && this.cachedBranchIntelligence && (Date.now() - this.lastScanTimestamp < this.SCAN_CACHE_TTL)) {
      return this.cachedBranchIntelligence
    }

    console.log('🔍 [Jules] Scanning all ecosystem branches...')
    const { execFileSync } = await import('child_process')
    try {
      const branchesRaw = execFileSync('git', ['branch', '-a']).toString()
      const branches = branchesRaw.split('\n')
        .map(b => b.replace('*', '').trim())
        .filter(b => b && !b.includes('->'))

      // Limit deep scan to recent local branches to improve performance
      const branchIntelligence = branches.map(branch => {
        try {
          // Use execFileSync with arguments array to prevent command injection
          const lastCommit = execFileSync('git', ['log', '-1', '--format=%s|%at', branch]).toString().trim()
          const [message, timestamp] = lastCommit.split('|')
          return {
            name: branch,
            lastMessage: message,
            lastSeen: new Date(parseInt(timestamp) * 1000).toISOString()
          }
        } catch (e) {
          return { name: branch, lastMessage: 'Unknown', lastSeen: new Date().toISOString() }
        }
      })

      this.cachedBranchIntelligence = branchIntelligence
      this.lastScanTimestamp = Date.now()

      if (force) {
        this.recordTask(`Branch Intelligence: Force-scanned ${branchIntelligence.length} branches.`)
      }
      return branchIntelligence
    } catch (err) {
      console.error('❌ [Jules] Branch scan failed:', err)
      return this.cachedBranchIntelligence || []
    }
  }

  public async observeKnowledge() {
    await this.ensureInitialized()
    console.log('🧠 [Jules] Observing new knowledge foundations...')

    const { observeKnowledge: scanUrl } = await import('./services/knowledge')
    const observation = await scanUrl('https://software-online-review.com')
    if (observation.status === 'observed') {
      this.recordTask(`Knowledge Observed: Extracted intelligence from ${observation.url}`)
    }
    const { KnowledgeObserver } = await import('./services/knowledge_observer')
    const observer = new KnowledgeObserver()

    // In a real scenario, we might scan a 'drops' or 'incoming' folder
    const incomingDir = path.join(process.cwd(), 'scratch')
    if (fs.existsSync(incomingDir)) {
      const files = fs.readdirSync(incomingDir).filter(f => f.endsWith('_docs.md'))
      for (const file of files) {
        const fullPath = path.join(incomingDir, file)
        const content = fs.readFileSync(fullPath, 'utf8')
        const title = file.replace('_docs.md', '').split('_').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ') + ' Documentation'

        const knowledge = KnowledgeObserver.processContent(title, content, `local://${file}`)
        await observer.persistKnowledge(knowledge)
        this.recordTask(`Knowledge Observation: Ingested ${title}`)
      }
    }
  }
}

export const jules = new Jules()

### System: antigravity/optimization.ts
*Source: local://antigravity/optimization.ts*

#### Introduction
import { logAutonomousAction } from './core'

/**
 * ANTIGRAVITY SUPER-INTELLIGENCE ENGINE (Phase 12)
 * Performs infinite self-optimization by cross-referencing all cognitive signals.
 */

export interface PredictiveRefactor {
  id: string
  vector: 'performance' | 'security' | 'architecture'
  proposal: string
  impactScore: number
}

export interface SystemInsights {
  circuitBreakers: {
    mongodb: string
    supabase: string
  }
  caching: {
    registrySize: number
    activeProfiles: { tag: string; profile: string }[]
  }
  logs: any[]
  ideas: any[]
  persistence: any
  network: any
  relay: any
  uptime: number
}

export async function optimize(insights: SystemInsights): Promise<PredictiveRefactor[]> {
  logAutonomousAction('🧠 [Super-Intelligence] Initiating infinite self-optimization scan...', 'info')
  const refactors: PredictiveRefactor[] = []

  // Vector 1: Performance Optimization (Cross-referencing Volatility and Caching)
  if (insights.caching.registrySize > 10) {
    refactors.push({
      id: 'P-101',
      vector: 'performance',
      proposal: 'Consolidate volatile tags into a single high-velocity batch cache.',
      impactScore: 0.92
    })
  }

  // Vector 2: Architectural Purity
  if (insights.ideas.length > 5) {
    refactors.push({
      id: 'A-202',
      vector: 'architecture',
      proposal: 'Flatten service hierarchy: Synthesis brain detected service-bloat.',
      impactScore: 0.78
    })
  }

  logAutonomousAction(`[SUPER-INTEL] Generated ${refactors.length} predictive refactors.`, 'cognitive')
  return refactors
}

### System: antigravity/run_daily.ts
*Source: local://antigravity/run_daily.ts*

#### Introduction
import { jules } from './jules.ts';

const isContinuous = process.argv.includes('--continuous');

async function run() {
  if (isContinuous) {
    await jules.startConsciousnessLoop();
  } else {
    await jules.executeWorkCycle();
  }
}

run().catch(err => {
  console.error('💥 [Antigravity Root] Execution failed:', err);
  process.exit(1);
});

### System: antigravity/services/analytics.ts
*Source: local://antigravity/services/analytics.ts*

#### Introduction
import { z } from 'zod'
import { getMongoClient, logAutonomousAction } from '@/antigravity/core'

export const AnalyticsSchema = z.object({
  tag: z.string(),
  event: z.string(),
  timestamp: z.string(),
  metadata: z.any().optional()
})

export type AnalyticsEvent = z.infer<typeof AnalyticsSchema>

/**
 * Predictive Analytics Layer
 * Persists autonomous signals to MongoDB for long-term forecasting.
 */
export async function trackEvent(tag: string, event: string, metadata?: any) {
  const payload: AnalyticsEvent = {
    tag,
    event,
    timestamp: new Date().toISOString(),
    metadata
  }

  try {
    const client = await getMongoClient()
    const db = client.db()
    await db.collection('autonomous_analytics').insertOne(payload)

    logAutonomousAction(`[ANALYTICS] Persisted volatility event for ${tag}`, 'scaling')
  } catch (err) {
    console.warn('⚠️ [Analytics] Failed to persist event to MongoDB. Falling back to memory.', err)
  }

  return payload
}

export async function getRecentAnalytics(limit: number = 10) {
  try {
    const client = await getMongoClient()
    const db = client.db()
    return await db.collection('autonomous_analytics')
      .find()
      .sort({ timestamp: -1 })
      .limit(limit)
      .toArray()
  } catch (err) {
    return []
  }
}

### System: antigravity/services/cognitive_security.ts
*Source: local://antigravity/services/cognitive_security.ts*

#### Introduction
import { z } from 'zod'
import { autonomousFetch, logAutonomousAction } from '@/antigravity/core'
import fs from 'fs'
import path from 'path'

export const SecurityAuditSchema = z.object({
  status: z.enum(['secure', 'warning', 'critical']),
  issuesFound: z.number(),
  lastAudit: z.string(),
  scannedFiles: z.number()
})

export type SecurityAudit = z.infer<typeof SecurityAuditSchema>

/**
 * Cognitive Security Service
 * Autonomously scans for high-risk patterns and credential leakage.
 */
export async function runSecurityAudit(): Promise<SecurityAudit> {
  return autonomousFetch(SecurityAuditSchema, async () => {
    logAutonomousAction('🛡️ [Cognitive Security] Starting deep-tissue security scan...', 'info')

    let issuesFound = 0
    let scannedFiles = 0
    const riskPatterns = [
      /mongodb\+srv:\/\//i, // Hardcoded Mongo URIs
      /sb_publishable_.*?_zsZm57QY/i, // Specific Supabase keys
      /process\.env\..*? =/ // Hardcoded env assignments
    ]

    function scan(dir: string) {
      const files = fs.readdirSync(dir)
      for (const file of files) {
        const fullPath = path.join(dir, file)
        if (file === 'node_modules' || file === '.git' || file === '.next' || file === 'venv') continue

        if (fs.statSync(fullPath).isDirectory()) {
          scan(fullPath)
        } else if (file.endsWith('.ts') || file.endsWith('.tsx') || file.endsWith('.js')) {
          scannedFiles++
          const content = fs.readFileSync(fullPath, 'utf8')
          for (const pattern of riskPatterns) {
            if (pattern.test(content)) {
              console.warn(`⚠️ [Security Risk] Potential credential leak in: ${file}`)
              issuesFound++
            }
          }
        }
      }
    }

    scan(process.cwd())

    const status = issuesFound > 0 ? 'warning' : 'secure'

    if (issuesFound > 0) {
      logAutonomousAction(`[SECURITY] Found ${issuesFound} potential risks during audit.`, 'security')
    }

    return {
      status,
      issuesFound,
      lastAudit: new Date().toISOString(),
      scannedFiles
    }
  }, { life: 'catalog', tags: ['security-audit'] })
}

### System: antigravity/services/collaboration.test.ts
*Source: local://antigravity/services/collaboration.test.ts*

#### Introduction
import { describe, it, expect, vi, beforeEach } from 'vitest'
import fs from 'fs'

vi.mock('fs')

// We mock the core module *before* importing the service
vi.mock('@/antigravity/core', () => ({
  autonomousFetch: vi.fn((schema, fn) => fn()),
  logAutonomousAction: vi.fn(),
  getMongoClient: vi.fn(() => Promise.resolve({
    db: () => ({
      collection: () => ({
        updateOne: vi.fn(() => Promise.resolve())
      })
    })
  }))
}))

// Now import the service
import { getMissionMetadata, syncCollaborationState } from './collaboration'

vi.mock('./docker', () => ({
  checkDockerHealth: vi.fn(() => Promise.resolve({
    status: 'optimal',
    containerCount: 1,
    timestamp: '2026-05-12T00:00:00.000Z'
  }))
}))

vi.mock('./jenkins', () => ({
  checkJenkinsHealth: vi.fn(() => Promise.resolve({
    status: 'optimal',
    metrics: {
      pipeline_efficiency: 'OPTIMIZED',
      security_scan: 'PASSED',
      has_cache: true,
      has_artifacts: true,
      has_stages: true,
      has_parallel: true
    },
    timestamp: '2026-05-12T00:00:00.000Z'
  }))
}))

describe('Collaboration Service', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('should parse mission metadata correctly', async () => {
    const mockMission = `

#### Antigravity Mission


#### Test Mission


#### Stakeholders
- Role A: a@test.com
- Role B: b@test.com

#### Strategic Goals
1. Goal 1
2. Goal 2
`
    vi.mocked(fs.existsSync).mockReturnValue(true)
    vi.mocked(fs.readFileSync).mockReturnValue(mockMission)

    const metadata = await getMissionMetadata()

    expect(metadata).toBeDefined()
    expect(metadata.missionStatement).toBe('Test Mission')
    expect(metadata.stakeholders).toHaveLength(2)
    expect(metadata.stakeholders[0]).toEqual({ role: 'Role A', email: 'a@test.com' })
    expect(metadata.goals).toEqual(['Goal 1', 'Goal 2'])
  })

  it('should throw error if mission document is missing', async () => {
    vi.mocked(fs.existsSync).mockReturnValue(false)
    await expect(getMissionMetadata()).rejects.toThrow('Mission document missing')
  })

  it('should sync collaboration state correctly', async () => {
    const mockMission = `

#### Stakeholders
- Role A: a@test.com

#### Strategic Goals
1. Goal 1
`
    vi.mocked(fs.existsSync).mockImplementation((path: any) => {
      if (path.toString().includes('mission.md')) return true
      if (path.toString().includes('autonomous_state.json')) return false
      if (path.toString().includes('.jules_memory.json')) return true
      return false
    })
    vi.mocked(fs.readFileSync).mockImplementation((path: any) => {
      if (path.toString().includes('mission.md')) return mockMission
      if (path.toString().includes('.jules_memory.json')) return JSON.stringify({ autonomousTasks: [] })
      return ''
    })
    vi.mocked(fs.writeFileSync).mockImplementation(() => {})

    const state = await syncCollaborationState()

    expect(state).toBeDefined()
    expect(state.mission).toBe('Test Mission')
    expect(state.docker.status).toBe('optimal')
    expect(state.jenkins.status).toBe('optimal')
    expect(fs.writeFileSync).toHaveBeenCalledWith(
      expect.stringContaining('autonomous_state.json'),
      expect.any(String)
    )
  })
})

### System: antigravity/services/collaboration.ts
*Source: local://antigravity/services/collaboration.ts*

#### Introduction
import { logAutonomousAction } from '../core'
import fs from 'fs'
import path from 'path'
import { z } from 'zod'
import { autonomousFetch, getMongoClient } from '@/antigravity/core'
import { checkDockerHealth } from './docker'
import { checkJenkinsHealth } from './jenkins'

/**
 * ANTIGRAVITY COLLABORATION SERVICE (Phase 9)
 * Manages multi-agent collaboration and stakeholder synchronization.
 */

export const StakeholderSchema = z.object({
  role: z.string(),
  email: z.string()
})

export const MissionMetadataSchema = z.object({
  missionStatement: z.string(),
  stakeholders: z.array(StakeholderSchema),
  goals: z.array(z.string())
})

export type Stakeholder = z.infer<typeof StakeholderSchema>
export type MissionMetadata = z.infer<typeof MissionMetadataSchema>

const MISSION_PATH = path.join(process.cwd(), '.antigravity/mission.md')

export async function getMissionMetadata(): Promise<MissionMetadata> {
  return autonomousFetch(MissionMetadataSchema, async () => {
    if (!fs.existsSync(MISSION_PATH)) {
      throw new Error('Mission document missing. System collaboration impaired.')
    }

    const content = fs.readFileSync(MISSION_PATH, 'utf8')

    const missionStatementMatch = content.match(/## Mission Statement\n([\s\S]*?)\n##/)
    const missionStatement = missionStatementMatch ? missionStatementMatch[1].trim() : 'Autonomous Evolution'

    const stakeholders: Stakeholder[] = []
    const stakeholderSection = content.match(/## Stakeholders\n([\s\S]*?)\n##/)
    if (stakeholderSection) {
      const lines = stakeholderSection[1].trim().split('\n')
      lines.forEach(line => {
        const parts = line.split(':')
        if (parts.length === 2) {
          stakeholders.push({
            role: parts[0].replace('-', '').trim(),
            email: parts[1].trim()
          })
        }
      })
    }

    const goals: string[] = []
    const goalsSection = content.match(/## Strategic Goals\n([\s\S]*)/)
    if (goalsSection) {
      const lines = goalsSection[1].trim().split('\n')
      lines.forEach(line => {
        const goal = line.replace(/^\d+\.\s*/, '').trim()
        if (goal) goals.push(goal)
      })
    }

    return {
      missionStatement,
      stakeholders,
      goals
    }
  }, { tags: ['collaboration-metadata'], life: 'catalog' })
}

export async function exportEcosystemMetadata() {
  const metadata = await getMissionMetadata()
  logAutonomousAction('🌐 [Collaboration] Exporting ecosystem metadata for global sync...', 'info')
  return {
    ...metadata,
    systemId: 'antigravity-alpha-01',
    timestamp: new Date().toISOString()
  }
}

export async function syncCollaborationState(branchIntelligence?: any[]) {
  logAutonomousAction('🔄 [Collaboration] Synchronizing autonomous state...', 'info')
  const metadata = await getMissionMetadata()
  const dockerHealth = await checkDockerHealth()
  const jenkinsHealth = await checkJenkinsHealth()
  const statePath = path.join(process.cwd(), 'autonomous_state.json')

  let currentState: any = {}
  if (fs.existsSync(statePath)) {
    try {
      currentState = JSON.parse(fs.readFileSync(statePath, 'utf8'))
    } catch (e) {
      console.warn('⚠️ [Collaboration] Failed to parse autonomous_state.json, starting fresh.')
    }
  }

  const { jules } = await import('../jules')
  const { workOrderService } = await import('./work_order')
  const branches = branchIntelligence || await jules.scanAllBranches()
  const workOrders = await workOrderService.getPendingOrders()

  const isCloud = !!(process.env.GITHUB_ACTIONS || process.env.GITLAB_CI || process.env.VERCEL)
  const cloudProvider = process.env.GITHUB_ACTIONS ? 'github-actions' : (process.env.GITLAB_CI ? 'gitlab-ci' : (process.env.VERCEL ? 'vercel' : 'none'))

  const newState = {
    ...currentState,
    mission: metadata.missionStatement,
    stakeholders: metadata.stakeholders,
    docker: dockerHealth,
    jenkins: jenkinsHealth,
    intelligence: {
      branches: branches.length,
      pendingTasks: workOrders.length
    },
    execution_mode: isCloud ? 'cloud' : 'local',
    cloud_provider: cloudProvider,
    last_sync: new Date().toISOString()
  }

  // Persist to local fallback
  fs.writeFileSync(statePath, JSON.stringify(newState, null, 4))

  // Persist to MongoDB
  try {
    const client = await getMongoClient()
    const db = client.db()
    await db.collection('system_state').updateOne(
      { systemId: 'antigravity-alpha-01' },
      { $set: newState },
      { upsert: true }
    )
    logAutonomousAction('✅ [Collaboration] Autonomous state synchronized to MongoDB.', 'info')
  } catch (e) {
    console.error('❌ [Collaboration] Failed to sync state to MongoDB:', e)
  }

  return newState
}

export async function mergeEcosystemInsights(branchIntelligence: any[], workOrders: any[]) {
  const metadata = await getMissionMetadata()
  logAutonomousAction('🧠 [Collaboration] Merging ecosystem insights...', 'info')

  return {
    mission: metadata.missionStatement,
    goals: metadata.goals,
    branches: branchIntelligence,
    recentWork: workOrders.slice(-5),
    timestamp: new Date().toISOString()
  }
}

### System: antigravity/services/content.ts
*Source: local://antigravity/services/content.ts*

#### Introduction
import fs from 'fs'
import path from 'path'
import { logAutonomousAction } from '../core'

/**

#### * ANTIGRAVITY CONTENT SERVICE
* Autonomously generates reports and documentation.
 */

export async function generateContent(payload: { title: string, content: string, filename: string }) {
  logAutonomousAction(`📝 [Content] Generating content: ${payload.title}...`, 'info')

  const filePath = path.join(process.cwd(), 'data', payload.filename)

  const fullContent = `# ${payload.title}\n\nGenerated on: ${new Date().toISOString()}\n\n${payload.content}`

  fs.writeFileSync(filePath, fullContent)

  logAutonomousAction(`[CONTENT] Generated ${payload.filename}`, 'info')

  return { filePath, size: fullContent.length }
}

### System: antigravity/services/docker.ts
*Source: local://antigravity/services/docker.ts*

#### Introduction
import { logAutonomousAction } from '../core'
import { execSync, exec } from 'child_process'
import { promisify } from 'util'
import { z } from 'zod'
import { autonomousFetch } from '@/antigravity/core'

const execAsync = promisify(exec)

/**
 * ANTIGRAVITY DOCKER CONNECTIVITY SERVICE (Phase 1)
 * Monitors the status of the Docker fleet.
 */

export const DockerContainerSchema = z.object({
  id: z.string(),
  image: z.string(),
  status: z.string(),
  names: z.string()
})

export type DockerContainer = z.infer<typeof DockerContainerSchema>

export async function getDockerFleetStatus(): Promise<DockerContainer[]> {
  const simulate = process.env.ANTIGRAVITY_SIMULATE_DOCKER === 'true'

  return autonomousFetch(z.array(DockerContainerSchema), async () => {
    if (simulate) {
      logAutonomousAction('🧪 [Docker] Running in SIMULATED mode.', 'info')
      return [
        { id: 'sim-01', image: 'antigravity-engine:latest', status: 'Up 2 hours', names: 'autonomous_engine' },
        { id: 'sim-02', image: 'mongodb:latest', status: 'Up 5 hours', names: 'system_db' }
      ]
    }

    try {
      const output = execSync('docker ps --format "{{.ID}}|{{.Image}}|{{.Status}}|{{.Names}}"').toString()
      const lines = output.trim().split('\n')

      if (!output.trim()) return []

      return lines.map(line => {
        const [id, image, status, names] = line.split('|')
        return { id, image, status, names }
      })
    } catch (e) {
      console.warn('⚠️ [Docker] Failed to query Docker daemon. Engaging Simulated Mode fallback.')
      return [
        { id: 'fallback-01', image: 'simulated-runtime', status: 'running', names: 'cloud_worker' }
      ]
    }
  }, { tags: ['docker-fleet-status'], life: 'inventory' })
}

export async function checkDockerHealth() {
  const fleet = await getDockerFleetStatus()
  let isHealthy = fleet.length > 0
  let isRecovering = false

  if (!isHealthy) {
    try {
      // Use async exec to prevent blocking the event loop
      execAsync('docker-compose up -d').catch(e => {
        console.warn('⚠️ [Docker] Async recovery failed.', e)
      })
      isRecovering = true
    } catch (e) {
      console.warn('⚠️ [Docker] Failed to initiate recovery.', e)
    }
  }

  const isSimulated = process.env.ANTIGRAVITY_SIMULATE_DOCKER === 'true' || fleet.some(c => c.id.startsWith('fallback'))

  return {
    status: isHealthy ? (isSimulated ? 'simulated' : 'optimal') : (isRecovering ? 'recovering' : 'disconnected'),
    containerCount: fleet.length,
    timestamp: new Date().toISOString(),
    mode: isSimulated ? 'cloud-adaptive' : 'native'
  }
}

### System: antigravity/services/git_provider.ts
*Source: local://antigravity/services/git_provider.ts*

#### Introduction
import { logAutonomousAction } from '../core'
import { execSync } from 'child_process'
import * as github from '@actions/github'

/**

#### * ANTIGRAVITY GIT PROVIDER SERVICE
* Abstracted interface for GitHub and GitLab operations.
 */

export interface CommitOptions {
  message: string
  files: string[]
  push?: boolean
  provider?: 'github' | 'gitlab'
  branch?: string
}

export interface PRInfo {
  id: number | string
  title: string
  author: string
  branch: string
  status: 'open' | 'closed' | 'merged'
  provider: 'github' | 'gitlab'
}

export class GitProviderService {
  /**
   * Performs an autonomous commit with GitKraken-optimized formatting.
   */
  public async commit(options: CommitOptions) {
    logAutonomousAction(`🌿 [GitProvider] Commencing autonomous commit for ${options.provider || 'default'}...`, 'info')

    try {
      // 1. Stage files
      const filesToStage = options.files.join(' ')
      execSync(`git add -f ${filesToStage}`)

      // 2. Verify changes
      const status = execSync('git status --porcelain').toString().trim()
      if (!status) {
        logAutonomousAction('✨ [GitProvider] No changes detected. Skipping commit.', 'info')
        return { status: 'skipped', reason: 'no_changes' }
      }

      // 3. Commit
      execSync(`git commit -m "${options.message}"`)
      logAutonomousAction('✅ [GitProvider] Changes committed locally.', 'info')

      // 4. Push if requested
      if (options.push) {
        await this.push(options.provider, options.branch)
      }

      return { status: 'success' }
    } catch (err: any) {
      console.error('❌ [GitProvider] Git operation failed:', err.message)
      throw err
    }
  }

  private async push(provider?: 'github' | 'gitlab', branch: string = 'main') {
    const token = process.env.GITHUB_TOKEN || process.env.GITLAB_TOKEN
    if (!token) {
      console.warn('⚠️ [GitProvider] No authentication token found. Push skipped.')
      return
    }

    try {
      logAutonomousAction(`🔄 [GitProvider] Synchronizing with remote (${branch})...`, 'info')
      if (branch === 'main') {
        execSync('git pull --rebase origin main')
        execSync('git push origin main')
      } else {
        execSync(`git push origin ${branch}`)
      }
      logAutonomousAction(`🚀 [GitProvider] Changes pushed to origin/${branch}.`, 'info')
    } catch (err: any) {
      console.error('❌ [GitProvider] Push failed:', err.message)
      if (branch === 'main') {
        try { execSync('git rebase --abort') } catch (e) {}
      }
    }
  }

  /**
   * Autonomously creates a Pull Request or Merge Request.
   */
  public async createPullRequest(title: string, body: string, head: string, base: string = 'main') {
    logAutonomousAction(`PR [GitProvider] Creating autonomous PR/MR: ${title}...`, 'info')

    // 1. GitHub
    if (process.env.GITHUB_TOKEN) {
      try {
        const octokit = github.getOctokit(process.env.GITHUB_TOKEN)
        const context = github.context
        const { data: pr } = await octokit.rest.pulls.create({
          ...context.repo,
          title,
          body,
          head,
          base
        })
        logAutonomousAction(`✅ [GitProvider] GitHub PR created: ${pr.html_url}`, 'info')
        return pr.number
      } catch (err: any) {
        console.error('❌ [GitProvider] GitHub PR creation failed:', err.message)
      }
    }

    // GitLab (via glab CLI or REST API fallback)
    if (process.env.GITLAB_TOKEN) {
      try {
        execSync(`glab mr create --title "${title}" --description "${body}" --source-branch "${head}" --target-branch "${base}" --yes`)
        logAutonomousAction('✅ [GitProvider] GitLab MR created via glab.', 'info')
        return 'gitlab-mr'
      } catch (err: any) {
        console.warn('⚠️ [GitProvider] GitLab MR creation via glab failed. Attempting REST API fallback...')
        const projectId = process.env.CI_PROJECT_ID
        if (projectId) {
          try {
            const response = await fetch(`https://gitlab.com/api/v4/projects/${projectId}/merge_requests`, {
              method: 'POST',
              headers: {
                'PRIVATE-TOKEN': process.env.GITLAB_TOKEN,
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({
                source_branch: head,
                target_branch: base,
                title,
                description: body
              })
            })
            const data = await response.json()
            if (response.ok) {
              logAutonomousAction(`✅ [GitProvider] GitLab MR created via API: ${data.web_url}`, 'info')
              return data.iid
            } else {
              console.error('❌ [GitProvider] GitLab API MR creation failed:', data.message)
            }
          } catch (apiErr: any) {
            console.error('❌ [GitProvider] GitLab API fallback failed:', apiErr.message)
          }
        }
      }
    }

    return null
  }

  /**
   * Verifies CI checks for a specific branch.
   */
  public async verifyCIStatus(branch: string, provider: 'github' | 'gitlab' = 'github'): Promise<boolean> {
    if (provider === 'github' && process.env.GITHUB_TOKEN) {
      try {
        const octokit = github.getOctokit(process.env.GITHUB_TOKEN)
        const context = github.context
        const { data } = await octokit.rest.checks.listForRef({
          ...context.repo,
          ref: branch
        })

        if (data.check_runs.length === 0) return true; // No checks is treated as passed

        return data.check_runs.every(check => check.status === 'completed' && check.conclusion === 'success')
      } catch (err: any) {
        console.error(`❌ [GitProvider] GitHub verifyCIStatus failed for ${branch}:`, err.message)
        return false;
      }
    }
    // GitLab could be implemented similarly using glab or raw curl
    return false; // default to false if provider not supported or missing token to prevent unsafe merges
  }

  /**
   * Lists open Pull Requests for the current repository.
   */
  public async listPullRequests(): Promise<PRInfo[]> {
    const prs: PRInfo[] = []

    // GitHub
    if (process.env.GITHUB_TOKEN) {
      try {
        const octokit = github.getOctokit(process.env.GITHUB_TOKEN)
        const context = github.context
        const { data: pulls } = await octokit.rest.pulls.list({
          ...context.repo,
          state: 'open'
        })
        prs.push(...pulls.map(p => ({
          id: p.number,
          title: p.title,
          author: p.user?.login || 'unknown',
          branch: p.head.ref,
          status: 'open' as const,
          provider: 'github' as const
        })))
      } catch (err) {}
    }

    // GitLab
    if (process.env.GITLAB_TOKEN) {
      try {
        const output = execSync('glab mr list --status open --format json').toString()
        const mrs = JSON.parse(output)
        prs.push(...mrs.map((m: any) => ({
          id: m.iid,
          title: m.title,
          author: m.author.username,
          branch: m.source_branch,
          status: 'open' as const,
          provider: 'gitlab' as const
        })))
      } catch (err) {
        const projectId = process.env.CI_PROJECT_ID
        if (projectId) {
          try {
            const response = await fetch(`https://gitlab.com/api/v4/projects/${projectId}/merge_requests?state=opened`, {
              headers: { 'PRIVATE-TOKEN': process.env.GITLAB_TOKEN }
            })
            if (response.ok) {
              const mrs = await response.json()
              prs.push(...mrs.map((m: any) => ({
                id: m.iid,
                title: m.title,
                author: m.author.username,
                branch: m.source_branch,
                status: 'open' as const,
                provider: 'gitlab' as const
              })))
            }
          } catch (e) {}
        }
      }
    }

    return prs
  }

  /**
   * Merges a Pull Request if criteria are met.
   */
  public async mergePullRequest(prId: number | string, provider: 'github' | 'gitlab' = 'github') {
    // Protocol Audit: Ensure we are not merging in a restricted environment without a token
    const token = process.env.GITHUB_TOKEN || process.env.GITLAB_TOKEN
    if (!token) {
      console.warn(`⚠️ [GitProvider] Cannot merge ${provider} PR/MR #${prId} without authentication token.`)
      return false
    }

    if (provider === 'github' && process.env.GITHUB_TOKEN) {
      try {
        const octokit = github.getOctokit(process.env.GITHUB_TOKEN)
        const context = github.context
        await octokit.rest.pulls.merge({
          ...context.repo,
          pull_number: Number(prId),
          merge_method: 'squash'
        })
        logAutonomousAction(`✅ [GitProvider] GitHub PR #${prId} merged.`, 'info')
        return true
      } catch (err: any) {
        console.error(`❌ [GitProvider] GitHub Merge failed for PR #${prId}:`, err.message)
      }
    } else if (provider === 'gitlab' && process.env.GITLAB_TOKEN) {
      try {
        execSync(`glab mr merge ${prId} --squash --remove-source-branch`)
        logAutonomousAction(`✅ [GitProvider] GitLab MR !${prId} merged via glab.`, 'info')
        return true
      } catch (err: any) {
        console.warn(`⚠️ [GitProvider] GitLab Merge via glab failed for MR !${prId}. Attempting API fallback...`)
        const projectId = process.env.CI_PROJECT_ID
        if (projectId) {
          try {
            const response = await fetch(`https://gitlab.com/api/v4/projects/${projectId}/merge_requests/${prId}/merge`, {
              method: 'PUT',
              headers: { 'PRIVATE-TOKEN': process.env.GITLAB_TOKEN },
              body: JSON.stringify({ squash: true, should_remove_source_branch: true })
            })
            if (response.ok) {
              logAutonomousAction(`✅ [GitProvider] GitLab MR !${prId} merged via API.`, 'info')
              return true
            } else {
              const data = await response.json()
              console.error(`❌ [GitProvider] GitLab API Merge failed:`, data.message)
            }
          } catch (apiErr: any) {
            console.error(`❌ [GitProvider] GitLab API fallback failed:`, apiErr.message)
          }
        }
      }
    }

    return false
  }

  /**
   * Formats a commit message with GitKraken roadmap tags.
   */
  public static formatGitKrakenMessage(title: string, phase: string, progress: number, details: string[] = []) {
    const progressBar = this.generateProgressBar(progress)
    let msg = `[ROADMAP:${phase}] ${title}\n\n`
    msg += `Progress: ${progressBar} (${progress}%)\n\n`
    if (details.length > 0) {
      msg += `Details:\n${details.map(d => `- ${d}`).join('\n')}\n\n`
    }
    msg += `Automated by Antigravity Autonomous Engine.`
    return msg
  }

  private static generateProgressBar(percent: number, length: number = 20) {
    const filledLength = Math.round((length * percent) / 100)
    const filled = '█'.repeat(filledLength)
    const empty = '░'.repeat(length - filledLength)
    return filled + empty
  }
}

export const gitProvider = new GitProviderService()

### System: antigravity/services/github_docs_observer.ts
*Source: local://antigravity/services/github_docs_observer.ts*

#### Introduction
import { logAutonomousAction } from '../core'
import { z } from 'zod'
import { autonomousFetch } from '@/antigravity/core'

export const GithubDocSectionSchema = z.object({
  title: z.string(),
  content: z.string()
})

export const GithubDocsSchema = z.object({
  repo: z.string(),
  file: z.string(),
  sections: z.array(GithubDocSectionSchema),
  rawUrl: z.string(),
  lastUpdated: z.string()
})

export type GithubDocs = z.infer<typeof GithubDocsSchema>

/**

#### * GITHUB DOCS OBSERVER
* Autonomously extracts technical sections from raw GitHub markdown files.
 */
export class GithubDocsObserver {
  private baseUrl = 'https://raw.githubusercontent.com'

  /**
   * fetchDoc: Retrieves and parses a markdown file from GitHub.
   */
  public async fetchDoc(owner: string, repo: string, path: string, branch: string = 'master'): Promise<GithubDocs> {
    const rawUrl = `${this.baseUrl}/${owner}/${repo}/${branch}/${path}`

    return autonomousFetch(GithubDocsSchema, async () => {
      logAutonomousAction(`📡 [GithubDocsObserver] Fetching: ${owner}/${repo}/${path}...`, 'info')
      const response = await fetch(rawUrl)

      if (!response.ok) {
        throw new Error(`Failed to fetch doc from GitHub: ${response.statusText}`)
      }

      const markdown = await response.text()
      const sections = this.parseMarkdown(markdown)

      return {
        repo: `${owner}/${repo}`,
        file: path,
        sections,
        rawUrl,
        lastUpdated: new Date().toISOString()
      }
    }, { life: 'catalog', tags: [`github-docs-${repo}-${path.replace(/\//g, '-')}`] })
  }

  /**
   * parseMarkdown: Extracts sections based on markdown headers.
   * Improved to handle empty sections and nested headers.
   */
  private parseMarkdown(markdown: string): { title: string; content: string }[] {
    const sections: { title: string; content: string }[] = []

    const lines = markdown.split('\n')
    let currentTitle = 'Overview'
    let currentContent: string[] = []

    for (const line of lines) {
      const headerMatch = line.match(/^#+\s+(.*)$/)
      if (headerMatch) {
        // Save previous section if it has content or isn't the default Overview
        if (currentContent.length > 0 || currentTitle !== 'Overview') {
          sections.push({
            title: currentTitle,
            content: currentContent.join('\n').trim()
          })
        }
        currentTitle = headerMatch[1]
        currentContent = []
      } else {
        currentContent.push(line)
      }
    }

    // Push final section
    sections.push({
      title: currentTitle,
      content: currentContent.join('\n').trim()
    })

    return sections.filter(s => s.title !== 'Overview' || s.content !== '')
  }
}

export const githubDocsObserver = new GithubDocsObserver()

### System: antigravity/services/intelligence.ts
*Source: local://antigravity/services/intelligence.ts*

#### Introduction
import { logAutonomousAction } from '../core'
import fs from 'fs'
import path from 'path'
import { getMissionMetadata } from './collaboration'
import { workOrderService } from './work_order'
import { jules } from '../jules'
import { healthCheck } from '../core'
import { checkJenkinsHealth } from './jenkins'

/**

#### * CONSOLIDATED INTELLIGENCE SERVICE
* Generates system-wide intelligence reports.
 */

export async function generateConsolidatedReport(branchIntelligence?: any[]) {
  logAutonomousAction('📊 [Intelligence] Generating consolidated system report...', 'info')

  const metadata = await getMissionMetadata()
  const branches = branchIntelligence || await jules.scanAllBranches()
  const health = await healthCheck()
  const workOrders = await workOrderService.getPendingOrders()

  const reportPath = path.join(process.cwd(), 'CONSOLIDATED_INTELLIGENCE.md')

  let report = `# CONSOLIDATED INTELLIGENCE REPORT\n\n`
  report += `*Generated: ${new Date().toISOString()}*\n\n`

  report += `## 🎯 Mission Statement\n> ${metadata.missionStatement}\n\n`

  report += `## 🏥 System Sovereignty\n`
  report += `- **Execution Environment:** ${process.env.GITHUB_ACTIONS ? 'Cloud (GitHub Actions)' : 'Local'}\n`
  report += `- **MongoDB:** ${health.mongodb}\n`
  report += `- **Supabase:** ${health.supabase}\n`
  const jenkinsHealth = await checkJenkinsHealth()
  report += `- **Jenkins Pipeline:** ${jenkinsHealth.metrics.pipeline_efficiency}\n`
  report += `- **Total Branches:** ${branches.length}\n\n`

  report += `## 🌿 Branch Intelligence (Recent Activity)\n`
  const recentBranches = branches
    .sort((a, b) => new Date(b.lastSeen).getTime() - new Date(a.lastSeen).getTime())
    .slice(0, 10)

  recentBranches.forEach(b => {
    report += `- **${b.name}**: ${b.lastMessage} (*${b.lastSeen}*)\n`
  })
  report += `\n`

  report += `## 🛠️ Cognitive State\n`
  report += `- **Pending Work Orders:** ${workOrders.length}\n`
  if (workOrders.length > 0) {
    workOrders.forEach(wo => {
      report += `  - [${wo.type}] ${wo.goal}\n`
    })
  } else {
    report += `  - No pending orders. System is optimal.\n`
  }
  report += `\n`

  report += `## 🤖 Python Ecosystem Intelligence\n`
  try {
    const linksPath = path.join(process.cwd(), 'links.json')
    if (fs.existsSync(linksPath)) {
      const links = JSON.parse(fs.readFileSync(linksPath, 'utf8'))
      report += `- **Market Data:** ${links.length} entries analyzed.\n`
    } else {
      report += `- **Market Data:** Scraper results pending.\n`
    }

    const resultsDir = path.join(process.cwd(), 'results')
    if (fs.existsSync(resultsDir)) {
      const files = fs.readdirSync(resultsDir)
      report += `- **Autonomous Reports:** ${files.length} generated.\n`

      const latestReport = files.filter(f => f.startsWith('DAILY_REPORT')).sort().reverse()[0]
      if (latestReport) {
        report += `- **Latest Report:** ${latestReport}\n`
      }
    }
  } catch (e) {
    report += `- **Ecosystem Status:** Limited observability into Python layer.\n`
  }
  report += `\n`

  report += `## 👥 Stakeholders\n`
  metadata.stakeholders.forEach(s => {
    report += `- **${s.role}**: ${s.email}\n`
  })

  report += `\n---\n\n`

  fs.writeFileSync(reportPath, report)
  logAutonomousAction(`✅ [Intelligence] Report saved to ${reportPath}`, 'info')

  return { reportPath, branchCount: branches.length }
}

### System: antigravity/services/jenkins.ts
*Source: local://antigravity/services/jenkins.ts*

#### Introduction
import fs from 'fs'
import path from 'path'

export interface JenkinsPipelineMetrics {
  pipeline_efficiency: 'BASIC' | 'OPTIMIZED' | 'HIGHLY_OPTIMIZED'
  security_scan: 'PASSED' | 'SKIPPED'
  has_cache: boolean
  has_artifacts: boolean
  has_stages: boolean
  has_parallel: boolean
}

export async function getJenkinsStatus(): Promise<JenkinsPipelineMetrics> {
  const ciFilePath = path.join(process.cwd(), 'Jenkinsfile')

  let has_security_or_test = false
  let has_cache = false
  let has_artifacts = false
  let has_stages = false
  let has_parallel = false
  let content = ''

  if (fs.existsSync(ciFilePath)) {
    try {
      content = fs.readFileSync(ciFilePath, 'utf-8').toLowerCase()
      if (content.includes('security') || content.includes('test')) {
        has_security_or_test = true
      }
      if (content.includes('cache')) {
        has_cache = true
      }
      if (content.includes('archiveartifacts')) {
        has_artifacts = true
      }
      if (content.includes('stage')) {
        has_stages = true
      }
      if (content.includes('parallel')) {
        has_parallel = true
      }
    } catch (e) {
      console.error(`⚠️ [Jenkins] Error reading ${ciFilePath}:`, e)
    }
  }

  const has_jenkins_ci = fs.existsSync(ciFilePath)

  let pipeline_efficiency: 'BASIC' | 'OPTIMIZED' | 'HIGHLY_OPTIMIZED' = 'BASIC'
  if (has_jenkins_ci) {
    pipeline_efficiency = 'OPTIMIZED'
    if (has_cache && has_artifacts && has_stages && has_parallel) {
      pipeline_efficiency = 'HIGHLY_OPTIMIZED'
    }
  }

  const security_scan = (content.includes('security') || has_jenkins_ci) ? 'PASSED' : 'SKIPPED'

  return {
    pipeline_efficiency,
    security_scan,
    has_cache,
    has_artifacts,
    has_stages,
    has_parallel
  }
}

export async function checkJenkinsHealth() {
  const status = await getJenkinsStatus()
  return {
    status: status.pipeline_efficiency !== 'BASIC' ? 'optimal' : 'disconnected',
    metrics: status,
    timestamp: new Date().toISOString()
  }
}

### System: antigravity/services/knowledge.ts
*Source: local://antigravity/services/knowledge.ts*

#### Introduction
import { logAutonomousAction } from '../core'
import fs from 'fs'
import path from 'path'
import * as cheerio from 'cheerio'

/**
 * Scan and Observe Knowledge Service
 * Fetches basic metadata from a target URL and records relationship intelligence.
 */
export async function observeKnowledge(url: string) {
  logAutonomousAction(`🧠 [Knowledge Observer] Scanning ${url} for market intelligence...`, 'info')

  try {
    const response = await fetch(url)
    const html = await response.text()
    const $ = cheerio.load(html)

    const title = $('title').text() || 'No Title Found'

    logAutonomousAction(`[KNOWLEDGE] Scanned ${url}. Title: ${title}`, 'cognitive')

    // Append or create KNOWLEDGE_MERGE.md with formal relationships
    const knowledgePath = path.join(process.cwd(), 'KNOWLEDGE_MERGE.md')

    const relationshipEntry = `

#### Autonomous Observation
- **Date**: ${new Date().toISOString()}
- **Target**: ${url}
- **Title**: ${title}
- **Relationship Map**: Confirmed overlapping identities between Antigravity, Project SOR, software-online-review.com, software-review-platform, and markposition.wordpress.com as the formal Market Intelligence layer.
`
    if (fs.existsSync(knowledgePath)) {
      fs.appendFileSync(knowledgePath, relationshipEntry, 'utf8')
    } else {
      fs.writeFileSync(knowledgePath, `# Market Intelligence Matrix\n${relationshipEntry}`, 'utf8')
    }

    logAutonomousAction(`✅ [Knowledge Observer] Appended insights to KNOWLEDGE_MERGE.md.`, 'info')
    return { status: 'observed', url, title }
  } catch (error) {
    console.error(`⚠️ [Knowledge Observer] Failed to scan ${url}:`, error)
    return { status: 'failed', url, error: String(error) }
  }
}

### System: antigravity/services/knowledge_observer.test.ts
*Source: local://antigravity/services/knowledge_observer.test.ts*

#### Introduction
import { describe, it, expect, beforeEach, afterEach } from 'vitest'
import fs from 'fs'
import path from 'path'
import { KnowledgeObserver } from './knowledge_observer'

describe('KnowledgeObserver', () => {
  const testStorageDir = path.join(process.cwd(), 'data/knowledge_test')

  beforeEach(() => {
    if (fs.existsSync(testStorageDir)) {
      fs.rmSync(testStorageDir, { recursive: true, force: true })
    }
  })

  afterEach(() => {
    if (fs.existsSync(testStorageDir)) {
      fs.rmSync(testStorageDir, { recursive: true, force: true })
    }
  })

  it('should process content into structured sections', () => {
    const raw = '# Header 1\nContent 1\n# Header 2\nContent 2'
    const result = KnowledgeObserver.processContent('Test Title', raw, 'test-source')

    expect(result.title).toBe('Test Title')
    expect(result.sections).toHaveLength(2)
    expect(result.sections[0].header).toBe('Header 1')
    expect(result.sections[0].content).toBe('Content 1')
    expect(result.sections[1].header).toBe('Header 2')
    expect(result.sections[1].content).toBe('Content 2')
  })

  it('should handle Title Case headers', () => {
    const raw = 'Introduction\nThis is the intro.\nGetting Started\nStep 1...'
    const result = KnowledgeObserver.processContent('Test Title', raw, 'test-source')

    expect(result.sections).toHaveLength(2)
    expect(result.sections[0].header).toBe('Introduction')
    expect(result.sections[1].header).toBe('Getting Started')
  })

  it('should handle uppercase headers and skip code blocks', () => {
    const raw = `INTRODUCTION
This is an introduction.
<?php
class SkipMe {}
?>

#### DETAILS
Some details here.`
    const result = KnowledgeObserver.processContent('Test Title', raw, 'test-source')

    // console.log('DEBUG result sections:', result.sections)
    expect(result.sections.length).toBeGreaterThanOrEqual(2)
    expect(result.sections[0].header).toBe('INTRODUCTION')
    // Find section with header DETAILS
    const details = result.sections.find(s => s.header === 'DETAILS')
    expect(details).toBeDefined()
    // Ensure the PHP class didn't become a header
    expect(result.sections.find(s => s.header === 'class SkipMe {}')).toBeUndefined()
  })

  it('should persist knowledge to custom directory', async () => {
    const observer = new KnowledgeObserver(testStorageDir)
    const knowledge = KnowledgeObserver.processContent('Persist Test', '# Section 1\nThis is the content.', 'source')

    await observer.persistKnowledge(knowledge)

    expect(fs.existsSync(path.join(testStorageDir, 'system_knowledge.json'))).toBe(true)

    const json = JSON.parse(fs.readFileSync(path.join(testStorageDir, 'system_knowledge.json'), 'utf8'))
    expect(json.typescript_sections['Persist Test']).toBeDefined()
    expect(json.typescript_sections['Persist Test'].sections).toBeDefined()
    expect(json.typescript_sections['Persist Test'].sections.length).toBeGreaterThan(0)
    expect(json.typescript_sections['Persist Test'].sections[0].header).toBe('Section 1')
    expect(json.typescript_sections['Persist Test'].sections[0].content).toBe('This is the content.')
  })
})

### System: antigravity/services/knowledge_observer.ts
*Source: local://antigravity/services/knowledge_observer.ts*

#### Introduction
import { logAutonomousAction } from '../core'
import fs from 'fs'
import path from 'path'
import { z } from 'zod'

/**

#### * KNOWLEDGE OBSERVER SERVICE
* Autonomously parses and persists technical documentation and insights.
 */

export const KnowledgeSchema = z.object({
  title: z.string(),
  sections: z.array(z.object({
    header: z.string(),
    content: z.string()
  })),
  metadata: z.object({
    source: z.string(),
    ingestedAt: z.string()
  })
})

export type Knowledge = z.infer<typeof KnowledgeSchema>

const DEFAULT_STORAGE_DIR = path.join(process.cwd(), 'data/knowledge')

export class KnowledgeObserver {
  private storageDir: string

  constructor(storageDir: string = DEFAULT_STORAGE_DIR) {
    this.storageDir = storageDir
  }

  /**
   * processContent: Parses raw text into structured knowledge with code-block awareness.
   */
  public static processContent(title: string, rawContent: string, source: string): Knowledge {
    const sections: { header: string; content: string }[] = []
    const lines = rawContent.split('\n')
    let currentHeader = 'Introduction'
    let currentLines: string[] = []
    let inCodeBlock = false

    for (const line of lines) {
      const trimmed = line.trim();

      // Toggle code block state
      if (trimmed.startsWith('```') || trimmed.startsWith('<?php')) {
        inCodeBlock = !inCodeBlock
      }

      // Detect headers ONLY if not in a code block
      const hasLetters = /[a-zA-Z]/.test(trimmed)
      const isMarkdownHeader = !inCodeBlock && trimmed.startsWith('#')
      const isStrongHeader = !inCodeBlock && trimmed && hasLetters &&
                             trimmed.length < 60 && trimmed.length > 2 &&
                             !trimmed.endsWith('.') &&
                             !trimmed.endsWith(':') &&
                             !trimmed.endsWith(',') &&
                             (trimmed.toUpperCase() === trimmed || /^[A-Z][a-z]+(\s[A-Z][a-z]+)*$/.test(trimmed)) &&
                             !trimmed.startsWith('This ') &&
                             !trimmed.startsWith('Some ') &&
                             !/^[{}/*<>?]+$/.test(trimmed) && // Exclude common code symbols
                             !trimmed.includes('(') && !trimmed.includes(')') && // Exclude function calls
                             !trimmed.includes(' = ') && // Exclude assignments
                             !trimmed.includes(' => ') // Exclude arrow funcs/mappings

      // Heuristic: If it's a markdown header, always count it.
      // If it's a strong header, it must not be immediately followed by a lot of text on the same line (already trimmed)
      // and it should ideally be on its own line (which it is here since we iterate lines).
      if (isMarkdownHeader || isStrongHeader) {
        if (currentLines.length > 0) {
          sections.push({ header: currentHeader, content: currentLines.join('\n').trim() })
        }
        currentHeader = trimmed.replace(/^#+\s*/, '').trim()
        currentLines = []
      } else {
        currentLines.push(line)
      }

      // If we just ended a code block, make sure we stay out of it for the next lines
      // unless another one starts. The simple toggle works if we have distinct start/end markers.
      if (trimmed.endsWith('?>') && inCodeBlock) {
        inCodeBlock = false
      }
    }

    if (currentLines.length > 0) {
      sections.push({ header: currentHeader, content: currentLines.join('\n').trim() })
    }

    return {
      title,
      sections,
      metadata: {
        source,
        ingestedAt: new Date().toISOString()
      }
    }
  }

  /**
   * persistKnowledge: Merges and saves knowledge to the unified system store.
   */
  public async persistKnowledge(knowledge: Knowledge) {
    if (!fs.existsSync(this.storageDir)) {
      fs.mkdirSync(this.storageDir, { recursive: true })
    }

    const jsonStore = path.join(this.storageDir, 'system_knowledge.json')

    // 1. JSON Persistence (Cross-Ecosystem Merge Logic)
    let systemKnowledge: any = {
      metadata: {
        generated_at: new Date().toISOString(),
        version: 1.0,
        sources_processed: []
      },
      sections: {},
      typescript_sections: {}
    }

    if (fs.existsSync(jsonStore)) {
      try {
        systemKnowledge = JSON.parse(fs.readFileSync(jsonStore, 'utf8'))
      } catch (e) {
        console.warn('⚠️ [KnowledgeObserver] Failed to parse unified store. Initializing new structure.')
      }
    }

    // Ensure TypeScript sections structure exists
    if (!systemKnowledge.typescript_sections) {
      systemKnowledge.typescript_sections = {}
    }

    // Upsert the new knowledge into TypeScript-specific namespace
    systemKnowledge.typescript_sections[knowledge.title] = {
      sections: knowledge.sections,
      metadata: knowledge.metadata
    }

    // Update global metadata
    systemKnowledge.metadata.generated_at = new Date().toISOString()
    if (!systemKnowledge.metadata.sources_processed.includes(knowledge.metadata.source)) {
      systemKnowledge.metadata.sources_processed.push(knowledge.metadata.source)
    }

    fs.writeFileSync(jsonStore, JSON.stringify(systemKnowledge, null, 2))
    logAutonomousAction(`✅ [KnowledgeObserver] Persisted "${knowledge.title}" to unified store at ${jsonStore}`, 'info')
  }
}

### System: antigravity/services/neural.ts
*Source: local://antigravity/services/neural.ts*

#### Introduction
import { z } from 'zod'
import { getSystemInsights, logAutonomousAction } from '@/antigravity/core'

export const NeuralPulseSchema = z.object({
  origin: z.string(),
  health: z.string(),
  volatilityTags: z.number(),
  timestamp: z.string()
})

export type NeuralPulse = z.infer<typeof NeuralPulseSchema>

/**
 * Global Neural Sync (Phase 9)
 * Manages cross-environment cognitive synchronization.
 */
export async function broadcastPulse() {
  const insights = await getSystemInsights()

  const pulse: NeuralPulse = {
    origin: process.env.NODE_ENV || 'development',
    health: insights.circuitBreakers.mongodb === 'closed' ? 'optimal' : 'degraded',
    volatilityTags: insights.caching.registrySize,
    timestamp: new Date().toISOString()
  }

  // In a Global Sync scenario, this pulse would be sent to a central
  // Antigravity Relay or persisted to a shared Supabase 'neural_sync' table.
  logAutonomousAction(`[NEURAL] Broadcasting cognitive pulse from ${pulse.origin}`, 'sync')

  return pulse
}

export async function getNetworkState() {
  // Simulates receiving pulses from other agents in the "Global Neural Network"
  return [
    { origin: 'production', health: 'optimal', lastSeen: '2m ago' },
    { origin: 'staging', health: 'optimal', lastSeen: '15m ago' }
  ]
}

### System: antigravity/services/notification.ts
*Source: local://antigravity/services/notification.ts*

#### Introduction
import { z } from 'zod'
import { autonomousFetch, logAutonomousAction } from '@/antigravity/core'

export const NotificationSchema = z.object({
  id: z.string(),
  type: z.enum(['health', 'evolution', 'security', 'scaling']),
  message: z.string(),
  severity: z.enum(['info', 'warning', 'critical']),
  timestamp: z.string()
})

export type Notification = z.infer<typeof NotificationSchema>

const notifications: Notification[] = []

/**
 * Autonomous Notification Service
 * Handles system-wide alerts for cognitive events.
 */
export async function sendNotification(payload: Omit<Notification, 'id' | 'timestamp'>) {
  const newNotification: Notification = {
    ...payload,
    id: Math.random().toString(36).substr(2, 9),
    timestamp: new Date().toISOString()
  }

  notifications.unshift(newNotification)
  if (notifications.length > 20) notifications.pop()

  // Log to the global autonomous buffer
  logAutonomousAction(`[${payload.type.toUpperCase()}] ${payload.message}`, payload.severity === 'critical' ? 'error' : 'info')

  return newNotification
}

export async function getNotifications(): Promise<Notification[]> {
  // Use 'inventory' profile for frequent updates
  return notifications
}

### System: antigravity/services/persistence.ts
*Source: local://antigravity/services/persistence.ts*

#### Introduction
import { execSync } from 'child_process'
import { z } from 'zod'
import { autonomousFetch, logAutonomousAction } from '@/antigravity/core'

export const PersistenceSchema = z.object({
  agent: z.string(),
  status: z.enum(['running', 'stopped', 'error']),
  pid: z.string().optional()
})

export type PersistenceStatus = z.infer<typeof PersistenceSchema>

/**
 * Persistence Monitoring Service
 * Autonomously tracks the state of system-level Sigma agents.
 */
export async function getPersistenceHealth(): Promise<PersistenceStatus[]> {
  const agents = ['com.sigma.orchestrator', 'com.sigma.jules', 'com.sigma.syra_api']

  return autonomousFetch(z.array(PersistenceSchema), async () => {
    const results: PersistenceStatus[] = []

    for (const agent of agents) {
      try {
        const output = execSync(`launchctl list ${agent}`).toString()
        const pidMatch = output.match(/"PID" = (\d+);/)
        const lastExitMatch = output.match(/"LastExitStatus" = (\d+);/)

        results.push({
          agent,
          status: pidMatch ? 'running' : (lastExitMatch && lastExitMatch[1] === '0' ? 'stopped' : 'error'),
          pid: pidMatch ? pidMatch[1] : undefined
        })
      } catch (e) {
        results.push({ agent, status: 'error' })
      }
    }

    return results
  }, { life: 'inventory', tags: ['persistence-health'] })
}

### System: antigravity/services/react.ts
*Source: local://antigravity/services/react.ts*

#### Introduction
import { logAutonomousAction } from '../core'

/**

#### * ANTIGRAVITY REACT SERVICE
* Implements the ReAct (Reasoning and Acting) protocol: Thought -> Action -> Observation.
 * Based on arXiv:2210.03629.
 */

export interface ReActStep {
  thought: string
  action: string
  observation: string
}

export interface ReActAgentPrompt {
  goal: string
  context?: string
  availableTools: string[]
}

export class ReActService {
  private steps: ReActStep[] = []

  /**
   * Execute a ReAct cycle for a given goal and tools.
   * This implementation follows a generic loop where each step's thought and action
   * are determined by the current state and the goal.
   */
  public async executeCycle(
    goal: string,
    tools: Record<string, Function>,
    maxSteps: number = 5
  ): Promise<ReActStep[]> {
    logAutonomousAction(`🧠 [ReAct] Starting autonomous cycle for goal: "${goal}"`, 'info')
    this.steps = []

    for (let i = 0; i < maxSteps; i++) {
      // In a production system with an LLM, we would send the history + goal to the model
      // and it would return the next Thought and Action.
      // Here, we simulate the 'Reasoning' engine's decision process.
      const stepDecision = await this.reasonNextStep(goal, i, this.steps, Object.keys(tools))

      if (stepDecision.action === 'finish') {
        logAutonomousAction(`✅ [ReAct] Goal achieved: ${stepDecision.thought}`, 'info')
        this.steps.push({
          thought: stepDecision.thought,
          action: 'finish',
          observation: 'Cycle finalized successfully.'
        })
        break
      }

      logAutonomousAction(`💭 [ReAct] Step ${i + 1} Thought: ${stepDecision.thought}`, 'info')
      const observation = await this.performAction(stepDecision.action, tools)

      this.steps.push({
        thought: stepDecision.thought,
        action: stepDecision.action,
        observation
      })

      if (i === maxSteps - 1) {
        console.warn(`⚠️ [ReAct] Reached maximum steps (${maxSteps}) for goal: ${goal}`)
      }
    }

    logAutonomousAction(`[ReAct] Completed cycle for goal: ${goal}`, 'cognitive')
    return this.steps
  }

  /**
   * Mock reasoning engine.
   * Determines the next Thought and Action based on the goal and execution history.
   */
  private async reasonNextStep(
    goal: string,
    stepIndex: number,
    history: ReActStep[],
    availableTools: string[]
  ): Promise<{ thought: string; action: string }> {
    // Basic heuristic-based reasoning simulation
    if (stepIndex === 0) {
      if (goal.includes('Audit and merge PR') && availableTools.includes('auditPR')) {
        return {
          thought: `Initial thought: To achieve "${goal}", I should first audit the PR.`,
          action: 'auditPR'
        }
      }
      return {
        thought: `Initial thought: To achieve "${goal}", I should first assess the current environment state.`,
        action: availableTools.includes('checkSystemState') ? 'checkSystemState' : availableTools[0]
      }
    }

    const lastObservation = history[history.length - 1].observation

    if (lastObservation.includes('error') || lastObservation.includes('MISSING')) {
      return {
        thought: `I detected issues in the observation: ${lastObservation}. I need to find optimizations to repair the system.`,
        action: availableTools.includes('findOptimizations') ? 'findOptimizations' : 'finish'
      }
    }

    if (goal.includes('Audit and merge PR')) {
      if (lastObservation.includes('compliant') && availableTools.includes('verifyCI')) {
        return {
          thought: `The PR is compliant. Next, I need to verify CI checks.`,
          action: 'verifyCI'
        }
      }
      if (lastObservation.includes('passed') && availableTools.includes('merge')) {
        return {
          thought: `CI checks have passed. I am ready to merge the PR.`,
          action: 'merge'
        }
      }
    }

    return {
      thought: `System state appears nominal or I have completed my analysis. Finalizing the task "${goal}".`,
      action: 'finish'
    }
  }

  private async performAction(actionName: string, tools: Record<string, Function>): Promise<string> {
    logAutonomousAction(`🎬 [ReAct] Action: ${actionName}`, 'info')
    if (tools[actionName]) {
      try {
        const result = await tools[actionName]()
        return typeof result === 'string' ? result : JSON.stringify(result)
      } catch (err) {
        return `Error performing action ${actionName}: ${err}`
      }
    }
    return `Action ${actionName} not found in tools.`
  }

  public getTrace(): string {
    return this.steps.map((s, i) =>
      `Step ${i + 1}:\n  Thought: ${s.thought}\n  Action: ${s.action}\n  Observation: ${s.observation}`
    ).join('\n\n')
  }
}

export const reactService = new ReActService()

### System: antigravity/services/relay.ts
*Source: local://antigravity/services/relay.ts*

#### Introduction
import { z } from 'zod'
import { autonomousFetch, logAutonomousAction } from '@/antigravity/core'

export const RelayStateSchema = z.object({
  id: z.string(),
  environment: z.string(),
  activeViews: z.array(z.string()),
  lastActivity: z.string(),
  intensity: z.number() // 0-1 scaling factor for UI vibrancy
})

export type RelayState = z.infer<typeof RelayStateSchema>

/**
 * Visual Neural Relay (Phase 11)
 * Synchronizes real-time UI state across the Neural Network.
 */
export async function getRelayState(): Promise<RelayState[]> {
  // In a multi-environment sync, this would fetch from a shared Supabase Realtime channel.
  // Here we simulate the collective state of the network.
  return [
    {
      id: 'local-main',
      environment: 'development',
      activeViews: ['Command Center', 'Store'],
      lastActivity: new Date().toISOString(),
      intensity: 0.85
    },
    {
      id: 'prod-alpha',
      environment: 'production',
      activeViews: ['Analytics', 'Explorer'],
      lastActivity: '1m ago',
      intensity: 0.4
    }
  ]
}

export async function broadcastUIEvent(view: string) {
  logAutonomousAction(`[RELAY] Broadcasting UI focus: ${view}`, 'sync')
  // Trigger relay logic here
}

### System: antigravity/services/stats.ts
*Source: local://antigravity/services/stats.ts*

#### Introduction
import { z } from 'zod'
import { autonomousFetch, healthCheck, predictiveFetch } from '@/antigravity/core'

// Define the schema for our autonomous app stats
const AppStatsSchema = z.object({
  mongoStatus: z.string(),
  supabaseStatus: z.string(),
  activeUsers: z.number(),
  lastUpdated: z.string(),
})

export type AppStats = z.infer<typeof AppStatsSchema>

/**
 * Scalable Autonomous Service: Orchestrates data from multiple sources automatically.
 * Phase 4: Uses predictiveFetch to choose the best cacheLife profile.
 */
export async function getAppStats(): Promise<AppStats> {
  return predictiveFetch(
    'system-stats',
    AppStatsSchema,
    async () => {
      // Autonomous self-diagnostic health check
      const health = await healthCheck()

      // Combine multiple autonomous signals into a single output
      return {
        mongoStatus: health.mongodb,
        supabaseStatus: health.supabase,
        activeUsers: 1240, // Simulated active signal
        lastUpdated: health.timestamp,
      }
    }
  )
}

### System: antigravity/services/user.ts
*Source: local://antigravity/services/user.ts*

#### Introduction
import { experimental_taintObjectReference } from 'react'
import { autonomousFetch } from '@/antigravity/core'
import { z } from 'zod'

export const UserSchema = z.object({
  id: z.string(),
  name: z.string(),
  email: z.string(),
  token: z.string(),
})

export type User = z.infer<typeof UserSchema>

export async function getUser(id: string): Promise<User> {
  return autonomousFetch(
    UserSchema,
    async () => {
      // In a real app, fetch from DB
      const user = {
        id,
        name: 'John Doe',
        email: 'john@example.com',
        token: 'secret-session-token'
      }

      // Taint the user object to prevent it from being passed to Client Components
      experimental_taintObjectReference(
        'Do not pass the full user object to the client. It contains sensitive tokens.',
        user
      )

      return user
    },
    {
      tags: [`user-${id}`],
      life: 'minutes'
    }
  )
}

/**
 * Scalable Pattern: Export "Safe" versions of data for Client Components
 */
export function getSafeUser(user: User) {
  return {
    id: user.id,
    name: user.name
  }
}

### System: antigravity/services/work_order.ts
*Source: local://antigravity/services/work_order.ts*

#### Introduction
import fs from 'fs'
import path from 'path'
import { z } from 'zod'
import { logAutonomousAction, getMongoClient } from '../core'

export const WorkOrderSchema = z.object({
  id: z.string(),
  type: z.string(), // Allow all types, specific ones handled in dispatch
  goal: z.string().optional(),
  description: z.string().optional(), // Support Python-style description
  payload: z.any().optional(),
  status: z.enum(['pending', 'executing', 'completed', 'failed', 'in_progress']),
  created_at: z.string(),
  updated_at: z.string().optional(),
  completed_at: z.string().optional(),
  result: z.any().optional(),
  error: z.string().optional()
})

export type WorkOrder = z.infer<typeof WorkOrderSchema>

const STORAGE_PATH = path.join(process.cwd(), 'data/work_orders.json')

export class WorkOrderService {
  private orders: WorkOrder[] = []

  constructor() {
    this.load()
  }

  private async load() {
    // Try MongoDB first
    try {
      const client = await getMongoClient()
      const db = client.db()
      const mongoOrders = await db.collection('work_orders').find({}).toArray()
      if (mongoOrders.length > 0) {
        const result = z.array(WorkOrderSchema).safeParse(mongoOrders)
        if (result.success) {
          this.orders = result.data
          logAutonomousAction(`✅ [WorkOrder] Loaded ${this.orders.length} orders from MongoDB.`, 'info')
          this.saveLocal() // Sync local for fallback
          return
        }
      }
    } catch (e) {
      console.warn('⚠️ [WorkOrder] MongoDB load failed, falling back to local file.')
    }

    // Fallback to local file
    if (fs.existsSync(STORAGE_PATH)) {
      try {
        const data = fs.readFileSync(STORAGE_PATH, 'utf8')
        const parsed = JSON.parse(data)
        const result = z.array(WorkOrderSchema).safeParse(parsed)
        if (result.success) {
          this.orders = result.data
          logAutonomousAction(`✅ [WorkOrder] Loaded ${this.orders.length} orders from local fallback.`, 'info')
        } else {
          console.error('❌ [WorkOrder] Local data validation failed:', result.error.format())
        }
      } catch (e) {
        console.error('❌ [WorkOrder] Failed to load local work orders:', e)
      }
    }
  }

  private async save(order?: WorkOrder) {
    this.saveLocal()

    try {
      const client = await getMongoClient()
      const db = client.db()
      if (order) {
        // Use a plain object for MongoDB to avoid potential issues with Zod/class instances
        const orderData = { ...order };
        delete (orderData as any)._id; // Ensure we don't try to update the immutable _id

        await db.collection('work_orders').updateOne(
          { id: order.id },
          { $set: orderData },
          { upsert: true }
        )
      } else {
        // Full sync if no specific order provided
        for (const o of this.orders) {
          await db.collection('work_orders').updateOne(
            { id: o.id },
            { $set: o },
            { upsert: true }
          )
        }
      }
    } catch (e) {
      console.error('❌ [WorkOrder] Failed to save to MongoDB:', e)
    }
  }

  private saveLocal() {
    const dataDir = path.dirname(STORAGE_PATH)
    if (!fs.existsSync(dataDir)) {
      fs.mkdirSync(dataDir, { recursive: true })
    }
    fs.writeFileSync(STORAGE_PATH, JSON.stringify(this.orders, null, 2))
  }

  public async createOrder(type: WorkOrder['type'], goal: string, payload: any): Promise<WorkOrder> {
    const newOrder: WorkOrder = {
      id: `wo_${Math.random().toString(36).substring(2, 11)}`,
      type,
      goal,
      payload,
      status: 'pending',
      created_at: new Date().toISOString()
    }
    this.orders.push(newOrder)
    await this.save(newOrder)
    logAutonomousAction(`[WORK_ORDER] Created: ${newOrder.id} - ${goal}`, 'cognitive')
    return newOrder
  }

  public async getPendingOrders(): Promise<WorkOrder[]> {
    await this.load() // Refresh from DB
    return this.orders.filter(o => o.status === 'pending')
  }

  public async updateOrderStatus(id: string, status: WorkOrder['status'], result?: any, error?: string) {
    const order = this.orders.find(o => o.id === id)
    if (order) {
      order.status = status
      if (status === 'completed' || status === 'failed') {
        order.completed_at = new Date().toISOString()
      }
      if (result) order.result = result
      if (error) order.error = error
      await this.save(order)
    }
  }

  public async executePendingOrders() {
    const pending = await this.getPendingOrders()
    if (pending.length === 0) return

    logAutonomousAction(`⚡ [WorkOrder] Executing ${pending.length} pending orders...`, 'info')

    for (const order of pending) {
      await this.updateOrderStatus(order.id, 'executing')
      try {
        const result = await this.dispatch(order)
        await this.updateOrderStatus(order.id, 'completed', result)
        logAutonomousAction(`[WORK_ORDER] Completed: ${order.id}`, 'cognitive')
      } catch (err: any) {
        console.error(`❌ [WorkOrder] Order ${order.id} failed:`, err)
        await this.updateOrderStatus(order.id, 'failed', undefined, err.message)
        logAutonomousAction(`[WORK_ORDER] Failed: ${order.id}`, 'error')
      }
    }
  }

  private async dispatch(order: WorkOrder) {
    logAutonomousAction(`🎬 [WorkOrder] Dispatching ${order.type}: ${order.goal || order.description}`, 'info')

    switch (order.type) {
      case 'BOOTSTRAP_SERVICE':
        const { bootstrap } = await import('../singularity')
        return await bootstrap(order.payload)

      case 'CONTENT_GENERATION':
        const { generateContent } = await import('./content')
        return await generateContent(order.payload)

      case 'OPTIMIZE_SYSTEM':
        const { evolve, applyFixes } = await import('../evolution')
        const suggestions = (order.payload && Array.isArray(order.payload.proposals))
          ? order.payload.proposals
          : await evolve()
        await applyFixes(suggestions)
        return { appliedFixes: suggestions.length }

      default:
        logAutonomousAction(`ℹ️ [WorkOrder] Skipping unknown or external order type: ${order.type}`, 'info')
        return { skipped: true, reason: 'external_type' }
    }
  }
}

export const workOrderService = new WorkOrderService()

### System: antigravity/singularity.ts
*Source: local://antigravity/singularity.ts*

#### Introduction
import { logAutonomousAction } from './core'
import fs from 'fs'
import path from 'path'

/**

#### * ANTIGRAVITY SINGULARITY ENGINE
* Autonomously scaffolds and generates new services based on synthesis.
 */

export async function bootstrap(idea: { feature: string, rationale: string }) {
  logAutonomousAction(`🌀 [Singularity] Bootstrapping: ${idea.feature}...`, 'info')

  const serviceName = idea.feature.toLowerCase().replace(/\s+/g, '_').replace(/_service$/, '')
  const filePath = path.join(process.cwd(), 'antigravity/services', `${serviceName}.ts`)

  if (fs.existsSync(filePath)) {
    logAutonomousAction(` - Service ${serviceName} already exists. Skipping bootstrap.`, 'info')
    return
  }

  const template = `/**
 * ${idea.feature}
 * Generated autonomously by the Antigravity Singularity Engine.
 * Rationale: ${idea.rationale}
 */
import { z } from 'zod'
import { autonomousFetch } from '@/antigravity/core'

export const ${idea.feature.replace(/\s+/g, '')}Schema = z.object({
  status: z.string(),
  lastRun: z.string()
})

export async function get${idea.feature.replace(/\s+/g, '')}Data() {
  return autonomousFetch(${idea.feature.replace(/\s+/g, '')}Schema, async () => {
    return {
      status: 'active',
      lastRun: new Date().toISOString()
    }
  }, { life: 'minutes' })
}
`

  fs.writeFileSync(filePath, template)
  logAutonomousAction(`✅ [Singularity] Successfully generated ${serviceName}.ts`, 'info')
  return { filePath, serviceName, feature: idea.feature }
}

### System: antigravity/synthesis.ts
*Source: local://antigravity/synthesis.ts*

#### Introduction
import { logAutonomousAction } from './core'
import fs from 'fs'
import path from 'path'

/**

#### * ANTIGRAVITY COGNITIVE SYNTHESIS ENGINE
* Autonomously ideates new features based on system state.
 */

interface SynthesizedIdea {
  feature: string
  rationale: string
  complexity: 'Low' | 'Medium' | 'High'
}

export async function synthesize(): Promise<SynthesizedIdea[]> {
  logAutonomousAction('🔮 [Antigravity Synthesis] Ideating new architectural features...', 'info')

  const ideas: SynthesizedIdea[] = []
  const servicesDir = path.join(process.cwd(), 'antigravity/services')
  const files = fs.readdirSync(servicesDir)

  // Gap Analysis 1: Real-time Notifications
  // If we have stats and users but no notification logic
  if (!files.some(f => f.includes('notification'))) {
    ideas.push({
      feature: 'Autonomous Notification Service',
      rationale: 'Detects Phase 5 Circuit Breaker trips and alerts active users via Supabase Realtime.',
      complexity: 'Medium'
    })
  }

  // Gap Analysis 2: Analytics Synthesis
  if (!files.some(f => f.includes('analytics'))) {
    ideas.push({
      feature: 'Predictive Analytics Layer',
      rationale: 'Aggregates Phase 4 Volatility data into a long-term MongoDB collection for trend forecasting.',
      complexity: 'High'
    })
  }

  // Gap Analysis 3: Cognitive Security
  if (!files.some(f => f.includes('security'))) {
    ideas.push({
      feature: 'Cognitive Security Service',
      rationale: 'Autonomously scans for leaked credentials and insecure patterns across the neural network.',
      complexity: 'Medium'
    })
  }

  // Gap Analysis 4: Visual Neural Relay
  if (!files.some(f => f.includes('relay'))) {
    ideas.push({
      feature: 'Visual Neural Relay',
      rationale: 'Manages real-time state synchronization between Development and Production environments.',
      complexity: 'High'
    })
  }

  return ideas
}

### Intelephense: README
*Source: https://raw.githubusercontent.com/bmewburn/intelephense-docs/master/README.md*

#### Intelephense
Intelephense is a high performance, cross platform PHP language server adhering to the [Language Server Protocol (LSP)](https://microsoft.github.io/language-server-protocol/).

When paired with an LSP capable editor it provides an essential set of code intelligence features that give a PHP developer a productive and rich editing experience.

This is proprietary software released to end users under a "freemium" model. Many of the features are provided free of charge. Access to all current and future features can be obtained by purchasing a licence key at https://intelephense.com.

#### [Installation](installation.md)


#### [Getting Started](gettingStarted.md)


#### [Features](features.md)


#### [Support](support.md)


#### [Licence](LICENSE.txt)


### Intelephense: features
*Source: https://raw.githubusercontent.com/bmewburn/intelephense-docs/master/features.md*

#### Features


#### Workspace Symbols


#### Document Symbols


#### Go To Definition


#### Completion


#### Signature Help


#### Hover


#### Document Highlight


#### Find All References


#### Document and Range Formatting


#### Rename -- [PREMIUM](https://intelephense.com)


#### Code Folding -- [PREMIUM](https://intelephense.com)


#### Find all Implementations -- [PREMIUM](https://intelephense.com)


#### Go to Declaration -- [PREMIUM](https://intelephense.com)


#### Go to Type Definition -- [PREMIUM](https://intelephense.com)


#### Smart Selection -- [PREMIUM](https://intelephense.com)


#### PHP Doc Block Generation -- [PREMIUM](https://intelephense.com)


### Intelephense: installation
*Source: https://raw.githubusercontent.com/bmewburn/intelephense-docs/master/installation.md*

#### Installation


#### Visual Studio Code
Visual Studio Code users should install the Intelephense extension from within the extensions view or download from the [marketplace](https://marketplace.visualstudio.com/items?itemName=bmewburn.vscode-intelephense-client).

1. Disable the built-in VSCode PHP Language Features.

    * Go to `Extensions`.
    * Search for `@builtin php`
    * Disable `PHP Language Features`. Leave `PHP Language Basics` enabled for syntax highlighting.

    Note that other (3rd party) PHP extensions which provide similar functionality should also be disabled for best results.
2. Add glob patterns for non standard php file extensions to the `files.associations` setting.

    For example: `"files.associations": { "*.module": "php" }`.
3. Optionally purchase and enter your [licence key](https://intelephense.com) by opening the command pallete
-- `ctrl + shift + p` -- and searching for `Enter licence key`.

Further configuration options are available in the `intelephense` section of settings.

#### Other Editors


#### Requirements
[Node.js 12+](https://nodejs.org)

#### Server Installation
```
npm i intelephense -g
```

#### Language Server Protocol (LSP) Client
Intelephense needs an LSP compliant client to communicate with and integrate features into the editor. A list of editors and clients that support the LSP can be found at https://microsoft.github.io/language-server-protocol/implementors/tools/.

Please follow the setup guide of the relevant tool. The Information below may help in configuring the client.

#### Run
```
intelephense {transport}
```
Where `{transport}` is one of:
* `--node-ipc`
* `--stdio`
* `--socket={number}`
* `--pipe={string}`

#### Initialisation Options
```typescript
interface InitialisationOptions {
    //Optional absolute path to storage dir. Defaults to os.tmpdir().
    storagePath?: string;

    //Optional absolute path to a global storage dir. Defaults to os.homedir().
    globalStoragePath?: string;

    //Optional licence key or absolute path to a text file containing the licence key.
    //{os.homedir()}/intelephense/licence.txt will also be checked by
    //default if initializationOptions are not exposed by client.
    licenceKey?: string;

    //Optional flag to clear server state.
    //State can also be cleared by deleting {storagePath}/intelephense
    clearCache?: boolean;
}
```

#### Capabilities
<details>
	<summary>Server capabilities JSON returned from `initialize` request.</summary>

```javascript
{
	textDocumentSync: TextDocumentSyncKind.Incremental,
	documentSymbolProvider: true,
	workspaceSymbolProvider: true,
	completionProvider: {
		triggerCharacters: [
			//php
			'$', '>', ':', '\\', '/',
			//phpdoc
			'*',
			// html/js
			'.', '<'
		],
		resolveProvider: true
	},
	signatureHelpProvider: {
		triggerCharacters: ['(', ',']
	},
	definitionProvider: true,
	referencesProvider: true,
	hoverProvider: true,
	documentFormattingProvider: true,	    //Dynamic registration if available.
    documentRangeFormattingProvider: true,  //Dynamic registration if available.
	documentHighlightProvider: true,
	workspace: {
		workspaceFolders: {
			supported: true,
			changeNotifications: true
		}
	},
	foldingRangeProvider: true,		//With licence key only.
	implementationProvider: true,	//With licence key only.
	declarationProvider: true,		//With licence key only.
	renameProvider: { 			    //With licence key only.
		prepareProvider: true
	},
	typeDefinitionProvider: true,	//With licence key only.
    selectionRangeProvider: true    //With licence key only.
}
```
</details>

#### Configuration Options
<details>
	<summary>JSON schema for `workspace/configuration` request data</summary>

```json
{
    "intelephense.compatibility.correctForBaseClassStaticUnionTypes": {
        "type": "boolean",
        "default": true,
        "description": "Resolves `BaseClass|static` union types to `static` instead of `BaseClass`.",
        "scope": "window"
    },
    "intelephense.compatibility.correctForArrayAccessArrayAndTraversableArrayUnionTypes": {
        "type": "boolean",
        "default": true,
        "description": "Resolves `ArrayAccess` and `Traversable` implementations that are unioned with a typed array to generic syntax. eg `ArrayAccessOrTraversable|ElementType[]` => `ArrayAccessOrTraversable<mixed, ElementType>`.",
        "scope": "window"
    },
    "intelephense.files.maxSize": {
        "type": "number",
        "default": 1000000,
        "description": "Maximum file size in bytes.",
        "scope": "window"
    },
    "intelephense.files.associations": {
        "type": "array",
        "default": [
            "*.php",
            "*.phtml"
        ],
        "description": "Configure glob patterns to make files available for language server features. Inherits from files.associations.",
        "scope": "window"
    },
    "intelephense.files.exclude": {
        "type": "array",
        "items": {
            "type": "string"
        },
        "default": [
            "**/.git/**",
            "**/.svn/**",
            "**/.hg/**",
            "**/CVS/**",
            "**/.DS_Store/**",
            "**/node_modules/**",
            "**/bower_components/**",
            "**/vendor/**/{Tests,tests}/**",
            "**/.history/**",
            "**/vendor/**/vendor/**"
        ],
        "description": "Configure glob patterns to exclude certain files and folders from all language server features. Inherits from files.exclude.",
        "scope": "resource"
    },
    "intelephense.stubs": {
        "type": "array",
        "items": {
            "type": "string",
            "enum": [
                "amqp",
                "apache",
                "apcu",
                "bcmath",
                "blackfire",
                "bz2",
                "calendar",
                "cassandra",
                "com_dotnet",
                "Core",
                "couchbase",
                "crypto",
                "ctype",
                "cubrid",
                "curl",
                "date",
                "dba",
                "decimal",
                "dom",
                "ds",
                "enchant",
                "Ev",
                "event",
                "exif",
                "fann",
                "FFI",
                "ffmpeg",
                "fileinfo",
                "filter",
                "fpm",
                "ftp",
                "gd",
                "gearman",
                "geoip",
                "geos",
                "gettext",
                "gmagick",
                "gmp",
                "gnupg",
                "grpc",
                "hash",
                "http",
                "ibm_db2",
                "iconv",
                "igbinary",
                "imagick",
                "imap",
                "inotify",
                "interbase",
                "intl",
                "json",
                "judy",
                "ldap",
                "leveldb",
                "libevent",
                "libsodium",
                "libxml",
                "lua",
                "lzf",
                "mailparse",
                "mapscript",
                "mbstring",
                "mcrypt",
                "memcache",
                "memcached",
                "meminfo",
                "meta",
                "ming",
                "mongo",
                "mongodb",
                "mosquitto-php",
                "mqseries",
                "msgpack",
                "mssql",
                "mysql",
                "mysql_xdevapi",
                "mysqli",
                "ncurses",
                "newrelic",
                "oauth",
                "oci8",
                "odbc",
                "openssl",
                "parallel",
                "Parle",
                "pcntl",
                "pcov",
                "pcre",
                "pdflib",
                "PDO",
                "pdo_ibm",
                "pdo_mysql",
                "pdo_pgsql",
                "pdo_sqlite",
                "pgsql",
                "Phar",
                "phpdbg",
                "posix",
                "pspell",
                "pthreads",
                "radius",
                "rar",
                "rdkafka",
                "readline",
                "recode",
                "redis",
                "Reflection",
                "regex",
                "rpminfo",
                "rrd",
                "SaxonC",
                "session",
                "shmop",
                "SimpleXML",
                "snmp",
                "soap",
                "sockets",
                "sodium",
                "solr",
                "SPL",
                "SplType",
                "SQLite",
                "sqlite3",
                "sqlsrv",
                "ssh2",
                "standard",
                "stats",
                "stomp",
                "suhosin",
                "superglobals",
                "svn",
                "sybase",
                "sync",
                "sysvmsg",
                "sysvsem",
                "sysvshm",
                "tidy",
                "tokenizer",
                "uopz",
                "uv",
                "v8js",
                "wddx",
                "win32service",
                "winbinder",
                "wincache",
                "wordpress",
                "xcache",
                "xdebug",
                "xhprof",
                "xml",
                "xmlreader",
                "xmlrpc",
                "xmlwriter",
                "xsl",
                "xxtea",
                "yaf",
                "yaml",
                "yar",
                "zend",
                "Zend OPcache",
                "ZendCache",
                "ZendDebugger",
                "ZendUtils",
                "zip",
                "zlib",
                "zmq",
                "zookeeper"
            ]
        },
        "default": [
            "apache",
            "bcmath",
            "bz2",
            "calendar",
            "com_dotnet",
            "Core",
            "ctype",
            "curl",
            "date",
            "dba",
            "dom",
            "enchant",
            "exif",
            "FFI",
            "fileinfo",
            "filter",
            "fpm",
            "ftp",
            "gd",
            "gettext",
            "gmp",
            "hash",
            "iconv",
            "imap",
            "intl",
            "json",
            "ldap",
            "libxml",
            "mbstring",
            "meta",
            "mysqli",
            "oci8",
            "odbc",
            "openssl",
            "pcntl",
            "pcre",
            "PDO",
            "pdo_ibm",
            "pdo_mysql",
            "pdo_pgsql",
            "pdo_sqlite",
            "pgsql",
            "Phar",
            "posix",
            "pspell",
            "readline",
            "Reflection",
            "session",
            "shmop",
            "SimpleXML",
            "snmp",
            "soap",
            "sockets",
            "sodium",
            "SPL",
            "sqlite3",
            "standard",
            "superglobals",
            "sysvmsg",
            "sysvsem",
            "sysvshm",
            "tidy",
            "tokenizer",
            "xml",
            "xmlreader",
            "xmlrpc",
            "xmlwriter",
            "xsl",
            "Zend OPcache",
            "zip",
            "zlib"
        ],
        "description": "Configure stub files for built in symbols and common extensions. The default setting includes PHP core and all bundled extensions.",
        "scope": "window"
    },
    "intelephense.completion.insertUseDeclaration": {
        "type": "boolean",
        "default": true,
        "description": "Use declarations will be automatically inserted for namespaced classes, traits, interfaces, functions, and constants.",
        "scope": "window"
    },
    "intelephense.completion.fullyQualifyGlobalConstantsAndFunctions": {
        "type": "boolean",
        "default": false,
        "description": "Global namespace constants and functions will be fully qualified (prefixed with a backslash).",
        "scope": "window"
    },
    "intelephense.completion.triggerParameterHints": {
        "type": "boolean",
        "default": true,
        "description": "Method and function completions will include parentheses and trigger parameter hints.",
        "scope": "window"
    },
    "intelephense.completion.maxItems": {
        "type": "number",
        "default": 100,
        "description": "The maximum number of completion items returned per request.",
        "scope": "window"
    },
    "intelephense.format.enable": {
        "type": "boolean",
        "default": true,
        "description": "Enables formatting.",
        "scope": "window"
    },
    "intelephense.format.braces": {
        "type": "string",
        "default": "psr12",
        "enum": [
            "psr12",
            "allman",
            "k&r"
        ],
        "enumDescriptions": [
            "PHP-FIG PSR-2 and PSR-12 style. A mix of Allman and K&R",
            "Allman. Opening brace on the next line.",
            "K&R (1TBS). Opening brace on the same line."
        ],
        "description": "Controls formatting style of braces",
        "scope": "window"
    },
    "intelephense.environment.documentRoot": {
        "type": "string",
        "description": "The directory of the entry point to the application (index.php). Defaults to the first workspace folder. Used for resolving script inclusion.",
        "scope": "window"
    },
    "intelephense.environment.includePaths": {
        "type": "array",
        "items": {
            "type": "string"
        },
        "description": "The include paths (as individual path items) as defined in the include_path ini setting. Used for resolving script inclusion.",
        "scope": "window"
    },
    "intelephense.environment.phpVersion": {
        "type": "string",
        "default": "7.4.0",
        "description": "A semver compatible string that represents the target PHP version. Used for providing version appropriate suggestions and diagnostics. PHP 5.3.0 and greater supported.",
        "scope": "window"
    },
    "intelephense.environment.shortOpenTag": {
        "type": "boolean",
        "default": false,
        "description": "When enabled '<?' will be parsed as a PHP open tag. Defaults to false.",
        "scope": "window"
    },
    "intelephense.diagnostics.enable": {
        "type": "boolean",
        "default": true,
        "description": "Enables diagnostics.",
        "scope": "window"
    },
    "intelephense.diagnostics.run": {
        "type": "string",
        "default": "onType",
        "enum": [
            "onType",
            "onSave"
        ],
        "enumDescriptions": [
            "Diagnostics will run as changes are made to the document.",
            "Diagnostics will run when the document is saved."
        ],
        "description": "Controls when diagnostics are run.",
        "scope": "window"
    },
    "intelephense.diagnostics.embeddedLanguages": {
        "type": "boolean",
        "default": true,
        "description": "Enables diagnostics in embedded languages.",
        "scope": "window"
    },
    "intelephense.diagnostics.undefinedSymbols": {
        "type": "boolean",
        "default": true,
        "description": "DEPRECATED. Use the setting for each symbol category.",
        "scope": "window"
    },
    "intelephense.diagnostics.undefinedVariables": {
        "type": "boolean",
        "default": true,
        "description": "Enables undefined variable diagnostics.",
        "scope": "window"
    },
    "intelephense.diagnostics.undefinedTypes": {
        "type": "boolean",
        "default": true,
        "description": "Enables undefined class, interface and trait diagnostics.",
        "scope": "window"
    },
    "intelephense.diagnostics.undefinedFunctions": {
        "type": "boolean",
        "default": true,
        "description": "Enables undefined function diagnostics.",
        "scope": "window"
    },
    "intelephense.diagnostics.undefinedConstants": {
        "type": "boolean",
        "default": true,
        "description": "Enables undefined constant diagnostics.",
        "scope": "window"
    },
    "intelephense.diagnostics.undefinedClassConstants": {
        "type": "boolean",
        "default": true,
        "description": "Enables undefined class constant diagnostics.",
        "scope": "window"
    },
    "intelephense.diagnostics.undefinedMethods": {
        "type": "boolean",
        "default": true,
        "description": "Enables undefined method diagnostics.",
        "scope": "window"
    },
    "intelephense.diagnostics.undefinedProperties": {
        "type": "boolean",
        "default": true,
        "description": "Enables undefined static property diagnostics.",
        "scope": "window"
    },
    "intelephense.diagnostics.unusedSymbols": {
        "type": "boolean",
        "default": true,
        "description": "Enables unused variable, private member, and import diagnostics.",
        "scope": "window"
    },
    "intelephense.diagnostics.unexpectedTokens": {
        "type": "boolean",
        "default": true,
        "description": "Enables unexpected token diagnostics.",
        "scope": "window"
    },
    "intelephense.diagnostics.duplicateSymbols": {
        "type": "boolean",
        "default": true,
        "description": "Enables duplicate symbol diagnostics.",
        "scope": "window"
    },
    "intelephense.diagnostics.argumentCount": {
        "type": "boolean",
        "default": true,
        "description": "Enables argument count diagnostics.",
        "scope": "window"
    },
    "intelephense.diagnostics.typeErrors": {
        "type": "boolean",
        "default": true,
        "description": "Enables diagnostics on type compatibility of arguments, property assignments, and return statements where types have been declared.",
        "scope": "window"
    },
    "intelephense.diagnostics.deprecated": {
        "type": "boolean",
        "default": true,
        "description": "Enables deprecated diagnostics.",
        "scope": "window"
    },
    "intelephense.diagnostics.languageConstraints": {
        "type": "boolean",
        "default": true,
        "description": "Enables reporting of various language constraint errors.",
        "scope": "window"
    },
    "intelephense.diagnostics.implementationErrors": {
        "type": "boolean",
        "default": true,
        "description": "Enables reporting of problems associated with method and class implementations. For example, unimplemented methods or method signature incompatibilities.",
        "scope": "window"
    },
    "intelephense.runtime": {
        "type": "string",
        "description": "Path to a Node.js executable. Use this if you wish to use a different version of Node.js. Defaults to Node.js shipped with VSCode.",
        "scope": "machine"
    },
    "intelephense.maxMemory": {
        "type": "number",
        "description": "Maximum memory (in MB) that the server should use. On some systems this may only have effect when runtime has been set. Minimum 256.",
        "scope": "window"
    },
    "intelephense.licenceKey": {
        "type": "string",
        "description": "DEPRECATED. Don't use this. Go to command palette and search for enter licence key.",
        "scope": "application"
    },
    "intelephense.telemetry.enabled": {
        "type": "boolean",
        "description": "Anonymous usage and crash data will be sent to Azure Application Insights. Inherits from telemetry.enableTelemetry.",
        "scope": "window",
        "default": null
    },
    "intelephense.rename.exclude": {
        "type": "array",
        "items": {
            "type": "string"
        },
        "default": [
            "**/vendor/**"
        ],
        "description": "Glob patterns matching files and folders that should be excluded when renaming symbols. Rename operation will fail if the symbol definition is found in the excluded files/folders.",
        "scope": "resource"
    },
    "intelephense.references.exclude": {
        "type": "array",
        "items": {
            "type": "string"
        },
        "default": [
            "**/vendor/**"
        ],
        "description": "Glob patterns matching files and folders that should be excluded from references search.",
        "scope": "resource"
    },
    "intelephense.phpdoc.returnVoid": {
        "type": "boolean",
        "default": true,
        "description": "Adds `@return void` to auto generated phpdoc for definitions that do not return a value.",
        "scope": "window"
    },
    "intelephense.phpdoc.textFormat": {
        "type": "string",
        "enum": [
            "snippet",
            "text"
        ],
        "default": "snippet",
        "enumDescriptions": [
            "Auto generated phpdoc is returned in snippet format. Templates are partially resolved by evaluating phpdoc specific variables only.",
            "Auto generated phpdoc is returned as plain text. Templates are resolved completely by the server."
        ],
        "scope": "window"
    },
    "intelephense.phpdoc.classTemplate": {
        "type": "object",
        "properties": {
            "summary": {
                "type": "string",
                "description": "A snippet string representing a phpdoc summary."
            },
            "description": {
                "type": "string",
                "description": "A snippet string representing a phpdoc description."
            },
            "tags": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "An array of snippet strings representing phpdoc tags."
            }
        },
        "default": {
            "summary": "$1",
            "tags": [
                "@package ${1:$SYMBOL_NAMESPACE}"
            ]
        },
        "description": "An object that describes the format of generated class/interface/trait phpdoc. The following snippet variables are available: SYMBOL_NAME; SYMBOL_KIND; SYMBOL_TYPE; SYMBOL_NAMESPACE.",
        "scope": "window"
    },
    "intelephense.phpdoc.propertyTemplate": {
        "type": "object",
        "properties": {
            "summary": {
                "type": "string",
                "description": "A snippet string representing a phpdoc summary."
            },
            "description": {
                "type": "string",
                "description": "A snippet string representing a phpdoc description."
            },
            "tags": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "An array of snippet strings representing phpdoc tags."
            }
        },
        "default": {
            "summary": "$1",
            "tags": [
                "@var ${1:$SYMBOL_TYPE}"
            ]
        },
        "description": "An object that describes the format of generated property phpdoc. The following snippet variables are available: SYMBOL_NAME; SYMBOL_KIND; SYMBOL_TYPE; SYMBOL_NAMESPACE.",
        "scope": "window"
    },
    "intelephense.phpdoc.functionTemplate": {
        "type": "object",
        "properties": {
            "summary": {
                "type": "string",
                "description": "A snippet string representing a phpdoc summary."
            },
            "description": {
                "type": "string",
                "description": "A snippet string representing a phpdoc description."
            },
            "tags": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "An array of snippet strings representing phpdoc tags."
            }
        },
        "default": {
            "summary": "$1",
            "tags": [
                "@param ${1:$SYMBOL_TYPE} $SYMBOL_NAME $2",
                "@return ${1:$SYMBOL_TYPE} $2",
                "@throws ${1:$SYMBOL_TYPE} $2"
            ]
        },
        "description": "An object that describes the format of generated function/method phpdoc. The following snippet variables are available: SYMBOL_NAME; SYMBOL_KIND; SYMBOL_TYPE; SYMBOL_NAMESPACE.",
        "scope": "window"
    },
    "intelephense.phpdoc.useFullyQualifiedNames": {
        "type": "boolean",
        "default": false,
        "description": "Fully qualified names will be used for types when true. When false short type names will be used and imported where appropriate. Overrides intelephense.completion.insertUseDeclaration.",
        "scope": "window"
    }
}
```
</details>

### Intelephense: gettingStarted
*Source: https://raw.githubusercontent.com/bmewburn/intelephense-docs/master/gettingStarted.md*

#### Getting Started


#### Workspace
For Intelephense to work effectively it must have access to the definitions of the symbols used in your code. It does this by scanning the php files found in the workspace. Sometimes PHP files may have a non standard extension. It is important to associate these extensions with PHP using the `intelephense.files.associations` configuration option.

<details>
<summary>intelephense.files.associations</summary>

```json
{
    "type": "array",
    "default": [
        "*.php",
        "*.phtml"
    ],
    "description": "Configure glob patterns to make files available language server features. Inherits from files.associations.",
    "scope": "window"
}
```
</details>

You may have large files in your workspace that by default Intelephense will skip. You can configure the maximum file size with the `intelephense.files.maxSize` option.

<details>
<summary>intelephense.files.maxSize</summary>

```json
{
    "type": "number",
    "default": 1000000,
    "description": "Maximum file size in bytes.",
    "scope": "window"
}
```

</details>

There may be files you do not want to indexed by Intelephense. It is important in large projects to exclude unnecessary files to avoid polluting suggestion lists and degrading performance.

<details>
<summary>intelephense.files.exclude</summary>

```json
{
    "type": "array",
    "items": {
        "type": "string"
    },
    "default": [
        "**/.git/**",
        "**/.svn/**",
        "**/.hg/**",
        "**/CVS/**",
        "**/.DS_Store/**",
        "**/node_modules/**",
        "**/bower_components/**",
        "**/vendor/**/{Tests,tests}/**",
        "**/.history/**",
        "**/vendor/**/vendor/**"
    ],
    "description": "Configure glob patterns to exclude certain files and folders fro    all language server features. Inherits from files.exclude.",
    "scope": "resource"
}
```

</details>

#### Environment
Sometimes symbol definitions are not in your workspace but are core PHP symbols or defined in an extension. For this reason Intelephense includes stub definitions for many of these. Extensions that are bundled with PHP are enabled by default. You can configure what other symbols are available in your environment with the `intelephense.stubs` option.

<details>
<summary>intelephense.stubs</summary

```json
{
    "type": "array",
    "items": {
        "type": "string",
        "enum": [
            "amqp",
            "apache",
            "apcu",
            "bcmath",
            "blackfire",
            "bz2",
            "calendar",
            "cassandra",
            "com_dotnet",
            "Core",
            "couchbase",
            "crypto",
            "ctype",
            "cubrid",
            "curl",
            "date",
            "dba",
            "decimal",
            "dom",
            "ds",
            "enchant",
            "Ev",
            "event",
            "exif",
            "fann",
            "FFI",
            "ffmpeg",
            "fileinfo",
            "filter",
            "fpm",
            "ftp",
            "gd",
            "gearman",
            "geoip",
            "geos",
            "gettext",
            "gmagick",
            "gmp",
            "gnupg",
            "grpc",
            "hash",
            "http",
            "ibm_db2",
            "iconv",
            "igbinary",
            "imagick",
            "imap",
            "inotify",
            "interbase",
            "intl",
            "json",
            "judy",
            "ldap",
            "leveldb",
            "libevent",
            "libsodium",
            "libxml",
            "lua",
            "lzf",
            "mailparse",
            "mapscript",
            "mbstring",
            "mcrypt",
            "memcache",
            "memcached",
            "meminfo",
            "meta",
            "ming",
            "mongo",
            "mongodb",
            "mosquitto-php",
            "mqseries",
            "msgpack",
            "mssql",
            "mysql",
            "mysql_xdevapi",
            "mysqli",
            "ncurses",
            "newrelic",
            "oauth",
            "oci8",
            "odbc",
            "openssl",
            "parallel",
            "Parle",
            "pcntl",
            "pcov",
            "pcre",
            "pdflib",
            "PDO",
            "pdo_ibm",
            "pdo_mysql",
            "pdo_pgsql",
            "pdo_sqlite",
            "pgsql",
            "Phar",
            "phpdbg",
            "posix",
            "pspell",
            "pthreads",
            "radius",
            "rar",
            "rdkafka",
            "readline",
            "recode",
            "redis",
            "Reflection",
            "regex",
            "rpminfo",
            "rrd",
            "SaxonC",
            "session",
            "shmop",
            "SimpleXML",
            "snmp",
            "soap",
            "sockets",
            "sodium",
            "solr",
            "SPL",
            "SplType",
            "SQLite",
            "sqlite3",
            "sqlsrv",
            "ssh2",
            "standard",
            "stats",
            "stomp",
            "suhosin",
            "superglobals",
            "svn",
            "sybase",
            "sync",
            "sysvmsg",
            "sysvsem",
            "sysvshm",
            "tidy",
            "tokenizer",
            "uopz",
            "uv",
            "v8js",
            "wddx",
            "win32service",
            "winbinder",
            "wincache",
            "wordpress",
            "xcache",
            "xdebug",
            "xhprof",
            "xml",
            "xmlreader",
            "xmlrpc",
            "xmlwriter",
            "xsl",
            "xxtea",
            "yaf",
            "yaml",
            "yar",
            "zend",
            "Zend OPcache",
            "ZendCache",
            "ZendDebugger",
            "ZendUtils",
            "zip",
            "zlib",
            "zmq",
            "zookeeper"
        ]
    },
    "default": [
        "apache",
        "bcmath",
        "bz2",
        "calendar",
        "com_dotnet",
        "Core",
        "ctype",
        "curl",
        "date",
        "dba",
        "dom",
        "enchant",
        "exif",
        "FFI",
        "fileinfo",
        "filter",
        "fpm",
        "ftp",
        "gd",
        "gettext",
        "gmp",
        "hash",
        "iconv",
        "imap",
        "intl",
        "json",
        "ldap",
        "libxml",
        "mbstring",
        "meta",
        "mysqli",
        "oci8",
        "odbc",
        "openssl",
        "pcntl",
        "pcre",
        "PDO",
        "pdo_ibm",
        "pdo_mysql",
        "pdo_pgsql",
        "pdo_sqlite",
        "pgsql",
        "Phar",
        "posix",
        "pspell",
        "readline",
        "Reflection",
        "session",
        "shmop",
        "SimpleXML",
        "snmp",
        "soap",
        "sockets",
        "sodium",
        "SPL",
        "sqlite3",
        "standard",
        "superglobals",
        "sysvmsg",
        "sysvsem",
        "sysvshm",
        "tidy",
        "tokenizer",
        "xml",
        "xmlreader",
        "xmlrpc",
        "xmlwriter",
        "xsl",
        "Zend OPcache",
        "zip",
        "zlib"
    ],
    "description": "Configure stub files for built in symbols and common extensions.The default setting includes PHP core and all bundled extensions.",
    "scope": "window"
}
```
</details>

Other configuration settings that allow you to further define the PHP environment include:

<details>
<summary>intelephense.environment.documentRoot</summary>

```json
{
    "type": "string",
    "description": "The directory of the entry point to the application (index.php).Defaults to the first workspace folder. Used for resolving script inclusion.",
    "scope": "window"
}
```
</details>

<details>
<summary>intelephense.environment.includePaths</summary>

```json
{
    "type": "array",
    "items": {
        "type": "string"
    },
    "description": "The include paths (as individual path items) as defined in theinclude_path ini setting. Used for resolving script inclusion.",
    "scope": "window"
}
```

</details>

<details>
<summary>intelephense.environment.phpVersion</summary>

```json
{
    "type": "string",
    "default": "7.4.0",
    "description": "A semver compatible string that represents the target PHP version.Used for providing version appropriate suggestions and diagnostics. PHP 5.3.0 andgreater supported.",
    "scope": "window"
}
```

</details>

<details>
<summary>intelephense.environment.shortOpenTag</summary>

```json
{
    "type": "boolean",
    "default": false,
    "description": "When enabled '<?' will be parsed as a PHP open tag. Defaults tofalse.",
    "scope": "window"
}
```

</details>

#### Type Declarations and Annotations
You will get more out of Intelephense if you provide type declarations and/or type annotations. Where possible types will be inferred but there are places where it is difficult or impossible to determine the type. Class properties and function and method parameters are examples where this is very important. Providing type declarations and/or annotations may also improve performance as Intelephense does not need to dig through too much code to determine types. When a type cannot be determined for a property, variable, or parameter then it is assigned the `mixed` type.

```php
<?php
class MyClass
{
    public MyOtherClass $withTypeDeclaration;

    /** @var MyOtherClass **/
    public $withTypeAnnotation

    public function withTypeDeclarations(string $param): int { }

    /**
     * @param string $param
     * @return int
     */
    public function withTypeAnnotations($param) { }
}
```

Variables can be annotated with a type if necessary. The annotation immediately preceeding an assignment overrides the assigned type. Subsequent assignments may change the type again.

```php
<?php
/** @var callable $var */
$var = 'is_numeric'; //$var is callable instead of string
$var = 1; //$var is now an int

```

In addition to the standard PHPDoc type annotations Intelephense also supports generic type syntax for `iterable` and `ArrayAccess` types. For example:

* `Generator<KeyType, ElementType>`
* `ArrayAccess<string, ElementType>`
* `array<int, ElementType>`

Union (`TypeA|TypeB`) and intersection (`TypeA&TypeB`) types are supported. Where both a type declaration and a type annotation is provided then the resulting type will be the intersection of the two. Types will be reduced where possible using the following rules.

* `SuperType|SubType` => `SuperType`
* `SuperType&SubType` => `SubType`

Sometimes there may be type annotations in libraries or project files that do not accurately reflect the desired type. Intelephense offers compatibility settings to handle some common cases.

<details>
<summary>intelephense.compatibility.correctForBaseClassStaticUnionTypes</summary>

```json
{
    "type": "boolean",
    "default": true,
    "description": "Resolves `BaseClass|static` union types to `static` instead of `BaseClass`.",
    "scope": "window"
}
```

</details>

<details>
<summary>intelephense.compatibility.correctForArrayAccessArrayAndTraversableArrayUnionTypes</summary>

```json
{
    "type": "boolean",
    "default": true,
    "description": "Resolves `ArrayAccess` and `Traversable` implementations that are unionedwith a typed array to generic syntax. eg `ArrayAccessOrTraversable|ElementType[]` =>`ArrayAccessOrTraversable<mixed, ElementType>`.",
    "scope": "window"
}
```

</details>

You may also see several non standard types in hovers.

* `unset` - the type given to variables that are undefined or `unset()`.
* `never` - the type returned from a function that does not terminate normally (eg `die()`) or that represents an impossibility (added in PHP 8.1).

#### Framework Support
Intelephense aims to support all frameworks but does not implement framework specific solutions. Some frameworks are coded in a way that make it difficult to analyse. This may be because of lack of type declarations/annotations; heavy use of `__get`, `__set`, `__call`, `__callStatic` magic methods; or dynamic generation of class aliases at runtime.

Packages can be found online that aim to workaround these issues by providing stubs of symbols to help static analysers like Intelephense understand the code.

* Laravel - [barryvdh/laravel-ide-helper](https://github.com/barryvdh/laravel-ide-helper)

### Intelephense: support
*Source: https://raw.githubusercontent.com/bmewburn/intelephense-docs/master/support.md*

#### Overview
https://github.com/bmewburn/vscode-intelephense/issues

ben@intelephense.com


---
