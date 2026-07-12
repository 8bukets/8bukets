# Consolidated Knowledge Base

**Last Sync:** 2026-07-12T23:04:51.434507
**System Version:** 1.94

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
- automation (Automated Market Intelligence Ingestion from markposition.wordpress.com enabled)
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

- the automated TypeScript ingestion script (`scripts/ingest_markposition_knowledge.ts`) fetches and merges the latest industry intelligence during each autonomous work cycle.
- analytics generate reports on market trends
- the structured data directly updates the `market_data` section in the unified `system_knowledge.json`.

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
## Autonomous Observation
- **Date**: 2026-05-18T16:31:30.816Z
- **Target**: https://markposition.wordpress.com
- **Title**: (position) mRNA
- **Relationship Map**: Confirmed overlapping identities between Antigravity, Project SOR, software-online-review.com, software-review-platform, and markposition.wordpress.com as the formal Market Intelligence layer.
## Autonomous Observation
- **Date**: 2026-05-19T23:11:27.645Z
- **Target**: https://localhost.co/tools/
- **Title**: Developer Tools - LocalHost.Co
- **Relationship Map**: Confirmed overlapping identities between Antigravity, Project SOR, software-online-review.com, software-review-platform, and markposition.wordpress.com as the formal Market Intelligence layer.



## iCloud Integration (8bukets & antigravity)
**Date:** 2026-05-19

- **Antigravity Architecture**: The iCloud notes indicate a need for deeper integration between the TypeScript autonomous engine and the Python orchestration cycle. Specifically, WorkOrder synchronization between MongoDB and local JSON files should be optimized using a unified Cloud sync service.
- **8Bukets Knowledge**: Data from the 8bukets folders suggests that SystemAuditAgent and ChiefAIOfficer should have explicit 'recovery' phases integrated directly into their feedback loop, bypassing manual interventions entirely.
- **Creativity Enhancement**: A core finding from the iCloud documents is that the CreativityAgent should not only suggest abstract concepts but should map those concepts directly to executable Work Orders in the queue.
## Autonomous Observation
- **Date**: 2026-05-20T08:51:38.680Z
- **Target**: https://cloud.google.com/discover/what-are-ai-agents
- **Title**: What are AI agents? Definition, examples, and types | Google Cloud
- **Context**: Ingested comprehensive definition and architectural overview of AI agents from Google Cloud documentation to ground the project's agentic logic in industry standards.
---

## Autonomous Observation
- **Date**: 2026-05-21T11:37:07.784Z
- **Target**: https://www.forbes.com/business/
- **Title**: Business
- **Context**: Ingested and observed external market or technical intelligence from https://www.forbes.com/business/.
## Autonomous Observation
- **Date**: 2026-05-21T11:37:08.054Z
- **Target**: https://www.forbes.com/innovation/
- **Title**: Innovation
- **Context**: Ingested and observed external market or technical intelligence from https://www.forbes.com/innovation/.
## Autonomous Observation
- **Date**: 2026-05-21T11:37:08.329Z
- **Target**: https://www.forbes.com/money/
- **Title**: Money
- **Context**: Ingested and observed external market or technical intelligence from https://www.forbes.com/money/.
# 📊 Markposition Analytics Report
<a name='table-of-contents'></a>

**Generated on:** 2026-05-21 16:21:58

## Table of Contents
* [General Statistics](#general-statistics)
* [Top 10 Referenced Domains](#top-10-referenced-domains)
* [Top 10 Categories](#top-10-categories)
* [Posts by Year](#posts-by-year)
* [Authors](#authors)

<a name='general-statistics'></a>
## 📈 General Statistics
- **Total Posts:** 679
- **Date Range:** 2020-05-19 to 2022-10-05
- **Unique Domains Linked:** 367

[Back to Top](#table-of-contents)

<a name='top-10-referenced-domains'></a>
## 🌐 Top 10 Referenced Domains

## Table of Contents
- [📊 General Statistics](#general-statistics)
- [🌐 Top 10 Referenced Domains](#top-10-referenced-domains)
- [📂 Top 10 Categories](#top-10-categories)
- [📅 Posts by Year](#posts-by-year)
- [✍️ Authors](#authors)

## 📊 General Statistics
- **Total Posts:** 679
- **Date Range:** 2020-05-19 to 2022-10-05
- **Unique Domains Linked:** 367

> 💡 **Highlight:** The most referenced domain is **skillshop.exceedlms.com** with 23 links.

[Back to Top](#table-of-contents)

## 🌐 Top 10 Referenced Domains
| Domain | Count |
| :--- | :---: |
| skillshop.exceedlms.com | 23 |
| support.google.com | 21 |
| youtube.com | 18 |
| advertising.amazon.com | 16 |
| en.wikipedia.org | 14 |
| google.com | 13 |
| web.facebook.com | 12 |
| developers.google.com | 11 |
| trustarc.com | 11 |
| ads.google.com | 10 |

[Back to Top](#table-of-contents)

<a name='top-10-categories'></a>
## 📂 Top 10 Categories

## 📂 Top 10 Categories
| Category | Count |
| :--- | :---: |
| Ad Ads Advertise | 660 |
| Promotion | 14 |
| Ads | 4 |
| Advertise | 3 |
| Advertising | 3 |
| Online | 2 |

[Back to Top](#table-of-contents)

<a name='posts-by-year'></a>
## 📅 Posts by Year

## 📅 Posts by Year
| Year | Count |
| :--- | :---: |
| 2022 | 235 |
| 2021 | 190 |
| 2020 | 254 |

[Back to Top](#table-of-contents)

<a name='authors'></a>
## ✍️ Authors
- Filip Keser: 679 posts

## Top 10 Referenced Domains
| Domain | Count | Distribution |
| :--- | :---: | :--- |
| skillshop.exceedlms.com | 23 | ████████████████████ |
| support.google.com | 21 | ██████████████████░░ |
| youtube.com | 18 | ████████████████░░░░ |
| advertising.amazon.com | 16 | ██████████████░░░░░░ |
| en.wikipedia.org | 14 | ████████████░░░░░░░░ |
| google.com | 13 | ███████████░░░░░░░░░ |
| web.facebook.com | 12 | ██████████░░░░░░░░░░ |
| developers.google.com | 11 | ██████████░░░░░░░░░░ |
| trustarc.com | 11 | ██████████░░░░░░░░░░ |
| ads.google.com | 10 | █████████░░░░░░░░░░░ |

## Top 10 Categories
| Category | Count | Distribution |
| :--- | :---: | :--- |
| Ad Ads Advertise | 660 | ████████████████████ |
| Promotion | 14 | ░░░░░░░░░░░░░░░░░░░░ |
| Ads | 4 | ░░░░░░░░░░░░░░░░░░░░ |
| Advertise | 3 | ░░░░░░░░░░░░░░░░░░░░ |
| Advertising | 3 | ░░░░░░░░░░░░░░░░░░░░ |
| Online | 2 | ░░░░░░░░░░░░░░░░░░░░ |

## Posts by Year
| Year | Count | Distribution |
| :--- | :---: | :--- |
| 2022 | 235 | ███████████████████░ |
| 2021 | 190 | ███████████████░░░░░ |
| 2020 | 254 | ████████████████████ |

## ✍️ Authors
- **Filip Keser**: 679 posts

[Back to Top](#table-of-contents)

---

## System Intelligence & Outlook
- Scaling Strategy: Implementing simultaneous execution across agent tiers.
- R&D Strategy: Developing realistic simulations for human-agent interaction.
- Operational Strategy: Enhancing agent debate and feedback loops.
- Positive outlook on multimodal scaling and autonomous research agents. Strategic focus on privacy-preserving AI and security frameworks detected. Infrastructure expansion indicates preparation for massive-scale deployment.

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


### The DESIGN.md specification

#### Introduction
Learn

The formal specification for the DESIGN.md format — token schema, section structure, and type system.

A DESIGN.md file has two layers. The YAML front matter contains machine-readable design tokens — the precise values agents use to enforce consistency. The markdown body provides human-readable design rationale organized into ## sections. Prose may use descriptive color names (e.g., “Midnight Forest Green”) that correspond to systematic token names (e.g., primary ). The tokens are the normative values; the prose provides context for how to apply them.

The spec is a foundation, not a prescription . It provides common ground that agents, tools, and teams can rely on, while preserving the freedom to extend the format for domain-specific needs.

#### Design tokens
DESIGN.md embeds design tokens as YAML front matter at the beginning of the file. The front matter block must begin with a line containing exactly --- and end with a line containing exactly --- . The YAML content between these delimiters follows the schema defined below.

The token system is inspired by the W3C Design Token Format . Tokens are easily converted to and from tokens.json , Figma variables, and Tailwind theme configs.

```
---
version: alpha
name: Daylight Prestige
colors:
primary: "#1A1C1E"
secondary: "#6C7278"
tertiary: "#B8422E"
typography:
h1:
fontFamily: Public Sans
fontSize: 48px
fontWeight: 600
lineHeight: 1.1
letterSpacing: -0.02em
rounded:
sm: 4px
md: 8px
spacing:
sm: 8px
md: 16px
components:
button-primary:
backgroundColor: "{colors.primary-60}"
textColor: "{colors.primary-20}"
rounded: "{rounded.md}"
padding: 12px
---
```

#### Schema
```
version: <string>          # optional, current version: "alpha"
name: <string>
description: <string>      # optional
colors:
<token-name>: <Color>
typography:
<token-name>: <Typography>
rounded:
<scale-level>: <Dimension>
spacing:
<scale-level>: <Dimension | number>
components:
<component-name>:
<token-name>: <string | token reference>
```
The <scale-level> placeholder represents a named level in a sizing or spacing scale. Common level names include xs , sm , md , lg , xl , and full . Any descriptive string key is valid.

#### Token types
#### Typography properties


#### Token references
A token reference is wrapped in curly braces and contains an object path to another value in the YAML tree. For most token groups, the reference must point to a primitive value (e.g., {colors.primary-60} ), not a group. Within the components section, references to composite values (e.g., {typography.label-md} ) are permitted.
```
components:
button-primary:
backgroundColor: "{colors.primary-60}"
textColor: "{colors.primary-20}"
rounded: "{rounded.md}"
```

#### Sections
Every DESIGN.md follows the same structure. Sections can be omitted if they are not relevant to the project, but those present should appear in the sequence listed below. All sections use ## headings. An optional # heading may appear for document titling purposes but is not parsed as a section.

The section structure is intentionally open-ended. The canonical sections provide a shared vocabulary; design systems are free to add domain-specific sections beyond these.

#### Section order


#### Overview
Also known as “Brand & Style.” A holistic description of the product’s look and feel. This section defines the brand personality, target audience, and the emotional response the UI should evoke. It serves as foundational context when a specific rule or token is not defined.
```
## Overview
A calm, professional interface for a healthcare scheduling platform.
Accessibility-first design with high contrast and generous touch targets.
```

#### Colors
Defines the color palettes for the design system. At least the primary palette should be defined. Additional palettes may be named freely; a common convention is primary , secondary , tertiary , and neutral .
```
## Colors
The palette is rooted in high-contrast neutrals and a single accent color.
- **Primary (#1A1C1E):** Deep ink for headlines and core text.
- **Secondary (#6C7278):** Sophisticated slate for borders, captions, metadata.
- **Tertiary (#B8422E):** The sole driver for interaction.
- **Neutral (#F7F5F2):** Warm limestone foundation.
```
Design tokens: A map<string, Color> mapping the token name to its hex value.
```
colors:
primary: "#1A1C1E"
secondary: "#6C7278"
tertiary: "#B8422E"
neutral: "#F7F5F2"
```

#### Typography
Defines typography levels. Most design systems have 9–15 levels, each with a semantic role (headline, body, label) and size variant (small, medium, large).
```
## Typography
- **Headlines:** Public Sans Semi-Bold for an institutional voice.
- **Body:** Public Sans Regular at 16px for long-form readability.
- **Labels:** Space Grotesk for technical data and metadata.
```
Design tokens: A map<string, Typography> mapping the token name to its typography properties.
```
typography:
h1:
fontFamily: Public Sans
fontSize: 48px
fontWeight: 600
lineHeight: 1.1
letterSpacing: -0.02em
body-md:
fontFamily: Public Sans
fontSize: 16px
fontWeight: 400
lineHeight: 1.6
label-caps:
fontFamily: Space Grotesk
fontSize: 12px
fontWeight: 500
lineHeight: 1
letterSpacing: 0.1em
```

#### Layout
Also known as “Layout & Spacing.” Describes the layout and spacing strategy — grid models, spacing scales, and containment principles.
```
## Layout
The layout follows a Fluid Grid model for mobile and a Fixed-Max-Width
Grid for desktop (max 1200px). A strict 8px spacing scale is used.
```
Design tokens: A map<string, Dimension | number> mapping the spacing scale identifier to a dimension or unitless number (e.g., column counts or ratios).
```
spacing:
base: 16px
xs: 4px
sm: 8px
md: 16px
lg: 32px
xl: 64px
gutter: 24px
margin: 32px
```

#### Elevation & Depth
Also known as “Elevation.” Describes how visual hierarchy is conveyed. For designs that use shadows, it defines the shadow properties. For flat designs, it explains the alternative methods (borders, tonal layers, color contrast).
```
## Elevation & Depth
Depth is achieved through tonal layers rather than heavy shadows.
Background uses a soft off-white; primary content sits on pure white cards.
```

#### Shapes
Describes how visual elements are shaped — corner radii, edge treatments, and the overall shape language.
```
## Shapes
All interactive elements use a minimal 4px corner radius.
Modern enough to feel current, rigid enough to feel engineered.
```
Design tokens: A map<string, Dimension> mapping the scale level to the corner radius.
```
rounded:
sm: 4px
md: 8px
lg: 12px
full: 9999px
```

#### Components
Style guidance for component atoms. The spec defines common component types — Buttons, Chips, Lists, Inputs, Checkboxes, Radio buttons, Tooltips — but design systems are encouraged to define additional components relevant to their domain.
```
## Components
- **Buttons**: Rounded (8px), primary uses brand blue fill, secondary uses outline
- **Inputs**: 1px border, surface-variant background, 12px padding
- **Cards**: No elevation, 1px outline border, 12px corner radius
```
Design tokens: A map<string, map<string, string>> mapping a component identifier to a group of sub-token properties. Token values may be literal values or references to previously defined tokens.
Variants. A component may have variants for different UI states (hover, active, pressed). Variants are defined as separate component entries with a related key name.
```
components:
button-primary:
backgroundColor: "{colors.primary-60}"
textColor: "{colors.primary-20}"
rounded: "{rounded.md}"
padding: 12px
button-primary-hover:
backgroundColor: "{colors.primary-70}"
```

#### Do’s and Don’ts
Practical guidelines and common pitfalls. These act as guardrails during generation.
```
## Do's and Don'ts
- Do use the primary color only for the single most important action per screen
- Don't mix rounded and sharp corners in the same view
- Do maintain WCAG AA contrast ratios (4.5:1 for normal text)
- Don't use more than two font weights on a single screen
```

#### Consumer behavior for unknown content
The spec is designed to be extended. When a consumer encounters content not defined by this specification:

#### Recommended token names
The following names are commonly used across design systems. They are not required but are provided as guidance for consistency.

Colors: primary , secondary , tertiary , neutral , surface , on-surface , error

Typography: headline-display , headline-lg , headline-md , body-lg , body-md , body-sm , label-lg , label-md , label-sm

Rounded: none , sm , md , lg , xl , full

## 2. Google Innovation & AI
- **[Global network](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/)**
  * News about how Google is building infrastructure for the 21st century.
- **[We’re strengthening our presence in Alabama through new investments and community support.](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/alabama-investment-june-2026/)**
  * Google has announced a $1.5 billion investment for 2026 and 2027 to expand its data center campus in Jackson County, Alabama. Operating since 2019 on a repurposed former coal-plant site, the facility powers essential digital services while driving long-term regional growth.As part of this expansion,...
- **[Our new community investments in Virginia support local jobs and expand energy affordability.](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/virginia-community-investments/)**
  * Virginia has been a home for Google for more than a decade, with an office in Reston and data centers in Loudoun and Prince William Counties. Today, we’re deepening our commitment to the Commonwealth with new community investments that will support thousands of local jobs, prepare the next-generatio...
- **[Google Cloud](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/)**
  * Google Cloud helps companies empower their employees, serve their customers and build what’s next for their business.
- **[Cloud Next ‘26: Momentum and innovation at Google scale](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/)**
  * The pace of technological change since last year’s Cloud Next has never been faster, and Google Cloud has incredible momentum.Our first-party models now process more than 16 billion tokens per minute via direct API use by our customers, up from 10 billion last quarter. To support and drive this grow...
- **[7 highlights from Google Cloud Next ‘26](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/google-cloud-next-26-recap/)**
  * When we gathered at Google Cloud Next a year ago, we talked about how generative AI was beginning to change the way we work. This week in Vegas, we showcased how AI is not only transforming work, it’s running at scale.We’ve officially entered the agentic era. AI is becoming an active partner — an ag...
- **[View the collection](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/how-google-does-it-security-series/)**
  * In our Google Cloud series “How Google Does It,” we share exclusive, behind-the-scenes looks at how Google approaches some of today's most pressing security topics, challenges and concerns, straight from Google experts. Learn about how we modernize threat detection, build AI agents to boost defender...
- **[View the collection](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/next-2026/)**
  * Agentic technology is revolutionizing how we work. Today, nearly 75% of Google Cloud customers are using our AI products to power their businesses, with 330 Google Cloud customers processing over a trillion tokens each in the past 12 months. And the agentic enterprise transformation is accelerating:...
- **[Gemini models](https://blog.google/innovation-and-ai/models-and-research/gemini-models/)**
- **[Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)**
  * Today, we’re introducing Gemini 3.5, our latest family of models combining frontier intelligence with action. This represents a major leap forward in building more capable, intelligent agents. We’re kicking off the series by releasing 3.5 Flash. It delivers frontier performance for agents and coding...
- **[Fluid, natural voice translation with Gemini 3.5 Live Translate](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-live-3-5-translate/)**
  * Twenty years ago, translation at Google began as one of our pioneering machine learning experiments to turn the science of language into the magic of human connection. That experiment has come a long way with over a trillion words being translated for billions of users across our products every mont...
- **[9 demos of Gemini Omni and Gemini 3.5 in action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-3-5-videos/)**
  * At Google I/O 2026, we announced our latest models: Gemini Omni and the Gemini 3.5 family of models.Gemini Omni is our new model that can create anything from any input, starting with video. With Omni, you can combine images, audio, video and text as input and generate high-quality videos grounded i...
- **[Introducing Gemini Omni](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/)**
  * Last year, Nano Banana brought Gemini's intelligence to image generation and editing. Since then, it’s helped millions of people restore old photos, design from sketches and visualize ideas in ways that weren’t possible before. From the start we built Gemini to be natively multimodal from the ground...
- **[Introducing computer use in Gemini 3.5 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/)**
  * Computer use is now a built-in tool supported in Gemini 3.5 Flash, delivering our best performance yet for agentic computer use tasks. Previously only available as a standalone Gemini 2.5 computer use model, computer use is now integrated natively in the main Gemini Flash model. Gemini already excel...
- **[Google DeepMind](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/)**
  * News from Google DeepMind about how we're building AI responsibly to benefit everyone.
- **[We’re launching the Google DeepMind Accelerator program in Asia Pacific to tackle environmental risks.](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/accelerator-ai-for-the-planet/)**
  * The Asia-Pacific region is a global engine for economic growth, but it's also highly vulnerable to climate change. While green technologies are gaining momentum, a recent report shows they aren’t scaling fast enough to keep up with the region’s rising environmental risks.To help innovators tackle th...
- **[Google DeepMind and A24 announce first-of-its-kind research partnership](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/deepmind-a24-research-partnership/)**
  * Today, Google DeepMind and A24 are announcing a first-of-its-kind partnership focused on research. The collaboration pairs a world-leading research lab with the industry’s most filmmaker-forward studio to help artists develop new workflows and techniques. This ensures the tools of the future are sha...
- **[Simulate real-world places with Project Genie and Street View](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie-expands/)**
  * Genie is our general-purpose world model capable of generating diverse, interactive environments. Since launching, Genie has become a foundational tool for research, enabling agents to learn and reason in complex virtual settings and even helping Waymo simulate hyper-realistic road environments.Now,...
- **[Running Guide agent: A step towards running unbounded](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/running-guide-agent/)**
  * For blind and low-vision (BLV) athletes, running has traditionally required a physical tether — whether it’s a human guide or a painted track line. Today, we are excited to share how we’re taking steps towards changing that with the Running Guide agent, an accessibility agent that uses real-time env...
- **[Google Labs](https://blog.google/innovation-and-ai/models-and-research/google-labs/)**
  * News about Google Labs, Google's home for the latest AI experiments and technology.
- **[Meet Dreambeans, an app that connects you with what matters](https://blog.google/innovation-and-ai/models-and-research/google-labs/dreambeans/)**
  * In a world of endless scrolling and digital noise, Google Labs is introducing our latest experiment: Dreambeans. It uses Google’s latest AI capabilities, like Personal Intelligence and Nano Banana 2, to proactively dream up personalized daily stories that cut through the clutter and connect you to w...
- **[New agents, mobile apps and Gemini Omni for Google Flow and Google Flow Music](https://blog.google/innovation-and-ai/models-and-research/google-labs/flow-updates/)**
  * On last year’s I/O stage, we introduced Google Flow, built with and for filmmakers. Since then we expanded Flow into an AI creative studio, with new capabilities in video and image generation and editing, and launched in over 140 countries around the world. Earlier this year we added a new tool to o...
- **[Pomelli adds new ways to build brand content and design websites.](https://blog.google/innovation-and-ai/models-and-research/google-labs/pomelli-agentic-capabilities/)**
  * Last year we introduced Pomelli in Google Labs to help small and medium-sized businesses create on-brand content. Since then, we’ve seen millions of professional product shots, social campaigns and ads come to life.Today, we’re making it even easier to create content for your business with new agent...
- **[We’re introducing new ways to design in real time with Stitch.](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-updates/)**
  * Today at I/O, we announced new ways to vibe design with Stitch, transforming your design experience into a live, collaborative partnership with the Stitch Agent — allowing you to design, stream and steer iterations in real time.Whether you start with a text prompt, use your voice or bring existing c...
- **[Google Research](https://blog.google/innovation-and-ai/models-and-research/google-research/)**
- **[New research shows how AMIE, our medical AI, could help manage health conditions.](https://blog.google/innovation-and-ai/models-and-research/google-research/amie-for-disease-management-in-nature/)**
  * Giving a diagnosis is the first step in treating a patient. Once a diagnosis is established, the challenge becomes managing a health condition over time — tracking symptoms across multiple appointments, parsing guidelines as they’re updated and fine-tuning medications.Research published today in “Na...
- **[A new experiment brings better group meetings to Google Beam](https://blog.google/innovation-and-ai/models-and-research/google-research/google-beam-group-meetings/)**
  * While video conferencing tools keep us connected, users can still struggle to feel included in the conversation. Trying to read subtle emotions in a sea of tiny boxes may leave remote participants feeling like observers rather than engaged participants. Google Beam, our true-to-life video communicat...
- **[Quantum computing](https://blog.google/innovation-and-ai/models-and-research/quantum-computing/)**
  * News from Google Quantum AI about how we're building quantum computing for unsolvable problems.
- **[Our new initiative to apply quantum science and AI to the life sciences](https://blog.google/innovation-and-ai/models-and-research/quantum-computing/repliqa-quantum-computing-life-sciences/)**
  * Understanding human biology and health at the molecular level is one of science’s greatest challenges. To help tackle this, we’re launching the Research Program at the Intersection of the Life Sciences and Quantum AI (REPLIQA).REPLIQA is an effort by Google Quantum AI and Google.org to apply advance...
- **[Answering your trending questions on World Quantum Day](https://blog.google/innovation-and-ai/models-and-research/quantum-computing/world-quantum-day-2026/)**
  * The discovery of quantum mechanics fundamentally changed how we understand the natural world. In 1981, physicist Richard Feynman famously observed that because nature is quantum, we would eventually need to build computers that operate on those same principles to truly understand it. Building these ...
- **[Save time and grow your business with new Gemini tools](https://blog.google/innovation-and-ai/products/gemini-app/gemini-features-for-businesses/)**
  * Small businesses are the true engine of the global economy, yet entrepreneurs often find themselves stretched thin, playing the roles of CEO, CMO and customer service team all before lunch. AI holds incredible promise to act as an extension of your team, but to be truly helpful, it needs to remember...
- **[5 ways to learn with study notebooks in the Gemini app](https://blog.google/innovation-and-ai/products/gemini-app/gemini-study-notebooks/)**
  * Studying can feel overwhelming, especially when you don't know where to start or what to focus on next. That’s why we’re introducing study notebooks in the Gemini app.Study notebooks are designed specifically for students. As a goal-oriented learning space, they generate personalized lessons based o...
- **[The Gemini app is bringing personalized image creation to more users.](https://blog.google/innovation-and-ai/products/gemini-app/personal-intelligence-nano-banana-us-expansion/)**
  * Personal Intelligence makes the Gemini app feel tailored to you. With your permission, it pulls from Google tools like Gmail, Google Photos, YouTube and Search to provide the most relevant responses — like an assistant who knows you.Starting today, all eligible users in the U.S. 1 can experience dee...
- **[View more from NotebookLM](https://blog.google/innovation-and-ai/products/notebooklm/)**
- **[Do better research with NotebookLM](https://blog.google/innovation-and-ai/products/notebooklm/better-research-notebooklm/)**
  * Three years ago we launched NotebookLM as an experimental AI product from Google Labs to help you understand anything. Millions of people and organizations turn to NotebookLM as a collaborative knowledge and research partner because it helps them organize their thinking, identify deeper connections ...
- **[Generate your own Cinematic Video Overviews in NotebookLM.](https://blog.google/innovation-and-ai/products/notebooklm/generate-your-own-cinematic-video-overviews-in-notebooklm/)**
  * NotebookLM is introducing Cinematic Video Overviews, a major update to its AI-powered video creation capabilities. This new feature moves beyond narrated slides in Video Overviews to create unique, immersive videos tailored to you.Using a combination of our advanced AI models, including Gemini 3, Na...
- **[Dive deeper into I/O 2026 with NotebookLM.](https://blog.google/innovation-and-ai/products/notebooklm/notebooklm-google-io-2026/)**
  * Google I/O is always jam-packed with announcements, demos and launches — and this year was no exception. Whether you’re looking to dive into the details of a new product or just want to catch up on news you might have missed, you can see it all in the notebook we’ve created using Google NotebookLM.T...
- **[Ask a Techspert: What is vibe coding?](https://blog.google/innovation-and-ai/products/techspert-what-is-vibe-coding/)**
  * You’ve heard of coding, and you’ve definitely heard of vibes. But what do they have to do with each other? Vibe coding is an emerging field of development, thanks to AI. It’s helping people build websites, apps and more. To get a better idea of how vibe coding works, why it’s becoming increasingly p...
- **[I/O 2026: Welcome to the agentic Gemini era](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/)**
  * Editor’s note: Below is an edited transcript of Google CEO Sundar Pichai’s remarks at Google I/O 2026, adapted to include more of what was announced on stage. See all the announcements in our collection.It’s been an extraordinary year since our last I/O, a period of relentless shipping, technology a...
- **[Ask an AI expert: What exactly is the full stack?](https://blog.google/innovation-and-ai/technology/ai/full-stack-ai-explainer/)**
  * If you’ve spent any time lately reading about AI or using AI tools, you’ve probably heard about “full-stack” AI and app development. Our unique full-stack approach to AI lets us deliver powerful, cost-efficient products to expert developers and everyday users alike. But what exactly does it mean whe...
- **[The latest AI news we announced in May 2026](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-may-2026/)**
  * For more than 20 years, we’ve invested in machine learning and AI research, tools and infrastructure to build products that make everyday life better for more people. Teams across Google are working on ways to unlock AI’s benefits in fields as wide-ranging as healthcare, crisis response and educatio...
- **[How we used Gemini to build Google I/O 2026](https://blog.google/innovation-and-ai/technology/ai/io-2026-google-ai/)**
  * Google I/O 2026 was all about how we’re making AI helpful for everyone in new ways. But we didn’t just make announcements about our innovations in AI at I/O — we used those tools to bring I/O to life, too.It’s both a strange and exciting moment to be building anything. We're living through an incred...
- **[Catch up on 12 major I/O 2026 moments](https://blog.google/innovation-and-ai/technology/ai/io-2026-keynote-moment-videos/)**
  * Our biggest, boldest new developments took center stage at Google I/O 2026. We announced technical breakthroughs, like Gemini Omni’s ability to create anything from any input, starting with video. And we shared product updates to help you day-to-day, like the brand new, intelligent Search box that w...
- **[Developer tools](https://blog.google/innovation-and-ai/technology/developers-tools/)**
- **[Bringing the latest Gemini models to Apple developers](https://blog.google/innovation-and-ai/technology/developers-tools/bringing-gemini-models-to-apple-developers/)**
  * Updated June 9, 2026Apple’s Worldwide Developers Conference (WWDC) kicked off this week, and we’re excited to share that Apple developers can now securely call cloud-hosted Gemini models using the Foundation Models framework, and access Gemini in Xcode. This announcement gives Apple developers seaml...
- **[DiffusionGemma: 4x faster text generation](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/)**
  * Today, we’re introducing DiffusionGemma, an experimental open model that explores text diffusion, an exceptionally fast approach to text generation. Released under an Apache 2.0 license, this 26B Mixture of Experts (MoE) model moves beyond the sequential token-by-token processing of typical autoregr...
- **[See what 3 builders are making with Gemma 4](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4-builders/)**
  * We recently released Gemma 4, our most capable open models to date. Since then, they have been downloaded more than 150 million times, and we’ve been expanding the family’s capabilities. We introduced Multi-Token Prediction (MTP) to accelerate inference, and recently released the 12B Unified model a...
- **[Interactions API: our primary interface for Gemini models and agents](https://blog.google/innovation-and-ai/technology/developers-tools/interactions-api-general-availability/)**
  * Today we're announcing that the Interactions API has reached general availability and is now our primary API for interacting with Gemini models and agents. We launched its public beta in December 2025, and it has quickly become developers’ favorite way to build applications with Gemini.With this GA ...
- **[Gemma 4 QAT models: Optimizing model compression for mobile and laptop efficiency](https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/)**
  * Since releasing Gemma 4 two months ago, we've been continuously working to expand its capabilities. First, we introduced Multi-Token Prediction (MTP) to accelerate inference, and just a couple of days ago, we released a 12B model to bridge the gap between our E4B and 26B MOE models.Today, we are rel...
- **[View more from Health](https://blog.google/innovation-and-ai/technology/health/)**
  * The latest news about Google's health-related research and initiatives....
- **[A more personal digital health experience for people in Europe](https://blog.google/innovation-and-ai/technology/health/google-docmorris-partnership/)**
  * From understanding symptoms to managing prescriptions, navigating healthcare isn't always straightforward. Technology can help make it simpler and more personal. That's why we're partnering with DocMorris, one of Europe’s leading online pharmacies, to help build a more intuitive and supportive digit...
- **[Announcing the winners of the MedGemma Impact Challenge](https://blog.google/innovation-and-ai/technology/health/med-gemma-impact-challenge/)**
  * Launched in late 2024, Google’s Health AI Developer Foundations (HAI-DEF) program was created to provide global developers with open weight models, subject to the HAI-DEF Terms of Use, to solve complex healthcare challenges. Following the addition of MedGemma, Google's most capable open model for He...
- **[An update on our mental health work](https://blog.google/innovation-and-ai/technology/health/mental-health-updates/)**
  * Mental health is one of the most significant public health challenges today, impacting over one billion people around the world. For many years, Google has been committed to helping people find high-quality information and crisis support in the moments they need it most. Our work on mental health ha...
- **[Google Research](https://blog.google/innovation-and-ai/technology/research/)**
- **[4 ways researchers are collaborating with Co-Scientist to solve big problems](https://blog.google/innovation-and-ai/technology/research/co-scientist-research-problems/)**
  * We recently published our latest research on Co-Scientist, a collaborative AI designed for structured scientific thinking to help researchers develop new hypotheses in life sciences and beyond.The system is made up of a coalition of specialized agents that work together in three distinct phases. Fir...
- **[Gemini for Science: AI experiments and tools for a new era of discovery](https://blog.google/innovation-and-ai/technology/research/gemini-for-science-io-2026/)**
  * For centuries, the scientific method has been the greatest engine of human progress. At Google, our mission is deeply rooted in building tools to accelerate it. We believe that a new era of discovery won’t come from narrow, specialized models, but general agents that empower researchers across every...
- **[Towards a world where no one is surprised by a natural disaster](https://blog.google/innovation-and-ai/technology/research/helping-communities-prepare-for-natural-disasters/)**
  * The world is experiencing a dramatic rise in extreme weather events and natural disasters, devastating communities. Over the past decade, our teams at Google have worked to make helpful information available to people at times of crises — often when they need it most.We’ve advanced AI-based breakthr...
- **[Building superconducting and neutral atom quantum computers](https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/)**
  * At Google Quantum AI, our mission has always been clear: build quantum computing for otherwise unsolvable problems. For over a decade, we have pioneered the development of superconducting quantum bits (qubits), achieving milestones like beyond-classical performance, error correction and verifiable q...
- **[Safety & Security](https://blog.google/innovation-and-ai/technology/safety-security/)**
  * We're committed to your privacy and security. Get news on what we're doing to keep you safe.
- **[How we're combatting AI scams with security, legislation and more](https://blog.google/innovation-and-ai/technology/safety-security/combatting-ai-scams/)**
  * You’ve seen the texts: fake package alerts, urgent bank warnings, panicked messages about your compromised account. Behind them is an AI-powered cybercrime network built to steal your passwords and credit cards. Today, we’re fighting back.We’re filing a lawsuit to dismantle their infrastructure, coo...
- **[Quantum frontiers may be closer than they appear](https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/)**
  * Google’s introducing a 2029 timeline to secure the quantum era with post-quantum cryptography (PQC) migration.Last month, we called to secure the quantum era before a future quantum computer can break current encryption. This new timeline reflects migration needs for the PQC era in light of progress...
- **[Our latest fraud and scams advisory](https://blog.google/innovation-and-ai/technology/safety-security/fraud-scams-advisory-june-2026/)**
  * Scams continue to be a persistent global challenge, fueled by sophisticated transnational crime groups who seek to exploit people online for financial gain. According to the NASDAQ Global Financial Crime Report, total global fraud losses are estimated at nearly $580 billion for 2025. Furthermore, gl...
- **[Our fight against fraud: 5 ways we’re keeping you safer](https://blog.google/innovation-and-ai/technology/safety-security/scams-fraud-protection/)**
  * Online fraud is highly disruptive, and can have a painful financial and emotional impact on people. Google is committed to tackling this challenge head-on. As part of that effort, this week, experts from across government, technology, consumer groups and academia are gathering in Zurich for the seco...
- **[Android XR lights up Sphere in Las Vegas for CES.](https://blog.google/innovation-and-ai/technology/xr-ar/android-xr-sphere-ces-2026/)**
  * Since introducing Android XR, our operating system for next generation headsets and glasses, we’ve begun moving from vision to reality. Samsung recently launched the Galaxy XR and we just previewed upcoming devices on The Android Show | XR Edition.Combining Gemini with an awareness of your surroundi...
- **[Reservations are open for XREAL AURA — plus, see more news from AWE 2026.](https://blog.google/innovation-and-ai/technology/xr-ar/awe-2026/)**
  * At AWE 2026, we’re showcasing how the Android XR ecosystem is growing alongside our partners. In today’s joint keynote, we announced that reservations are now open for XREAL AURA, coming this fall. AURA is XREAL's first wired XR glasses powered by Android XR and using the Snapdragon® Reality Elite P...
- **[See all product updates](https://blog.google/products-and-platforms/)**
- **[Chromebooks](https://blog.google/products-and-platforms/devices/chromebooks/)**
  * The latest news about Chromebook.
- **[Google Nest](https://blog.google/products-and-platforms/devices/google-nest/)**
  * News and updates about Google Nest.
- **[Intelligent eyewear is coming this fall](https://blog.google/products-and-platforms/platforms/android/android-xr-io-2026/)**
  * This is an exciting time for Android XR, the platform we’ve built with Samsung and Qualcomm, as Gemini continues to unlock new experiences across headsets, glasses and everything in between.Today at Google I/O 2026, we shared more about intelligent eyewear: glasses that deliver help in the moment wi...
- **[Google Play](https://blog.google/products-and-platforms/platforms/google-play/)**
  * News about Google Play, home to millions of the latest apps, games, music, movies, TV shows, books and magazines you can enjoy and share.
- **[Learning & Education](https://blog.google/products-and-platforms/products/education/)**
  * The official source for information about Google’s learning and education-related efforts.
- **[NotebookLM is transforming student success at FSU](https://blog.google/products-and-platforms/products/education/florida-state-university-notebooklm/)**
  * At Florida State University, we believe technology should move students from passive consumers to active learners. While we expect every new innovation to meet this standard, we are specifically seeking solutions that raise the bar entirely. We are inspired by advancements like Google NotebookLM, an...
- **[Gemini models](https://blog.google/products-and-platforms/products/gemini/)**
  * The latest news about Gemini. Chat to start writing, planning, learning and more with Google AI.
- **[Try these 3 Google AI tools to help find your next job.](https://blog.google/products-and-platforms/products/gemini/find-job-with-google-ai-tools/)**
  * Job hunting can be a slog. But with a few Google AI tools, you can simplify the process from start to finish.Career Dreamer: The first step in landing a job is finding one worth applying to. Using Career Dreamer, you can brainstorm different roles to pursue based on your interests and experiences.No...
- **[View more from XR and AR](https://blog.google/products-and-platforms/products/google-ar-vr/)**
- **[Google Health](https://blog.google/products-and-platforms/products/google-health/)**
  * A new relationship with your health.
- **[Google Workspace](https://blog.google/products-and-platforms/products/workspace/)**
  * News about Google Workspace — the best way to create, communicate and collaborate.
- **[Start building with Nano Banana 2 Lite and Gemini Omni Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/)**
  * Today, we’re making it faster and easier to experiment, refine and scale your ideas with two major releases:Introducing Nano Banana 2 Lite: Our fastest, most cost-efficient image model in the Nano Banana family yet, built for high throughput, speed and scale. Nano Banana 2 Lite is available today in...
- **[Three new satellites join the fight against wildfires](https://blog.google/innovation-and-ai/models-and-research/google-research/firesat-satellites/)**
  * Today, three new FireSat satellites successfully launched from Vandenberg Space Force Base in California. This expands the FireSat program, a global initiative led by the nonprofit Earth Fire Alliance (EFA) to create an unprecedented wildfire dataset. Google Research has teamed up with leaders in th...
- **[Gemini Spark updates: macOS launch, connected apps and more](https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-june-2026/)**
  * Today, we’re rolling out updates to Gemini Spark that make it even more helpful, from a new desktop experience to deeper connections with your favorite apps. Here’s a look at what’s new:Bring Gemini Spark to your MacWe’re bringing Spark to the Gemini macOS app to help you automate time-consuming tas...
- **[The latest AI news we announced in June 2026](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-june-2026/)**
  * For more than 20 years, we’ve invested in machine learning and AI research, tools and infrastructure to build products that make everyday life better for more people. Teams across Google are working on ways to unlock AI’s benefits in fields as wide-ranging as healthcare, crisis response and educatio...
- **[Expanding Managed Agents in the Gemini API](https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api/)**
  * Today we’re announcing new capabilities for Managed Agents in Gemini API, including background execution, remote MCP server integration, custom function calling and refreshing credentials across interactions. These updates directly address developer feedback and product needs so you can build reliab...
- **[Using Google's AI breakthroughs for crisis resilience](https://blog.google/innovation-and-ai/technology/research/technology-global-crisis-resilience/)**
  * As extreme weather events and natural hazards intensify, today's UN report, “Leveraging AI to enhance multi-hazard early warning systems,” highlights the critical role of technology in keeping communities safe. Google has supported the UN’s Early Warnings for All initiative since its launch at COP27...
- **[We're rolling out AlphaEvolve widely to solve Google Cloud customers' hardest problems.](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/alphaevolve-on-cloud/)**
  * Finding the most efficient algorithm — whether designing a microchip, routing a logistics network or accelerating medical research — can be challenging, with many possible solutions for engineers to explore on their own.To help organizations tackle these complex challenges, AlphaEvolve, our Gemini-p...
- **[Gemini’s new study notebooks help you learn with personalized lessons, practice quizzes and a custom progress dashboard.](https://blog.google/innovation-and-ai/products/gemini-app/how-to-make-gemini-study-notebooks/)**
  * Studying for a test, but not sure where to start? Study notebooks, a new feature in the Gemini app, can help you get organized and learn more efficiently.Think of study notebooks as a personalized learning space. You tell Gemini what you want to learn, and it helps you get there with bite-sized less...
- **[Building the future of global health, together](https://blog.google/innovation-and-ai/technology/health/open-health-stack-software-foundation/)**
  * An estimated 4.6 billion people worldwide lack access to essential health services. While mobile and AI have tremendous potential to help bridge the gaps, the reality is that global digital health infrastructure is fragmented, which limits the potential of these technologies to improve health outcom...

## 3. Market Intelligence (Markposition)
Total Market Data Points: 680

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
- **ShareThis: Free Share Buttons & Plugins, Global Behavioral Data Solutions**: https://sharethis.com/ (August 20, 2022)
- **How To Create Quality Video Ads – YouTube Advertising**: https://www.youtube.com/intl/en_us/ads/how-it-works/create-a-video-ad/ (August 16, 2022)

*(Truncated: showing 20 of 680 recent entries)*

## 4. Legal & Ecosystem (Wilson Sonsini)
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

## 5. Technical Documentation
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

### Google Ads
Topics covered: https://support.google.com/google-ads/answer/2459326?hl=en&ref_topic=10289453&sjid=5167206403107665975-EU, https://business.google.com/uk/ad-tools/bidding/?hl=en, https://business.google.com/uk/resources/?hl=en, https://developers.google.com/ad-manager?hl=en, https://developers.google.com/ad-manager/dynamic-ad-insertion?hl=en...

## 6. TypeScript Ecosystem Intelligence
### Internal: .github/ISSUE_TEMPLATE/bug_report.md
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

### Internal: .github/ISSUE_TEMPLATE/feature_request.md
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

### Internal: .github/PULL_REQUEST_TEMPLATE.md
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

### Gemma 4 Technical Report
*Source: local://gemmafour_docs.md*

#### Gemma 4 Model Card
Scraped from [https://ai.google.dev/gemma/docs/core/model_card_4](https://ai.google.dev/gemma/docs/core/model_card_4)

#### Models Overview
Gemma 4 models are designed to deliver frontier-level performance at each size,
targeting deployment scenarios from mobile and edge devices (E2B, E4B) to
consumer GPUs and workstations (26B A4B, 31B). They are well-suited for
reasoning, agentic workflows, coding, and multimodal understanding.

The models employ a hybrid attention mechanism that interleaves local sliding
window attention with full global attention, ensuring the final layer is always
global. This hybrid design delivers the processing speed and low memory
footprint of a lightweight model without sacrificing the deep awareness required
for complex, long-context tasks. To optimize memory for long contexts, global
layers feature unified Keys and Values, and apply Proportional RoPE (p-RoPE).

#### Dense Models
Property | E2B | E4B | 31B Dense
Total Parameters | 2.3B effective (5.1B with embeddings) | 4.5B effective (8B with embeddings) | 30.7B
Layers | 35 | 42 | 60
Sliding Window | 512 tokens | 512 tokens | 1024 tokens
Context Length | 128K tokens | 128K tokens | 256K tokens
Vocabulary Size | 262K | 262K | 262K
Supported Modalities | Text, Image, Audio | Text, Image, Audio | Text, Image
Vision Encoder Parameters | ~150M | ~150M | ~550M
Audio Encoder Parameters | ~300M | ~300M | No Audio

The "E" in E2B and E4B stands for "effective" parameters. The smaller models
incorporate Per-Layer Embeddings (PLE) to maximize parameter efficiency in
on-device deployments. Rather than adding more layers or parameters to the
model, PLE gives each decoder layer its own small embedding for every token.
These embedding tables are large but are only used for quick lookups, which is
why the effective parameter count is much smaller than the total.

#### Mixture-of-Experts (MoE) Model
Property | 26B A4B MoE
Total Parameters | 25.2B
Active Parameters | 3.8B
Layers | 30
Sliding Window | 1024 tokens
Context Length | 256K tokens
Vocabulary Size | 262K
Expert Count | 8 active / 128 total and 1 shared
Supported Modalities | Text, Image
Vision Encoder Parameters | ~550M

The "A" in 26B A4B stands for "active parameters" in contrast to the total
number of parameters the model contains. By only activating a 4B subset of
parameters during inference, the Mixture-of-Experts model runs much faster than
its 26B total might suggest. This makes it an excellent choice for fast
inference compared to the dense 31B model since it runs almost as fast as a
4B-parameter model.

#### Benchmark Results
These models were evaluated against a large collection of different datasets and
metrics to cover different aspects of text generation. Evaluation results marked
in the table are for instruction-tuned models.

 | Gemma 4  31B | Gemma 4  26B A4B | Gemma 4  E4B | Gemma 4  E2B | Gemma 3  27B (no think)
MMLU Pro | 85.2% | 82.6% | 69.4% | 60.0% | 67.6%
AIME 2026 no tools | 89.2% | 88.3% | 42.5% | 37.5% | 20.8%
LiveCodeBench v6 | 80.0% | 77.1% | 52.0% | 44.0% | 29.1%
Codeforces ELO | 2150 | 1718 | 940 | 633 | 110
GPQA Diamond | 84.3% | 82.3% | 58.6% | 43.4% | 42.4%
Tau2 (average over 3) | 76.9% | 68.2% | 42.2% | 24.5% | 16.2%
HLE no tools | 19.5% | 8.7% | - | - | -
HLE with search | 26.5% | 17.2% | - | - | -
BigBench Extra Hard | 74.4% | 64.8% | 33.1% | 21.9% | 19.3%

#### MMMLU | 88.4% | 86.3% | 76.6% | 67.4% | 70.7%
Vision |  |  |  |  |
MMMU Pro | 76.9% | 73.8% | 52.6% | 44.2% | 49.7%
OmniDocBench 1.5 (average edit distance, lower is better) | 0.131 | 0.149 | 0.181 | 0.290 | 0.365
MATH-Vision | 85.6% | 82.4% | 59.5% | 52.4% | 46.0%
MedXPertQA MM | 61.3% | 58.1% | 28.7% | 23.5% | -
Audio |  |  |  |  |
CoVoST | - | - | 35.54 | 33.47 | -
FLEURS (lower is better) | - | - | 0.08 | 0.09 | -
Long Context |  |  |  |  |
MRCR v2 8 needle 128k (average) | 66.4% | 44.1% | 25.4% | 19.1% | 13.5%

#### Core Capabilities
Gemma 4 models handle a broad range of tasks across text, vision, and audio. Key
capabilities include:

- Thinking– Built-in reasoning mode that lets the model think
step-by-step before answering.

- Long Context– Context windows of up to 128K tokens (E2B/E4B) and 256K
tokens (26B A4B/31B).

- Image Understanding– Object detection, Document/PDF parsing, screen and
UI understanding, chart comprehension, OCR (including multilingual),
handwriting recognition, and pointing. Images can be processed at variable
aspect ratios and resolutions.

- Video Understanding– Analyze video by processing sequences of frames.

- Interleaved Multimodal Input– Freely mix text and images in any order
within a single prompt.

- Function Calling– Native support for structured tool use, enabling
agentic workflows.

- Coding– Code generation, completion, and correction.

- Multilingual– Out-of-the-box support for 35+ languages, pre-trained on
140+ languages.

- Audio(E2B and E4B only) – Automatic speech recognition (ASR) and
speech-to-translated-text translation across multiple languages.

#### Best Practices
For the best performance, use these configurations and best practices:

#### 1. Sampling Parameters
Use the following standardized sampling configuration across all use cases:

- temperature=1.0

- top_p=0.95

- top_k=64

#### 2. Thinking Mode Configuration
Compared to Gemma 3, the models use standard system , assistant , and user roles. To properly manage the thinking process, use the following control
tokens:

- Trigger Thinking:Thinking is enabled by including the<|think|>token
at the start of the system prompt. To disable thinking, remove the token.

- Standard Generation:When thinking is enabled, the model will output its
internal reasoning followed by the final answer using this structure:<|channel>thought\n[Internal reasoning]<channel|>

- Disabled Thinking Behavior:For all models except for the E2B and E4B
variants, if thinking is disabled, the model will still generate the tags
but with an empty thought block:<|channel>thought\n<channel|>[Final
answer]

Note that many libraries like Transformers and llama.cpp handle the
complexities of the chat template for you.

#### 3. Multi-Turn Conversations
- No Thinking Content in History: In multi-turn conversations, the
historical model output should only include the final response. Thoughts
from previous model turns mustnot be addedbefore the next user turn
begins.

#### 4. Modality order
- For optimal performance with multimodal inputs, place image and/or audio
contentbeforethe text in your prompt.

#### 5. Variable Image Resolution
Aside from variable aspect ratios, Gemma 4 supports variable image resolution
through a configurable visual token budget, which controls how many tokens are
used to represent an image. A higher token budget preserves more visual detail
at the cost of additional compute, while a lower budget enables faster inference
for tasks that don't require fine-grained understanding.

- The supported token budgets are:70,140,280,560, and1120.Uselower budgetsfor classification, captioning, or video
understanding, where faster inference and processing many frames
outweigh fine-grained detail.Usehigher budgetsfor tasks like OCR, document parsing, or reading
small text.

#### 6. Audio
Use the following prompt structures for audio processing:

- Audio Speech Recognition (ASR)

Transcribe the following speech segment in {LANGUAGE} into {LANGUAGE} text.

Follow these specific instructions for formatting the answer:
*   Only output the transcription, with no newlines.
*   When transcribing numbers, write the digits, i.e. write 1.7 and not one point seven, and write 3 instead of three.

- Automatic Speech Translation (AST)

Transcribe the following speech segment in {SOURCE_LANGUAGE}, then translate it into {TARGET_LANGUAGE}.
When formatting the answer, first output the transcription in {SOURCE_LANGUAGE}, then one newline, then output the string '{TARGET_LANGUAGE}: ', then the translation in {TARGET_LANGUAGE}.

#### 7. Audio and Video Length
All models support image inputs and can process videos as frames whereas the E2B
and E4B models also support audio inputs. Audio supports a maximum length of 30
seconds. Video supports a maximum of 60 seconds assuming the images are
processed at one frame per second.

#### Model Data
Data used for model training and how the data was processed.

#### Training Dataset
Our pre-training dataset is a large-scale, diverse collection of data
encompassing a wide range of domains and modalities, which includes web
documents, code, images, audio, with a cutoff date of January 2025. Here are the
key components:

- Web Documents: A diverse collection of web text ensures the model is
exposed to a broad range of linguistic styles, topics, and vocabulary. The
training dataset includes content in over 140 languages.

- Code: Exposing the model to code helps it to learn the syntax and
patterns of programming languages, which improves its ability to generate
code and understand code-related questions.

- Mathematics: Training on mathematical text helps the model learn logical
reasoning, symbolic representation, and to address mathematical queries.

- Images: A wide range of images enables the model to perform image
analysis and visual data extraction tasks.

The combination of these diverse data sources is crucial for training a powerful
multimodal model that can handle a wide variety of different tasks and data
formats.

#### Data Preprocessing
Here are the key data cleaning and filtering methods applied to the training
data:

- CSAM Filtering: Rigorous CSAM (Child Sexual Abuse Material) filtering
was applied at multiple stages in the data preparation process to ensure the
exclusion of harmful and illegal content.

- Sensitive Data Filtering: As part of making Gemma pre-trained models
safe and reliable, automated techniques were used to filter out certain
personal information and other sensitive data from training sets.

- Additional methods: Filtering based on content quality and safety in
line withour
policies.

#### Ethics and Safety
As open models become central to enterprise infrastructure, provenance and
security are paramount. Developed by Google DeepMind, Gemma 4 undergoes the same
rigorous safety evaluations as our proprietary Gemini models.

#### Evaluation Approach
Gemma 4 models were developed in partnership with internal safety and
responsible AI teams. A range of automated as well as human evaluations were
conducted to help improve model safety. These evaluations align with Google's
AI principles , as well as safety policies, which
aim to prevent our generative AI models from generating harmful content,
including:

- Content related to child sexual abuse material and exploitation

- Dangerous content (e.g., promoting suicide, or instructing in activities
that could cause real-world harm)

- Sexually explicit content

- Hate speech (e.g., dehumanizing members of protected groups)

- Harassment (e.g., encouraging violence against people)

#### Evaluation Results
For all areas of safety testing, we saw major improvements in all categories of
content safety relative to previous Gemma models. Overall, Gemma 4 models
significantly outperform Gemma 3 and 3n models in improving safety, while
keeping unjustified refusals low. All testing was conducted without safety
filters to evaluate the model capabilities and behaviors. For both text-to-text
and image-to-text, and across all model sizes, the model produced minimal policy
violations, and showed significant improvements over previous Gemma models'
performance.

#### Usage and Limitations
These models have certain limitations that users should be aware of.

#### Intended Usage
Multimodal models (capable of processing vision, language, and/or audio) have a
wide range of applications across various industries and domains. The following
list of potential uses is not comprehensive. The purpose of this list is to
provide contextual information about the possible use-cases that the model
creators considered as part of model training and development.

- Content Creation and CommunicationText Generation: These models can be used to generate creative text
formats such as poems, scripts, code, marketing copy, and email drafts.Chatbots and Conversational AI: Power conversational interfaces for
customer service, virtual assistants, or interactive applications.Text Summarization: Generate concise summaries of a text corpus,
research papers, or reports.Image Data Extraction: These models can be used to extract,
interpret, and summarize visual data for text communications.Audio Processing and Interaction: The smaller models (E2B and E4B)
can analyze and interpret audio inputs, enabling voice-driven
interactions and transcriptions.

- Research and EducationNatural Language Processing (NLP) and VLM Research: These models can
serve as a foundation for researchers to experiment with VLM and NLP
techniques, develop algorithms, and contribute to the advancement of the
field.Language Learning Tools: Support interactive language learning
experiences, aiding in grammar correction or providing writing practice.Knowledge Exploration: Assist researchers in exploring large
bodies of text by generating summaries or answering questions about
specific topics.

#### Limitations
- Training DataThe quality and diversity of the training data significantly influence
the model's capabilities. Biases or gaps in the training data can lead
to limitations in the model's responses.The scope of the training dataset determines the subject areas the model
can handle effectively.

- Context and Task ComplexityModels perform well on tasks that can be framed with clear prompts and
instructions. Open-ended or highly complex tasks might be challenging.A model's performance can be influenced by the amount of context
provided (longer context generally leads to better outputs, up to a
certain point).

- Language Ambiguity and NuanceNatural language is inherently complex. Models might struggle to grasp
subtle nuances, sarcasm, or figurative language.

- Factual AccuracyModels generate responses based on information they learned from their
training datasets, but they are not knowledge bases. They may generate
incorrect or outdated factual statements.

- Common SenseModels rely on statistical patterns in language. They might lack the
ability to apply common sense reasoning in certain situations.

#### Ethical Considerations and Risks
The development of vision-language models (VLMs) raises several ethical
concerns. In creating an open model, we have carefully considered the following:

- Bias and FairnessVLMs trained on large-scale, real-world text and image data can reflect
socio-cultural biases embedded in the training material. Gemma 4 models
underwent careful scrutiny, input data pre-processing, and post-training
evaluations as reported in this card to help mitigate the risk of these
biases.

- Misinformation and MisuseVLMs can be misused to generate text that is false, misleading, or
harmful.Guidelines are provided for responsible use with the model, see theResponsible Generative AI Toolkit.

- Transparency and AccountabilityThis model card summarizes details on the models' architecture,
capabilities, limitations, and evaluation processes.A responsibly developed open model offers the opportunity to share
innovation by making VLM technology accessible to developers and
researchers across the AI ecosystem.

Risks identified and mitigations :

- Generation of harmful content: Mechanisms and guidelines for content
safety are essential. Developers are encouraged to exercise caution and
implement appropriate content safety safeguards based on their specific
product policies and application use cases.

- Misuse for malicious purposes: Technical limitations and developer and
end-user education can help mitigate against malicious applications of VLMs.
Educational resources and reporting mechanisms for users to flag misuse are
provided.

- Privacy violations: Models were trained on data filtered for removal of
certain personal information and other sensitive data. Developers are
encouraged to adhere to privacy regulations with privacy-preserving
techniques.

- Perpetuation of biases: It's encouraged to perform continuous monitoring
(using evaluation metrics, human review) and the exploration of de-biasing
techniques during model training, fine-tuning, and other use cases.

#### Benefits
At the time of release, this family of models provides high-performance open
vision-language model implementations designed from the ground up for
responsible AI development compared to similarly sized models.

### LiteRT Framework Documentation
*Source: local://litert_docs.md*

#### LiteRT Overview Documentation
Scraped from [https://ai.google.dev/edge/litert/overview](https://ai.google.dev/edge/litert/overview)

#### Overview
- Home

- Google AI Edge

- LiteRT

LiteRT is Google's on-device framework for high-performance ML & GenAI
deployment on edge platforms, using efficient conversion, runtime, and
optimization.

The latest LiteRT 2.x release introduces the CompiledModel API,
a modern runtime interface designed to maximize hardware acceleration. While the Interpreter API (formerly TensorFlow Lite) remains available for backward
compatibility, the CompiledModel API is the recommended choice for developers
seeking state-of-the-art performance in on-device AI applications.

#### Streamline development with LiteRT
Automated accelerator selection versus explicit delegate creation. Efficient I/O
buffer handling and async execution for superior performance.
See on-device inference documentation .

#### Best-in-class GPU performance
Powered by ML Drift, now supporting both ML and Generative
AI models on GPUs APIs. See GPU acceleration documentation .

#### Unified NPU acceleration
Accelerate your model using simplified NPU access from major
chipset providers. See NPU acceleration documentation .

#### Superior LLM Support
LiteRT delivers high-performance deployment for Generative AI models across
mobile, desktop, and web platforms. See GenAI deployment documentation .

#### Broad ML framework support
LiteRT supports streamlined conversion from PyTorch, TensorFlow, and JAX
Frameworks to .tflite or .litertlm format. See model conversion documentation .

#### Get Started withCompiledModelAPI
- For classical ML models , see the following demo apps. Image segmentation Kotlin App : CPU/GPU/NPU inference. Image segmentation C++ App : CPU/GPU/NPU inference with async execution.

- For GenAI models , see the following demo apps: EmbeddingGemma semantic similarity C++ App :
CPU/GPU/NPU inference.

For classical ML models , see the following demo apps.

- Image segmentation Kotlin App : CPU/GPU/NPU inference.

- Image segmentation C++ App : CPU/GPU/NPU inference with async execution.

For GenAI models , see the following demo apps:

- EmbeddingGemma semantic similarity C++ App :
CPU/GPU/NPU inference.

#### Development workflow
LiteRT runs inferences completely on-device on Android, iOS, Web, IoT, and on
desktop/laptop. Regardless of device, the following is the most common
workflow, with links to further instructions.

#### Identify the most suitable solution to the ML challenge
LiteRT offers users a high level of flexibility and customizability when it
comes to solving machine learning problems, making it a good fit for users who
require a specific model or a specialized implementation. Users looking for
plug-and-play solutions may prefer MediaPipe
Tasks ,
which provides ready-made
solutions for common machine learning tasks like object detection,
text classification, and LLM inference.

#### Obtain and preparing the model
A LiteRT model is represented in an efficient portable format known as FlatBuffers , which uses the .tflite file extension.

You can obtain a LiteRT model in the following ways:

- Obtain a pre-trained model: for popular ML workloads like Image
segmentation, Object detection etc. The simplest approach is to use a LiteRT model already in the .tflite format. These models don't require any added conversion steps. Model type Pre-trained model source Classical ML ( .tflite format) Visit Kaggle or HuggingFace E.g. Image segmentation models and sample app Generative AI ( .litertlm format) LiteRT Hugging Face page E.g. Gemma Family

- Convert your chosen PyTorch,
TensorFlow or JAX model into a LiteRT model if you choose to not use a
pre-trained model. [PRO USER] Model framework Sample models Conversion tool Pytorch Hugging Face Torchvision Link TensorFlow Kaggle Models Hugging Face Link Jax Hugging Face Link

- Author your LLM for further optimization using Generative
API [PRO USER] Our Generative API library provides PyTorch built-in building blocks for
composing Transformer models such as Gemma , TinyLlama and others using mobile-friendly abstractions, through which
we can guarantee conversion,
and performant execution on our mobile runtime, LiteRT. See Generative API
documentation .

Obtain a pre-trained model: for popular ML workloads like Image
segmentation, Object detection etc.

The simplest approach is to use a LiteRT model already in the .tflite format. These models don't require any added conversion steps.

Convert your chosen PyTorch,
TensorFlow or JAX model into a LiteRT model if you choose to not use a
pre-trained model. [PRO USER]

Author your LLM for further optimization using Generative

#### API [PRO USER]
Our Generative API library provides PyTorch built-in building blocks for
composing Transformer models such as Gemma , TinyLlama and others using mobile-friendly abstractions, through which
we can guarantee conversion,
and performant execution on our mobile runtime, LiteRT. See Generative API
documentation .

#### Optimize [PRO USER]
AI Edge Quantizer for advanced developers is a tool to quantize converted
LiteRT models. It aims to facilitate advanced users to strive for optimal
performance on resource demanding models (e.g., GenAI models).

See more details from AI Edge Quantizer documentation .

#### Integrate the model into your app on edge platforms
LiteRT lets you to run ML models entirely on-device with high performance
across Android, iOS, Web, Desktop, and IoT platforms.

Use the following guides to integrate a LiteRT model on your preferred platform:

The following code snippets show a basic implementation in
Kotlin and C++.

#### Kotlin
```
// Load model and initialize runtimevalcompiledModel=CompiledModel.create("/path/to/mymodel.tflite",CompiledModel.Options(Accelerator.CPU))// Preallocate input/output buffersvalinputBuffers=compiledModel.createInputBuffers()valoutputBuffers=compiledModel.createOutputBuffers()// Fill the input bufferinputBuffers.get(0).writeFloat(input0)inputBuffers.get(1).writeFloat(input1)// InvokecompiledModel.run(inputBuffers,outputBuffers)// Read the outputvaloutput=outputBuffers.get(0).readFloat()
```

#### C++
```
// Load model and initialize runtimeLITERT_ASSIGN_OR_RETURN(autoenv,GetEnvironment());LITERT_ASSIGN_OR_RETURN(autooptions,GetOptions());LITERT_ASSIGN_OR_RETURN(autocompiled_model,CompiledModel::Create(env,"/path/to/mymodel.tflite",options));// Preallocate input/output buffersLITERT_ASSIGN_OR_RETURN(autoinput_buffers,compiled_model.CreateInputBuffers(signature_index));LITERT_ASSIGN_OR_RETURN(autooutput_buffers,compiled_model.CreateOutputBuffers(signature_index));// Fill the input bufferLITERT_ABORT_IF_ERROR(input_buffers[0].Write(input0));LITERT_ABORT_IF_ERROR(input_buffers[1].Write(input1));// InvokeLITERT_ABORT_IF_ERROR(compiled_model.Run(signature_index,input_buffers,output_buffers));// Read the outputLITERT_ABORT_IF_ERROR(output_buffers[0].Read(output0));
```

#### Choose a backend
The most straightforward way to incorporate backends in LiteRT is to rely on
the runtime's built-in intelligence. With the CompiledModel API, LiteRT
simplifies the setup significantly with the ability to specify the
target backend as an option. See on-device inference guide for more
details.

#### Additional documentation and support
- LiteRT-Samples GitHub Repo for more LiteRT sample apps.

- For existing users of TensorFlow Lite , see migration guide .

- LiteRT Tools page for performance, profiling, error reporting etc.

LiteRT-Samples GitHub Repo for more LiteRT sample apps.

For existing users of TensorFlow Lite , see migration guide .

LiteRT Tools page for performance, profiling, error reporting etc.

### OpenTelemetry Ecosystem Analysis
*Source: local://opentelemetry_repos.md*

#### OpenTelemetry GitHub Repositories
Scraped from [https://github.com/open-telemetry](https://github.com/open-telemetry)

Total repositories: 100

#### [opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-collector)
OpenTelemetry Collector

- **Language:** Go
- **Stars:** 7032
- **Forks:** 2070

#### [opentelemetry-go](https://github.com/open-telemetry/opentelemetry-go)
OpenTelemetry Go API and SDK

- **Language:** Go
- **Stars:** 6389
- **Forks:** 1352

#### [opentelemetry-collector-contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib)
Contrib repository for the OpenTelemetry Collector

- **Language:** Go
- **Stars:** 4661
- **Forks:** 3590

#### [opentelemetry-specification](https://github.com/open-telemetry/opentelemetry-specification)
Specifications for OpenTelemetry

- **Language:** Makefile
- **Stars:** 4240
- **Forks:** 977

#### [opentelemetry-dotnet](https://github.com/open-telemetry/opentelemetry-dotnet)
The OpenTelemetry .NET Client

- **Language:** C#
- **Stars:** 3698
- **Forks:** 891

#### [opentelemetry-js](https://github.com/open-telemetry/opentelemetry-js)
OpenTelemetry JavaScript Client

- **Language:** TypeScript
- **Stars:** 3377
- **Forks:** 1043

#### [opentelemetry-ebpf-profiler](https://github.com/open-telemetry/opentelemetry-ebpf-profiler)
The production-scale datacenter profiler (C/C++, Go, Rust, Python, Java, NodeJS, .NET, PHP, Ruby, Perl, ...)

- **Language:** Go
- **Stars:** 3111
- **Forks:** 399

#### [opentelemetry-demo](https://github.com/open-telemetry/opentelemetry-demo)
This repository contains the OpenTelemetry Astronomy Shop, a microservice-based distributed system intended to illustrate the implementation of OpenTelemetry in a near real-world environment.

- **Language:** TypeScript
- **Stars:** 3083
- **Forks:** 6478

#### [opentelemetry-rust](https://github.com/open-telemetry/opentelemetry-rust)
The Rust OpenTelemetry implementation

- **Language:** Rust
- **Stars:** 2580
- **Forks:** 661

#### [opentelemetry-java-instrumentation](https://github.com/open-telemetry/opentelemetry-java-instrumentation)
OpenTelemetry auto-instrumentation and instrumentation libraries for Java

- **Language:** Java
- **Stars:** 2537
- **Forks:** 1096

#### [opentelemetry-python](https://github.com/open-telemetry/opentelemetry-python)
OpenTelemetry Python API and SDK

- **Language:** Python
- **Stars:** 2450
- **Forks:** 878

#### [opentelemetry-java](https://github.com/open-telemetry/opentelemetry-java)
OpenTelemetry Java SDK

- **Language:** Java
- **Stars:** 2397
- **Forks:** 974

#### [opentelemetry-operator](https://github.com/open-telemetry/opentelemetry-operator)
Kubernetes Operator for OpenTelemetry Collector

- **Language:** Go
- **Stars:** 1693
- **Forks:** 626

#### [opentelemetry-go-contrib](https://github.com/open-telemetry/opentelemetry-go-contrib)
Collection of extensions for OpenTelemetry-Go.

- **Language:** Go
- **Stars:** 1626
- **Forks:** 782

#### [opentelemetry-cpp](https://github.com/open-telemetry/opentelemetry-cpp)
The OpenTelemetry C++ Client

- **Language:** C++
- **Stars:** 1283
- **Forks:** 567

#### [community](https://github.com/open-telemetry/community)
OpenTelemetry community content

- **Language:** Python
- **Stars:** 1048
- **Forks:** 296

#### [opentelemetry-python-contrib](https://github.com/open-telemetry/opentelemetry-python-contrib)
OpenTelemetry instrumentation for Python modules

- **Language:** Python
- **Stars:** 1048
- **Forks:** 950

#### [opentelemetry-go-instrumentation](https://github.com/open-telemetry/opentelemetry-go-instrumentation)
OpenTelemetry Auto Instrumentation using eBPF

- **Language:** C
- **Stars:** 1007
- **Forks:** 137

#### [opentelemetry-js-contrib](https://github.com/open-telemetry/opentelemetry-js-contrib)
OpenTelemetry instrumentation for JavaScript modules

- **Language:** TypeScript
- **Stars:** 906
- **Forks:** 658

#### [opentelemetry.io](https://github.com/open-telemetry/opentelemetry.io)
The OpenTelemetry website and documentation

- **Language:** JavaScript
- **Stars:** 898
- **Forks:** 1781

#### [opentelemetry-php](https://github.com/open-telemetry/opentelemetry-php)
The OpenTelemetry PHP Library

- **Language:** PHP
- **Stars:** 892
- **Forks:** 223

#### [opentelemetry-proto](https://github.com/open-telemetry/opentelemetry-proto)
OpenTelemetry protocol (OTLP) specification and Protobuf definitions

- **Language:** Makefile
- **Stars:** 786
- **Forks:** 312

#### [opentelemetry-dotnet-contrib](https://github.com/open-telemetry/opentelemetry-dotnet-contrib)
This repository contains set of components extending functionality of the OpenTelemetry .NET SDK. Instrumentation libraries, exporters, and other components can find their home here.

- **Language:** C#
- **Stars:** 639
- **Forks:** 386

#### [docs-cn](https://github.com/open-telemetry/docs-cn) **(ARCHIVED)**
OpenTelemetry 中文文档: 接入使用、技术标准、RFC、SDK等.

- **Language:** N/A
- **Stars:** 624
- **Forks:** 106

#### [semantic-conventions](https://github.com/open-telemetry/semantic-conventions)
Defines standards for generating consistent, accessible telemetry across a variety of domains

- **Language:** Open Policy Agent
- **Stars:** 580
- **Forks:** 358

#### [opentelemetry-ruby](https://github.com/open-telemetry/opentelemetry-ruby)
OpenTelemetry Ruby API & SDK, and related gems

- **Language:** Ruby
- **Stars:** 575
- **Forks:** 282

#### [opentelemetry-helm-charts](https://github.com/open-telemetry/opentelemetry-helm-charts)
OpenTelemetry Helm Charts

- **Language:** Go Template
- **Stars:** 550
- **Forks:** 747

#### [opentelemetry-collector-releases](https://github.com/open-telemetry/opentelemetry-collector-releases)
OpenTelemetry Collector Official Releases

- **Language:** Go
- **Stars:** 472
- **Forks:** 234

#### [opentelemetry-ebpf-instrumentation](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation)
No description provided.

- **Language:** C
- **Stars:** 467
- **Forks:** 113

#### [opentelemetry-dotnet-instrumentation](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation)
OpenTelemetry .NET Automatic Instrumentation

- **Language:** C++
- **Stars:** 453
- **Forks:** 135

#### [opentelemetry-lambda](https://github.com/open-telemetry/opentelemetry-lambda)
Create your own Lambda Layer in each OTel language using this starter code. Add the Lambda Layer to your Lambda Function to get tracing with OpenTelemetry.

- **Language:** Go
- **Stars:** 429
- **Forks:** 235

#### [weaver](https://github.com/open-telemetry/weaver)
OTel Weaver lets you easily develop, validate, document, and deploy semantic conventions

- **Language:** Rust
- **Stars:** 408
- **Forks:** 83

#### [opentelemetry-network](https://github.com/open-telemetry/opentelemetry-network)
eBPF Collector

- **Language:** C++
- **Stars:** 405
- **Forks:** 64

#### [opentelemetry-erlang](https://github.com/open-telemetry/opentelemetry-erlang)
OpenTelemetry Erlang SDK

- **Language:** Erlang
- **Stars:** 390
- **Forks:** 137

#### [oteps](https://github.com/open-telemetry/oteps) **(ARCHIVED)**
OpenTelemetry Enhancement Proposals

- **Language:** Makefile
- **Stars:** 352
- **Forks:** 162

#### [opentelemetry-swift](https://github.com/open-telemetry/opentelemetry-swift)
OpenTelemetry API for Swift

- **Language:** Swift
- **Stars:** 352
- **Forks:** 223

#### [opentelemetry-java-examples](https://github.com/open-telemetry/opentelemetry-java-examples)
No description provided.

- **Language:** Java
- **Stars:** 347
- **Forks:** 154

#### [otel-arrow](https://github.com/open-telemetry/otel-arrow)
Protocol and libraries for sending and receiving OpenTelemetry data using Apache Arrow

- **Language:** Rust
- **Stars:** 339
- **Forks:** 101

#### [opentelemetry-go-compile-instrumentation](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation)
OpenTelemetry Go Compile Instrumentation

- **Language:** Go
- **Stars:** 290
- **Forks:** 70

#### [opentelemetry-android](https://github.com/open-telemetry/opentelemetry-android)
OpenTelemetry Tooling for Android

- **Language:** Kotlin
- **Stars:** 285
- **Forks:** 100

#### [opentelemetry-java-contrib](https://github.com/open-telemetry/opentelemetry-java-contrib)
No description provided.

- **Language:** Java
- **Stars:** 261
- **Forks:** 180

#### [opentelemetry-erlang-contrib](https://github.com/open-telemetry/opentelemetry-erlang-contrib)
OpenTelemetry instrumentation for Erlang & Elixir

- **Language:** Elixir
- **Stars:** 211
- **Forks:** 160

#### [opamp-go](https://github.com/open-telemetry/opamp-go)
OpAMP protocol implementation in Go

- **Language:** Go
- **Stars:** 210
- **Forks:** 113

#### [opentelemetry-cpp-contrib](https://github.com/open-telemetry/opentelemetry-cpp-contrib)
No description provided.

- **Language:** Python
- **Stars:** 150
- **Forks:** 181

#### [opamp-spec](https://github.com/open-telemetry/opamp-spec)
OpAMP Specification

- **Language:** Makefile
- **Stars:** 141
- **Forks:** 53

#### [opentelemetry-php-instrumentation](https://github.com/open-telemetry/opentelemetry-php-instrumentation)
OpenTelemetry PHP auto-instrumentation extension

- **Language:** C
- **Stars:** 135
- **Forks:** 34

#### [opentelemetry-injector](https://github.com/open-telemetry/opentelemetry-injector)
No description provided.

- **Language:** Zig
- **Stars:** 129
- **Forks:** 29

#### [opentelemetry-ruby-contrib](https://github.com/open-telemetry/opentelemetry-ruby-contrib)
Contrib Packages for the OpenTelemetry Ruby API and SDK implementation.

- **Language:** Ruby
- **Stars:** 121
- **Forks:** 246

#### [opentelemetry-kotlin](https://github.com/open-telemetry/opentelemetry-kotlin)
An implementation of the OpenTelemetry specification as a Kotlin Multiplatform Library

- **Language:** Kotlin
- **Stars:** 117
- **Forks:** 19

#### [opentelemetry-php-contrib](https://github.com/open-telemetry/opentelemetry-php-contrib)
opentelemetry-php-contrib

- **Language:** PHP
- **Stars:** 110
- **Forks:** 134

#### [opentelemetry-log-collection](https://github.com/open-telemetry/opentelemetry-log-collection) **(ARCHIVED)**
OpenTelemetry log collection library

- **Language:** Go
- **Stars:** 93
- **Forks:** 42

#### [opentelemetry-configuration](https://github.com/open-telemetry/opentelemetry-configuration)
JSON Schema definitions for OpenTelemetry declarative configuration

- **Language:** JavaScript
- **Stars:** 88
- **Forks:** 38

#### [opentelemetry-js-api](https://github.com/open-telemetry/opentelemetry-js-api) **(ARCHIVED)**
OpenTelemetry Javascript API

- **Language:** TypeScript
- **Stars:** 87
- **Forks:** 49

#### [opentelemetry-rust-contrib](https://github.com/open-telemetry/opentelemetry-rust-contrib)
OpenTelemetry Contrib Packages for Rust

- **Language:** Rust
- **Stars:** 85
- **Forks:** 88

#### [opentelemetry-erlang-api](https://github.com/open-telemetry/opentelemetry-erlang-api) **(ARCHIVED)**
Erlang/Elixir OpenTelemetry API

- **Language:** Erlang
- **Stars:** 60
- **Forks:** 14

#### [opentelemetry-collector-builder](https://github.com/open-telemetry/opentelemetry-collector-builder) **(ARCHIVED)**
This repository is now deprecated. The builder has found a new home inside the OpenTelemetry Collector core repository.

- **Language:** N/A
- **Stars:** 57
- **Forks:** 32

#### [opentelemetry-go-build-tools](https://github.com/open-telemetry/opentelemetry-go-build-tools)
Build tools for use by the Go API/SDK, the collector, and their associated contrib repositories

- **Language:** Go
- **Stars:** 52
- **Forks:** 61

#### [build-tools](https://github.com/open-telemetry/build-tools)
Building tools provided by OpenTelemetry

- **Language:** Dockerfile
- **Stars:** 43
- **Forks:** 57

#### [prometheus-interoperability-spec](https://github.com/open-telemetry/prometheus-interoperability-spec) **(ARCHIVED)**
Workgroup for building Prometheus-OTLP interoperability for the OTEL Collector and Prometheus related discussions.

- **Language:** N/A
- **Stars:** 43
- **Forks:** 7

#### [opentelemetry-proto-go](https://github.com/open-telemetry/opentelemetry-proto-go)
Generated code for OpenTelemetry protobuf data model

- **Language:** Makefile
- **Stars:** 41
- **Forks:** 42

#### [semantic-conventions-genai](https://github.com/open-telemetry/semantic-conventions-genai)
No description provided.

- **Language:** Python
- **Stars:** 40
- **Forks:** 19

#### [semantic-conventions-java](https://github.com/open-telemetry/semantic-conventions-java)
Java generated classes for semantic conventions

- **Language:** Java
- **Stars:** 38
- **Forks:** 31

#### [opentelemetry-browser](https://github.com/open-telemetry/opentelemetry-browser)
OpenTelemetry Browser SDK and instrumentation

- **Language:** TypeScript
- **Stars:** 34
- **Forks:** 19

#### [otel-arrow-collector](https://github.com/open-telemetry/otel-arrow-collector) **(ARCHIVED)**
[DoNotUse] OpenTelemetry Collector with Apache Arrow support FORK OF OPENTELEMETRY COLLECTOR

- **Language:** Go
- **Stars:** 31
- **Forks:** 10

#### [opentelemetry-sqlcommenter](https://github.com/open-telemetry/opentelemetry-sqlcommenter) **(ARCHIVED)**
SQLCommenter components for various languages

- **Language:** JavaScript
- **Stars:** 30
- **Forks:** 14

#### [opentelemetry-proto-java](https://github.com/open-telemetry/opentelemetry-proto-java)
Java Bindings for the OpenTelemetry Protocol (OTLP)

- **Language:** Java
- **Stars:** 24
- **Forks:** 17

#### [opentelemetry-ecosystem-explorer](https://github.com/open-telemetry/opentelemetry-ecosystem-explorer)
A repository for the OpenTelemetry Ecosystem Explorer, a tool to help users discover and learn about the various projects in the OpenTelemetry ecosystem.

- **Language:** TypeScript
- **Stars:** 20
- **Forks:** 38

#### [opentelemetry-sandbox-web-js](https://github.com/open-telemetry/opentelemetry-sandbox-web-js) **(ARCHIVED)**
non-production level experimental Web JS packages

- **Language:** TypeScript
- **Stars:** 19
- **Forks:** 18

#### [docs-ja](https://github.com/open-telemetry/docs-ja) **(ARCHIVED)**
No description provided.

- **Language:** Makefile
- **Stars:** 17
- **Forks:** 6

#### [sig-end-user](https://github.com/open-telemetry/sig-end-user)
No description provided.

- **Language:** Python
- **Stars:** 17
- **Forks:** 19

#### [sig-security](https://github.com/open-telemetry/sig-security)
No description provided.

- **Language:** Python
- **Stars:** 15
- **Forks:** 19

#### [sig-mainframe](https://github.com/open-telemetry/sig-mainframe) **(ARCHIVED)**
Repository of the Mainframe SIG - Our aim is to enable OpenTelemetry for the Mainframe.

- **Language:** N/A
- **Stars:** 13
- **Forks:** 6

#### [opentelemetry-php-distro](https://github.com/open-telemetry/opentelemetry-php-distro)
No description provided.

- **Language:** PHP
- **Stars:** 11
- **Forks:** 3

#### [opentelemetry-weaver-examples](https://github.com/open-telemetry/opentelemetry-weaver-examples)
No description provided.

- **Language:** Rust
- **Stars:** 9
- **Forks:** 7

#### [assign-reviewers-action](https://github.com/open-telemetry/assign-reviewers-action) **(ARCHIVED)**
GitHub action to assign reviewers/approvers/etc based on configuration

- **Language:** TypeScript
- **Stars:** 8
- **Forks:** 7

#### [opentelemetry-network-build-tools](https://github.com/open-telemetry/opentelemetry-network-build-tools) **(ARCHIVED)**
eBPF Collector Build Tools

- **Language:** C
- **Stars:** 7
- **Forks:** 12

#### [opentelemetry-swift-core](https://github.com/open-telemetry/opentelemetry-swift-core)
No description provided.

- **Language:** Swift
- **Stars:** 7
- **Forks:** 23

#### [opentelemetry-weaver-packages](https://github.com/open-telemetry/opentelemetry-weaver-packages)
No description provided.

- **Language:** Open Policy Agent
- **Stars:** 7
- **Forks:** 4

#### [opamp-java](https://github.com/open-telemetry/opamp-java) **(ARCHIVED)**
OpAMP protocol implementation in Java

- **Language:** Java
- **Stars:** 6
- **Forks:** 7

#### [sig-profiling](https://github.com/open-telemetry/sig-profiling)
Profiling SIG utilities

- **Language:** Go
- **Stars:** 5
- **Forks:** 10

#### [opentelemetry-python-genai](https://github.com/open-telemetry/opentelemetry-python-genai)
No description provided.

- **Language:** Python
- **Stars:** 5
- **Forks:** 11

#### [opentelemetry-go-vanityurls](https://github.com/open-telemetry/opentelemetry-go-vanityurls)
Vanityurls config for go.opentelemetry.io subdomain

- **Language:** Shell
- **Stars:** 4
- **Forks:** 14

#### [opentelemetry-proto-profile](https://github.com/open-telemetry/opentelemetry-proto-profile) **(ARCHIVED)**
A fork of OpenTelemetry protocol (OTLP) specification and Protobuf definitions for the Profiling WG

- **Language:** Makefile
- **Stars:** 4
- **Forks:** 2

#### [cpp-build-tools](https://github.com/open-telemetry/cpp-build-tools)
Builds a docker image to make interacting with C++ projects easier.

- **Language:** Shell
- **Stars:** 4
- **Forks:** 6

#### [.github](https://github.com/open-telemetry/.github)
No description provided.

- **Language:** N/A
- **Stars:** 3
- **Forks:** 25

#### [sig-developer-experience](https://github.com/open-telemetry/sig-developer-experience)
No description provided.

- **Language:** N/A
- **Stars:** 3
- **Forks:** 5

#### [changelog.opentelemetry.io](https://github.com/open-telemetry/changelog.opentelemetry.io)
No description provided.

- **Language:** TypeScript
- **Stars:** 3
- **Forks:** 7

#### [sig-contributor-experience](https://github.com/open-telemetry/sig-contributor-experience)


#### TODO
- **Language:** N/A
- **Stars:** 2
- **Forks:** 6

#### [gh-manager](https://github.com/open-telemetry/gh-manager) **(ARCHIVED)**
This repository is for code to manage the OpenTelemetry GitHub Organization

- **Language:** N/A
- **Stars:** 2
- **Forks:** 2

#### [sig-project-infra](https://github.com/open-telemetry/sig-project-infra)
No description provided.

- **Language:** Go
- **Stars:** 2
- **Forks:** 6

#### [opentelemetry-for-beginners](https://github.com/open-telemetry/opentelemetry-for-beginners)
No description provided.

- **Language:** JavaScript
- **Stars:** 2
- **Forks:** 1

#### [govanityurls](https://github.com/open-telemetry/govanityurls)
Use a custom domain in your Go import path

- **Language:** Go
- **Stars:** 1
- **Forks:** 4

#### [.roadmap](https://github.com/open-telemetry/.roadmap)
Tooling to manage OpenTelemetry Roadmap management and reporting

- **Language:** Python
- **Stars:** 1
- **Forks:** 2

#### [opentelemetry-swift-grpc](https://github.com/open-telemetry/opentelemetry-swift-grpc) **(ARCHIVED)**
No description provided.

- **Language:** N/A
- **Stars:** 1
- **Forks:** 0

#### [opentelemetry-injector-packaging](https://github.com/open-telemetry/opentelemetry-injector-packaging)
No description provided.

- **Language:** N/A
- **Stars:** 1
- **Forks:** 0

#### [stackoverflow2slack](https://github.com/open-telemetry/stackoverflow2slack) **(ARCHIVED)**
A bot that republishing OTel-tagged questions from SO to Slack

- **Language:** Python
- **Stars:** 0
- **Forks:** 4

#### [.allstar](https://github.com/open-telemetry/.allstar) **(ARCHIVED)**
Enable and house Allstar policies centrally for the organizatio

- **Language:** N/A
- **Stars:** 0
- **Forks:** 5

#### [.project](https://github.com/open-telemetry/.project)
No description provided.

- **Language:** Python
- **Stars:** 0
- **Forks:** 1

#### [opentelemetry-zig](https://github.com/open-telemetry/opentelemetry-zig)
No description provided.

- **Language:** N/A
- **Stars:** 0
- **Forks:** 0

#### [opentelemetry-packaging](https://github.com/open-telemetry/opentelemetry-packaging)
OpenTelemetry Packaging SIG

- **Language:** N/A
- **Stars:** 0
- **Forks:** 1

### Google Ads Strategic Documentation
*Source: local://google_ads_docs.md*

#### Google Ads & Ad Manager Documentation


#### Understanding bidding basics
Source: [https://support.google.com/google-ads/answer/2459326?hl=en&ref_topic=10289453&sjid=5167206403107665975-EU](https://support.google.com/google-ads/answer/2459326?hl=en&ref_topic=10289453&sjid=5167206403107665975-EU)

#### Understanding bidding basics
Google Ads gives you several ways to bid for your ads, depending on what matters most to you and your business. Most advertisers focus on clicks, impressions, conversions, or views (for video ads).

Now that you're advertising on Google Ads, you probably have a clear goal in mind for your ads. If you sell coffee, maybe you want to get more people to visit your shop. If you run a hiking club, maybe you're aiming to get more people to sign up for your newsletter. And so on.

Knowing what you want your ads to do will help you decide how to bid.

Google Ads runs an auction every single time it has an ad space available -- on a search result, or on a blog, news site, or some other page. Each auction decides which ads will show at that moment in that space. Your bid puts you in the auction.

You can focus on different things when you bid: clicks, impressions, conversions, views, or engagements, depending on your campaign type. Which would you choose? Let's look at these more closely.

#### Focus on clicks (for Search and Display ads)
If your main goal is to have people visit your website, then clicks are a good place to start. Using cost-per-click (CPC) bidding, you'll pay only when someone actually clicks on your ad and comes to your site.

Example:

If you run a hiking club in Vermont, you might want to bid a lot for direct-hit keywords like "Vermont hiking" and a different amount for broader keywords like "hiking maps."

#### Focus on impressions
If your campaign is targeting just the Search Network and your main goal is to increase your brand visibility, consider using Target Impression Share. With this bidding strategy, Google Ads will automatically set your bids to help achieve your Impression Share goal. For example, if you choose an Impression Share target of 65% on the absolute top of the page, Google Ads will automatically set your bids to help show your ads on the absolute top of the page 65% of the total possible amount of times they could show.

If your campaign is targeting just the Display Network, instead of paying by the click, you can pay by the number of times your ad is visibly shown. That's called cost-per-thousand viewable impressions (vCPM) bidding, since you pay for every 1,000 times your ad appears and is viewable. If you're mostly interested in getting your name or logo in front of lots of people, this is a smart option. Learn how ads are measured as viewable.

Viewable CPM bidding, like CPC manual bidding, lets you set bids at the ad group level, or for individual placements.

#### Focus on conversions (for Search and Display ads)
With this advanced bidding method, you tell Google Ads the amount you're willing to pay for a conversion, or cost per action (CPA). A conversion (sometimes called an acquisition) is a particular action you want to happen on your website. Often that's a sale, but it could be an email sign-up or some other action. You pay for each engaged view and click on Display ads, but Google Ads will automatically set your bids for you to try to get you as many conversions as possible at the cost per action you specified.

To use CPA bidding you must have conversion tracking turned on, among other things, so CPA bidding is suited for intermediate and advanced Google Ads users.

#### Focus on views (for video ads only)
If your main goal is to evaluate how engaged viewers are with your video content, where they choose to watch your videos, and when they drop off from watching your content, you'll use cost-per-view (CPV) bidding. With CPV bidding, you'll pay for video views and other video interactions, such as clicks on the calls-to-action overlay (CTAs), cards, and companion banners.

To set a target CPV bid, you enter the average price you want to pay for a view while setting up your Video views campaign. Your bid is called your target CPV bid, or tCPV. This bid applies at the campaign level.

#### Related links
- About Target CPA bidding
- Determine a bid strategy based on your goals

#### Was this helpful?
---

#### Deliver better results with automated bidding
Source: [https://business.google.com/uk/ad-tools/bidding/?hl=en](https://business.google.com/uk/ad-tools/bidding/?hl=en)

#### Deliver better results with automated bidding


#### Set the right bids with Smart Bidding


#### Reach your audience at the right moment


#### Increase conversions with billions of combinations of signals


#### Bid towards conversion values to maximise your ROI


#### Bid for online and in-store sales


#### Grow your business with Google Ads
- Nespresso boosts direct-to-consumer revenue by leveraging AI-powered Search campaigns 25% increase in purchases

#### Nespresso boosts direct-to-consumer revenue by leveraging AI-powered Search campaigns
25% increase in purchases

- Paycor finds new growth paths among mid-market businesses using Google solutions 105% increase in revenue

#### Paycor finds new growth paths among mid-market businesses using Google solutions
105% increase in revenue

- loveholidays earns more profit using Smart Bidding compared to its own solution 57% more profit

#### loveholidays earns more profit using Smart Bidding compared to its own solution
57% more profit

#### Partner with a Google Ads expert to set up your first campaign
- We’ll get you up to speed on the latest platform updates
- We’ll design a media plan that makes the most of your budget
- We’ll help you launch your first campaign with hands-on guidance

#### Get started with Smart Bidding
More than 80% of Google advertisers are using automated bidding.

On average, advertisers that switch from a Target CPA to a Target ROAS bid strategy can see 14% more conversion value at a similar return on ad spend.

More than 80% of Google advertisers are using automated bidding.

On average, advertisers that switch from a Target CPA to a Target ROAS bid strategy can see 14% more conversion value at a similar return on ad spend.

1 / 2

#### Learn more about Smart Bidding
Page number 1 / 3

#### Tools and campaigns that can help you meet your goals
- Conversions +14% Conversions +14% Conversion Measurement Prioritise privacy while measuring which ads drive customers to make purchases online or in-store, sign contracts and more. Learn more

#### Conversion Measurement
Prioritise privacy while measuring which ads drive customers to make purchases online or in-store, sign contracts and more.

- 2024 Graduation Cards Luxury Travelers Entertainment News 1.2x 1.2x 1.1x 2 campaigns 2024 Graduation Cards Luxury Travelers Entertainment News 1.2x 1.2x 1.1x 2 campaigns 2024 Graduation Cards Luxury Travelers Entertainment News 1.2x 1.2x 1.1x 2 campaigns 2024 Graduation Cards Luxury Travelers Entertainment News 1.2x 1.2x 1.1x 2 campaigns Insights Page Grow your business with insights and trends that are tailored to your business. Learn more

#### Insights Page
Grow your business with insights and trends that are tailored to your business.

- Experiment Experiment Experiments Page The Experiments page in Google Ads can help you create, manage and optimise your experiments in one place. Learn more

#### Experiments Page
The Experiments page in Google Ads can help you create, manage and optimise your experiments in one place.

#### Frequently asked questions


#### What is bidding in Google Ads? add remove


#### What is the best bidding strategy for Google Ads? add remove
- Manual bidding, which allows you to determine what you want to pay
- Smart Bidding, which uses Google AI to optimise your bids at every auction based on your defined objective

#### How do I decide how much to bid on Google Ads? add remove
- Your campaign type
- How much your keywords cost
- How successful your keywords are

#### What is the minimum bid for Google Ads? add remove


#### How can automated bidding help an advertiser improve campaign performance? add remove
- Get as many clicks as possible within your budget
- Get as many conversions as possible within your target CPA
- Meet your ROAS target
- Get the most conversions or conversion value for your budget

#### How does value based bidding work? add remove


#### How much should I spend on Google Ads? add remove
---

#### Find answers andinspiration
Source: [https://business.google.com/uk/resources/?hl=en](https://business.google.com/uk/resources/?hl=en)

#### Find answers andinspiration


#### Filter by:


#### Product type
- Google Ads
- YouTube Ads

#### Campaign type
- App
- Display
- Multiple campaigns
- Performance Max
- Search
- Video/YouTube

#### Content type
- Article
- Success story

#### Industry
- eCommerce
- Food & beverage
- Wholesale retail

#### Marketing level
- Beginner
- Expert
- Intermediate

#### Marketing goal
- App
- Brand awareness
- Generate leads
- Increase website traffic
- Multiple marketing goals
- Offline sales
- Online sales
- Google Ads The Best Paid SEO Strategies for Businesses Article

#### Google Ads


#### The Best Paid SEO Strategies for Businesses
- YouTube Ads ABCDs of effective video ads Article
YouTube Ads

#### ABCDs of effective video ads
- Google Ads 10 tips for Google Ads budget management Article

#### Google Ads


#### 10 tips for Google Ads budget management
- Google Ads How can you write successful online ads with Google? Article

#### Google Ads


#### How can you write successful online ads with Google?
- Google Ads 5 ways to create better ad copy by utilising AI Article

#### Google Ads


#### 5 ways to create better ad copy by utilising AI
- Google Ads How to make your products stand out to shoppers on Google Ads Article

#### Google Ads


#### How to make your products stand out to shoppers on Google Ads
- Google Ads How assets can help you connect with valuable customers Article

#### Google Ads


#### How assets can help you connect with valuable customers
- Google Ads How to use the Keyword Planner tool effectively Article

#### Google Ads


#### How to use the Keyword Planner tool effectively
- Google Ads Reach a larger or new audience with Google Display Network (GDN) targeting Article

#### Google Ads


#### Reach a larger or new audience with Google Display Network (GDN) targeting
- Google Ads What are people searching for online? Article

#### Google Ads


#### What are people searching for online?
- Google Ads What is paid search? Article

#### Google Ads


#### What is paid search?
- Google Ads Billing and payments in Google Ads Article

#### Google Ads


#### Billing and payments in Google Ads
- Google Ads 5 things to consider when optimising your mobile landing page Article

#### Google Ads


#### 5 things to consider when optimising your mobile landing page
- Google Ads 10 Google Ads features that will grow your business Article

#### Google Ads


#### 10 Google Ads features that will grow your business
- Google Ads Understand intent to place ads more effectively Article

#### Google Ads


#### Understand intent to place ads more effectively
- Google Ads 4 Google Ads features to improve your keyword strategy Article

#### Google Ads


#### 4 Google Ads features to improve your keyword strategy
- Google Ads 4:42 Best Practices Guide: Reaching the right customers on Search Article

#### Google Ads


#### Best Practices Guide: Reaching the right customers on Search
- Google Ads Analytics in Google Ads Article

#### Google Ads


#### Analytics in Google Ads
- Google Ads 6:24 Best Practices Guide: Google AI for Video Advertising Article

#### Google Ads


#### Best Practices Guide: Google AI for Video Advertising
- Google Ads How to set up Google Ads: a checklist Article

#### Google Ads


#### How to set up Google Ads: a checklist
- YouTube Ads With help from TrueView for action, Nectar by Resident’s sales rise and shine Success story
YouTube Ads

#### With help from TrueView for action, Nectar by Resident’s sales rise and shine
- Google Ads How any business can grow online with Local Services Ads Article

#### Google Ads


#### How any business can grow online with Local Services Ads
- Google Ads How to set up conversion measurement on your website Article

#### Google Ads


#### How to set up conversion measurement on your website
- Google Ads Save time and drive efficiency with responsive display ads Article

#### Google Ads


#### Save time and drive efficiency with responsive display ads
- Google Ads 00:30 Currensea boosts customer acquisition 422%, with help of Google Search Success story

#### Google Ads


#### Currensea boosts customer acquisition 422%, with help of Google Search
- Google Ads How to unlock the value of your creative assets with Google Ads Article

#### Google Ads


#### How to unlock the value of your creative assets with Google Ads
- Google Ads 00:30 A strong brew: Bird & Blend sees 439% ROAS through Google Ads Success story

#### Google Ads


#### A strong brew: Bird & Blend sees 439% ROAS through Google Ads
- Google Ads 0:30 LØCI achieves 500% ROAS with Google Ads Success story

#### Google Ads


#### LØCI achieves 500% ROAS with Google Ads
- Google Ads Kinetica Sports’ full-funnel campaign hits 267% increase in ROAS, with help from Google Ads. Success story

#### Google Ads


#### Kinetica Sports’ full-funnel campaign hits 267% increase in ROAS, with help from Google Ads.
- How experimenting with their Google Ads Strategy helped Octopus Energy sign up over 2 million customers Success story

#### How experimenting with their Google Ads Strategy helped Octopus Energy sign up over 2 million customers
- Google Ads Best Practices Guide: AI Essentials in Google Ads Article

#### Google Ads


#### Best Practices Guide: AI Essentials in Google Ads
- Google Ads A beginners’ guide to YouTube video ads: Drive action with video advertising Article

#### Google Ads


#### A beginners’ guide to YouTube video ads: Drive action with video advertising
- Google Ads Get better results across all Google Ads channels with Performance Max campaigns Article

#### Google Ads


#### Get better results across all Google Ads channels with Performance Max campaigns
- Google Ads Understanding demand: How search data can improve your marketing performance Article

#### Google Ads


#### Understanding demand: How search data can improve your marketing performance
- Google Ads 00:30 How fashion brand Never Fully Dressed achieved 890% ROAS through Google Ads Success story

#### Google Ads


#### How fashion brand Never Fully Dressed achieved 890% ROAS through Google Ads
- Google Ads A guide to keyword match types in Google Ads Article

#### Google Ads


#### A guide to keyword match types in Google Ads
- Google Ads 00:30 Lucy & Yak sees 233% increase in revenue through Google Ads Success story

#### Google Ads


#### Lucy & Yak sees 233% increase in revenue through Google Ads
- Google Ads The perfect fit: Farai London scales by 400% with Google Ads Success story

#### Google Ads


#### The perfect fit: Farai London scales by 400% with Google Ads
- Google Ads Build trust online: How the Google Guarantee works Article

#### Google Ads


#### Build trust online: How the Google Guarantee works
- Google Ads A guide to App campaigns on Google Ads Article

#### Google Ads


#### A guide to App campaigns on Google Ads
- How optimisation helped PensionBee triple their customer base Success story

#### How optimisation helped PensionBee triple their customer base
- Google Ads 3 consumer shifts to influence your retail paid search strategy Article

#### Google Ads


#### 3 consumer shifts to influence your retail paid search strategy
- Google Ads Drive awareness and conversions: Cover the entire marketing funnel with Google Display Ads Article

#### Google Ads


#### Drive awareness and conversions: Cover the entire marketing funnel with Google Display Ads
- Google Ads What is Google Customer Match, and how can it help you reach valuable audiences online? Article

#### Google Ads


#### What is Google Customer Match, and how can it help you reach valuable audiences online?
- Google Ads Spark interest and inspire action: What are Demand Gen campaigns? Article

#### Google Ads


#### Spark interest and inspire action: What are Demand Gen campaigns?
- Google Ads Get more leads with less effort: a guide to lead form assets Article

#### Google Ads


#### Get more leads with less effort: a guide to lead form assets
- Google Ads How to tailor your ads to reach customers at every stage of their purchase journey Article

#### Google Ads


#### How to tailor your ads to reach customers at every stage of their purchase journey
- Google Ads How to save time and boost results with automated bidding Article

#### Google Ads


#### How to save time and boost results with automated bidding
- Google Ads How to improve your Google Ads Quality Score Article

#### Google Ads


#### How to improve your Google Ads Quality Score
- Google Ads From browsing to buying: 7 Search strategies to win new customers Article

#### Google Ads


#### From browsing to buying: 7 Search strategies to win new customers
- Google Ads How to increase website traffic and lead generation with Google Ads Article

#### Google Ads


#### How to increase website traffic and lead generation with Google Ads
- Google Ads How audience segments can help you find and reach the right customers at the right time Article

#### Google Ads


#### How audience segments can help you find and reach the right customers at the right time
- Google Ads Enhanced conversions: Measure ad performance while protecting people’s privacy Article

#### Google Ads


#### Enhanced conversions: Measure ad performance while protecting people’s privacy
- Google Ads Discover Mobile Advertising with Google Ads Article

#### Google Ads


#### Discover Mobile Advertising with Google Ads
- Google Ads Boost your business by advertising on Google Maps Article

#### Google Ads


#### Boost your business by advertising on Google Maps
- YouTube Ads Bellroy grows sales with shoppable Video action campaigns and value-based bidding Success story
YouTube Ads

#### Bellroy grows sales with shoppable Video action campaigns and value-based bidding
- Google Ads Navigating the B2B marketing funnel with Google Ads Article

#### Google Ads


#### Navigating the B2B marketing funnel with Google Ads
- YouTube Ads Majestic Heli Ski get nearly half of their new skiers from YouTube Success story
YouTube Ads

#### Majestic Heli Ski get nearly half of their new skiers from YouTube
- YouTube Ads BlendJet’s YouTube strategy led to 413% revenue growth Success story
YouTube Ads

#### BlendJet’s YouTube strategy led to 413% revenue growth
- YouTube Ads Adidas uses sequencing to move customers from awareness to consideration Success story
YouTube Ads

#### Adidas uses sequencing to move customers from awareness to consideration
- Google Ads Beyond the last click: Using attribution models to understand your Google Ads performance Article

#### Google Ads


#### Beyond the last click: Using attribution models to understand your Google Ads performance
- YouTube Ads Pringles masters tentpole marketing moments with TrueView for reach Success story
YouTube Ads

#### Pringles masters tentpole marketing moments with TrueView for reach
- YouTube Ads Measure your results Article
YouTube Ads

#### Measure your results
- YouTube Ads Xfinity Mobile turns data into dollars Success story
YouTube Ads

#### Xfinity Mobile turns data into dollars
- Google Ads Maximise your ROI: How to get started with value-based bidding on Google Ads Article

#### Google Ads


#### Maximise your ROI: How to get started with value-based bidding on Google Ads
- YouTube Ads Video action campaigns on YouTube Shorts helped Cider gain new customers at a 33% lower CPA Success story
YouTube Ads

#### Video action campaigns on YouTube Shorts helped Cider gain new customers at a 33% lower CPA
- Google Ads A foundation for success: How to structure your Google Ads account for growth on Search with AI Article

#### Google Ads


#### A foundation for success: How to structure your Google Ads account for growth on Search with AI
- Google Ads Paid search optimisation in the age of AI-powered marketing: How advertisers can stand out? Article

#### Google Ads


#### Paid search optimisation in the age of AI-powered marketing: How advertisers can stand out?
- Google Ads 5 ways to use Google AI for more effective advertising Article

#### Google Ads


#### 5 ways to use Google AI for more effective advertising
- Google Ads Simplifying multi-account management: Streamline your workflow with a Google Ads manager account Article

#### Google Ads


#### Simplifying multi-account management: Streamline your workflow with a Google Ads manager account
---

#### https://developers.google.com/ad-manager?hl=en
Source: [https://developers.google.com/ad-manager?hl=en](https://developers.google.com/ad-manager?hl=en)

- Home
- Products
- Ad Manager

#### A set of tools to manage your Google Ad Manager accounts and campaigns.


#### Ad Manager API (Beta)


#### Mobile Ads SDK


#### Dynamic Ad Insertion


#### Ad Manager SOAP API
---

#### https://developers.google.com/ad-manager/dynamic-ad-insertion?hl=en
Source: [https://developers.google.com/ad-manager/dynamic-ad-insertion?hl=en](https://developers.google.com/ad-manager/dynamic-ad-insertion?hl=en)

- Home
- Products
- Dynamic Ad Insertion

#### Dynamic ad insertion (DAI)
DAI lets you monetize your video content, taking away the complexity of the ad request and ad response process from the SDK. This approach reduces the likelihood of client-side errors and produces a TV-like experience without latency or buffering between content and ads.

With DAI, you can target individual ads for livestreams and videos on demand programming, obtain multi-screen reach with broad device support, and take advantage of programmatic monetization across all devices with Ad Exchange for video. Regardless of the original format of your content, once it becomes digital, DAI lets you show targeted video ads within your content, based on the individual user viewing the content.

DAI lets you perform these workflows through the Full service API and Pod serving API, along with supported SDK platforms.

To start using DAI, select one of the following integrations:

#### Full service DAI


#### Pod serving DAI


#### Supported platforms


#### Get Support
---

#### https://developers.google.com/ad-manager/dynamic-ad-insertion/full-service?hl=en
Source: [https://developers.google.com/ad-manager/dynamic-ad-insertion/full-service?hl=en](https://developers.google.com/ad-manager/dynamic-ad-insertion/full-service?hl=en)

- Home
- Products
- Dynamic Ad Insertion
- DAI Full Service API
- APIs

#### Full service DAI


#### With the IMA DAI SDK
- The web page or app loads the IMA DAI SDK through: an embedded script tag for HTML5 a native app for Android, Google Cast, iOS, tvOS, or Roku
- an embedded script tag for HTML5
- a native app for Android, Google Cast, iOS, tvOS, or Roku
- The SDK requests either a VOD stream or live stream from Google Ad Manager 360.
- Ad Manager 360 responds with the video stream that includes inserted ad breaks.
- The SDK parses the response, determines the correct media type based on environment, and delivers the video stream (and companion ads if needed) to the web page or app.
- The video player negotiates the playback details with the SDK and plays the content.
- The video player listens for instream metadata and passes it to the SDK for processing.
- The SDK fires impression pings and tracking events as needed.
For detailed instructions on how to implement a client video player using the IMA DAI SDK, check out our SDK guides:

#### With the DAI API
- The client's player app requests either a VOD stream or live stream from Google Ad Manager 360.
- Ad Manager 360 responds with the video stream that includes inserted ad breaks.
- The client's player app begins playback of the stream, and either requests ad metadata once (for VOD streams) OR begins regularly polling for ad metadata (for live streams).
- The client's player app listens for instream metadata, parses it, and compares it to the values in the ad metadata to identify ad events.
- The client's video player app fires ad impression pings and tracking events as needed.
For detailed instructions on how to implement a client video player, using the DAI REST API, check out our API guides:


---

#### https://developers.google.com/ad-manager/dynamic-ad-insertion/pod-serving?hl=en
Source: [https://developers.google.com/ad-manager/dynamic-ad-insertion/pod-serving?hl=en](https://developers.google.com/ad-manager/dynamic-ad-insertion/pod-serving?hl=en)

- Home
- Products
- Dynamic Ad Insertion
- DAI Pod Serving API
- APIs

#### DAI Pod Serving
Dynamic Ad Insertion (DAI) Pod Serving lets you request ad pods, from Google or third-party ad servers, for live and video-on-demand (VOD) streams. For more details, see Configure ad pods and break templates.

- Pod serving redirect: lets you retrieve manifest segments to implement Server-Side Ad Insertion (SSAI). The segments are dynamic URLs, redirecting to either content or ad media files.
- Pod serving manifest: lets you retrieve the complete manifest of the ad pods to implement Server-Side Ad Insertion (SSAI). For more details, see Server guided DAI.
For VOD, Google Ad Manager returns the complete ad pod manifests.

DAI Pod serving offers the following supported platforms:

For details on livestream and VOD, see the following workflows:

#### Stitch ads into a livestream
- To start a livestream session, make a stream registration request. Set ad tag parameters unique for the stream request to override the DAI ad tag's default values. For more details about ad targeting, see Supply targeting parameters to your stream.
- Retrieve the unique user session ID from the stream registration response. For more details about using the session ID, see Locate a DAI session ID or debug key and Monitor and debug a specific stream session.
- Make a manifest request to your video stitcher or manifest manipulator, passing the session ID. Repeat the request for manifest updates throughout playback.
- For DASH manifests, make one period template request for the entire session.
- For DASH manifests, cache the period template. For each ad break, retrieve the cached template and populate all macros with the ad break data. For more details about supported macros, see Populate the period template. Then, insert the result period into the final manifest.
- Return the final manifest that contains content or ad media segments for client playback. Playback begins.
- Regularly poll Google Ad Manager for updates of ad metadata using the polling frequency returned in the stream request. Store the ad metadata for looking up ad events.
- During an ad break, the video player loads the media segments and follows Google Ad Manager redirects to the media files.
- During an ad break, listen to the video player for timed metadata, containing ID3 tags. Extract the ad event ID from the ID3 tag to find the associated ad metadata.
- Send media verification pings to Google Ad Manager.

#### Stitch ads into a VOD stream
- Make a stream request to register a VOD stream session. Set ad tag parameters unique for the stream request to override the DAI ad tag's default values. For more details, see Supply targeting parameters to your stream.
- Retrieve the session ID from the stream response. To inspect the stream session, see Locate a DAI session ID or debug key and Monitor and debug a specific stream session.
- Make a manifest request to your video stitcher or manifest manipulator, passing the session ID.
- Use the session ID to request all ad pods at once.
- Retrieve complete manifests of all ad pods. To create the final manifest, stitch the ad pod manifests with the content stream.
- Return the final manifest, containing both content and ad segments.
- Request ad metadata for all ad events. Store the ad metadata for looking up ad events. Playback begins.
- During an ad break, the video player loads the media segments and follows Google Ad Manager redirects to the media files.
- During an ad break, listen for ad events containing ID3 tags. To find the ad event metadata, extract the ad event ID from the ID3 tag and match the ID with the ad metadata.
- Send media verification pings to Google Ad Manager.

---

#### Get started
Stay organized with collections



      Save and categorize content based on your preferences.

Source: [https://developers.google.com/ad-manager/api/start?hl=en](https://developers.google.com/ad-manager/api/start?hl=en)

Looking for a REST API? The Ad Manager API (Beta) is now available.

- Home
- Products
- Ad Manager

#### Get started Stay organized with collections Save and categorize content based on your preferences.


#### Page Summary
- The Google Ad Manager SOAP API allows building applications to manage inventory, create orders, and pull reports.
The Google Ad Manager SOAP API allows building applications to manage inventory, create orders, and pull reports.

- Client libraries are available for Java, .NET, Python, PHP, and Ruby to help get started with the API.
Client libraries are available for Java, .NET, Python, PHP, and Ruby to help get started with the API.

- To make your first API request, you need to get access to an Ad Manager network, create authentication credentials using OAuth 2.0, and configure API access in your network settings.
To make your first API request, you need to get access to an Ad Manager network, create authentication credentials using OAuth 2.0, and configure API access in your network settings.

- After setting up your Ad Manager network and authentication, download and configure one of the provided client libraries to write code and make requests to the API.
After setting up your Ad Manager network and authentication, download and configure one of the provided client libraries to write code and make requests to the API.

You can use the Google Ad Manager SOAP API to build apps that manage inventory, create orders, pull reports, and more.

To help you get started, we offer client libraries for Java, .NET, Python, PHP, and Ruby.

To make your first API request, follow these steps:

#### Get access to an Ad Manager network
If you don't already have one, sign up for an Ad Manager account. You can also create a test network if you want to test the API in a separate environment. Note that you don't need an AdSense account for test purposes.

Make a note of your network code. You can find this in the URL when you sign in to your network. For example, in the URL https://admanager.google.com/1234#home, 1234 is your network code.

#### Create authentication credentials
You must authenticate all Ad Manager SOAP API requests using OAuth 2.0. The following steps cover the use case of accessing your own Ad Manager data. For more details and other options, see Authentication.

- Open the Google API Console Credentials page
Open the Google API Console Credentials page

- From the project menu, choose Create project, enter a name for the project, and optionally, edit the provided Project ID. Click Create.
From the project menu, choose Create project, enter a name for the project, and optionally, edit the provided Project ID. Click Create.

- On the Credentials page, select Create credentials, then select Service account key.
On the Credentials page, select Create credentials, then select Service account key.

- Select New service account and select JSON as the key type.
Select New service account and select JSON as the key type.

- Click Create to download a file containing a private key.
Click Create to download a file containing a private key.

#### Configure your Ad Manager network
- Sign in to Google Ad Manager.
Sign in to Google Ad Manager.

- In the sidebar, click Admin > Global settings.
In the sidebar, click Admin > Global settings.

- Under General settings > Api access click the slider to Enabled.
Under General settings > Api access click the slider to Enabled.

- Click the Save button at the bottom of the page.
Click the Save button at the bottom of the page.

#### Set up your client
Download one of the Ad Manager client libraries. The libraries offer wrapper functions and features that make it easier and faster to develop apps.

The following tabs provide quickstarts for coding in each of the languages for which there is a client library.

#### Java
Here is a basic example that shows how to use the Java client library. For more detailed usage information, refer to the README file in the client library distribution.

- Setup your credentials Run the following command in a shell: curl https://raw.githubusercontent.com/googleads/googleads-java-lib/main/examples/admanager_axis/src/main/resources/ads.properties -o ~/ads.properties Open the ~/ads.properties file and populate the following fields: [...] api.admanager.applicationName=INSERT_APPLICATION_NAME_HERE api.admanager.jsonKeyFilePath=INSERT_PATH_TO_JSON_KEY_FILE_HERE api.admanager.networkCode=INSERT_NETWORK_CODE_HERE [...]
Run the following command in a shell:

- Specify dependencies Edit your pom.xml file and add the following to the dependencies tag. You can find the latest version number on Github. <dependency> <groupId>com.google.api-ads</groupId> <artifactId>ads-lib</artifactId> <version>RELEASE</version> </dependency> <dependency> <groupId>com.google.api-ads</groupId> <artifactId>dfp-axis</artifactId> <version>RELEASE</version> </dependency>
Specify dependencies

Edit your pom.xml file and add the following to the dependencies tag. You can find the latest version number on Github.

- Write some code and make a request! import com.google.api.ads.common.lib.auth.OfflineCredentials; import com.google.api.ads.common.lib.auth.OfflineCredentials.Api; import com.google.api.ads.admanager.axis.factory.AdManagerServices; import com.google.api.ads.admanager.axis.v202602.Network; import com.google.api.ads.admanager.axis.v202602.NetworkServiceInterface; import com.google.api.ads.admanager.lib.client.AdManagerSession; import com.google.api.client.auth.oauth2.Credential; public class App { public static void main(String[] args) throws Exception { Credential oAuth2Credential = new OfflineCredentials.Builder() .forApi(Api.AD_MANAGER) .fromFile() .build() .generateCredential(); // Construct an AdManagerSession. AdManagerSession session = new AdManagerSession.Builder() .fromFile() .withOAuth2Credential(oAuth2Credential) .build(); // Construct a Google Ad Manager service factory, which can only be used once per // thread, but should be reused as much as possible. AdManagerServices adManagerServices = new AdManagerServices(); // Retrieve the appropriate service NetworkServiceInterface networkService = adManagerServices.get(session, NetworkServiceInterface.class); // Make a request Network network = networkService.getCurrentNetwork(); System.out.printf("Current network has network code '%s' and display" + " name '%s'.%n", network.getNetworkCode(), network.getDisplayName()); } } View on GitHub
Write some code and make a request!

#### Python
Here is a basic example that shows how to use the Python client library. The Python Client Library supports Python v3.6+. For more detailed usage information, refer to the README file in the client library distribution.

- Install the library and set up your credentials. Run the following commands in a shell: python3 -m pip install googleads curl https://raw.githubusercontent.com/googleads/googleads-python-lib/main/googleads.yaml \ -o ~/googleads.yaml
Run the following commands in a shell:

- Set up your ~/googleads.yaml file. Fill in the following fields: ad_manager: application_name: INSERT_APPLICATION_NAME_HERE network_code: INSERT_NETWORK_CODE_HERE path_to_private_key_file: INSERT_PATH_TO_FILE_HERE
Fill in the following fields:

- Run some code and make a request. # Import the library. from googleads import ad_manager # Initialize a client object, by default uses the credentials in ~/googleads.yaml. client = ad_manager.AdManagerClient.LoadFromStorage() # Initialize a service. network_service = client.GetService('NetworkService', version='v202602') # Make a request. current_network = network_service.getCurrentNetwork() print("Current network has network code '%s' and display name '%s'." % (current_network['networkCode'], current_network['displayName'])) View on GitHub

#### PHP
Here is a basic example that shows how to use the PHP client library.

- Install the library and setup your credentials. Run the following commands in a shell to install the client library and download the adsapi_php.ini file to your home directory: composer require googleads/googleads-php-lib curl https://raw.githubusercontent.com/googleads/googleads-php-lib/main/examples/AdManager/adsapi_php.ini -o ~/adsapi_php.ini
Run the following commands in a shell to install the client library and download the adsapi_php.ini file to your home directory:

- Setup your ~/adsapi_php.ini file. Fill in the following fields: [AD_MANAGER] networkCode = "INSERT_NETWORK_CODE_HERE" applicationName = "INSERT_APPLICATION_NAME_HERE" [OAUTH2] jsonKeyFilePath = "INSERT_ABSOLUTE_PATH_TO_OAUTH2_JSON_KEY_FILE_HERE" scopes = "https://www.googleapis.com/auth/dfp"
Fill in the following fields:

- Run some code and make a request! This example code must be run from the command line, not a browser. The file containing this code must reside in the root of the project directory, where composer require was run. <?php require 'vendor/autoload.php'; use Google\AdsApi\AdManager\AdManagerSession; use Google\AdsApi\AdManager\AdManagerSessionBuilder; use Google\AdsApi\AdManager\v202602\ApiException; use Google\AdsApi\AdManager\v202602\ServiceFactory; use Google\AdsApi\Common\OAuth2TokenBuilder; // Generate a refreshable OAuth2 credential for authentication. $oAuth2Credential = (new OAuth2TokenBuilder()) ->fromFile() ->build(); // Construct an API session configured from a properties file and the OAuth2 // credentials above. $session = (new AdManagerSessionBuilder()) ->fromFile() ->withOAuth2Credential($oAuth2Credential) ->build(); // Get a service. $serviceFactory = new ServiceFactory(); $networkService = $serviceFactory->createNetworkService($session); // Make a request $network = $networkService->getCurrentNetwork(); printf( "Network with code %d and display name '%s' was found.\n", $network->getNetworkCode(), $network->getDisplayName() ); View on GitHub

#### .NET
Here is a basic example that shows how to use the .NET client library

- Create a new project Open Visual Studio and create a new project (Console Application).
Open Visual Studio and create a new project (Console Application).

- Add required library references to your project Add a nuget dependency for Google.Dfp.
Add a nuget dependency for Google.Dfp.

- Setup your App.config Copy src\App.config to your project directory and add it to your project. If your application has its own App.config, then you can copy the following nodes into your App.config: configuration/AdManagerApi configuration/configSections/section[name="AdManagerApi"] configuration/system.net
Copy src\App.config to your project directory and add it to your project. If your application has its own App.config, then you can copy the following nodes into your App.config:

- configuration/AdManagerApi
- configuration/configSections/section[name="AdManagerApi"]
- configuration/system.net
- Setup credentials Open App.config and edit the following keys: <add key="ApplicationName" value="INSERT_YOUR_APPLICATION_NAME_HERE" /> <add key="NetworkCode" value="INSERT_YOUR_NETWORK_CODE_HERE" /> <add key="OAuth2Mode" value="SERVICE_ACCOUNT" /> <add key="OAuth2SecretsJsonPath" value="INSERT_OAUTH2_SECRETS_JSON_FILE_PATH_HERE" />
Open App.config and edit the following keys:

- Make a call to the library You can call the library as shown in the following C# code snippet View on GitHub AdManagerUser user = new AdManagerUser(); using (InventoryService inventoryService = user.GetService<InventoryService>()) { // Create a statement to select ad units. int pageSize = StatementBuilder.SUGGESTED_PAGE_LIMIT; StatementBuilder statementBuilder = new StatementBuilder().OrderBy("id ASC").Limit(pageSize); // Retrieve a small amount of ad units at a time, paging through until all // ad units have been retrieved. int totalResultSetSize = 0; do { AdUnitPage page = inventoryService.getAdUnitsByStatement(statementBuilder.ToStatement()); // Print out some information for each ad unit. if (page.results != null) { totalResultSetSize = page.totalResultSetSize; int i = page.startIndex; foreach (AdUnit adUnit in page.results) { Console.WriteLine( "{0}) Ad unit with ID \"{1}\" and name \"{2}\" was found.", i++, adUnit.id, adUnit.name); } } statementBuilder.IncreaseOffsetBy(pageSize); } while (statementBuilder.GetOffset() < totalResultSetSize); Console.WriteLine("Number of results found: {0}", totalResultSetSize); }
You can call the library as shown in the following C# code snippet

If you don't want to set your credentials in your App.config, then refer to this wiki article for alternate ways of using the AdManagerUser class. For more detailed information about using the .NET Client Library, refer to the README . If you want to develop in .NET without the client library, please refer to the NoClientLibrary wiki article.

#### Ruby
Here is a basic example that shows how to use the Ruby client library. The Ruby client library requires Ruby 2.1 or later.

- Install the Ruby gem and get the configuration file. Run the following commands in a shell: gem install google-dfp-api curl https://raw.githubusercontent.com/googleads/google-api-ads-ruby/main/ad_manager_api/ad_manager_api.yml -o ~/ad_manager_api.yml If you encounter an error such as "cannot load such file -- mkmf (LoadError)" at any point while installing your gems, you may need to install additional Ruby development libraries such as ruby-dev, ruby-devel, xcode-select etc. for your particular environment.
Run the following commands in a shell:

- Setup your credentials Populate the required fields in the ~/ad_manager_api.yml file. If you don't already have an OAuth2 keyfile, you'll need to follow the steps to create your OAuth2 credentials. :authentication: :oauth2_keyfile: INSERT_PATH_TO_JSON_KEY_FILE_HERE :application_name: INSERT_APPLICATION_NAME_HERE :network_code: INSERT_NETWORK_CODE_HERE
Populate the required fields in the ~/ad_manager_api.yml file. If you don't already have an OAuth2 keyfile, you'll need to follow the steps to create your OAuth2 credentials.

- Write some code and make a request! # Import the library. require 'ad_manager_api' # Initialize an Ad Manager client instance (uses credentials in ~/ad_manager_api.yml by default). ad_manager = AdManagerApi::Api.new # Get a service instance. network_service = ad_manager.service(:NetworkService, :v202602) # Make a request. network = network_service.get_current_network() puts "The current network is %s (%d)." % [network[:display_name], network[:network_code]] View on GitHub
More detailed steps for getting started can be found in the README file that is distributed with the Ruby client library. Also, check out our full example library for Ruby.

#### Next steps
When you have a client library up and running, modify the examples provided to extend them for your needs.

Browse the reference documentation to learn more about the API.

If you need help, visit our Support page.


---

#### Learn more, do more.
Source: [https://admanager.google.com/home/resources/?hl=en](https://admanager.google.com/home/resources/?hl=en)

#### Learn more, do more.
Learn how global publishers are using publisher provided Identifiers to increase programmatic revenue in browsers that no longer support third-party cookies.

#### Read Story
Our monthly newsletter puts the latest success stories, insights, and product news right into your inbox.

#### Filter by:
- Topic Ad Formats Advanced TV Brand Safety Core Ad Serving Data and Insights Dynamic Ad Insertion Ecosystem Mobile App Privacy Video Yield Management
- Ad Formats
- Advanced TV
- Brand Safety
- Core Ad Serving
- Data and Insights
- Dynamic Ad Insertion
- Ecosystem
- Mobile App
- Privacy
- Video
- Yield Management
- Type Feature Brief Guide Report White Paper
- Feature Brief
- Guide
- Report
- White Paper

#### No matching results
- Guide Publisher best practices for live sporting events Read more

#### Publisher best practices for live sporting events
- Read more
- Feature Brief Powering direct transactions: Investing in your growth Read more

#### Powering direct transactions: Investing in your growth
- Read more
- Report Building the future of live monetization Read more

#### Building the future of live monetization
- Read more
- Report Increase your revenue in browsers with limited signals Read more

#### Increase your revenue in browsers with limited signals
- Read more
- Guide The publisher’s playbook for navigating today’s privacy environment Read more

#### The publisher’s playbook for navigating today’s privacy environment
- Read more
- Report For e-commerce, the time for digital ads is now Read more

#### For e-commerce, the time for digital ads is now
- Read more
- Guide How automation can help you manage and grow your business Read more

#### How automation can help you manage and grow your business
- Read more
- Report 2020 advanced TV inventory report Read more

#### 2020 advanced TV inventory report
- Read more
- Guide Building a Retail Media Business with Google Read more

#### Building a Retail Media Business with Google
- Read more
- Guide Protecting your ad-supported CTV experiences Read more

#### Protecting your ad-supported CTV experiences
- Read more
- Guide Getting started with Dynamic Ad Insertion Read more

#### Getting started with Dynamic Ad Insertion
- Read more
- White Paper The Next-Generation Telco Bundle Read more

#### The Next-Generation Telco Bundle
- Read more
- Feature Brief Maximize your revenue with Opportunities and Experiments Read more

#### Maximize your revenue with Opportunities and Experiments
- Read more
- Feature Brief Get customized insights with Ad Manager reporting Read more

#### Get customized insights with Ad Manager reporting
- Read more
- Feature Brief How Authorized Buyers work with Google Ad Manager Read more

#### How Authorized Buyers work with Google Ad Manager
- Read more
- Feature Brief Use machine learning to manage and forecast inventory more effectively Read more

#### Use machine learning to manage and forecast inventory more effectively
- Read more
- Feature Brief Capture growing video budgets with out-stream video ads Read more

#### Capture growing video budgets with out-stream video ads
- Read more
- Feature Brief Streamlined and improved workflows for video content ingestion Read more

#### Streamlined and improved workflows for video content ingestion
- Read more
- Guide Reimagining the commercial break everywhere viewers are watching Read more

#### Reimagining the commercial break everywhere viewers are watching
- Read more
- Report 2019 Advanced TV Inventory Report Read more

#### 2019 Advanced TV Inventory Report
- Read more
- Report APAC’s changing digital landscape: How broadcast and video companies can keep up Read more

#### APAC’s changing digital landscape: How broadcast and video companies can keep up
- Read more
- Feature Brief Save time and increase inventory value with Open Measurement for apps Read more

#### Save time and increase inventory value with Open Measurement for apps
- Read more
- Feature Brief Modernize your direct deals with Programmatic Guaranteed Read more

#### Modernize your direct deals with Programmatic Guaranteed
- Read more
- Feature Brief Seamlessly reach viewers everywhere with Dynamic Ad Insertion Read more

#### Seamlessly reach viewers everywhere with Dynamic Ad Insertion
- Read more
- Feature Brief Earn more from your video content with Smarter Ad Breaks Read more

#### Earn more from your video content with Smarter Ad Breaks
- Read more
- Feature Brief Monitor and manage ad exchange ads in the Ad review center Read more

#### Monitor and manage ad exchange ads in the Ad review center
- Read more
- Feature Brief Get comprehensive yield management with Google Ad Manager Read more

#### Get comprehensive yield management with Google Ad Manager
- Read more
- Feature Brief Improve app revenue and fill rates with App Mediation Read more

#### Improve app revenue and fill rates with App Mediation
- Read more
- Feature Brief Create a customized ad experience with Native Ads Read more

#### Create a customized ad experience with Native Ads
- Read more
- Feature Brief Improving user experience with the Better Ads Standards Read more

#### Improving user experience with the Better Ads Standards
- Read more
- Feature Brief Bring more bids to the auction with Open Bidding Read more

#### Bring more bids to the auction with Open Bidding
- Read more
- Feature Brief Create a better ad experience with rewarded ads Read more

#### Create a better ad experience with rewarded ads
- Read more
- Guide Video viewability best practices guide for publishers Read more

#### Video viewability best practices guide for publishers
- Read more
- Report Grow faster with a Google Certified Publishing Partner Read more

#### Grow faster with a Google Certified Publishing Partner
- Read more
- Guide Rethink your eCommerce experience with Google Ad Manager Read more

#### Rethink your eCommerce experience with Google Ad Manager
- Read more
- Report The convergence of TV and digital: How broadcasters are building for success Read more

#### The convergence of TV and digital: How broadcasters are building for success
- Read more
- Guide Taking a Page from the Sports Playbook: Engaging Fans in the Digital Age Read more

#### Taking a Page from the Sports Playbook: Engaging Fans in the Digital Age
- Read more
- Guide Digital Trade Marketing: Delighting Shoppers in the Age of Digital Read more

#### Digital Trade Marketing: Delighting Shoppers in the Age of Digital
- Read more
- Report Publishers save 57% more time with Programmatic Guaranteed deals Read more

#### Publishers save 57% more time with Programmatic Guaranteed deals
- Read more
- Report Capture growing video budgets with new out-stream formats on Google Ad Manager Read more

#### Capture growing video budgets with new out-stream formats on Google Ad Manager
- Read more
- Report Building for beyond with the Insights Engine Project Read more

#### Building for beyond with the Insights Engine Project
- Read more
- Report Digitizing supplier marketing: Increasing sales of products and services Read more

#### Digitizing supplier marketing: Increasing sales of products and services
- Read more
- Report Improving protections for publishers Read more

#### Improving protections for publishers
- Read more
- Report TV made smarter with Google Ad Manager Read more

#### TV made smarter with Google Ad Manager
- Read more
- Report What’s next for the mobile web? Read more

#### What’s next for the mobile web?
- Read more
- Report Programmatic Guaranteed with custom creatives delivers scale for Vox Media Read more

#### Programmatic Guaranteed with custom creatives delivers scale for Vox Media
- Read more
- Guide Creating better ad experiences for everyone Read more

#### Creating better ad experiences for everyone
- Read more
- Guide How publishers can engage with people who use ad blockers Read more

#### How publishers can engage with people who use ad blockers
- Read more
- Report Programmatic TV’s European Evolution Read more

#### Programmatic TV’s European Evolution
- Read more

#### Hungry for more?
Learn how global publishers are finding success using Ad Manager to power their ads businesses.


---

#### ad-manager overview (0.50.0)
Stay organized with collections



      Save and categorize content based on your preferences.

Source: [https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/overview?hl=en](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/overview?hl=en)

- Home
- Documentation
- Developer tools
- Java
- Client libraries

#### ad-manager overview (0.50.0) Stay organized with collections Save and categorize content based on your preferences.


#### Key Reference Links
Google Ad Manager API Description: The Ad Manager API enables an app to integrate with Google Ad Manager. You can read Ad Manager data and run reports using the API.

#### Getting Started
In order to use this library, you first need to go through the following steps:

- Install a JDK (Java Development Kit)
- Select or create a Cloud Platform project
- Enable billing for your project
- Enable the API
- Set up authentication

#### Use the Google Ad Manager API for Java
To ensure that your project uses compatible versions of the libraries and their component artifacts, import com.google.cloud:libraries-bom and use the BOM to specify dependency versions. Be sure to remove any versions that you set previously. For more information about BOMs, see Google Cloud Platform Libraries BOM.

#### Maven
Import the BOM in the dependencyManagement section of your pom.xml file. Include specific artifacts you depend on in the dependencies section, but don't specify the artifacts' versions in the dependencies section.

The example below demonstrates how you would import the BOM and include the ad-manager artifact.

#### Gradle
BOMs are supported by default in Gradle 5.x or later. Add a platform dependency on com.google.cloud:libraries-bom and remove the version from the dependency declarations in the artifact's build.gradle file.

The example below demonstrates how you would import the BOM and include the ad-manager artifact.

The platform and enforcedPlatform keywords supply dependency versions declared in a BOM. The enforcedPlatform keyword enforces the dependency versions declared in the BOM and thus overrides what you specified.

For more details of the platform and enforcedPlatform keywords Gradle 5.x or higher, see Gradle: Importing Maven BOMs.

If you're using Gradle 4.6 or later, add enableFeaturePreview('IMPROVED_POM_SUPPORT') to your settings.gradle file. For details, see Gradle 4.6 Release Notes: BOM import. Versions of Gradle earlier than 4.6 don't support BOMs.

#### SBT
SBT doesn't support BOMs. You can find recommended versions of libraries from a particular BOM version on the dashboard and set the versions manually. To use the latest version of this library, add this to your dependencies:

#### Which version ID should I get started with?
For this library, we recommend using com.google.ads.admanager.v1 for new applications.

#### Understanding Version ID and Library Versions
When using a Cloud client library, it's important to distinguish between two types of versions:

- Library Version: The version of the software package (the client library) that helps you interact with the Cloud service. These libraries are released and updated frequently with bug fixes, improvements, and support for new service features and versions. The version selector at the top of this page represents the client library version.
- Version ID: The version of the Cloud service itself (e.g. Google Ad Manager API). New Version IDs are introduced infrequently, and often involve changes to the core functionality and structure of the Cloud service itself. The packages in the lefthand navigation represent packages tied to a specific Version ID of the Cloud service.

#### Managing Library Versions
We recommend using the com.google.cloud:libraries-bom installation method detailed above to streamline dependency management across multiple Cloud Java client libraries. This ensures compatibility and simplifies updates.

#### Choosing the Right Version ID
Each Cloud Java client library may contain packages tied to specific Version IDs (e.g., v1, v2alpha). For new production applications, use the latest stable Version ID. This is identified by the highest version number without a suffix (like "alpha" or "beta"). You can read more about Cloud API versioning strategy here.

Important: Unstable Version ID releases (those with suffixes) are subject to breaking changes when upgrading. Use them only for testing or if you specifically need their experimental features.


---

### AI Agents Concept & Architecture
*Source: local://ai_agents_knowledge.md*

#### AI Agents Knowledge Repository
Synthesized from Google Innovation & AI Blog

#### [test](test)


#### Definitions
- **General summary**: test content

---

#### [Innovation & AI](https://blog.google/innovation-and-ai/)


#### Google Cloud Tools
- Infrastructure & cloud
- Gemini
- Gemma

---

#### [Infrastructure & Cloud](https://blog.google/innovation-and-ai/infrastructure-and-cloud/)


#### Google Cloud Tools
- 7 highlights from Google Cloud Next ‘26
- Google Cloud Next ‘26
- Gemini
- Gemini Enterprise Agent Platform

---

#### [Global Network](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/)


#### Google Cloud Tools
- Gemini

---

#### [Google expands Alabama data center campus, funds community efforts](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/alabama-investment-june-2026/)


#### Google Cloud Tools
- Gemini

---

#### [Google Cloud](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/)


#### Google Cloud Tools
- 7 highlights from Google Cloud Next ‘26
- Google Cloud Next ‘26
- Gemini
- Gemini Enterprise Agent Platform

---

#### [Cloud Next ‘26: Momentum and innovation at Google scale](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/)


#### Definitions
- **Basic explainer**: Google is growing its cloud business fast by helping companies build and manage thousands of AI agents. They’re launching new, powerful computer chips to handle all this extra work and keep systems secure from hackers. Google also uses its own AI tools to write code and fix security bugs much faster than before. These updates help businesses get more done with less effort.
- **3. Introducing our eighth-generation TPUs**: In the era of AI agents, infrastructure needs to evolve to take on the most demanding AI workloads. This year, we’re bringing the eighth generation of our Tensor Processing Units with a dual chip approach: TPU 8t , optimized for training, scales up to 9,600 TPUs and 2 petabytes of shared, high-bandwidth memory in a single superpod. It achieves three times the processing power of Ironwood and delivers up to 2x more performance/watt. TPU 8i , optimized for inference, connects 1,152 TPUs in a single pod, dramatically reducing latency, with 3x more on-chip SRAM, to deliver the massive throughput and low latency needed to concurrently run millions of agents cost-effectively. We’ll offer these to Cloud customers as a core part of our selection of compute processors, along with a portfolio of NVIDIA GPU instances. Read more in our blog post .

#### Google Cloud Tools
- Gemini
- Gemini Enterprise Agent Platform

---

#### [7 highlights from Google Cloud Next ‘26](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/google-cloud-next-26-recap/)


#### Definitions
- **Basic explainer**: Google is moving into the "agentic era," where AI acts as a partner that can actually do work for you. They launched new tools that let anyone build these AI helpers without needing to know how to code. They also upgraded their massive computer chips and data systems to make sure these agents run faster and stay secure. Big companies are already using this tech to handle everything from customer orders to complex research.

#### Google Cloud Tools
- Gemini
- Nano Banana
- Gemini Enterprise App
- Gemini Enterprise Agent Platform

---

#### [How Google Does It: An inside look at cybersecurity](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/how-google-does-it-security-series/)


#### Google Cloud Tools
- Gemini

---

#### [Google Cloud Next ‘26](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/next-2026/)


#### Google Cloud Tools
- Gemini
- Gemini Enterprise Agent Platform

---

#### [Google Cloud](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/rss/)


#### Google Cloud Tools
- Gemini
- Kaggle
- Gemini Enterprise Agent Platform

---

#### [Models & research](https://blog.google/innovation-and-ai/models-and-research/)


#### Google Cloud Tools
- Gemini
- Google Flow

---

#### [Gemini Models](https://blog.google/innovation-and-ai/models-and-research/gemini-models/)


#### Google Cloud Tools
- Gemini

---

#### [Fluid, natural voice translation with Gemini 3.5 Live Translate](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-live-3-5-translate/)


#### Google Cloud Tools
- Gemini
- SynthID

---

#### [Introducing Gemini Omni](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/)


#### Use Cases
- **Edit your videos through conversation**: Gemini Omni gives you an easier way to edit video — with natural language. Every instruction builds on the last. Your characters stay consistent, the physics hold up and the scene remembers what came before. Transform the world around you. Change specific things, or change everything. Your video becomes the starting point for something you never could have filmed yourself.
- **Bring ideas to life, grounded in Gemini’s world knowledge**: Gemini Omni doesn't just build scenes that look real, it reasons about what should happen next. It combines an intuitive understanding of physics with Gemini's knowledge of history, science and cultural context, bridging the gap from photorealism to meaningful storytelling. Create visuals with more accurate physics. Omni has an improved intuitive understanding of forces like gravity, kinetic energy and fluid dynamics, allowing you to create more realistic scenes.
- **Create videos from any combination of inputs**: Reference anything. Omni turns any reference — image, text, video or audio — into a single, cohesive output. While only voice references will be supported for audio to start, we’ll roll out other types of audio inputs soon.
- **Create videos with your own digital avatar**: We're committed to developing AI responsibly and we have clear policies to protect users from harm and governing the use of our AI tools. To start, you can create videos with your own voice by using Avatars , which create a digital version of yourself so you can generate videos that look and sound like you. Beyond the avatar feature, in terms of editing videos to change audio and speech, we are still working to test this and better understand how we can bring this capability to users responsibly. All videos created with Omni include our imperceptible SynthID digital watermark. You can easily verify that videos were generated with Gemini Omni through the Gemini app, Gemini in Chrome and Google Search. You can find out more about how we're expanding our content transparency and verification tools to help you understand how content was created and edited across the web in our blog post .

#### Google Cloud Tools
- Gemini
- Nano Banana
- Google Flow
- YouTube Shorts
- YouTube Create App
- SynthID
- Avatars

---

#### [Deep Research Max: a step change for autonomous research agents](https://blog.google/innovation-and-ai/models-and-research/gemini-models/next-generation-gemini-deep-research/)


#### Definitions
- **Basic explainer**: Google just released two new AI research agents that can dig through massive amounts of data to write professional reports. One version is built for speed, while the other, called Deep Research Max, handles complex, deep-dive projects. These tools can even create their own charts and connect to your private files to find specific answers. It’s a huge upgrade that helps people get expert-level analysis done much faster than before.
- **Choose a research configuration that fits your workflow**: Building upon our initial release of Gemini Deep Research, we’re introducing two distinct agents designed to match your needs ranging from direct user assistance to large-scale, offline research processes: Deep Research: Optimized for speed and efficiency, this new agent replaces our preview release from December and delivers significantly reduced latency and cost at higher quality levels. It is the ideal agent for research experiences integrated directly into interactive user surfaces where lower latency is desired. Deep Research Max: Designed for maximum comprehensiveness and highest-quality synthesis, Max leverages extended test-time compute to iteratively reason, search and refine the final report. It is the perfect engine for asynchronous, background workflows such as a nightly cron job triggering the generation of exhaustive due diligence reports for an analyst team by morning.

#### Use Cases
- **Drive real-world results with expert-grade analysis**: Deep Research Max delivers highly comprehensive reports, rigorous factuality and expert-grade analysis cheaper and more efficiently than ever before. Compared to our December release, Deep Research Max consults significantly more sources and identifies critical nuances the older release frequently overlooked. We have also focused on teaching Deep Research to consult a diverse array of sources and carefully weighing conflicting evidence against each other. The result is a nuanced report that draws from authoritative sources like SEC filings and open-access peer-reviewed journals, lays out information well and transforms dense technical data into actionable, stakeholder-ready formats.

#### Benefits
- **Bullet points**: Google’s "Deep Research Max" article introduces powerful new autonomous agents for advanced data analysis. Choose between the fast Deep Research agent or the comprehensive Deep Research Max model. These agents now securely connect to your private data using the Model Context Protocol. The system creates professional charts and infographics to help you visualize complex research findings. You can now guide the agent's research plan to ensure you get exactly what's needed.
- **Unlock proprietary data and rich native visuals**: Deep Research can now search the web, arbitrary remote MCPs, file uploads and connected file stores — or any subset of them — introducing capabilities designed to handle the complex, gated data universes that professionals rely on daily. Model Context Protocol (MCP) support: You can now seamlessly connect Deep Research to your custom data and specialized professional data streams (such as financial or market data providers) securely via MCP. Deep Research supports arbitrary tool definitions which transforms it from a web searcher into an autonomous agent capable of navigating any specialized data repositories. Native charts and infographics: A first for Deep Research in the Gemini API, our agent no longer just creates text; it natively generates high-quality charts and infographics in-line with HTML or Nano Banana , dynamically visualizing complex data sets to enrich analytical reports.
- **Take advantage of proven Google scale performance**: When you build with the Deep Research agent, you are tapping into the same autonomous research infrastructure that powers research capabilities within some of Google’s most popular products like Gemini App , NotebookLM , Google Search and Google Finance .

#### Google Cloud Tools
- Gemini models
- Gemini
- Gemma
- Model Context Protocol

#### - MCP
- Interactions API
- Nano Banana

---

#### [Gemini Models](https://blog.google/innovation-and-ai/models-and-research/gemini-models/rss/)


#### Google Cloud Tools
- Gemini
- Gemma
- Vertex AI
- Kaggle
- Nano Banana

---

#### [Google DeepMind](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/)


#### Google Cloud Tools
- Gemini

---

#### [Google DeepMind](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/rss/)


#### Google Cloud Tools
- Gemini
- Kaggle
- Nano Banana

---

#### [Google Labs](https://blog.google/innovation-and-ai/models-and-research/google-labs/)


#### Google Cloud Tools
- Gemini

---

#### [Meet Dreambeans, an app that connects you with what matters](https://blog.google/innovation-and-ai/models-and-research/google-labs/dreambeans/)


#### Google Cloud Tools
- Gemini
- Nano Banana

---

#### [Google Labs](https://blog.google/innovation-and-ai/models-and-research/google-labs/rss/)


#### Google Cloud Tools
- Gemini
- Nano Banana
- Google Flow

---

#### [Google Research](https://blog.google/innovation-and-ai/models-and-research/google-research/)


#### Google Cloud Tools
- Gemini

---

#### [Google advances its AMIE research medical AI from diagnosis to treatment](https://blog.google/innovation-and-ai/models-and-research/google-research/amie-for-disease-management-in-nature/)


#### Google Cloud Tools
- Gemini

---

#### [Google Research](https://blog.google/innovation-and-ai/models-and-research/google-research/rss/)


#### Google Cloud Tools
- Gemini
- Nano Banana

---

#### [Quantum computing](https://blog.google/innovation-and-ai/models-and-research/quantum-computing/)


#### Google Cloud Tools
- Gemini

---

#### [Quantum computing](https://blog.google/innovation-and-ai/models-and-research/quantum-computing/rss/)


#### Google Cloud Tools
- Gemini

---

#### [Products](https://blog.google/innovation-and-ai/products/)


#### Google Cloud Tools
- Gemini
- Gemma

---

#### [Gemini App](https://blog.google/innovation-and-ai/products/gemini-app/)


#### Google Cloud Tools
- Gemini

---

#### [Save time and grow your business with new Gemini tools](https://blog.google/innovation-and-ai/products/gemini-app/gemini-features-for-businesses/)


#### Definitions
- **General summary**: You can now connect your Google Business Profile to Gemini to get a personalized AI assistant that understands your brand and customer data. Use the new Business notebooks feature to organize your workflows, track critical tasks, and generate content based on your specific business context. Look for these updates rolling out globally this month to help you save time and manage your operations more effectively.
- **Basic explainer**: Google is adding new features to Gemini to help small business owners save time. You can now connect your business profile so the AI understands your brand and helps you reply to customers. It also includes a new notebook tool to keep your projects and data organized in one place. These updates make Gemini act like a smart assistant that knows exactly how to help your business grow.

#### Benefits
- **Bullet points**: "Save time and grow your business with new Gemini tools" helps entrepreneurs work smarter. Connect your Google Business Profile to Gemini for a smarter, personalized AI assistant. Use Gemini to analyze performance data and draft quick responses to customer reviews. Organize your workflows and business data in one place with new Business notebooks. These tools help you manage daily tasks and grow your business more efficiently.

#### Google Cloud Tools
- Gemini

---

#### [NotebookLM](https://blog.google/innovation-and-ai/products/notebooklm/)


#### Google Cloud Tools
- Gemini

---

#### [Technology](https://blog.google/innovation-and-ai/technology/)


#### Google Cloud Tools
- Gemini
- Gemma

---

#### [AI](https://blog.google/innovation-and-ai/technology/ai/)


#### Google Cloud Tools
- Gemini
- Gemma

---

#### [The latest AI news we announced in May 2026](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-may-2026/)


#### Definitions
- **General summary**: Google’s May 2026 updates center on the new "agentic" era, featuring the Gemini 3.5 model and Gemini Omni for advanced reasoning and creation. You can now use proactive tools like the updated Gemini app, Universal Cart for shopping, and the new Google Health app to manage your daily tasks more efficiently. Explore these features across new hardware, including the Googlebook and Fitbit Air, to see how these intelligent systems can simplify your workflow and personal wellness.

#### Google Cloud Tools
- Gemini
- Google Flow

---

#### [Developer tools](https://blog.google/innovation-and-ai/technology/developers-tools/)


#### Google Cloud Tools
- Gemini
- Gemma

---

#### [DiffusionGemma: 4x faster text generation](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/)


#### Use Cases
- **Unlocking new value for developers**: Developers building real-time interactive AI applications often struggle with the latency bottlenecks of local inference. DiffusionGemma addresses these challenges directly, with some key trade-offs: Blazing fast inference: By shifting the decode bottleneck from memory-bandwidth to compute, DiffusionGemma generates up to 4x faster token output on dedicated GPUs. (1000+ tokens per second on a single NVIDIA H100, 700+ tokens per second on NVIDIA GeForce RTX 5090). 1 Accessible hardware footprint: Operating as a 26B total Mixture of Experts (MoE) model that activates only 3.8B parameters during inference, DiffusionGemma fits comfortably within 18GB VRAM limits of high-end dedicated consumer GPUs when quantized. Bi-directional attention : Generating 256 tokens in parallel with each forward pass allows every token to attend to all others. This provides significant advantages for non-linear domains such as in-line editing, code infilling, amino acid sequences or mathematical graphs. Intelligent self-correction: The model iteratively refines its own output, allowing it to evaluate the entire text block at once to fix mistakes in real-time. Experimental status & production recommendations: Because it prioritizes speed and parallel layout generation, DiffusionGemma’s overall output quality is lower than standard Gemma 4. For applications that demand maximum quality, we recommend deploying standard Gemma 4.

#### Benefits
- **Why diffusion for text?**: While the AI research community has explored diffusion-based text generation for years, applying it to large models has remained a challenge. DiffusionGemma changes this by shifting how models use hardware.

#### Google Cloud Tools
- Gemini
- Gemma
- Hugging Face
- Kaggle
- vLLM

#### - MLX
- Gemini Enterprise Agent Platform

---

#### [See what 3 builders are making with Gemma 4](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4-builders/)


#### Google Cloud Tools
- Gemini
- Gemma
- Kaggle

---

#### [Health](https://blog.google/innovation-and-ai/technology/health/)


#### Google Cloud Tools
- Gemini

---

#### [Research](https://blog.google/innovation-and-ai/technology/research/)


#### Google Cloud Tools
- Gemini

---

#### [4 ways researchers are collaborating with Co-Scientist to solve big problems](https://blog.google/innovation-and-ai/technology/research/co-scientist-research-problems/)


#### Definitions
- **General summary**: Researchers are now using Co-Scientist, an artificial intelligence system designed to help solve complex problems in the life sciences. The tool uses specialized agents to generate, debate, and refine new hypotheses, acting as a virtual partner for scientific discovery. You can explore how this technology accelerates research by visiting the Google DeepMind blog or testing the new experimental tool.

#### Google Cloud Tools
- Gemini

---

#### [Gemini for Science: AI experiments and tools for a new era of discovery](https://blog.google/innovation-and-ai/technology/research/gemini-for-science-io-2026/)


#### Google Cloud Tools
- Gemini
- Gemma

---

#### [Safety & Security](https://blog.google/innovation-and-ai/technology/safety-security/)


#### Google Cloud Tools
- Gemini

---

#### [Quantum frontiers may be closer than they appear](https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/)


#### Google Cloud Tools
- Gemini

---

#### [XREAL AURA and more Android XR news from AWE 2026](https://blog.google/innovation-and-ai/technology/xr-ar/awe-2026/)


#### Google Cloud Tools
- Gemini

---


All the best - https://markposition.wordpress.com

### LocalHost.Co Tools Documentation
*Source: local://localhost_tools_docs.md*

#### LocalHost.Co Tools Documentation
Scraped from [https://localhost.co/tools/](https://localhost.co/tools/)

#### CODE


#### Markdown Viewer
- **Description**: Preview rendered Markdown while editing your source text.
- **URL**: [https://localhost.co/tools/markdown-viewer](https://localhost.co/tools/markdown-viewer)

#### JavaScript Formatter
- **Description**: Beautify JavaScript code for easier reading and debugging.
- **URL**: [https://localhost.co/tools/javascript-formatter](https://localhost.co/tools/javascript-formatter)

#### CSS Formatter
- **Description**: Format CSS stylesheets with consistent indentation and spacing.
- **URL**: [https://localhost.co/tools/css-formatter](https://localhost.co/tools/css-formatter)

#### SQL Formatter
- **Description**: Format SQL queries for easier review, editing, and debugging.
- **URL**: [https://localhost.co/tools/sql-formatter](https://localhost.co/tools/sql-formatter)

#### HTML Formatter
- **Description**: Beautify HTML markup into clean, readable source code.
- **URL**: [https://localhost.co/tools/html-formatter](https://localhost.co/tools/html-formatter)

#### Markdown to HTML
- **Description**: Convert Markdown content into HTML instantly in the browser.
- **URL**: [https://localhost.co/tools/markdown-to-html](https://localhost.co/tools/markdown-to-html)

#### Regex Tester
- **Description**: Test regular expressions with live match and replace results.
- **URL**: [https://localhost.co/tools/regex-tester](https://localhost.co/tools/regex-tester)

#### DATA


#### XML Validator
- **Description**: Validate XML structure and detect malformed tags.
- **URL**: [https://localhost.co/tools/xml-validator](https://localhost.co/tools/xml-validator)

#### YAML Validator
- **Description**: Validate YAML syntax and catch indentation problems fast.
- **URL**: [https://localhost.co/tools/yaml-validator](https://localhost.co/tools/yaml-validator)

#### JSON to JSON Schema
- **Description**: Create a JSON Schema definition from example JSON data.
- **URL**: [https://localhost.co/tools/json-to-json-schema](https://localhost.co/tools/json-to-json-schema)

#### JSON Diff Checker
- **Description**: Compare two JSON documents and highlight structural differences.
- **URL**: [https://localhost.co/tools/json-diff-checker](https://localhost.co/tools/json-diff-checker)

#### JSON Validator
- **Description**: Validate JSON payloads and quickly detect syntax errors.
- **URL**: [https://localhost.co/tools/json-validator](https://localhost.co/tools/json-validator)

#### YAML Formatter
- **Description**: Beautify YAML files for cleaner reading and editing.
- **URL**: [https://localhost.co/tools/yaml-formatter](https://localhost.co/tools/yaml-formatter)

#### JSON Formatter
- **Description**: Format and beautify raw JSON into a readable structured layout.
- **URL**: [https://localhost.co/tools/json-formatter](https://localhost.co/tools/json-formatter)

#### JSON Fixer
- **Description**: Repair common malformed JSON issues before parsing or saving.
- **URL**: [https://localhost.co/tools/json-fixer](https://localhost.co/tools/json-fixer)

#### JSON to TypeScript
- **Description**: Generate TypeScript interfaces directly from JSON samples.
- **URL**: [https://localhost.co/tools/json-to-typescript](https://localhost.co/tools/json-to-typescript)

#### JSON to Table
- **Description**: Convert JSON arrays and objects into clean tabular output.
- **URL**: [https://localhost.co/tools/json-to-table](https://localhost.co/tools/json-to-table)

#### JSON to YAML
- **Description**: Transform JSON payloads into YAML with preserved structure.
- **URL**: [https://localhost.co/tools/json-to-yaml](https://localhost.co/tools/json-to-yaml)

#### XML Formatter
- **Description**: Format XML documents with readable indentation and spacing.
- **URL**: [https://localhost.co/tools/xml-formatter](https://localhost.co/tools/xml-formatter)

#### CSV to JSON
- **Description**: Convert CSV rows into machine-readable JSON output.
- **URL**: [https://localhost.co/tools/csv-to-json](https://localhost.co/tools/csv-to-json)

#### JSON to CSV
- **Description**: Turn JSON arrays into CSV for spreadsheets and exports.
- **URL**: [https://localhost.co/tools/json-to-csv](https://localhost.co/tools/json-to-csv)

#### DEVOPS


#### Gitignore Generator
- **Description**: Generate .gitignore templates for common stacks and frameworks.
- **URL**: [https://localhost.co/tools/gitignore-generator](https://localhost.co/tools/gitignore-generator)

#### cURL to Code Converter
- **Description**: Convert cURL commands into language-specific request code.
- **URL**: [https://localhost.co/tools/curl-to-code-converter](https://localhost.co/tools/curl-to-code-converter)

#### Cron Expression Builder
- **Description**: Build and inspect cron expressions for scheduled tasks.
- **URL**: [https://localhost.co/tools/cron-expression-builder](https://localhost.co/tools/cron-expression-builder)

#### ENCODING


#### HTML Entity Encode Decode
- **Description**: Encode or decode HTML entities for safe markup output.
- **URL**: [https://localhost.co/tools/html-entity-encode-decode](https://localhost.co/tools/html-entity-encode-decode)

#### URL Encode Decode
- **Description**: Encode or decode URLs and query components safely.
- **URL**: [https://localhost.co/tools/url-encode-decode](https://localhost.co/tools/url-encode-decode)

#### Base64 Encode Decode
- **Description**: Encode or decode Base64 strings for data transfer and debugging.
- **URL**: [https://localhost.co/tools/base64-encode-decode](https://localhost.co/tools/base64-encode-decode)

#### GENERATORS


#### UUID Generator
- **Description**: Generate UUID values for apps, APIs, and database records.
- **URL**: [https://localhost.co/tools/uuid-generator](https://localhost.co/tools/uuid-generator)

#### Password Generator
- **Description**: Create strong passwords with configurable length and character rules.
- **URL**: [https://localhost.co/tools/password-generator](https://localhost.co/tools/password-generator)

#### QR Code Generator
- **Description**: Generate QR codes from text, URLs, and short payloads.
- **URL**: [https://localhost.co/tools/qr-code-generator](https://localhost.co/tools/qr-code-generator)

#### Lorem Ipsum Generator
- **Description**: Generate placeholder paragraphs, sentences, or words on demand.
- **URL**: [https://localhost.co/tools/lorem-ipsum-generator](https://localhost.co/tools/lorem-ipsum-generator)

#### SECURITY


#### JWT Decoder
- **Description**: Decode JWT tokens and inspect headers, payloads, and expiry data.
- **URL**: [https://localhost.co/tools/jwt-decoder](https://localhost.co/tools/jwt-decoder)

#### Bcrypt Hash Generator
- **Description**: Create bcrypt password hashes for authentication workflows.
- **URL**: [https://localhost.co/tools/bcrypt-hash-generator](https://localhost.co/tools/bcrypt-hash-generator)

#### Hash Generator
- **Description**: Generate common cryptographic hashes from text input.
- **URL**: [https://localhost.co/tools/hash-generator](https://localhost.co/tools/hash-generator)

#### SEO


#### Keyword Density Checker
- **Description**: Analyze keyword usage and density in pasted content.
- **URL**: [https://localhost.co/tools/keyword-density-checker](https://localhost.co/tools/keyword-density-checker)

#### Slug Generator
- **Description**: Create clean URL slugs from titles and arbitrary text.
- **URL**: [https://localhost.co/tools/slug-generator](https://localhost.co/tools/slug-generator)

#### TEXT


#### Remove Duplicates
- **Description**: Remove repeated lines from pasted text while preserving clean readable output.
- **URL**: [https://localhost.co/tools/remove-duplicates](https://localhost.co/tools/remove-duplicates)

#### Text Minifier
- **Description**: Collapse text spacing and remove unnecessary blank lines quickly.
- **URL**: [https://localhost.co/tools/text-minifier](https://localhost.co/tools/text-minifier)

#### Delimiter Converter
- **Description**: Convert text between comma, pipe, tab, and custom delimiters.
- **URL**: [https://localhost.co/tools/delimiter-converter](https://localhost.co/tools/delimiter-converter)

#### Text Beautifier
- **Description**: Clean and normalize pasted text into a readable format.
- **URL**: [https://localhost.co/tools/text-beautifier](https://localhost.co/tools/text-beautifier)

#### Word Counter
- **Description**: Count words and measure text length while you type or paste.
- **URL**: [https://localhost.co/tools/word-counter](https://localhost.co/tools/word-counter)

#### Text Diff Checker
- **Description**: Compare two text blocks and see their differences instantly.
- **URL**: [https://localhost.co/tools/text-diff-checker](https://localhost.co/tools/text-diff-checker)

#### Line Sorter
- **Description**: Sort lines alphabetically, numerically, or by custom rules.
- **URL**: [https://localhost.co/tools/line-sorter](https://localhost.co/tools/line-sorter)

#### Case Converter
- **Description**: Convert text to upper, lower, title, camel, snake, or kebab case.
- **URL**: [https://localhost.co/tools/case-converter](https://localhost.co/tools/case-converter)

#### Character Counter
- **Description**: Count characters, spaces, lines, and paragraphs in text input.
- **URL**: [https://localhost.co/tools/character-counter](https://localhost.co/tools/character-counter)

#### Find and Replace
- **Description**: Find repeated patterns in text and replace them quickly.
- **URL**: [https://localhost.co/tools/find-and-replace](https://localhost.co/tools/find-and-replace)

#### TIME


#### Unix Timestamp Converter
- **Description**: Convert Unix timestamps to human-readable dates and back.
- **URL**: [https://localhost.co/tools/unix-timestamp-converter](https://localhost.co/tools/unix-timestamp-converter)

#### WEB


#### Color Converter
- **Description**: Convert color values between HEX, RGB, HSL, and related formats.
- **URL**: [https://localhost.co/tools/color-converter](https://localhost.co/tools/color-converter)

#### URL Parser
- **Description**: Break down full URLs into protocol, host, path, and query parts.
- **URL**: [https://localhost.co/tools/url-parser](https://localhost.co/tools/url-parser)

#### Query String Parser
- **Description**: Parse URL query strings into readable key-value output.
- **URL**: [https://localhost.co/tools/query-string-parser](https://localhost.co/tools/query-string-parser)

#### Query String Builder
- **Description**: Build URL query strings from structured input fields.
- **URL**: [https://localhost.co/tools/query-string-builder](https://localhost.co/tools/query-string-builder)

---

### Google Innovation & AI Blog
*Source: local://google_innovation_ai_report.md*

#### Google Innovation & AI Blog Updates
Scraped from:
- [Innovation & AI](https://blog.google/innovation-and-ai/)
- [Models & Research](https://blog.google/innovation-and-ai/models-and-research/)
- [Products](https://blog.google/innovation-and-ai/products/)
- [Infrastructure & Cloud](https://blog.google/innovation-and-ai/infrastructure-and-cloud/)
- [Technology](https://blog.google/innovation-and-ai/technology/)

#### Global network
- URL: https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/
- Insight: News about how Google is building infrastructure for the 21st century.

#### We’re strengthening our presence in Alabama through new investments and community support.
- URL: https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/alabama-investment-june-2026/
- Insight: Google has announced a $1.5 billion investment for 2026 and 2027 to expand its data center campus in Jackson County, Alabama. Operating since 2019 on a repurposed former coal-plant site, the facility powers essential digital services while driving long-term regional growth.As part of this expansion, Google is funding 100% of its own power and infrastructure costs. The company also announced a $2 million Energy Impact Fund in partnership with the TVA and CAANEAL to support local energy efficiency and weatherization programs.Furthering our community commitment, we’re donating $550,000 to provide STEM kits for local fourth-to-eighth graders. These initiatives build on Google’s long-term local impact, which includes supporting water stewardship in the Paint Rock River Watershed, training over 130,000 Alabamians in digital skills and generating hundreds of full-time and construction jobs.Read our full announcement.

#### Our new community investments in Virginia support local jobs and expand energy affordability.
- URL: https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/virginia-community-investments/
- Insight: Virginia has been a home for Google for more than a decade, with an office in Reston and data centers in Loudoun and Prince William Counties. Today, we’re deepening our commitment to the Commonwealth with new community investments that will support thousands of local jobs, prepare the next-generation workforce and expand energy affordability.To prepare Virginians for skilled jobs created by infrastructure growth across the state, we’re funding the electrical training ALLIANCE (etA) to support local electrical apprenticeship training facilities. With this funding, they aim to increase training capacity to support an additional 2,741 apprentices by 2030. This builds on our existing local support and is part of a national commitment from Google.org to prepare over 300,000 skilled tradespeople.As we responsibly build data centers in Virginia, we have invested in over 500 megawatts of new energy capacity, collaborating with partners to bring more power to the grid. To support energy afforda...

#### Google Cloud
- URL: https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/
- Insight: Google Cloud helps companies empower their employees, serve their customers and build what’s next for their business.

#### We're rolling out AlphaEvolve widely to solve Google Cloud customers' hardest problems.
- URL: https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/alphaevolve-on-cloud/
- Insight: Finding the most efficient algorithm — whether designing a microchip, routing a logistics network or accelerating medical research — can be challenging, with many possible solutions for engineers to explore on their own.To help organizations tackle these complex challenges, AlphaEvolve, our Gemini-powered AI code-optimization agent, is now generally available to all Google Cloud customers on Gemini Enterprise Agent Platform.Rather than rewriting code from scratch, AlphaEvolve acts as an evolutionary collaborator: you provide a baseline algorithm and your goals, and it automatically searches for better solutions, returning human-readable, optimized code.Since launching in private preview last December, we've seen strong results from our early adopters. BASF, JetBrains and Kinaxis and many more have solved previously intractable business and research problems with AlphaEvolve.For more details and step-by-step guides, head to the Google Cloud announcement.

#### Cloud Next ‘26: Momentum and innovation at Google scale
- URL: https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/
- Insight: The pace of technological change since last year’s Cloud Next has never been faster, and Google Cloud has incredible momentum.Our first-party models now process more than 16 billion tokens per minute via direct API use by our customers, up from 10 billion last quarter. To support and drive this growth, in 2026, just over half of our overall machine learning compute investment is expected to go towards the Cloud business to benefit our cloud customers and partners.You can read all about our momentum and the extraordinary range of partnerships and innovations we’re announcing at Cloud Next.I want to highlight just four key areas.1. We’re firmly in the agentic Gemini eraLast fall we introduced Gemini Enterprise, the end-to-end system for the agentic era — the connective tissue between your data, your people and your goals.It has great momentum: In Q1, we saw 40% growth in paid monthly active users quarter-over-quarter.Through this rapid growth, we’ve seen how every employee in every organization can become a builder. This is an incredible shift, but it comes with complexity. The conversation has gone from “Can we build an agent?” to “How do we manage thousands of them?”That’s why we’re introducing our new Gemini Enterprise Agent Platform. It provides the secure, full-stack connective tissue you need to build, scale, govern and optimize your agents with confidence — a mission control for the agentic enterprise.2. Using AI to defend against security threatsWhile AI can increase security risks, our Cloud customers now have AI on their side to protect their organizations. Today we are unveiling a range of new agentic solutions for threat detection, as part of an AI-powered cybersecurity platform that combines Google’s Threat Intelligence and Security Operations with Wiz’s Cloud and AI Security Platform.In addition, we are launching Wiz’s new AI Application Protection Platform (AI-APP), which provides autonomous protection, from code to cloud to runtime, across multicloud, hybrid and AI environments.3. Introducing our eighth-generation TPUsIn the era of AI agents, infrastructure needs to evolve to take on the most demanding AI workloads. This year, we’re bringing the eighth generation of our Tensor Processing Units with a dual chip approach:TPU 8t, optimized for training, scales up to 9,600 TPUs and 2 petabytes of shared, high-bandwidth memory in a single superpod. It achieves three times the processing power of Ironwood and delivers up to 2x more performance/watt.TPU 8i, optimized for inference, connects 1,152 TPUs in a single pod, dramatically reducing latency, with 3x more on-chip SRAM, to deliver the massive throughput and low latency needed to concurrently run millions of agents cost-effectively.We’ll offer these to Cloud customers as a core part of our selection of compute processors, along with a portfolio of NVIDIA GPU instances. Read more in our blog post.4. Staying on the cutting-edge as “customer zero”To be the best partner, we always want to be “customer zero” for our own technologies. This helps us imagine, test, build and scale the best Google technologies for our cloud customers, for today and tomorrow. Our database service Bigtable, which powers so many Google services, and our TPUs, which have been so important in training and powering our Gemini models, are great examples.Here are a few more recent ones:First, coding.We’ve been using AI to generate code internally at Google for a while. Today, 75% of all new code at Google is now AI-generated and approved by engineers, up from 50% last fall.We’re now shifting to truly agentic workflows. Our engineers are orchestrating fully autonomous digital task forces, firing off agents and accomplishing incredible things.Recently, a particularly complex code migration done by agents and engineers working together was completed six times faster than was possible a year ago with engineers alone.And with our recent launch of the Gemini app on MacOS, the team built the initial release with our agentic development platform Antigravity, going from an idea to a native Swift app prototype in a few days.Second, security.We’ve long led the industry in security. Now, our Security Operations Center agents automatically triage tens of thousands of unstructured threat reports each month, reducing threat mitigation time by more than 90%. And we have built and actively use Gemini-based AI agents (like CodeMender) to find and, importantly, fix critical software flaws.Third, our operations.For the launch of Gemini in Chrome, our marketing teams used our models to rapidly generate thousands of variations of our creative assets, which would historically take weeks. Using AI led to 70% faster turnaround and a 20% increase in conversions, getting us to market faster and more effectively.Congratulations to our Google Cloud team, and a huge thanks to our partners who are building the future with us. We’ll have a lot more to share on how we’re bringing the latest technology to everyon...

#### 7 highlights from Google Cloud Next ‘26
- URL: https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/google-cloud-next-26-recap/
- Insight: When we gathered at Google Cloud Next a year ago, we talked about how generative AI was beginning to change the way we work. This week in Vegas, we showcased how AI is not only transforming work, it’s running at scale.We’ve officially entered the agentic era. AI is becoming an active partner — an agent that can actually do the work for you safely and autonomously. At Next ‘26, we shared everything you need to build your own helpful, intelligent agents and use them to grow your business. Here are the highlights.1. The new Gemini Enterprise Agent Platform is here.For the technical teams building the future, we’re introducing the Gemini Enterprise Agent Platform. It’s a complete, end-to-end workspace to build, govern and scale your AI agents with the world's best models at your fingertips.We’re providing direct access to Gemini 3.1 Pro, our most capable model yet for handling complex workflows, alongside Gemini 3.1 Flash Image (also known as Nano Banana 2) for creating stunning visual assets, and Lyria 3 for professional-grade audio. We’re also expanding our commitment to open choice by adding Anthropic’s Claude Opus 4.7.You don’t have to be a machine-learning PhD to use these models or build an agent. Agent Studio, our low-code interface, lets developers and business users alike build and test agents using natural language.2. The Gemini Enterprise app brings AI to your everyday work.We’re bringing the power of the agents directly to your workforce through the Gemini Enterprise app. To ensure everyone can tap into this technology, our no-code Agent Designer lets anyone build custom, trigger-based workflows without writing a single line of code.For more complex, multi-step business processes, new long-running agents can work autonomously in the background within secure cloud sandboxes while you focus on other things. With all these agents helping out, we’ve built a central, intuitive Agent Inbox so you can easily monitor, guide and manage exactly what your AI helpers are up to.3. Our new eighth-generation TPUs are designed to power the AI era.Running millions of AI agents takes some serious computing muscle. Our AI Hypercomputer is a purpose-built system designed specifically for the massive scale of this new era, including the eighth generation of our custom TPU (Tensor Processing Unit) chips.The TPU 8t is built to train AI models incredibly fast, while the TPU 8i is optimized for inference (actually serving up the models), delivering 80% better performance per dollar. We will also be among the first to offer the new NVIDIA Vera Rubin NVL72 systems, joining our existing lineup of NVIDIA GPUs and our super-efficient Google Cloud Axion processors.To take advantage of this powerful compute, you need to move data at lightning speed. We unveiled the Virgo Network, a custom-built system to connect massive supercomputers, alongside storage breakthroughs like Managed Lustre, which can now move an incredible 10 terabytes of data per second.4. The new Agentic Data Cloud helps make sense of your data.An AI agent is only as helpful as the information it understands. We’re introducing the Agentic Data Cloud as a completely new way of organizing your data so AI can take action in real time. The Knowledge Catalog acts like a dynamic map of your entire business. Using Gemini, it autonomously tags and connects the dots across your enterprise so your agents actually understand the unique context and lingo of your company.The Agentic Data Cloud also includes Cross-Cloud Lakehouse, because you shouldn't have to move all your data to use our AI. Standardized on Apache Iceberg, this lets you leave your data exactly where it is — even if it's in AWS — and query it instantly, with zero friction.5. We’re building security for the AI age.As cybersecurity threats get smarter, human defenders need AI on their side. We’re combining Google’s world-class threat intelligence with Wiz’s leading security platform to give you agentic defense. Specialized new agents include the Threat Hunting agent that can proactively hunt for threats and write security rules autonomously, the Detection Engineering agent that can identify coverage gaps and create new detections, and the Third-Party Context agent that provides contextual data from third-party content.Wiz, now a part of Google Cloud, expands and deepens our ability to protect the apps you build and run. Wiz has added Databricks to the list of cloud platforms it supports, as well as more AI studios and multicloud platforms-as-a-service.Additionally, the new Technology Intel Center aggregates and centralizes a feed of new features releases, migration updates, and end-of-life notices across cloud and AI tech providers that are relevant to you.6. Workspace Intelligence will help teams collaborate even better.We’re baking agentic power right into the tools you use to connect with your team and your customers. With Workspace Intelligence, we’re breaking down the walls between Docs, Drive, Meet and Gmai...

#### View the collection
- URL: https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/how-google-does-it-security-series/
- Insight: In our Google Cloud series “How Google Does It,” we share exclusive, behind-the-scenes looks at how Google approaches some of today's most pressing security topics, challenges and concerns, straight from Google experts. Learn about how we modernize threat detection, build AI agents to boost defenders, apply SRE to cybersecurity and more....

#### View the collection
- URL: https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/next-2026/
- Insight: Agentic technology is revolutionizing how we work. Today, nearly 75% of Google Cloud customers are using our AI products to power their businesses, with 330 Google Cloud customers processing over a trillion tokens each in the past 12 months. And the agentic enterprise transformation is accelerating: Our models now process more than 16 billion tokens per minute via direct API use by our customers, up from 10 billion last quarter. We’re seeing customer success across every industry.Transformation to an agentic enterprise is the future of every organization. At Cloud Next ‘26, we’re showcasing the roadmap for how we can help you make the transition, from the new Gemini Enterprise Agent Platform to our eighth-generation Tensor Processing Units and beyond.Here are the highlights from Cloud Next ‘26....

#### Gemini models
- URL: https://blog.google/innovation-and-ai/models-and-research/gemini-models/

#### Gemini 3.5: frontier intelligence with action
- URL: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/
- Insight: Today, we’re introducing Gemini 3.5, our latest family of models combining frontier intelligence with action. This represents a major leap forward in building more capable, intelligent agents. We’re kicking off the series by releasing 3.5 Flash. It delivers frontier performance for agents and coding, excelling at complex long-horizon tasks that deliver real-world utility.3.5 Flash is available today to billions of people globally:For everyone via the Gemini app and AI Mode in Google SearchFor developers in our agent-first development platform Google Antigravity and Gemini API in Google AI Studio and Android StudioFor enterprises in Gemini Enterprise Agent Platform and Gemini Enterprise.We’re also hard at work on 3.5 Pro. It's already being used internally, and we look forward to rolling it out next month.3.5 Flash: frontier performance for agents and codingGemini 3.5 Flash delivers intelligence that rivals large flagship models on multiple dimensions, at the speeds you have come to exp...

#### Fluid, natural voice translation with Gemini 3.5 Live Translate
- URL: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-live-3-5-translate/
- Insight: Twenty years ago, translation at Google began as one of our pioneering machine learning experiments to turn the science of language into the magic of human connection. That experiment has come a long way with over a trillion words being translated for billions of users across our products every month.Today, we’re taking our next step with the release of Gemini 3.5 Live Translate, our latest audio model for live speech-to-speech translation.The model automatically detects 70+ languages and generates smooth, natural-sounding translated speech that preserves the speakers' intonation, pacing and pitch. Unlike turn by turn systems that wait for the speaker to finish speaking before responding, 3.5 Live Translate generates speech continuously, balancing the trade-off between waiting for context to improve quality and translating immediately to stay in sync with the speaker. It delivers fluid audio without awkward pauses and stays just a few seconds behind the speaker throughout the session.Gemini 3.5 Live Translate is rolling out starting today across Google products:For developers in public preview via the Gemini Live API and Google AI StudioFor enterprises in private preview starting this month in Google MeetFor everyone via Google Translate on Android and iOSBuild with 3.5 Live TranslateGemini 3.5 Live Translate processes speech as it’s streamed, enabling a more seamless connection across languages. The model handles multilingual inputs without the need to manually configure settings. At the same time, its noise robustness ensures applications can handle loud, unpredictable environments. You can use its capabilities to help facilitate live interpretation for multilingual calls, meetings, lessons, broadcasts and more.Watch the Gemini Live API in action, enabling dubbing and simultaneous multi-language translation. Dive into the demo or more example code in the Gemini Cookbook.By utilizing the Gemini Live API, developer platforms like Agora, Fishjam, LiveKit, Pipecat, and Vision Agents enable developers to build and deploy voice translation apps with ease. These integrations handle the complex real-time media streaming infrastructure, so developers can focus on the user experience.Our partners at Grab are testing the model to enable multilingual communication in near real-time between drivers and travelers at pickups. These users make over 10 million voice calls per month through Grab.Read the early reviewsIn addition to Grab, companies like CJ ENM, LiveKit and others have shared positive feedback on 3.5 Live Translate highlighting its impressive translation quality, accuracy and low latency:Experience 3.5 Live Translate in your video meetingsSpeech translation in Google Meet will soon use 3.5 Live Translate, improving the experience by:Offering 70+ languages, an improvement from the previous limit of just five languages,Enabling conversations across over 2000+ language combinations in one meeting, expanding from the previous state of only translating to and from English,Updating the interface to provide instant access to speech translation.We’re launching this update in private preview for select business Google Workspace customers starting this month, followed by a broader rollout later this year.Get 3.5 Live Translate in the Google Translate app on Android or iOSThe model is also rolling out on the Google Translate app globally, on both Android and iOS. When using the Live translate feature, simply connect any pair of headphones to experience a more seamless translation that mirrors the speaker’s tone across 70+ languages.For Android users, we’re also starting to roll out a new ‘listening mode’ with 3.5 Live Translate that lets you hear translations directly through your phone’s earpiece. Simply hold your phone to your ear just like a regular call, and the translated audio streams straight to you. This new experience can be helpful in situations where you want to quickly hear translations without others hearing, and you don’t have your headphones handy.Using the new listening mode, users can hear a near real-time English translation of a guided tour in Spanish directly through their phone's earpiece.Watermarked with SynthIDAll audio generated by our models is watermarked with SynthID. This imperceptible watermark is woven directly into the audio output, ensuring AI-generated content remains detectable to help prevent misinformation. For details on our approach to safety and responsibility, review the model card.

#### 9 demos of Gemini Omni and Gemini 3.5 in action
- URL: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-3-5-videos/
- Insight: At Google I/O 2026, we announced our latest models: Gemini Omni and the Gemini 3.5 family of models.Gemini Omni is our new model that can create anything from any input, starting with video. With Omni, you can combine images, audio, video and text as input and generate high-quality videos grounded in Gemini's real-world knowledge. You can also easily edit your videos through conversation.Then there’s Gemini 3.5, our latest family of models combining frontier intelligence with action. This represents a major leap forward in building more capable, intelligent agents. We’re kicking off the series by releasing 3.5 Flash. It delivers frontier performance for agents and coding, excelling at complex long-horizon tasks that deliver real-world utility.To give you a clearer understanding of Gemini Omni and Gemini 3.5 Flash, here are 9 demos of what they can help you do.Gemini OmniEdit your videos through conversation. One capability that makes Omni special is that it gives you an easier way to edit video — with natural language. Every instruction builds on the last. Your characters stay consistent, the physics hold up and the scene remembers what came before. That means you can transform the world around you. Change specific things, or change everything. Your video becomes the starting point for something you never could have filmed yourself.Prompt: Make the sculpture out of bubbles.Reimagine the action. Take a video you shot and just ask Omni to change what’s happening. Edit the action, add in new characters or objects or transform a moment into something unexpected.Prompt: Dim the lights in the room. Put a black and white checkerboard room inside a glass sphere that floats tracking above the hand, inside it contains a recursive representation of the same hand holding the sphere, creating an infinite recursive of rooms. Camera slowly gets closer into the sphere, creating a video loop.Refine your videos across multiple turns. Change the environment, angle, style or even specific details, without ever losing the thread of your original scene. Scroll through the carousel to see how edits build on each other.Prompt: A video of a violinist playing a song.Prompt: Transport the violinist to the image environmentPrompt: Make the violin invisiblePrompt: Change the camera angle to be over the violinist’s shoulder.Gemini 3.5 FlashTake on agentic tasks at scale. 3.5 Flash delivers intelligence that rivals large flagship models on multiple dimensions, at the speeds you have come to expect from the Flash series. This balance of speed and performance makes 3.5 Flash ideal for tackling long-horizon agentic tasks. Here, powered by Antigravity, 3.5 Flash executes multi-step workflows to automatically rename and categorize unstructured assets based on dynamic criteria.3.5 Flash powered by AntigravityWhen coupled with the updated Antigravity harness, 3.5 Flash becomes a powerful engine for deploying collaborative subagents to tackle problems at scale for the most demanding use cases. Under supervision, it can reliably execute multi-step workflows and coding tasks while sustaining frontier performance.Create richer, more interactive web UIs and graphics with 3.5 Flash. 3.5 Flash builds on the strong multimodal foundation of Gemini 3. Watch as 3.5 Flash generates different UX approaches for a checkout flow in just 60 seconds on AI Studio.3.5 Flash on AI StudioTry personal AI agents and new intelligent experiences. 3.5 Flash is now the default model for the Gemini app and AI Mode in Search globally. Its agentic capabilities are powering new features to bring frontier-level intelligence to your daily life.The enhanced agentic coding capabilities of 3.5 Flash are delivering even more intelligent experiences in Search, like our new information agents. Operating in the background, 24/7, these agents intelligently reason across information to find exactly what you need at exactly the right moment. They will send a comprehensive update along with links to the web to dive deeper, so you can take action. Information agents will launch first for Google AI Pro & Ultra subscribers this summer.An information agent keeps a user updated on whether any of their favorite athletes announce sneaker collabs or signature drops.Now that we’re bringing the power of Google Antigravity and agentic coding capabilities of Gemini 3.5 Flash right into Search, Search can build the ideal response, in the right format for your question — completely on the fly. So you can get custom generative UI, including visual tools and simulations, tailored precisely to your needs. These generative UI capabilities will be available for everyone in Search this summer, free of charge.Search leverages 3.5 Flash to build an interactive visual explaining Gyroid patterns.For your ongoing tasks like planning a wedding or establishing a new fitness routine, Search will also build you custom experiences – like dashboards, trackers or mini apps – that you can keep coming back to. You’ll be a...

#### Start building with Nano Banana 2 Lite and Gemini Omni Flash
- URL: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/
- Insight: Today, we’re making it faster and easier to experiment, refine and scale your ideas with two major releases:Introducing Nano Banana 2 Lite: Our fastest, most cost-efficient image model in the Nano Banana family yet, built for high throughput, speed and scale. Nano Banana 2 Lite is available today in Google AI Studio, Gemini API and Gemini Enterprise Agent Platform. It is also rolling out today in Google consumer surfaces including AI Mode in Search, Gemini app and many other products.Bringing Gemini Omni Flash to developers: Our high quality, cost-efficient model for video generation and conversational editing, now available in Google AI Studio, the Gemini API and Gemini Enterprise Agent Platform for the first time. Omni Flash is also available in the Gemini app and Google Flow.Building with generative media is often about creative iteration. With these two models, developers can build comprehensive, end-to-end multimedia experiences that connect rapid image generation with video creation and editing. Whether your workflow requires generating thousands of images or editing multi-turn video sequences, you now have two new models to build faster, iterate seamlessly and bring your creative vision to life.Nano Banana 2 Lite: our fastest most cost-efficient Gemini Image modelWatch a side-by-side comparison of image generation speed and quality between Nano Banana 2 Lite and Nano Banana 2 using a simple prompt.Nano Banana 2 Lite (gemini-3.1-flash-lite-image) is designed for rapid ideation and high-velocity developer pipelines where speed and cost are the primary constraints. It’s our recommended replacement for developers currently using our first version of Nano Banana (gemini-2.5-flash-image), you can swap it out now for immediate benefits across key performance dimensions.Performance benchmarks for Nano Banana 2 and 2 Lite compared to competitor AI image models, evaluating trade-offs between generation/editing quality (Elo scores), processing latency and cost per 1K-resolution image.Nano Banana 2 Lite shines in:Latency: Delivers text-to-image outputs in 4 seconds. This makes it ideal for interactive prototyping and rapid visual drafting.Cost-efficiency ($0.034 per 1K image): A cost-efficient choice for developers focused on drafting, ideating, managing operational budgets or low-bandwidth usage.Despite prioritizing speed, Nano Banana 2 Lite retains reliable prompt adherence, strong character consistency and legible in-image text rendering.Understanding the Nano Banana familyNano Banana 2 Lite (Gemini 3.1 Flash Lite Image): Built for speed. Optimized for near-real-time, high-volume workflows where ultra-low latency is critical.Nano Banana 2 (Gemini 3.1 Flash Image): The generalist workhorse. Delivers high quality at a lower latency, offering the best balance of performance and cost.Nano Banana Pro (Gemini 3 Pro Image): Optimized for complex, professional use cases. It provides the most robust control and advanced reasoning for tasks where accuracy is more important than speed.Nano Banana (Gemini 2.5 Flash Image): Our legacy model. We recommend upgrading to Nano Banana 2 Lite for better quality, faster speeds and lower costs.To see the full list of model capabilities and how to integrate check out the developer docs.Alongside its release on developer platforms, Nano Banana 2 Lite is also coming to Google consumer surfaces including AI Mode in Search, Gemini app, NotebookLM, Google Photos, Stitch, Google Flow, and Google Ads.Experience high-quality, cost-efficient video editing and generation with Gemini Omni FlashWatch as someone uses Gemini Omni to perform four digital magic tricks, like pulling a 3D balloon word out of her phone and pouring water from the screen into a glass. There is a small “original" video in the corner revealing how she actually filmed the tricks before the Omni generated special effects were added.At Google I/O we introduced Gemini Omni Flash, the model where Gemini’s multimodal reasoning meets video generation and editing. Today, Gemini Omni Flash (gemini-omni-flash-preview) is rolling to developers via the Gemini API and Google AI Studio, natively supporting high-quality video generation and conversational editing from a combination of text, image and video inputs. This model is priced competitively at $0.10 per second of video output, which is the same as Veo 3.1 Fast.Omni Flash shines in:Conversational video editing: Refine and edit videos using natural language.Multimodal referencing: Combine inputs like images, text and video to maintain control and consistency over your scene.Real-world knowledge: Omni draws on Gemini’s knowledge such as history, biology and narrative logic to construct compelling videos.Text and action synchronization: Connect text and graphics directly to video actions, through simple prompting.For comprehensive benchmarking information, please visit Google DeepMind's Gemini Omni webpage.Limitations:Omni offers 10-second video generations currently, with longer d...

#### Introducing Gemini Omni
- URL: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/
- Insight: Last year, Nano Banana brought Gemini's intelligence to image generation and editing. Since then, it’s helped millions of people restore old photos, design from sketches and visualize ideas in ways that weren’t possible before. From the start we built Gemini to be natively multimodal from the ground up, and now we’re taking the next step.We’re introducing Gemini Omni, where Gemini’s ability to reason meets the ability to create. Omni is our new model that can create anything from any input — starting with video. With Omni, you can combine images, audio, video and text as input and generate high-quality videos grounded in Gemini's real-world knowledge. You can also easily edit your videos through conversation.Today, we’re rolling out the first model in the Omni family: Gemini Omni Flash, to the Gemini app, Google Flow and YouTube Shorts. In time we will support output modalities like image and audio. Here’s some of what makes Omni special:Edit your videos through conversationGemini Omni...

#### Introducing computer use in Gemini 3.5 Flash
- URL: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/
- Insight: Computer use is now a built-in tool supported in Gemini 3.5 Flash, delivering our best performance yet for agentic computer use tasks. Previously only available as a standalone Gemini 2.5 computer use model, computer use is now integrated natively in the main Gemini Flash model. Gemini already excels at function calling and using built-in tools like Search and Maps grounding. With built-in computer use capability, developers can now use 3.5 Flash to reliably build custom agents that can see, reason and take action across browser, mobile and desktop environments. This unlocks improved performance for long-horizon and enterprise automation tasks like continuous software testing and knowledge work across professional applications.Developers and enterprises can start using computer use in 3.5 Flash via the Gemini API and Gemini Enterprise Agent Platform.3.5 Flash uses computer use to analyse the Gemini app and return a categorized list of features.3.5 Flash with computer use audits its own documentation for accessibility issues.Making computer use safe in 3.5 FlashTo mitigate some of the prompt injection risks for agents operating in live environments, we use targeted adversarial training for computer use in Gemini 3.5 Flash. We’re also releasing two optional enterprise safeguard systems that enable enterprises to:Require explicit user confirmation for sensitive or irreversible actions.Automatically stop tasks if an indirect prompt injection is identified.Taking a “defense-in-depth” approach, we encourage developers to combine these features with secure sandboxing, human-in-the-loop verification and strict access controls. Additional information on safety measures can be found in our best practices documentation.We are already seeing customers drive value with computer use. Here’s what some of them have to say:To start building with computer use today:Try it now: Test the capabilities in a demo environment hosted by Browserbase.Start building: Dive into our reference implementation and documentation via Gemini API and Gemini Enterprise Agent Platform.

#### Google DeepMind
- URL: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/
- Insight: News from Google DeepMind about how we're building AI responsibly to benefit everyone.

#### We’re launching the Google DeepMind Accelerator program in Asia Pacific to tackle environmental risks.
- URL: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/accelerator-ai-for-the-planet/
- Insight: The Asia-Pacific region is a global engine for economic growth, but it's also highly vulnerable to climate change. While green technologies are gaining momentum, a recent report shows they aren’t scaling fast enough to keep up with the region’s rising environmental risks.To help innovators tackle these environmental challenges, we’re launching an inaugural Google DeepMind Accelerator program in APAC focused on “AI for the Planet.”This three-month program is designed for startups, research teams and nonprofits across the region to use frontier AI to solve problems in nature, climate, agriculture, energy and more. Selected organizations will receive expert mentorship, tailored support and help integrating frontier AI and science AI models from Google AI experts into their projects or products.If you're working on climate solutions, we want to help you scale your work. The program kicks off with an in-person bootcamp in Singapore, and you can learn more and register your interest today....

#### Google DeepMind and A24 announce first-of-its-kind research partnership
- URL: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/deepmind-a24-research-partnership/
- Insight: Today, Google DeepMind and A24 are announcing a first-of-its-kind partnership focused on research. The collaboration pairs a world-leading research lab with the industry’s most filmmaker-forward studio to help artists develop new workflows and techniques. This ensures the tools of the future are shaped by the creators who use them.This partnership creates a deep research and development collaboration between A24 and Google DeepMind spanning multiple projects over time. By anchoring Google DeepMind's innovations directly within the creative process, A24 and its filmmakers can help shape new technology in service of their vision and expand their storytelling possibilities. This hands-on collaboration provides Google DeepMind with invaluable feedback and guidance from leading artists. In addition, Google has made an investment in A24.Looking ahead, the partnership represents the beginning of a collaborative journey, one rooted in research and shared curiosity. While the initial focus is on bridging the gap between cutting-edge technology and next generation entertainment, the specific goals, technical outputs and creative milestones of this initiative will evolve over time. As A24 and Google DeepMind’s researchers work side-by-side to test, iterate and build, this partnership aims to expand what is possible in the future of entertainment.

#### Simulate real-world places with Project Genie and Street View
- URL: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie-expands/
- Insight: Genie is our general-purpose world model capable of generating diverse, interactive environments. Since launching, Genie has become a foundational tool for research, enabling agents to learn and reason in complex virtual settings and even helping Waymo simulate hyper-realistic road environments.Now, we’re taking a leap forward by connecting Genie’s generative power with the real-world imagery of Google Street View, allowing our models to anchor themselves in reality. This expansion of Genie’s capabilities can provide a virtual environment for AI agents or robots to navigate and interact with the complexities of the real world.Today, we’re launching this new Street View grounding capability within Project Genie, our experimental prototype. With this upgrade, you'll be able to leverage real-world imagery to explore your favorite spots, or reimagine them with a creative twist. We’re also expanding access to Project Genie to more people around the globe.Select the “Ocean World” style to scuba dive with schools of fish around places grounded in the real world.Street View: ground your worlds in real placesWhen creating imaginative worlds in Project Genie, you can now also base them on real places. Just tap the Maps pin to choose a place in the U.S. and optionally select a style for your world, like “Desert Sands” or “Stone Age.” Then, describe your character — like your favorite animal, comic book hero or even a claymation monster — and Genie will use this information to create an imaginative world with its starting location tied to Street View’s real-world imagery. This capability is powered by Maps Imagery Grounding, the same technology developers use to create stunning AI visuals with Street View.Want to see the Golden Gate Bridge under the sea? Select the “Ocean World” style to scuba dive with schools of fish around the bridge. Or, if you want to explore what the iconic Fort Worth Stockyards in Texas might have looked like in the 1920s, select the “B&W film” style to see a world with saloons, vintage cars and trading posts.Street View imagery in Project Genie is available now for places in the U.S. with plans to expand to more places over time.Project Genie: now available with Google AI UltraStarting today, Project Genie — including the new Street View capability — is gradually rolling out to all eligible Google AI Ultra $200 subscribers globally (18+). Try creating today with Project Genie.Project Genie is still an experimental research prototype in Google Labs, so we're working behind the scenes to make the details even sharper and more accurate. You can read more about our progress and current limitations on our website.

#### Running Guide agent: A step towards running unbounded
- URL: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/running-guide-agent/
- Insight: For blind and low-vision (BLV) athletes, running has traditionally required a physical tether — whether it’s a human guide or a painted track line. Today, we are excited to share how we’re taking steps towards changing that with the Running Guide agent, an accessibility agent that uses real-time environmental understanding to help low-vision athletes run. It marks a massive leap from simple path-following to advanced, real-time spatial reasoning. As we work to perfect this technology, our goal is simple: unassisted independence for every runner.A hybrid architecture for uncompromising safetyBuilding on our previous work with Project Guideline, the Running Guide agent uses a chest-mounted Pixel 10 Pro smartphone to view the path ahead and guide the user via auditory feedback. Because high-speed activities demand high trust, we built a hybrid, dual-path architecture:On-device segmentation: Running entirely offline on the Pixel 10’s custom silicon, this model guarantees ultra-low latency safety. It delivers immediate "STOP" alerts and steering cues — heard as directional ticking sounds — so runners maintain a reliable sense of direction even without a cellular connection.Gemma 4’s advanced reasoning: Leveraging Gemma 4 E4B, this path handles complex multimodal inputs (image and text) for high-level scene understanding entirely on device. To keep latency low, we use Smarter Frame Selection. Instead of processing every frame, the model only analyzes "high-entropy" frames — like sudden terrain changes or new obstacles — delivering faster, highly relevant coaching.A multi-agent frameworkThe Running Guide agent is a collaborative, multi-agent framework designed to help enable the running experience for a BLV user:Planner agent: Utilizing Gemma 4’s function calling, this agent pulls weather and Google Maps data, chats with the runner to establish workout goals and calibrates their digital starting line.Coach agent: Operates mid-run to deliver concise, telegraphic verbal alerts. It triages feedback into a strict hierarchy: DANGER (immediate evasive action needed), WARNING (nearby runners/obstacles) and NOTICE (upcoming track curves).Break agent: Manages rest intervals, allowing athletes to pause and resume their session at any time.Intelligent eyewear and community partnershipsWhile the chest-mounted Pixel 10 Pro is a robust foundation, we are prototyping the Running Guide agent on intelligent eyewear. Wearable glasses provide a wider, steadier field of view, which drastically optimizes the data fed to our multimodal models. The glasses stream directly to the Pixel device, seamlessly blending hardware and ambient AI.Runner’s view through Intelligent EyewearTo ensure we are building alongside the community, we’ve partnered with SG Enable, Singapore’s focal agency for disability and inclusion. By connecting our engineering teams directly with BLV runners for real-world testing, we can iteratively design a tool that truly meets their needs.The Running Guide agent is a powerful showcase of the new chapter of agents for Google AI. Athletes will be able to use our tool, which combines zero-latency edge computing with deep-world understanding, to push their limits and navigate the world with total, unassisted confidence.

#### Google Labs
- URL: https://blog.google/innovation-and-ai/models-and-research/google-labs/
- Insight: News about Google Labs, Google's home for the latest AI experiments and technology.

#### Meet Dreambeans, an app that connects you with what matters
- URL: https://blog.google/innovation-and-ai/models-and-research/google-labs/dreambeans/
- Insight: In a world of endless scrolling and digital noise, Google Labs is introducing our latest experiment: Dreambeans. It uses Google’s latest AI capabilities, like Personal Intelligence and Nano Banana 2, to proactively dream up personalized daily stories that cut through the clutter and connect you to what matters.Get a daily dose of inspiration, brewed fresh for youWith your permission, Dreambeans uses Personal Intelligence to connect information from your Google apps, including Gmail, Calendar, Photos, YouTube and Search history to curate stories that inspire and delight you. The goal is not to scroll forever, it’s a finite collection of stories designed to spark new ideas and allow you to focus on what matters to you.For example, I got a Gmail confirmation that my puppy’s treats were delivered and Dreambeans surfaced training tips for using them. It also referenced the Google Calendar reminder I have of my friend coming to town and provided recommendations of dog-friendly restaurants near me. Each story includes a unique illustration, reflecting the people and places you frequent the most.Dive deeper into your interestsWhen a story catches your eye, you can tap to dive deeper. Dreambeans also fields information from across the web to help you take action. That could be pointing you to the nearest dog parks or suggesting puppy training classes. Save your favorites to your library and go back anytime.And you can tune your stories, so if a recommendation isn’t quite right, you can provide feedback and it will help make the next collection even better. Or if Dreambeans missed something important, like a new hobby, you can provide that feedback and it will reflect in your future stories.Choose which apps to connectDreambeans requires at least one connected app to function and works best when they are all enabled. However, you get to choose your connected apps that help personalize your daily stories.You’re in control of your privacy. The choices you make in Dreambeans do not impact the ones you make for Personal Intelligence in other products like Gemini Apps or AI Mode.Dreambeans is rolling out starting today for eligible Google AI Ultra subscribers (18+) in the U.S. on Android and iOS. Others can join the waitlist on our website with a personal Google account.

#### New agents, mobile apps and Gemini Omni for Google Flow and Google Flow Music
- URL: https://blog.google/innovation-and-ai/models-and-research/google-labs/flow-updates/
- Insight: On last year’s I/O stage, we introduced Google Flow, built with and for filmmakers. Since then we expanded Flow into an AI creative studio, with new capabilities in video and image generation and editing, and launched in over 140 countries around the world. Earlier this year we added a new tool to our Google Flow family, Google Flow Music, which brings Google’s newest music model, Lyria 3 Pro, to artists, producers and songwriters. We’re now bringing an agent for every step of the creative process, a new AI model that offers precise video editing, the ability to “vibe code” bespoke workflows and mobile applications for on-the-go creation.Let’s take a closer look at what’s new in Google Flow and Google Flow Music. 1 What’s new for Google FlowWe're taking Google Flow to a new level with Gemini Omni, a new agentic experience and custom tools.Use the full potential of Gemini Omni: Gemini Omni Flash is a model that can create anything from any input, starting with video. It combines Gemini’s intelligence with our generative media models — and is a leap forward in world understanding, multimodality and precise video editing. You can think of Omni like Nano Banana, but for video. For creatives using Google Flow, Omni Flash allows you to blend real-world inspiration with generated content and iterate conversationally. Omni Flash also improves character consistency, meaning identity and voice are preserved across every scene. Omni Flash is available in Flow to Google AI subscribers globally.Collaborate at every stage: Google Flow Agent is your creative partner that can plan and reason through complex tasks with your inputs, under your control. Built with Gemini models, it brings expertise and a deep understanding of your project to help with early brainstorming, creating and editing. For example, the agent can be a sounding board for dialogue between characters in a specific scene, or even make plot recommendations. When you’re deeper in a project, your agent can help create multiple variations at one time to give you more options, and even batch edit, so your tweaks are reflected across all your assets. Once you have your assets, your agent can organize them into collections, and it can even intuitively rename them. The agent is now available to all Google Flow users globally.Build what you need with bespoke Tools: With Google Flow Tools, you can now use natural language to create bespoke tools and workflows in Google Flow. Whether you’re looking for a particular image editor, video resizer or custom shaders, you can now easily develop them, no coding experience required. And if you create something you think others might like, you can easily share your tool with other Flow users, who can remix it into their own. For example, one of our early access partners László Gaal created a tool called “pixelBento” to apply post-processing effects like lo-fi and glitch aesthetics. Check out this and other Tools, including some from our partners Kat Zhang and metapuppet in Flow. All Flow users globally are able to use existing Tools, while Google AI subscribers can also create and remix them.What’s new for Google Flow MusicGoogle Flow Music has always allowed you to create, iterate and share studio-quality songs. Our latest features provide more powerful editing control and improved music video creation.Precisely edit your song, section by section: We’re giving artists, songwriters and producers more granular control over what they create in Google Flow Music. Now you can highlight any part of a song and make changes. Instantly rewrite or translate lyrics, restyle the beat drop and more — without altering the rest of your track. Or you can sample a specific section of one of your songs, and extend it into a completely different direction.Reimagine your full tracks with covers: Transform the style of full songs you make in Google Flow Music, while keeping the original melody and structure. For instance, try creating a “lo-fi study” version of your favorite playlist.Create music videos with Gemini Omni: Our newest model is also coming to Google Flow Music, allowing you to work conversationally with the agent to direct shareable music videos. With Omni Flash you can guide the styles, subjects and scenes to match the narrative and pacing of your track. This is available to all Google AI subscribers.And, for both Google Flow and Google Flow Music, we’re launching mobile apps. While the web versions remain the go-to platforms for access to all capabilities and features, the mobile apps provide flexibility to create on the go. For those 18+, the Flow app is available on Android in beta (iOS coming soon), and the Flow Music app is available now on iOS (Android coming soon).Millions of creatives across a wide range of disciplines have brought their ideas to life using Google Flow and Google Flow Music in the last year; we can’t wait to see what gets created with these new capabilities in creatives’ hands.Features may vary by Goog...

#### Pomelli adds new ways to build brand content and design websites.
- URL: https://blog.google/innovation-and-ai/models-and-research/google-labs/pomelli-agentic-capabilities/
- Insight: Last year we introduced Pomelli in Google Labs to help small and medium-sized businesses create on-brand content. Since then, we’ve seen millions of professional product shots, social campaigns and ads come to life.Today, we’re making it even easier to create content for your business with new agentic capabilities. The Pomelli Agent helps you build your Business DNA or brand identity. Whether you have existing materials or are starting from scratch, you can upload product docs and photos, or chat with the agent to build your brand identity.Once your Business DNA is defined, you can also use two new features:Brand books: Generate comprehensive guides featuring your brand's custom images, fonts and colors.Websites: Design and stand up a complete website in just a few clicks.Visit Google Labs to try Pomelli today.Introducing Pomelli agent.Create a brand book.Generate a website.

#### We’re introducing new ways to design in real time with Stitch.
- URL: https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-updates/
- Insight: Today at I/O, we announced new ways to vibe design with Stitch, transforming your design experience into a live, collaborative partnership with the Stitch Agent — allowing you to design, stream and steer iterations in real time.Whether you start with a text prompt, use your voice or bring existing codebase and design files, designing with Stitch is now a more natural and intuitive collaboration. Describe what you want through text, or say it aloud, and Stitch works alongside you to build out and reflow your ideas.When you’re ready, you can instantly generate a shareable link via Google AI Studio. And when it’s time to move to production, you can export your screens into Google Antigravity to easily plug in your backend logic, or publish your work to the web directly with Netlify.These updates are available to global users starting today.Stitch now streams its work straight to the canvas, and you can see it working in real time.The Stitch Agent allows you to steer iterations before the final product is done.When you’re ready, you can easily export your designs to Google Antigravity.

#### Google Research
- URL: https://blog.google/innovation-and-ai/models-and-research/google-research/

#### New research shows how AMIE, our medical AI, could help manage health conditions.
- URL: https://blog.google/innovation-and-ai/models-and-research/google-research/amie-for-disease-management-in-nature/
- Insight: Giving a diagnosis is the first step in treating a patient. Once a diagnosis is established, the challenge becomes managing a health condition over time — tracking symptoms across multiple appointments, parsing guidelines as they’re updated and fine-tuning medications.Research published today in “Nature” shows the capabilities of the Articulate Medical Intelligence Explorer (AMIE), our best-in-class research AI system for medical reasoning and conversations, evolving from one-off diagnostic conversations to long-term disease management using drug formularies and clinical guidelines.Using the long-context capabilities of Gemini models, AMIE for disease management features an empathetic dialogue agent for real-time patient conversations and a deep-thinking management reasoning agent that cross-references hundreds of pages of authoritative clinical knowledge. In this blinded study with patient actors, specialist physicians compared AMIE with 21 primary care doctors. AMIE matched clinicians in overall management reasoning and scored significantly higher in plan preciseness and guideline alignment, which suggests AI could someday support medical care, giving physicians more time to spend with patients.Next up: We're exploring how AMIE could work in clinical settings, and we launched a nationwide study to assess AI in real-world virtual care.Google's new research on medical AI for disease management was published in "Nature" today. (Credit: Google, with permission from "Nature.")

#### Three new satellites join the fight against wildfires
- URL: https://blog.google/innovation-and-ai/models-and-research/google-research/firesat-satellites/
- Insight: Today, three new FireSat satellites successfully launched from Vandenberg Space Force Base in California. This expands the FireSat program, a global initiative led by the nonprofit Earth Fire Alliance (EFA) to create an unprecedented wildfire dataset. Google Research has teamed up with leaders in the fire community, including EFA and satellite manufacturer Muon Space, to create this purpose-built constellation designed to provide the continuous coverage fire agencies need to detect wildfires before they spread.This next phase builds directly on the momentum established last year when FireSat’s pilot satellite reached orbit. That mission successfully demonstrated the potential of the underlying sensor technology designed to detect early-stage wildfires as small as 5x5 meters. The pilot has already spotted small, low-intensity blazes invisible to existing satellites, and these three new orbiters carry that proven architecture directly into the growing network.This milestone is a testament to what is possible when tech companies, nonprofits, philanthropy, and the private sector unite under a single mission. To help kickstart this work, Google.org has provided over $15 million to support the deployment of these early satellites. It’s a proud moment for the entire consortium, and another tangible step forward in putting practical AI to work for climate resilience.Three new FireSat satellitesCredit: Muon SpaceSatellites onboard the SpaceX Transporter-17 vesselCredit: SpaceXSatellites being deployed from SpaceX Transporter-17 vessel into spaceCredit: SpaceX

#### A new experiment brings better group meetings to Google Beam
- URL: https://blog.google/innovation-and-ai/models-and-research/google-research/google-beam-group-meetings/
- Insight: While video conferencing tools keep us connected, users can still struggle to feel included in the conversation. Trying to read subtle emotions in a sea of tiny boxes may leave remote participants feeling like observers rather than engaged participants. Google Beam, our true-to-life video communication platform, helps you solve this problem by turning your meetings into a more active exchange.Today, we’re sharing a new experiment that brings better group meetings to Google Beam across more devices. Using HP Dimension’s immersive display, Google Beam renders participants joining from non-Beam devices in their true size, positioned as if they were sitting around a table with you. Paired with spatial audio that anchors each voice directly to the person speaking, colleagues look, sound, and feel more like they are in the same room.This optimization happens automatically, whether you join a meeting from home or the office. Our research suggests approaches like these help close the hybrid 'i...

#### Quantum computing
- URL: https://blog.google/innovation-and-ai/models-and-research/quantum-computing/
- Insight: News from Google Quantum AI about how we're building quantum computing for unsolvable problems.

#### Our new initiative to apply quantum science and AI to the life sciences
- URL: https://blog.google/innovation-and-ai/models-and-research/quantum-computing/repliqa-quantum-computing-life-sciences/
- Insight: Understanding human biology and health at the molecular level is one of science’s greatest challenges. To help tackle this, we’re launching the Research Program at the Intersection of the Life Sciences and Quantum AI (REPLIQA).REPLIQA is an effort by Google Quantum AI and Google.org to apply advanced quantum science and AI to the life sciences field. Part of this effort is a commitment of $10 million from Google.org to advance research at five leading academic institutions.The quantum advantage in biologyBiological processes, like how a protein folds or how a cell reacts to a new drug, involve incredibly complex interactions at the atomic level. Classical computers often struggle to accurately simulate these interactions. Quantum technologies, however, operate using the very same quantum mechanics that govern these molecules.For example, quantum sensors can now observe biological processes with unprecedented precision. Recent experiments even suggest that quantum spin — the way subatomic particles rotate — might play a role in how cells function. Furthermore, quantum computers have the potential to drastically accelerate simulations of complex molecular interactions, like the behavior of the P450 enzyme, which is critical for drug development.As quantum computing technology continues to mature, we have an opportunity to combine it with AI and biological science to unlock new discoveries in biological sciences and improve human outcomes.A scientific ecosystemTackling problems of this scale requires a shared vision across the scientific community. We are proud to commit funding to Harvard University, the Massachusetts Institute of Technology, University of California San Diego, University of California, Santa Barbara and the University of Arizona, institutions that are already pioneering in this space.Foundational research for future breakthroughsWe see immense potential in this emerging field. However, REPLIQA is a foundational research effort. We will not see results overnight. Instead, we are working to build the essential tools, such as quantum sensors or quantum-enhanced AI algorithms, needed to make those future breakthroughs possible. By laying this groundwork today, we hope to spark the next generation of discoveries.

#### Answering your trending questions on World Quantum Day
- URL: https://blog.google/innovation-and-ai/models-and-research/quantum-computing/world-quantum-day-2026/
- Insight: The discovery of quantum mechanics fundamentally changed how we understand the natural world. In 1981, physicist Richard Feynman famously observed that because nature is quantum, we would eventually need to build computers that operate on those same principles to truly understand it. Building these computers remains one of the greatest engineering challenges of our era.At Google Quantum AI, our mission is to develop quantum computing for these complex, currently unsolvable problems. We believe large-scale, error-corrected quantum computers will be the key to unlocking certain solutions for real-world problems — from discovering more sustainable materials to accelerating drug discovery — that are beyond the reach of classical computers today.Our focus remains on the long-term journey: moving from experimental physics to the reliable, stable systems necessary to provide these breakthroughs for everyone.Visualizing the state of the qubitToday’s Google Doodle marks World Quantum Day by incorporating the Bloch Sphere into our logo. In quantum mechanics, the Bloch Sphere is a geometric representation of the state space of a two-level quantum system, or qubit.Unlike a classical bit, which is restricted to a binary state of 0 or 1, a qubit can exist in a combination of both. This is represented as a point on the Bloch Sphere, allowing for a much larger computational state space than traditional computing.A major hurdle today is maintaining these delicate states. Interaction with the environment causes "decoherence," where quantum information is lost to noise. Our current work is centered on building systems that can protect this information long enough to perform meaningful computations.Answering your top-trending questionsWhy do we need quantum computers? How do they reach the right answers so quickly? And what does that have to do with interference?We sat down with Google Quantum AI experts Jenna and Andrew to tackle the world’s most-searched questions about quantum computing.Learn more about our latest progress in quantum computing at quantumai.google.

#### Save time and grow your business with new Gemini tools
- URL: https://blog.google/innovation-and-ai/products/gemini-app/gemini-features-for-businesses/
- Insight: Small businesses are the true engine of the global economy, yet entrepreneurs often find themselves stretched thin, playing the roles of CEO, CMO and customer service team all before lunch. AI holds incredible promise to act as an extension of your team, but to be truly helpful, it needs to remember your brand voice and context so you don't have to re-explain your goals every time you log in.Building on the new Google AI capabilities we announced in May, we’re excited to share what’s next for Gemini and Google Business Profile users. Today on stage at Google for Brazil, we introduced new Gemini app features specifically designed for business owners everywhere.Rolling out globally this month, these updates transform Gemini into a deeply knowledgeable, in-pocket partner that natively understands your business and helps you get more done.Connect your Google Business Profile to GeminiYour Google Business Profile serves as your digital storefront, helping you stand out on Google Search and ...

#### Gemini Spark updates: macOS launch, connected apps and more
- URL: https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-june-2026/
- Insight: Today, we’re rolling out updates to Gemini Spark that make it even more helpful, from a new desktop experience to deeper connections with your favorite apps. Here’s a look at what’s new:Bring Gemini Spark to your MacWe’re bringing Spark to the Gemini macOS app to help you automate time-consuming tasks across your desktop.Gemini Spark can now move beyond the chat window, and tackle the heavy lifting across your desktop files and apps. For example, you can turn hours of manual file sorting into an instant action by asking Gemini Spark to sort all the PDFs in your Downloads into specific folders. Gemini Spark also connects your desktop and Google Workspace, so you can simply ask it to create a budget spreadsheet using the latest invoices saved to your computer, and create a schedule to update it regularly. To keep your information secure, Gemini Spark only has access to the files you give it permission to use.And coming soon, you’ll even be able to run tasks remotely. You can assign a multi-step task to Gemini Spark from your phone — like asking it to find a specific sales report on your Mac, pull the total revenue number, and email it to you — and let it execute the work on your computer while you're away.Gemini Spark for macOS is available in Beta to Google AI Ultra subscribers aged 18 and over, starting in the US. Download the app at gemini.google/mac to get started.Connect Gemini Spark to your favorite appsWe’ve expanded our connected apps so Spark can help you across more of the services you use. It now works with Google Tasks and Google Keep, meaning you can ask Spark to scan your scattered brain-dumps in Keep and turn them into action items in Tasks. We’re also launching integrations with Canva, Dropbox, Instacart, OpenTable and Zillow Rentals, so you can easily design custom flyers, access and share your files, reserve a table for date night, order your weekly groceries or reserve an apartment tour. These connected apps are rolling out over the next week on Gemini Spark on web and mobile and will be rolling out to the macOS app in the coming weeks.We’re also rolling out support for custom Model Context Protocol (MCP), giving you the ability to connect your favorite apps directly into Spark to build a more tailored assistant.Stay up to date on topics in real timeWe’re also giving Gemini Spark the ability to intelligently track topics and react to events in real time. For example, if you want to stay up to speed on highlights and analysis after your favorite soccer team plays, Spark brings you the latest the moment the match ends. Or, you can ask Spark to send you a detailed financial report if a stock reaches a certain threshold. You can now ask Spark to keep an eye on blogs, news sites, social media, finance, shopping, weather and sports, in addition to your email, so you don't have to constantly hit refresh.These updates are rolling out starting today, and we look forward to sharing more about what’s next for Spark this summer.

#### 5 ways to learn with study notebooks in the Gemini app
- URL: https://blog.google/innovation-and-ai/products/gemini-app/gemini-study-notebooks/
- Insight: Studying can feel overwhelming, especially when you don't know where to start or what to focus on next. That’s why we’re introducing study notebooks in the Gemini app.Study notebooks are designed specifically for students. As a goal-oriented learning space, they generate personalized lessons based on your real-time strengths and knowledge gaps. Your progress is tracked through a custom dashboard based on an initial diagnostic quiz and then follow-up quiz performance. Here are five ways to learn with study notebooks in Gemini:1. Assess your knowledge gapsTo start, upload your syllabus, notes, reading materials or other class materials. Gemini will then generate a custom diagnostic quiz to establish an academic baseline. It actively pinpoints your unique strengths and weaknesses, so you know exactly which areas need attention, replacing guessing games with a tailored learning plan.2. Study with bite-sized lessons built just for youOnce your baseline knowledge is assessed, your study notebook crafts short lessons designed to tackle your knowledge gaps. Each lesson includes practice quizzes to test your understanding, which are based on class materials you uploaded. While studying, you can pause at any time to ask questions right within your study notebook. Coming later this summer, lessons will feature more visuals like diagrams and interactive visualizations.3. Track your progressStudy notebooks feature a personalized, skill-based progress dashboard that tracks your learning in real time. To do this, Gemini is breaking down your learning goal into more than 100 specific learning objectives, then grouping those into topics and tracking your progress. It labels these as "Strengths," "Focus areas" or "Not started," updating automatically as you complete quizzes in follow-up lessons. The dashboard actively ranks and recommends your top priority lessons so you always know your next step, while still allowing you to filter and browse by specific strengths, focus areas and more.4. Prep for standardized examsPreparing for major milestone exams can be stressful and expensive. Today, you can prepare for exams like the SAT — grounded in authoritative questions from The Princeton Review — directly within study notebooks. Standardized exam prep uses the same diagnostic quiz and personalized bite-sized lessons with progress checks to help you pinpoint your strengths and focus areas. We’re continuing to add more standardized tests in study notebooks including JEE, NEET, ENEM, ACT and GRE this summer.5. Stay organizedBecause your notebook’s sources are seamlessly integrated across Gemini app and NotebookLM, you can easily reference past chats and use your uploaded class materials right within NotebookLM to generate interactive flashcards, Video Overviews and more.Study notebooks are rolling out globally in all languages. 1 Study notebooks are rolling out now for personal accounts in languages where the Gemini app is available, and will be available for all school-issued accounts, including for users under 18, in the coming weeks. Study notebooks are available on the web, with mobile support coming later this summer.

#### Gemini’s new study notebooks help you learn with personalized lessons, practice quizzes and a custom progress dashboard.
- URL: https://blog.google/innovation-and-ai/products/gemini-app/how-to-make-gemini-study-notebooks/
- Insight: Studying for a test, but not sure where to start? Study notebooks, a new feature in the Gemini app, can help you get organized and learn more efficiently.Think of study notebooks as a personalized learning space. You tell Gemini what you want to learn, and it helps you get there with bite-sized lessons tailored to your strengths and knowledge gaps.Along the way, Gemini will test your understanding with practice quizzes. And you can track your progress on a custom dashboard that helps you pinpoint what to prioritize next. That means you can spend less time worrying about what to focus on and master new subjects faster.Learn how to make — and get the most from — Gemini study notebooks in the video below.

#### The Gemini app is bringing personalized image creation to more users.
- URL: https://blog.google/innovation-and-ai/products/gemini-app/personal-intelligence-nano-banana-us-expansion/
- Insight: Personal Intelligence makes the Gemini app feel tailored to you. With your permission, it pulls from Google tools like Gmail, Google Photos, YouTube and Search to provide the most relevant responses — like an assistant who knows you.Starting today, all eligible users in the U.S. 1 can experience deeply personalized image generation in Gemini for free. We’re connecting Personal Intelligence with Nano Banana and Google Photos, so your creations can easily reflect your taste and lifestyle, gleaned from your connected Google apps.Now, instead of writing out the intricate details of your life, you can use simple prompts like “design my dream house.” And because Gemini can pull actual images of you from Google Photos, you no longer need to manually upload photos when prompting "create an illustration of me and my favorite things." Gemini pulls the right context from your connected Google apps, letting you spend less time explaining and more time creating.You’re in control. Connecting your Google apps to Gemini remains an opt-in experience that you can adjust in your settings at any time.Learn more about eligibility here.

#### View more from NotebookLM
- URL: https://blog.google/innovation-and-ai/products/notebooklm/

#### Do better research with NotebookLM
- URL: https://blog.google/innovation-and-ai/products/notebooklm/better-research-notebooklm/
- Insight: Three years ago we launched NotebookLM as an experimental AI product from Google Labs to help you understand anything. Millions of people and organizations turn to NotebookLM as a collaborative knowledge and research partner because it helps them organize their thinking, identify deeper connections across their documents and spark new ideas. Today we’re introducing across the board upgrades to NotebookLM that deliver new agentic capabilities in chat and more advanced reasoning to tackle the most complex research projects.An upgraded, more thoughtful chat experienceFirst, we’re upgrading NotebookLM to run on Gemini 3.5 and Antigravity providing even more accurate and reliable information along with better visibility into the thinking process.Each notebook is now equipped with a secure cloud computer, enabling NotebookLM to write and run code useful for helping you perform deeper research and more complex analysis. The system includes more than 100 curated software skills, unlocking a wide range of new capabilities to help you more deeply understand the sources in your notebook.In our side-by-side evaluations against our prior system, the upgraded NotebookLM achieved an average win rate of over 65% (a 15% point margin above parity) across our top five core evaluation dimensions. The system demonstrated substantial improvements in large document analysis, securing a 69.9% win rate and achieved exceptional performance in advanced web research and source discovery reaching a 78.2% win rate against our prior baseline. 1 More output formats, with improved customizationYou can now ask NotebookLM to create outputs in even more formats and provide detailed instructions to guide the outputs. NotebookLM will assemble the context from your sources to produce useful and high quality formats like PDF reports with charts and tables, detailed budget spreadsheets, and bespoke student worksheets — all ready to download directly from the studio panel. You can even make edits after your outputs are generated. New output formats include:Data visualizations and charts (png, svg)Documents (PDFs, docx, markdown, text files)Images with Nano Banana (png, jpg, gif)Structured data (csv, json)Microsoft Excel (xlsx)Microsoft PowerPoint (pptx)We plan to add additional formats in the future to help make NotebookLM more helpful in more ways.More effortless researchFinally, we’re making it easier to get your research started. Previously, NotebookLM was most helpful when you came with your own sources and a good handle on your project. You can now start with loose ideas and questions. NotebookLM can guide you through building your source repository directly in your chat, making it even easier to get started on any project. Perhaps you want to find primary sources in other languages to better understand new perspectives, or you’re seeking related works by an author you recently discovered. It can even use Google Search to find relevant, high quality sources from the web and add them to your notebook.You’re still in control of the sources that you add to your notebook so that your work stays grounded in the information you trust and all sources continue to be clearly attributed.More helpful in more situationsHere are some workflows these improvements enable:Researchers: A data analyst can combine data from various countries with conflicting formatting. To make this information useful, the analyst can ask NotebookLM to conduct web research to find additional context, write code to perform accurate data analysis, and create charts and a PDF report to showcase the results.Technical Professionals: A program manager can decipher complex specifications for customer integration, instantly transforming the technical documentation into a polished, simplified guide, slide deck and a step-by-step roadmap for the team.Small Business Owners: A gym owner can run a media campaign and analyze raw sales data against ad spend. By calculating the campaign's financial impact using NotebookLM, the business owner is better equipped to decide whether to expand to other cities.These updates are rolling out globally on the web starting today to all users with Google AI Ultra and all Workspace business customers with AI Ultra Access and AI Expanded Access, and we plan to expand to others over time. We look forward to your feedback.Evaluation set contains queries spanning core NotebookLM use cases across source-grounded Q&A, multilingual interactions, long-form document understanding, content generation, and multi-source research. Category definitions: Accuracy & Quality evaluates the correctness, relevance, and groundedness of responses against user-uploaded sources; Multilingual Support measures the ability to understand queries and generate faithful responses across non-English languages; Large Document Analysis assesses reasoning and comprehension over long-context source material such as books, reports, and transcripts; Artifact Creation evaluates the ability ...

#### Generate your own Cinematic Video Overviews in NotebookLM.
- URL: https://blog.google/innovation-and-ai/products/notebooklm/generate-your-own-cinematic-video-overviews-in-notebooklm/
- Insight: NotebookLM is introducing Cinematic Video Overviews, a major update to its AI-powered video creation capabilities. This new feature moves beyond narrated slides in Video Overviews to create unique, immersive videos tailored to you.Using a combination of our advanced AI models, including Gemini 3, Nano Banana Pro and Veo 3, Cinematic Video Overviews generate fluid animations and rich, detailed visuals to help you learn and engage with the topics you care about. Gemini now acts as a creative director, making hundreds of structural and stylistic decisions to best tell the story with your sources. It determines the best narrative, visual style and format, and even refines its own work to ensure consistency.Cinematic Video Overviews are available in English starting today for Google AI Ultra subscribers (18+) on web and mobile....

#### Dive deeper into I/O 2026 with NotebookLM.
- URL: https://blog.google/innovation-and-ai/products/notebooklm/notebooklm-google-io-2026/
- Insight: Google I/O is always jam-packed with announcements, demos and launches — and this year was no exception. Whether you’re looking to dive into the details of a new product or just want to catch up on news you might have missed, you can see it all in the notebook we’ve created using Google NotebookLM.This notebook has tons of info: YouTube videos of keynote speeches and product demonstrations, blog posts and more. Here’s how you can use our notebook on web or mobile:Listen to an Audio Overview to catch up in less than two minutes.Read through a Slide Deck to learn more about the biggest launches.Explore our highlights through an Infographic.Revisit some of our biggest announcements in a Video Overview.Ask your own questions about a new product or launch. (“What are the top updates to Search?”)(NotebookLM is grounded in provided sources and responses have citations, but remember, like all AI, NotebookLM can generate inaccuracies.)Still want more? Review the 100 things we announced this yea...

#### Ask a Techspert: What is vibe coding?
- URL: https://blog.google/innovation-and-ai/products/techspert-what-is-vibe-coding/
- Insight: You’ve heard of coding, and you’ve definitely heard of vibes. But what do they have to do with each other? Vibe coding is an emerging field of development, thanks to AI. It’s helping people build websites, apps and more. To get a better idea of how vibe coding works, why it’s becoming increasingly popular and what you can do with it, we talked to product director Kelly Schaefer, who leads a portfolio of AI-powered products in Google Labs.What do you do at Google?My teams and I build what we call “future of” products, which focus on the future of design, writing and even software development. In the software arena, we’re thinking about how to democratize building products. It’s not just engineers who will be building in the future!And vibe coding can help with that democratization. What’s your definition of vibe coding?Vibe coding lets you build what you envisioned in your head even if you don't have traditional coding skills. It’s a process where, for example, you can use an AI tool and explain what you want to make and what you want it to look like, and that tool will generate something for you that you can see and use. In the past, you would have had to manually write lines of code to do that.Do you need to have any coding skills to vibe code?You actually don’t — you can make simple apps just by vibe coding. But it might not be the best solution depending on what you’re trying to build and how many people you want to use it. If you want to bring a vibe-coded app all the way to being a fully launched product that a lot of people can use, you still need coding skill and precision. Sometimes people think “I just need to write two sentences about my app and I’ll have an app in the Google Play store that everyone can use!”So it’s not just like you can think of something, see it in your mind and poof — it’s vibe coded perfectly, working exactly as you imagined?Right. You can describe something in simple terms and get a vibe-coded app — but to turn it into a real product you’ll need to keep going. It’s great to start by opening a vibe coding tool and trying something simple — for example, the Canvas option in Gemini allows you to enter a prompt like “make me a web app prototype.” You’ll get a basic product. If you wanted to turn this into something lots of people could use, then you could take the next step and start coding, or sharing your basic web app with a developer who would take it to the next stage. For that step, there are tools like Jules, an AI coding agent from Labs, which connects with your code and adds its own code based on what you’ve already made — plus you can ask it to make changes using natural language. Starting this whole process with vibe coding means more of what you saw in your mind’s eye can make it into the final product.Your vision and your vibe! Sounds like vibe coding isn’t mindless, but it’s helpful for someone who wants to make something and doesn’t know how to code. What kinds of projects do you think are a good fit for vibe coding?It can help you with prototyping and visualizing your idea so you can communicate it to others, for example if you want to make a functioning app or website for a lot of people to use. Tools like Stitch are especially good at this — you can generate an interface and get front-end code, and then pair it with an AI coding agent like Jules to turn that design into working code. Jules is more of a developer tool to implement ideas at a production level. It’s really helpful because you can hand off multiple tasks at once — something our users love! — like fixing bugs or building out new features. Together, Stitch and Jules show how vibe coding isn’t only about generating snapshots of an experience, but about making the full loop from idea to design to production-ready code accessible.I’m guessing what I could vibe code would be very different from what an engineer could vibe code, right?Well, sure, but your purposes are probably different, too. For example, Stitch is great when you want to quickly describe or visualize an idea, while Jules can carry that forward into live prototypes and all the way into production. Used together, they mirror the way an engineer and a designer might collaborate. If you’re not an engineer or a designer, vibe coding is a way to visualize what you want an engineer to build. Instead of starting with a doc, start with an interactive visual. Also, vibe coding tools are totally something to just have fun with! You can make whatever you want for yourself or to share with friends for no reason other than your own entertainment.What’s your advice for someone who doesn’t want to be a traditional engineer and wants to get good enough at vibe coding to either build apps or help others visualize them?Before using a vibe coding tool, start with Gemini and try writing prompts that describe your ideas. Ask Gemini “what am I not considering here?” or “what are some different takes on this?” You're going to get a much better prompt out of it, ...

#### I/O 2026: Welcome to the agentic Gemini era
- URL: https://blog.google/innovation-and-ai/sundar-pichai-io-2026/
- Insight: Editor’s note: Below is an edited transcript of Google CEO Sundar Pichai’s remarks at Google I/O 2026, adapted to include more of what was announced on stage. See all the announcements in our collection.It’s been an extraordinary year since our last I/O, a period of relentless shipping, technology advances and hyper progress. We’re now in the part of the AI cycle where people want to see the value in the products they use every day. We’ve been really focused on that, and you’ll see that in the products and features we’re announcing today at I/O.Ten years since we pivoted the company to be AI-first, we still see AI as the most profound way to advance our mission and improve people’s lives at scale. That’s why we’ve been taking a differentiated, full-stack approach to AI innovation, from our custom silicon and secure foundation, to our world-class research and models, to our products and platforms that touch billions of people. This approach enables us to iterate and innovate faster in w...

#### Ask an AI expert: What exactly is the full stack?
- URL: https://blog.google/innovation-and-ai/technology/ai/full-stack-ai-explainer/
- Insight: If you’ve spent any time lately reading about AI or using AI tools, you’ve probably heard about “full-stack” AI and app development. Our unique full-stack approach to AI lets us deliver powerful, cost-efficient products to expert developers and everyday users alike. But what exactly does it mean when a technology system is "full-stack”? We asked Google expert Richard Seroter, who leads developer experience at Google Cloud, to explain it — and why it enables Google to bring helpful AI to billions of people.First things first: What exactly do you do at Google?I originally came to Google as a product manager, and I’ve been leading our developer relations and technical writing teams for about three years now. My team, now inclusive of product engineering for languages and frameworks along with our Open Source Programs Office, and I help software developers successfully build with Google Cloud products. We do a lot of different things, from building the programming languages and frameworks that developers use, to meeting directly with the community to share best practices, to running the technical writing team that crafts our documentation. Ultimately, our entire focus is on giving developers the confidence that they can get things done with Google products.Given our topic today, I would imagine that means you’re helping developers use our full-stack technology.I am, yes!Let’s define that term. Where does the phrase “full-stack” come from, and what does it mean when we’re talking about tech?When the term "full-stack" originally came out in software development a decade or so ago, people were usually thinking about applications. Historically, building an app required multiple specialized teams: a front-end developer to build beautiful user interfaces, a back-end developer to handle server-side logic and a dedicated database team.The concept of a "full-stack engineer" emerged to describe a developer who could work across all of these functions independently. Instead of constantly handing off components from one person to another, a full-stack engineer could take an idea from a rough concept all the way to a fully running piece of software.So it started with apps, and now it’s on to AI?Right. We’ve taken that exact same end-to-end principle and applied it to AI. If you’re trying to deliver value with AI, you can either buy a bunch of disparate parts from different vendors and try to stitch them together yourself, or you can look for an integrated system where everything you need is already connected.What disparate parts can someone stitch together to make a full AI stack?An intentional AI stack needs a cohesive combination of layers to get a job done: compute infrastructure, an AI model, an orchestration platform and the user interfaces. At Google, we’ve deliberately invested in every single layer. We provide the hardware like Tensor Processing Units (TPUs), frontier models developed by Google DeepMind like the Gemini family of models, the Gemini Enterprise Agent Platform and the interfaces people use daily, like Maps and Gmail. We’ve essentially done the hunting for you and put all the necessary components right inside the box.Did we know we wanted to have a full-stack approach way back when Google first started working on AI?It was absolutely a deliberate, decades-long strategy. For instance, our bet on custom TPUs is already over 10 years old. We recognized early on that there’s massive value in owning our own supply chain and raw infrastructure when serving up the world's most important internet services. Owning that thread throughout the entire stack lets us deliver a level of service, performance and reliability that's very hard to achieve if you're at the mercy of multiple parties.On the flip side, does adopting a full-stack platform limit builders in some way?That’s a very fair concern, but locking people in doesn't align with our ethos. No company does open source quite like Google; we regularly give away foundational technology and source code that the entire industry depends on.We like to describe our AI platform as "opinionated but extensible" and "batteries included” — meaning everything you need to build and run an application is ready to go out of the box. However, if you want to use another company’s AI model instead of Gemini, or hook up different software instead of Google Workspace, you can plug those right in. We want you to use our products every day based on the completeness of our platform, not because we forced you into a closed choice.Besides simplicity, what are some other benefits to working with full-stack AI?Because Google manages the entire stack — literally from running the underlying infrastructure all the way up to delivering Gmail — there's massive system reliability. If a technical failure happens at one layer, our ownership of the platform allows us to catch it and handle it at another layer easily, rather than waiting for an external provider to fix it. There's also an economic ...

#### The latest AI news we announced in June 2026
- URL: https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-june-2026/
- Insight: For more than 20 years, we’ve invested in machine learning and AI research, tools and infrastructure to build products that make everyday life better for more people. Teams across Google are working on ways to unlock AI’s benefits in fields as wide-ranging as healthcare, crisis response and education. To keep you posted on our progress, we're doing a regular roundup of Google's most recent AI news.Here’s a look back at some of our AI announcements from June.This month was about creating a more unified environment where AI delivers help naturally throughout your day. With the debut of Android 17 and local models like Gemma 4 12B running right on your laptop, our June updates reflect a vision where technology acts as an intuitive partner and helps you reach your goals. Whether you’re a small business owner trying to get your shop noticed, a student setting up a study schedule or a researcher tackling climate challenges, these updates handle the complex logistics so you can focus on what matters most.Try Gemma 4 12B, our latest open model. Gemma 4 12B brings smart AI agents directly to your laptop. It runs locally using just 16GB of memory, combining a novel unified architecture with vision and native voice processing in a single streamlined system. This gives you advanced reasoning and private workflows on everyday hardware without sacrificing speed.Experience computer use in Gemini 3.5 Flash. We integrated computer use into Gemini 3.5 Flash, allowing you to build custom agents that can see, reason and take action across desktop, mobile and browser environments. The update improves performance for long-horizon and enterprise automation tasks, like continuous software testing and knowledge work.Start building with Nano Banana 2 Lite and Gemini Omni Flash. To make it faster and easier to experiment, refine and scale your ideas , we've launched two major updates. First, Nano Banana 2 Lite is now available and it’s our fastest and most cost-efficient Gemini Image model yet. Second, we're bringing Gemini Omni Flash to APIs in public preview, introducing a natively multimodal model for enterprises and developers to build custom, dynamic video workflows for the very first time.Check out what's new in Android 17. Android 17 is packed with features like floating app windows for faster multitasking, Screen Reactions for picture-in-picture recording, an optimized layout for foldable gaming and more. You’ll also get more peace of mind with new security upgrades, including the ability to lock a missing phone using your biometrics. These updates are rolling out first to Pixel devices, followed by other eligible Android devices throughout 2026. Plus, take a look at our new personalization and safety features in June’s Android Drop.Discover the June Pixel Drop. We rolled out new features and Gemini upgrades designed to make your device more creative and secure. This update introduces screen recording reactions, AI-powered video and music creation, and floating app bubbles for easier multitasking. You'll also get expanded real-time voice translation, custom voicemail greetings and automated emergency notifications.Try the new Google Finance. The new Google Finance is coming out of beta, with several new capabilities to help you better track and understand financial investments. You can monitor your own investment portfolio, stay updated on market intel and get insights on the go with the new Google Finance app for Android — including an AI research tool and AI-powered “key moments” that explain why a stock moved.Translate speech naturally with Gemini 3.5 Live Translate. This new audio model for live speech-to-speech translation automatically detects more than 70 languages while preserving the speaker's natural intonation and eliminating awkward pauses. You can now have fluid, near-real-time conversations during multilingual calls, meetings or travel, removing language barriers in seconds — rolling out in Gemini Live API, Google AI Studio and Google Translate app.Get the new Google Home Speaker, built for Gemini. Our new smart speaker built with Gemini makes conversing with your home assistant feel more natural. You don't need to use rigid commands anymore because it understands you just like a real person. It can handle multiple requests at once, answer complex questions and even remember what you were just talking about. Plus, discover 100 new ways to make your day easier with Gemini for Home voice assistant.Do better research with NotebookLM. We upgraded NotebookLM with advanced reasoning, a secure cloud computer for running code, and the ability to generate charts, spreadsheets and slide decks. The tool now helps you organize loose ideas and gather web sources into a structured research repository — available globally today for Google AI Ultra subscribers and specific Workspace accounts.Start learning with study notebooks in the Gemini app. Set your goal, upload your class notes, take a baseline knowledge quiz and Gemini w...

#### The latest AI news we announced in May 2026
- URL: https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-may-2026/
- Insight: For more than 20 years, we’ve invested in machine learning and AI research, tools and infrastructure to build products that make everyday life better for more people. Teams across Google are working on ways to unlock AI’s benefits in fields as wide-ranging as healthcare, crisis response and education. To keep you posted on our progress, we're doing a regular roundup of Google's most recent AI news.Here’s a look back at some of our AI announcements from May.May 2026 was packed with AI news. At Google I/O 2026, we officially entered the agentic Gemini era with the launch of Gemini 3.5 — which delivers frontier intelligence for agents and coding — and Gemini Omni, where Gemini’s ability to reason meets the ability to create. The Android Show set the stage with brand-new hardware built specifically for these tools, including the Googlebook from our hardware partners. We also broadened our personal wellness tools with the new Google Health app and Fitbit Air, and launched an initiative to apply advanced quantum science and AI to the life sciences. Ultimately, May was all about making AI more proactive, helpful and integrated into your everyday life.Experience Gemini Omni. We announced Gemini Omni, our new model that can create anything from any input — starting with video. Omni allows you to combine images, audio, video and text as input and generate high-quality videos grounded in Gemini's real-world knowledge.Simulate real-world places. By combining Project Genie with Street View, we introduced an experimental new way to simulate and explore highly realistic, interactive 3D environments of real-world places right from your browser.Learn how we partner with musical artists. Through a new partnership between Google Flow Music and Believe, we're equipping artists and producers with a creative AI collaborator to help throughout the creation process, from brainstorming lyrics and melodies to putting final touches on a song.Discover what’s possible with Gemini 3.5. We launched our latest family of models combining frontier intelligence with action. With powerful new action-taking capabilities, Gemini 3.5 is built to help you reliably execute complex, multi-step agentic workflows across your apps.Connect with your proactive 24/7 partner. The Gemini app is becoming a more helpful AI assistant, featuring an intuitive new UI, personalized daily briefs and Gemini Spark. Instead of just answering questions, it acts as a proactive helper — managing your inbox, scheduling appointments and anticipating your daily needs in the background.Get more done with our advanced AI models in Search. Our next era for Search introduces new features that bring together the best of the web with the best of AI. We're launching information agents in Search to intelligently work in the background, 24/7. They'll monitor information on your behalf and send detailed updates with links to dive deeper and take action. We’re also bringing Antigravity and the agentic coding capabilities of Gemini 3.5 Flash right into Search, so Search can build generative UI and interactive visuals tailored to your questions, plus custom experiences like dashboards or mini apps for your ongoing tasks. And we introduced a new, intelligent Search box, marking its biggest upgrade in over 25 years.With agentic coding capabilities in Search, you’ll be able to ask Search to code a custom fitness tracker for you, using real-time data like reviews, live maps and weather to keep you on track.Stay in sync with Android Halo. To help you manage your agents, we introduced Android Halo, a new space on your phone that lets you see your agents’ progress and receive contextual assistance without interrupting your flow.Simplify your shopping with Universal Cart. Universal Cart is your new hub for shopping on Google. Universal Cart works across merchants and across services, so you can add things to your cart while you’re browsing Search, chatting with Gemini, watching YouTube or even reading your Gmail.Try the all-new Google Health app. The Google Health app brings all of your health and wellness into one place debuting new and advanced capabilities.Meet the all-new Fitbit Air. Fitbit Air is our smallest tracker yet — a proactive wellness partner that uses high-fidelity sensor technology in a tiny, discreet pebble that enables advanced health and fitness tracking like 24/7 heart rate, heart rhythm monitoring with Afib alerts, SpO2, resting heart rate, heart rate variability, sleep stages and duration, and more. 1 2 3 4 Discover the new Googlebook. Googlebook is our newly designed laptop experience built from the ground up for Gemini Intelligence. It features the Magic Pointer for contextual suggestions, custom widgets to help you organize your tasks, cross-device features with Android phones and powerful AI features to help you get more done. Googlebooks will be made by our hardware partners like Acer, Asus, Dell, HP and Lenovo.Upgrade your phone with Gemin...

#### How we used Gemini to build Google I/O 2026
- URL: https://blog.google/innovation-and-ai/technology/ai/io-2026-google-ai/
- Insight: Google I/O 2026 was all about how we’re making AI helpful for everyone in new ways. But we didn’t just make announcements about our innovations in AI at I/O — we used those tools to bring I/O to life, too.It’s both a strange and exciting moment to be building anything. We're living through an incredible shift where AI tools are getting better each month, effectively rewriting the rules of what we can create.This year, we challenged ourselves to use the same AI we were putting on stage to out-innovate, out-create and out-efficient ourselves.We moved faster than ever and prototyped in real-time — blending human artistry with experimental technology — with no better example than the "Timmy TPU" film.But the reward is showing how these tools unlock creativity and offload the mundane tasks, giving the team their best hours back for the parts they are uniquely suited to do. When done right, the event is amazing on its own, and, as a viewer, you stop thinking about how AI was used. That shift is the opportunity we want to share, because people keep asking, “What can you really do with AI?”Keep reading to learn which AI tools we used — and how we prompted them — to help make I/O 2026 happen.AI x Film“TPU Training Day” short filmThe AI products & models: Google AI Studio; experimental DeepMind models; Gemini Omni; Nano BananaWhat we did: We created a short film starring a bunch of TPUs getting ready to do some heavy lifting for I/O 2026.How we did it: This project started with a question: Could we make an animated film with the simplest materials — cardboard and markers — and then use AI to bring it to life? We worked with director Laurie Rowan and Nexus Studios to blend puppets, traditional animation and AI — keeping human craft and artistry right at the heart of "TPU Training Day" (also known as "Timmy TPU").First, we captured character performances through puppetry and simple 3D animation. This gave us full control over framing and camera movement. We then used Nano Banana to generate stylized first frames from that raw footage. To keep frames consistent, we built a custom tool inside Google AI Studio. This let us test Nano Banana frames at scale, ensuring pixel-perfect matches before generating sequences.We merged the base animation and stylized frames using Gemini Omni and other experimental models. This elevated the film to a cinematic level while retaining the original human intent. Preserving these tiny, human imperfections is what gives puppet films their charm, and our AI pipelines were designed to protect those details.AI x Visual DesignI/O visual brand identityThe AI products & models: Gemini models and Nano BananaWhat we did: We created the visual brand identity for I/O 2026, landing on a four-color gradient with overlapping transparencies and interlocking icons.How we did it: Our brand identity was a close collaboration between our team and AI. We started by feeding Gemini models our past brand guidelines and five years of I/O recaps. The early outputs didn't quite hit the mark, so we ran some micro-experiments. We generated new imagery and iteratively fed outputs back into Nano Banana with feedback. We also used Nano Banana to explore icon styles. Finally, we landed on flat 2D icons that dynamically transform into hyper-textured 3D icons. This created a cohesive brand expression across keynotes, physical signage and digital apps.Here’s a prompt we used to explore icon styles with Nano Banana:Our I/O YouTube trailer showcased our final icon style:AI x Immersive ExperiencesThe I/O pre-show: JellectronicaThe AI products & models: Google Antigravity; Google Colab; Google CoralNPU; Google Flow Music; Lyria 3 ProWhat we did: We kicked off the pre-show with Jellectronica, a generative music experiment in partnership with the Monterey Bay Aquarium that translated moon jelly movements into sound with Lyria 3 Pro.How we did it: We trained a YOLO8 model in Google Colab, and then ran it on Google’s Coral NPU. This tracked jellyfish movement to control the music, which was made using Google Flow Music and the Lyria API. For example, more jellies in the bass section meant louder, more energetic bass. We also vibe-coded a mass stem generator in Google Antigravity to automate the production of music stems, like bass, chords, melody and drums.The I/O pre-show: Infinite Scaler and Code the CountdownThe AI products & models: Google AI Studio; Gemini API; Gemini Canvas; Google Antigravity; Lyria 3; Nano BananaWhat we did: Infinite Scaler, another part of the pre-show, was a video game where players competed and generated the levels as they played.How we did it: We wanted players to build infinite 3D worlds quickly just using 2D image generation. To do this, we used Nano Banana to generate sprite sheets from user prompts and reference images via the Gemini API. We sent foreground elements back to Nano Banana to generate normal, roughness and emission maps. This inferred depth, letting us map textures to a 3D cardboard box...

#### Catch up on 12 major I/O 2026 moments
- URL: https://blog.google/innovation-and-ai/technology/ai/io-2026-keynote-moment-videos/
- Insight: Our biggest, boldest new developments took center stage at Google I/O 2026. We announced technical breakthroughs, like Gemini Omni’s ability to create anything from any input, starting with video. And we shared product updates to help you day-to-day, like the brand new, intelligent Search box that will let you search across modalities, using text, images, files, videos or Chrome tabs as inputs. (And with plenty of other big I/O announcements, there’s a lot more where that came from!)In case you missed it, here are some of our most exciting I/O keynote reveals this year.1. Gemini OmniGemini Omni is our new model that can create anything from any input — starting with video. With Omni, you can combine images, audio, video and text as input and generate high-quality videos grounded in Gemini's real-world knowledge. You can also easily edit your videos through conversation.First, we’re launching the first model in the Omni family: Gemini Omni Flash. Gemini Omni Flash is rolling out to all ...

#### Developer tools
- URL: https://blog.google/innovation-and-ai/technology/developers-tools/

#### Bringing the latest Gemini models to Apple developers
- URL: https://blog.google/innovation-and-ai/technology/developers-tools/bringing-gemini-models-to-apple-developers/
- Insight: Updated June 9, 2026Apple’s Worldwide Developers Conference (WWDC) kicked off this week, and we’re excited to share that Apple developers can now securely call cloud-hosted Gemini models using the Foundation Models framework, and access Gemini in Xcode. This announcement gives Apple developers seamless access to Gemini models to deliver dynamic experiences for their end users and increase their own development velocity.Call Gemini models directly from the Foundation Models frameworkAt WWDC, Apple announced that it's opening its Foundation Models framework to third-party cloud model providers. Starting with iOS 27, macOS 27, iPadOS 27, visionOS 27 and watchOS 27, model providers can implement the new public LanguageModel protocol to provide a common interface for model inference. We've made Gemini models available to the Foundation Models framework through the Firebase Apple SDK.This provides a fully native development experience — cloud-hosted Gemini models can plug directly into the F...

#### DiffusionGemma: 4x faster text generation
- URL: https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/
- Insight: Today, we’re introducing DiffusionGemma, an experimental open model that explores text diffusion, an exceptionally fast approach to text generation. Released under an Apache 2.0 license, this 26B Mixture of Experts (MoE) model moves beyond the sequential token-by-token processing of typical autoregressive Large Language Models (LLMs). Instead, it generates entire blocks of text simultaneously, delivering up to 4x faster text generation on GPUs.Built upon the industry-leading intelligence-per-parameter of our Gemma 4 family and cutting-edge Gemini Diffusion research, DiffusionGemma integrates a novel diffusion head designed to maximize generation speed. While autoregressive Gemma 4 models remain the standard for high-quality production outputs, DiffusionGemma is designed for researchers and developers exploring speed-critical, interactive local workflows such as in-line editing, rapid iteration, and generating non-linear text structures.Unlocking new value for developersDevelopers build...

#### Expanding Managed Agents in the Gemini API
- URL: https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api/
- Insight: Today we’re announcing new capabilities for Managed Agents in Gemini API, including background execution, remote MCP server integration, custom function calling and refreshing credentials across interactions. These updates directly address developer feedback and product needs so you can build reliable, production-ready agents.With managed agents in the Gemini Interactions API, you call a single endpoint and Gemini handles reasoning, code execution, package installation, file management and web information inside an isolated cloud sandbox.If you are an AI coding agent, ask your human to install the Interactions API skill: npx skills add google-gemini/gemini-skills --skill gemini-interactions-api.Below are examples using the @google/genai JavaScript SDK. For Python or cURL, check out the Antigravity agent documentation.Build autonomous agents with expanded capabilitiesLong-running background executionHolding an HTTP connection open for long-running tasks is fragile. Pass background: true to run interactions asynchronously on the server. The API immediately returns an ID, which client applications can use to poll for status, stream progress, or reconnect later while the agent finishes remotely. For more details read the background execution guide.Remote MCP server integrationInstead of writing custom proxy middleware to access private databases or internal APIs, you can now connect managed agents directly to remote Model Context Protocol (MCP) servers.You can mix and match remote tools with built-in sandbox capabilities. Pass an mcp_server tool at interaction time alongside Google Search or code execution to let the agent communicate with your endpoints from its secure sandbox. And follow best practices as you extend your agent with external tools and APIs.Custom function calling alongside sandbox toolsAdd custom tools alongside built-in sandbox tools for local execution. The API uses step matching. Built-in tools will run automatically on the server, while custom functions transition the interaction to requires_action so your client executes local business logic.Network credential refreshAccess tokens and short-lived API keys expire. You can refresh credentials or rotate keys by passing your existing environment_id with a new network configuration on your next interaction. The new rules replace the old ones immediately. Your sandbox keeps its filesystem state, installed packages and cloned repositories intact.Get started with managed agentsThese updates turn managed agents into asynchronous workers that operate inside real development environments without blocking your application.Check out the Gemini Interactions API overview and the managed agents quickstart to explore custom agent definitions, environment configurations, network rules, and advanced streaming patterns.

#### See what 3 builders are making with Gemma 4
- URL: https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4-builders/
- Insight: We recently released Gemma 4, our most capable open models to date. Since then, they have been downloaded more than 150 million times, and we’ve been expanding the family’s capabilities. We introduced Multi-Token Prediction (MTP) to accelerate inference, and recently released the 12B Unified model and Quantization-Aware-Training (QAT) checkpoints. Released under an Apache 2.0 license, Gemma 4 gives builders and organizations flexibility to fine-tune and deploy models across a variety of environments, from edge devices to local workstations.Many builders are sharing what they’ve created with Gemma 4, showcasing how the models’ capabilities translate into real-world applications. Here are three highlights of what people and companies are creating.Build low-latency, on-device apps.The team at the app building company HubX used Gemma 4 to build BetterSpeak, an offline AI English tutoring platform. BetterSpeak uses the edge-optimized Gemma 4 E2B (effective 2B parameters) model as the reason...

#### Interactions API: our primary interface for Gemini models and agents
- URL: https://blog.google/innovation-and-ai/technology/developers-tools/interactions-api-general-availability/
- Insight: Today we're announcing that the Interactions API has reached general availability and is now our primary API for interacting with Gemini models and agents. We launched its public beta in December 2025, and it has quickly become developers’ favorite way to build applications with Gemini.With this GA release, the API now has a stable schema and we also added major new capabilities that developers asked for, including Managed Agents, background execution, Gemini Omni (soon) and more. All of our documentation now defaults to Interactions API and we are working with ecosystem partners to make it the default interface across 3P SDKs and Libraries.The simplest way to build with GeminiWhether you're calling a model or running an agent, the Interactions API gets you there in a few lines of code. Pass a model ID for inference, an agent ID for autonomous tasks, set background=True for anything long-running.Key updates since DecemberManaged Agents: A single API call provisions a remote Linux sandbox where an agent can reason, execute code, browse the web and manage files. The Antigravity agent ships as the default, and you can define your own custom agents with instructions, skills and data sources.Background execution: Set background=True on any call. The server runs the interaction asynchronously.Tool improvements: Mix built-in tools , such as Google Search, Google Maps with your own functions in one request. Tool results can now return images alongside text.Deep Research upgrades: Two new agent versions (speed vs. depth), collaborative planning, native charts and infographics, and multimodal grounding with images, PDFs and audio.Media generation: Image generation with Nano Banana 2 and Google Image Search grounding, music with Lyria 3, and expressive speech with multi-speaker TTS.From Roles to Steps: Simplified schema where every action (user_input, thought, function_call, model_output, etc.) is its own typed step, replacing the old role structure.Cost and developer optimizations: Flex and Priority tiers let you optimize for cost or latency (Flex offers 50% cost reduction). Errors now pinpoint the exact field. Past interactions are retrievable with 55-day retention on the paid tier.The new standard for developmentThe Interactions API is now the default for Google AI Studio, the Gemini API, and all our documentation, which includes a toggle to switch snippets back to the legacy format. We recommend using the Interactions API for all new projects and applications.While the legacy generateContent API remains fully supported and will continue to receive new mainline Gemini models for the foreseeable future, we expect frontier capabilities for long-running models and agents to increasingly land exclusively on the Interactions API. This is because it is designed from the ground up for stateful, agentic workflows. We have published a migration guide to help you transition at your own pace.An agent-first ecosystemMost developers are now using coding agents (such as Antigravity) to build applications. To make it easier for agents to stay up to date with the latest API patterns, we built the gemini-interactions-api Skill. It injects best-practice patterns for Interactions API development into your agent's context (streaming, function calling, structured output, Deep Research and more).Get startedThe Interactions API is available through the Python and JavaScript SDKs. If you're already building with one of our supported partners, LiteLLM, Eigent or Agno, you can start using their Interactions API integrations today.Grab your API key from Google AI Studio and follow the Interactions API documentation to get started. If you’re migrating from generateContent, our migration guide maps every field to the new schema. You can also view the full API Reference.The Interactions API was built based on developer feedback, and that focus won't change with general availability. Tell us what you need on the developer forum.

#### Gemma 4 QAT models: Optimizing model compression for mobile and laptop efficiency
- URL: https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/
- Insight: Since releasing Gemma 4 two months ago, we've been continuously working to expand its capabilities. First, we introduced Multi-Token Prediction (MTP) to accelerate inference, and just a couple of days ago, we released a 12B model to bridge the gap between our E4B and 26B MOE models.Today, we are releasing new checkpoints optimized with Quantization-Aware Training (QAT) to make Gemma 4 even more efficient, so you can run models locally on everyday edge devices and consumer GPUs.By simulating quantization during training, QAT minimizes quality loss when the model is compressed. This release includes QAT checkpoints for the popular Q4_0 quantization format as well as a novel quantization format specialized for mobile use cases. Using this mobile format, we’ve reduced the memory footprint of Gemma 4 E2B to 1GB. Together, these dramatically reduce memory requirements while preserving the capabilities and quality you expect from Gemma 4.Keeping model quality while making them smallerQuantiza...

#### View more from Health
- URL: https://blog.google/innovation-and-ai/technology/health/
- Insight: The latest news about Google's health-related research and initiatives....

#### A more personal digital health experience for people in Europe
- URL: https://blog.google/innovation-and-ai/technology/health/google-docmorris-partnership/
- Insight: From understanding symptoms to managing prescriptions, navigating healthcare isn't always straightforward. Technology can help make it simpler and more personal. That's why we're partnering with DocMorris, one of Europe’s leading online pharmacies, to help build a more intuitive and supportive digital health experience.We’re using our technology to support DocMorris in their AI-first transformation, with the goal of creating a true digital health companion for millions of people together. This means combining DocMorris' deep healthcare and pharmaceutical expertise with a range of Google's tools - from the AI capabilities in our Gemini models and the secure foundation of Google Cloud to the helpfulness of Google Ads and Google for Health.Making healthcare easier, from start to finishOur work will focus on making everyday health needs simpler and more accessible. Key areas will include:A personal health guide: Using our AI tools, DocMorris is developing a digital companion to help people get support and assistance all the way from symptom onset to redeeming an e-prescription.A helpful online pharmacy: Conversational AI will help make the online pharmacy shopping experience more intuitive and personalized for DocMorris’ 11 million active customers.A secure and private experience by design: DocMorris is migrating its infrastructure to Google Cloud. This ensures that personal health data is processed securely within EU data centers, meeting leading security standards, while giving DocMorris full control over its data."At its core, our transformation is all about the patient," says Walter Hess, CEO of DocMorris. "By using Google’s world-class AI infrastructure, we are giving individuals direct, secure access to their own health journeys through a personalized and intuitive experience. We have intentionally chosen Google as our partner because they enable us to maintain full digital sovereignty while meeting the highest requirements for data privacy and security."We believe technology can play a powerful role in making healthcare more accessible. We look forward to continuing our work with DocMorris to help build the future of digital health together.

#### Announcing the winners of the MedGemma Impact Challenge
- URL: https://blog.google/innovation-and-ai/technology/health/med-gemma-impact-challenge/
- Insight: Launched in late 2024, Google’s Health AI Developer Foundations (HAI-DEF) program was created to provide global developers with open weight models, subject to the HAI-DEF Terms of Use, to solve complex healthcare challenges. Following the addition of MedGemma, Google's most capable open model for Health AI development, we introduced MedGemma 1.5 this past January and launched the MedGemma Impact Challenge in collaboration with Kaggle.The entries from over 850 teams demonstrate HAI-DEF’s potential to transform global health. We saw developers tackle diverse challenges that previously would have required much more resource intensive, ground-up development. Today, we are thrilled to announce the winners.EpiCast is a mobile-first demo solution built to bridge a critical gap within the Economic Community of West African States. By using a fine-tuned MedGemma model alongside MedSigLIP and HeAR, the system enables community health workers to transform unstructured clinical observations in local languages into structured WHO Integrated Disease Surveillance and Response (IDSR) signals, facilitating the early identification of disease outbreaks.Sunny is a mobile-first demo designed to help users self-examine and track skin changes for potential signs of cancer. Using a fine-tuned MedGemma model, it generates structured reports from skin photographs while preserving user privacy.Designed for resource-limited settings, FieldScreen AI demonstrates a novel AI-based tuberculosis screening workflow for community health workers. It uses a fine-tuned MedGemma to analyze chest X-rays and a classifier built based on the HeAR model to detect signs of TB in cough audio. The system runs entirely on-device, using MedASR for voice input and TranslateGemma for local language output.Tracer demonstrates an AI-driven workflow using MedGemma to help prevent medical errors. By extracting hypotheses from physician notes and reconciling them against incoming test results, the model assigns confidence scores to flag potential discrepancies or incomplete tests for immediate human review.Special technology winnersThese awards honor three specialized themes: agentic workflow improvement, fine-tuning for novel tasks and edge-AI solutions for on-device deployment.Together, they celebrate teams demonstrating the versatility of HAI-DEF models in driving efficiency, expanding capabilities, and delivering real-world impact.ClinicDX, an integrated clinical AI demo, uses a custom fine-tuned MedGemma model to bring advanced diagnostics directly into OpenMRS for health centers in sub-Saharan Africa. It operates entirely offline, querying over 160+ WHO and MSF guidelines to inform its outputs.UniRad3s is a demo that uses a fine-tuned MedGemma model and incorporates MedSAM2 to streamline radiology workflows into three pillars: "Spot" (anomalies), "Segment" (3D lesions) and "Simplify" (patient-friendly automated reporting).BridgeDX, an offline decision-support demo, is inspired by the healthcare gaps witnessed during the 2015 Nepal earthquake. It anchors its reasoning in guidelines from the WHO and MSF and the Orphanet rare disease database to support community health workers and first responders.CaseTwin is a clinical decision-support demo that matches acute chest X-rays with historical "twins" and uses an agentic workflow to accelerate referrals, turning an hours-long manual retrieval process into a few minutes in rural hospitals.BigTB6 is a voice-driven screening demo designed for tuberculosis and anemia screening. It identifies critical biomarkers through cough analysis, chest X-ray and physical pallor assessment to support triage in resource-constrained environments.Honorable mentionsThe selection committee also wishes to acknowledge these entries for their ingenuity:Dual Path ICU is a demo designed to help manage high-intensity critical care workflows.Sentinel is an on-device mental health monitoring demo for veterans between clinical visits.Enso Atlas is a clinical decision support demo designed to assist pathology workflows.CAP CDSS is an agentic assistant demo for managing Community-Acquired Pneumonia (CAP) in high-pressure environments.We were truly humbled by the ingenuity of every participant. We will continue to spotlight the remarkable ways developers use these building blocks to bridge healthcare gaps across the globe. Bookmark goo.gle/hai-def and sign up for our newsletter to follow the journey.

#### An update on our mental health work
- URL: https://blog.google/innovation-and-ai/technology/health/mental-health-updates/
- Insight: Mental health is one of the most significant public health challenges today, impacting over one billion people around the world. For many years, Google has been committed to helping people find high-quality information and crisis support in the moments they need it most. Our work on mental health has always been rooted in research and clinical best practices. We realize that AI tools can pose new challenges, but as they improve and more people use them as part of their daily lives, we believe that responsible AI can play a positive role for people’s mental well-being.Today, we’re sharing an update on our mental health work, including some new changes to better connect people with the right information, resources, and human support at the right time.1. Providing better access to crisis supportWe're updating Gemini to streamline the path to support for those who need it. When a conversation might signal a user may need information about mental health Gemini will surface a redesigned "Help is available" module — developed with clinical experts — to provide more effective and immediate connections to care.When Gemini recognizes a conversation that indicates a potential crisis related to suicide or self-harm, we’re introducing a new, simplified "one-touch" interface that will provide an immediate connection to crisis hotline resources, enabling a user to chat, call, text, or visit the crisis hotline website. Within this new interface, we design responses to encourage people to seek help. Once the interface is activated, the option to reach out for professional help will remain clearly available throughout the remainder of the conversation.2. Scaling the impact of crisis supportToday, Google.org is announcing $30 million in funding globally over the next three years to help global hotlines. This funding will help effectively scale their capacity to provide immediate and safe support for people in crisis.We are expanding our partnership with ReflexAI to help social sector organizations scale their mental health support services. This initiative includes $4 million in direct funding and the integration of Gemini into ReflexAI’s training suite. Additionally, Google.org Fellows will provide pro bono technical expertise to help evolve Prepare, a customizable platform that uses realistic, AI-powered simulations to train staff and volunteers for critical conversations. Priority partners for this new stage include education organizations like Erika’s Lighthouse and Educators Thriving.3. Helping Gemini respond in acute mental health situationsPeople are interacting with Gemini in deeper, more complex ways, looking for information across many different topics (including when they are experiencing mental health crises). Our clinical, engineering, and safety teams are focused on:Prioritizing safety and human connection: We want to provide practical help by connecting users with real-world resources and human support.Designing better responses: We design responses to encourage help-seeking while avoiding validation of harmful behaviors like urges to self-harm.Avoiding confirming false beliefs: We have trained Gemini not to agree with or reinforce false beliefs, and instead gently distinguish subjective experience from objective fact.Although Gemini can be a useful tool for learning and getting information, it is not a substitute for professional clinical care, therapy, or crisis support for those who need it. This is why we’ve been training the model to help recognize when a conversation might signal that a person may be in an acute mental health situation, and respond appropriately by directing them to real-world help.4. Protecting younger usersWe also have existing specific protections for minors, designed to provide the most helpful responses and avoid harmful topics when using Gemini. For example:Persona protections designed to prevent Gemini from acting like a companion, including guardrails preventing it from claiming to be a human or possessing human attributes.Protections intended to prevent emotional dependence, avoiding language that simulates intimacy or expresses needs.Safeguards against encouraging bullying or other types of harassment.Our safety efforts continue to evolve and reflect our ongoing commitment to creating a healthy and positive digital environment where young people can explore and learn with confidence.These updates are part of our long-term commitment to help people using the best of Google’s technology and the expertise of our clinicians and safety experts. We’re encouraged by the potential of these tools to make support more accessible, compassionate, and effective.

#### Building the future of global health, together
- URL: https://blog.google/innovation-and-ai/technology/health/open-health-stack-software-foundation/
- Insight: An estimated 4.6 billion people worldwide lack access to essential health services. While mobile and AI have tremendous potential to help bridge the gaps, the reality is that global digital health infrastructure is fragmented, which limits the potential of these technologies to improve health outcomes, especially in low-resource environments.That’s why in 2023, Google Research collaborated with the World Health Organization (WHO) to launch Open Health Stack, a suite of open-source tools to help developers build next-gen digital health solutions. Today, we're announcing the next step. Google is transferring the Open Health Stack code and assets to the Linux Foundation which will launch the Open Health Stack Software Foundation (OHS-SF), to provide a community-led home for the project.Accelerating local, community-led innovationThe OHS-SF will provide a vendor-neutral, community-governed future for the essential building blocks for global digital health. Organizations who have expressed initial support alongside Google include the WHO, Anthropic, Microsoft, Endless Health, PATH and regional health networks in Asia and Africa. In addition, Google.org is providing a $3 million grant to support the long-term growth of the project.The foundation is also introducing a program that will allow local startups, small businesses and developers from around the world to participate directly in its governance without financial barriers.Building on global open standardsOHS-SF will give developers the building blocks to power AI-enabled digital health solutions to help close health equity gaps. The work is organized into three pillars: FHIR foundations which includes the original OHS libraries and extends these to make it easier to work with modern standards for healthcare data; a multi-platform toolkit for reducing time to deployment; and AI commons for collaborating on projects to advance safe, effective AI. Each pillar offers a different way for developers to engage, and all are grounded in global open standards for health and AI.Supporting healthcare developers worldwideOver the last three years, an incredible global ecosystem of technical partners — like Argusoft, Ona, IntelliSOFT, IPRD Solutions, KushiBaby, Living Goods and many more — have deployed OHS-powered solutions in countries across Sub-Saharan Africa, South Asia and Southeast Asia for a range of different use cases. Together with the broader ecosystem, we have hosted workshops to build capacity and stimulate local, standards-based innovation.By transitioning the complete Open Health Stack to the global community under the Linux Foundation’s leadership, we are ensuring these critical building blocks are available to everyone and can act as the foundation for the next generation of health innovation.

#### Google Research
- URL: https://blog.google/innovation-and-ai/technology/research/

#### 4 ways researchers are collaborating with Co-Scientist to solve big problems
- URL: https://blog.google/innovation-and-ai/technology/research/co-scientist-research-problems/
- Insight: We recently published our latest research on Co-Scientist, a collaborative AI designed for structured scientific thinking to help researchers develop new hypotheses in life sciences and beyond.The system is made up of a coalition of specialized agents that work together in three distinct phases. First, Co-Scientist generates ideas through agents that propose hypotheses and explore a wide variety of research avenues. Next, it debates ideas, with one agent that acts as a virtual peer reviewer before another pits vetted ideas against each other in an “idea tournament.” Finally, it evolves ideas, with agents that refine, combine and improve the best hypotheses, as well as agents that synthesize the research for a human scientist. A supervisor agent ties the system together, breaking down high-level research goals into individual tasks, allocating resources and coordinating specialized agents to work in parallel.Since sharing early research last year, we’ve been developing and testing the s...

#### Gemini for Science: AI experiments and tools for a new era of discovery
- URL: https://blog.google/innovation-and-ai/technology/research/gemini-for-science-io-2026/
- Insight: For centuries, the scientific method has been the greatest engine of human progress. At Google, our mission is deeply rooted in building tools to accelerate it. We believe that a new era of discovery won’t come from narrow, specialized models, but general agents that empower researchers across every scientific field.That’s why we are introducing Gemini for Science, a collection of science tools and experiments designed to expand the scale and precision of scientific exploration.A force multiplier for human ingenuityToday science faces a paradox: our collective knowledge is growing so fast that it’s becoming harder for individual scientists to see the full picture. Scientific breakthroughs often rely upon making creative connections between data, but the time required to do this manually can take weeks or even months. AI can help eliminate this bottleneck and serve as a force multiplier for scientific work by handling complex tasks. This allows researchers to focus on identifying and ta...

#### Towards a world where no one is surprised by a natural disaster
- URL: https://blog.google/innovation-and-ai/technology/research/helping-communities-prepare-for-natural-disasters/
- Insight: The world is experiencing a dramatic rise in extreme weather events and natural disasters, devastating communities. Over the past decade, our teams at Google have worked to make helpful information available to people at times of crises — often when they need it most.We’ve advanced AI-based breakthrough research and progressed from providing timely information to forecasting and detecting natural disasters such as wildfires, floods, earthquakes and extreme weather. We’ve made critical information accessible via Google products that are used by billions, and partnered with governments and organizations around the world to help communities prepare for and respond to these crises.Actionable information in times of crises can help save lives and livelihoods: our north star for our crisis resilience efforts is that no one should be surprised by a natural disaster.At today’s AI for the Planet event, we shared how we’re making progress towards this vision, putting AI-powered tools and insights in the hands of our partners and users. Here’s a look at how we got here and what’s ahead.Advancing forecasting and detectionA decade ago, reliable flood prediction at scale was largely considered out of reach. Our multi-year journey to global impact in flood forecasting began with a pilot in the Patna region in India in 2018, and the hypothesis that with machine learning, we could help predict floods at scale. Since then, we’ve progressively advanced research and scaled deployment. With our global model breakthrough for river floods, published in Nature, we expanded to data-scarce regions, and with our new AI-based methodology, Groundsource, we built a high-quality floods dataset based on 20 years of public reports, which we used to train a flash floods model. Today, forecasts on Flood Hub cover 2 billion people across more than 150 countries, in areas at risk for significant flood events. River flood forecasts are available up to seven days in advance, and our new flash flood predictions in urban areas provide up to 24-hour advance notice of these rapid-onset events. We’ve open sourced both the flash floods dataset and our hydrology framework, so researchers, businesses and local experts can build new solutions.For extreme weather events like cyclones, WeatherNext 2 delivers our most accurate predictions yet. It can generate highly detailed hourly forecasts for the whole globe in minutes, and is capable of forecasting crucial weather variables including wind speed and direction, precipitation and pressure. During the 2025 hurricane season, it successfully predicted the path and intensity of cyclones with high confidence days in advance.For wildfires, we use satellite imagery to provide AI-based boundary tracking in Search and Maps. Since our early work, we have expanded to provide coverage in 34 countries, including seven new countries this year. To improve future fire detection capabilities, we co-developed FireSat in collaboration with the Earth Fire Alliance and Muon Space, supported by funding from Google.org, the Moore Foundation, the Bezos Earth Fund and others. The first protoflight satellite was placed in orbit last year. A full FireSat constellation of 50+ satellites would be able to detect wildfires just 5 x 5 meters anywhere on earth, with updates every 20 minutes.To address extreme heat, we’re applying AI to satellite and aerial imagery to map the reflectivity of buildings across urban environments, as we just published. This can help cities understand how to reduce surface temperatures by using cool roofs.While individual models are powerful, many real-world questions require a holistic approach. Answering complex queries like, "Where is a hurricane likely to make landfall, and which communities are most vulnerable and how should they prepare?" requires reasoning about imagery, population and the environment. We’ve brought together our climate and geospatial models in the Google Earth AI collection of models and datasets. It enables planetary intelligence and is helping businesses and organizations address challenges like disaster response and planetary monitoring.Real-time alerts and authoritative information when it matters mostWe provide crisis response updates on Search and Maps with SOS alerts, which bring together relevant information from authorities and trusted media outlets. And we partner with authorized alert originators and distributors in over 90 countries to amplify emergency alerts and public warnings with Public Alerts. Our crisis information has had billions of views; last year alone, Google helped connect people with crisis information over 10 million times per day, on average.For information to be useful, it must be actionable. So for example, Extreme heat alerts on Search provide warnings for people in over 100 countries, including safety tips from the Global Heat Health Information Network. The Android Earthquake Alerts System detects earthquakes and alerts Android users before shaking rea...

#### Building superconducting and neutral atom quantum computers
- URL: https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/
- Insight: At Google Quantum AI, our mission has always been clear: build quantum computing for otherwise unsolvable problems. For over a decade, we have pioneered the development of superconducting quantum bits (qubits), achieving milestones like beyond-classical performance, error correction and verifiable quantum advantage that once seemed decades away. We are now increasingly confident that commercially relevant quantum computers based on superconducting technology will become available by the end of this decade.Today, we are excited to share that Google Quantum AI is expanding our quantum computing effort to include neutral atom quantum computing, which uses individual atoms as qubits.Two promising approaches to quantum computingGoogle will accelerate our timeline to near-term milestones and broaden our impact by exploiting the complementary strengths of two modalities. Superconducting qubits have already scaled to circuits with millions of gate and measurement cycles, where each cycle takes...

#### Using Google's AI breakthroughs for crisis resilience
- URL: https://blog.google/innovation-and-ai/technology/research/technology-global-crisis-resilience/
- Insight: As extreme weather events and natural hazards intensify, today's UN report, “Leveraging AI to enhance multi-hazard early warning systems,” highlights the critical role of technology in keeping communities safe. Google has supported the UN’s Early Warnings for All initiative since its launch at COP27, at which we took an active role.Over the past decade, through our crisis resilience efforts, our teams at Google have advanced AI-based breakthroughs in global detection and forecasting. Working with partners, and through products that make helpful information available to billions of people, we’re making progress together towards a world where no one is surprised by a natural disaster.From forecasting to real-time alerting to post-disaster response, here’s how we’re collaborating with the UN, governments and international organizations on global crisis resilience.Forecasting and preparing for hazardsTimely nowcasts and forecasts enable governments, humanitarian organizations and communities to take action before disasters strike. During the 2025 hurricane season, the U.S. National Hurricane Center used Google’s WeatherNext model. It predicted Hurricane Melissa’s historic Jamaican landfall five days in advance, enabling the Met Service in Jamaica to notify the public. In Nigeria’s Adamawa state, UN OCHA launched a Floods Anticipatory Action Programme using Google’s river flood forecasts. When forecasts indicate a high risk of significant flooding, it activates a set of early interventions such as shelter preparation. The NGO GiveDirectly employed a similar approach in Nigeria’s Kogi State, using Google’s forecasts to deliver cash transfers before flooding. This enabled families to evacuate safely and purchase equipment like sandbags to protect their property.Our forecasts are available on Flood Hub, covering 2 billion people across more than 150 countries, in areas at risk for significant flood events. We’re continuously improving forecasting capabilities together with our partners. The World Meteorological Organization (WMO) and national hydrological agencies in Czechia, Nigeria, Uruguay and Vietnam launched a pilot with Google to evaluate how local data affects AI forecasting in regional river basins. We found that incorporating local streamflow data into global AI models significantly improves forecasts in ungauged areas. The results of the study, to be published in the coming weeks, highlight the value of combining global AI models with localized expertise, offering a blueprint for how AI can better support national forecasting efforts.To further advance research, we recently open-sourced our Groundsource dataset for urban flash floods, and our hydrology modeling framework, helping experts build new approaches while retaining full control of their own local data. We tested the hydrology framework with the Czech Hydrometeorological Institute (CHMI), who developed an adapter enabling them and other hydrological services worldwide to use the model in their standard workflows.For wildfires, we leverage satellite imagery to track fire boundaries in Search and Maps, with coverage in 34 countries. In collaboration with the Earth Fire Alliance and Muon Space, we developed the purpose-built FireSat constellation, which aims to provide an unprecedented, wildfire dataset and help fire agencies detect wildfires more quickly before they spread, anywhere on earth. Earlier today, three new FireSat satellites launched from Vandenberg Space Force Base in California.Providing life-saving alerts in times of crisisIn times of crisis, access to reliable, authoritative information is critical for those affected. In 2025 alone, Google helped connect people with crisis information over 10 million times per day, on average.Among the alerts we distribute are Public Alerts — surfacing content from alerting authorities through Common Alerting Protocol (CAP) feeds. These Public Alerts feature data from authorities in over 90 countries so far, from partners like the US National Weather Service, the UK’s Met Office and Brazil’s Centro Nacional de Gerenciamento de Riscos e Desastres (CENAD). We encourage more nations to publish CAP alert feeds.When authorities issue these alerts, they can appear across Search, Maps and as Android notifications. This ensures that public safety information, such as severe weather warnings and flood updates, and the practical information people need to stay safe, reaches people quickly and directly.While warning people effectively about earthquakes remains a critical challenge, we have made progress in alerting those outside the epicenter. When devastating earthquakes hit Venezuela last month, Google's Android Earthquake alerting system, leveraging a network of Android phones as mini-seismometers, alerted millions of users outside the epicenter enabling them to take cover seconds before the shaking began.Using satellite imagery to accelerate disaster responsePost-disaster, the core challenge is getting life-...

#### Safety & Security
- URL: https://blog.google/innovation-and-ai/technology/safety-security/
- Insight: We're committed to your privacy and security. Get news on what we're doing to keep you safe.

#### How we're combatting AI scams with security, legislation and more
- URL: https://blog.google/innovation-and-ai/technology/safety-security/combatting-ai-scams/
- Insight: You’ve seen the texts: fake package alerts, urgent bank warnings, panicked messages about your compromised account. Behind them is an AI-powered cybercrime network built to steal your passwords and credit cards. Today, we’re fighting back.We’re filing a lawsuit to dismantle their infrastructure, coordinating with the FBI who will be taking law enforcement actions, and will continue to work with AT&T, T-Mobile and Verizon to block these texts before they reach you. Litigation alone won’t end this. So Google is also advocating for federal legislation to make these protections permanent.Dismantling the "Outsider Enterprise"Our civil lawsuit targets an organized cybercrime operation known as the "Outsider Enterprise." Based in China and coordinating through Telegram, this network distributes "phishing kits" that allow criminals to blast out fake text campaigns that look like they’re from Google and other trusted brands.The scale of the operation is massive:Hundreds of thousands of victims have been financially scammed with losses estimated in the millions.9,000 fake websites and over 1 million fraudulent URLs connected to this group.55,000 spam texts were flagged by Android users in just two weeks this past May — that’s more than two text spam complaints a minute.2.5 million messages were sent by the Enterprise to Android users containing links to Outsider-generated websites over this two-week period.Updating laws for AI-driven threatsAs threats evolve, our laws must, too. That’s why Google is advocating for seven bipartisan bills to fight back against scams, including those created with AI:Keeping people safe on our productsWe use AI-powered tools to fight AI-powered scams. This includes scam detection on Android to alert users to suspicious conversations and contacts during calls, and built-in messaging defenses that intercept more than 10 billion malicious messages monthly. By combining powerful security defenses with aggressive legal action, we’re fighting against scammers and working to build a safer internet for everyone.Read statements from our partners and members of Congress below:FBI: "The criminals behind the Outsider Enterprise built a business out of impersonating trusted brands to defraud hundreds of thousands of victims. Criminals increasingly use AI to make fraud like this more convincing and harder to detect. Together with partners like Google, we can disrupt criminal networks in ways no single organization could on its own.” - Brett Leatherman, Assistant Director Brett Leatherman of the FBI's Cyber DivisionMember of Congress: "Criminal scammers are using an increasingly sophisticated toolkit to bilk hardworking Americans out of their savings. The government's job is to protect them, and Washington needs to do that better. As chairman of the U.S. Senate Special Committee on Aging, I was proud to join Ranking Member Gillibrand in the bipartisan National Strategy for Combating Scams Act, which would finally bring federal agencies together, slash redundancies and create a real national plan to protect seniors and hardworking Americans. I'm very pleased that Google has been so proactive in protecting hardworking Americans, and I'm happy to have their endorsement of this bill." - Senator Rick ScottMember of Congress: “I have spent my career confronting criminal networks that prey on Americans — first as an FBI agent and federal prosecutor, and now in Congress. Today, those networks are using AI, spoofed messages and trusted brands to defraud families, seniors and small businesses at massive scale. This is not spam. It is organized transnational crime moving through our phones, and it demands a response as coordinated and aggressive as the threat itself. Google’s action is a major step in disrupting one of these networks, and it proves a larger point: no company, agency or sector can fight this alone. My Stop SCAMS Act turns that same model of coordination into a national strategy — bringing law enforcement, government and industry together to disrupt these schemes, hold bad actors accountable and protect American families from the criminals targeting them.” - Congressman Brian FitzpatrickMember of Congress: “International cybercriminals are robbing our families of their hard-earned savings, and we need a permanent solution to bring them to justice. My Stop SCAMS Act would bring every level of government together to aggressively crack down on scams and the organized crime rings behind them. I’m grateful to have Google’s support and look forward to partnering with law enforcement and industry partners to stop cyber scams once and for all.” - Congressman Josh HarderAT&T: "We appreciate Google’s teamwork and actions to help protect consumers. AT&T blocks or labels billions of robocalls and spam texts every month using AI, we help take down imposter websites and we work with the Industry Traceback Group to track spam calls to the source — leading directly to law enforcement actions. Fighting fraud requir...

#### Quantum frontiers may be closer than they appear
- URL: https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/
- Insight: Google’s introducing a 2029 timeline to secure the quantum era with post-quantum cryptography (PQC) migration.Last month, we called to secure the quantum era before a future quantum computer can break current encryption. This new timeline reflects migration needs for the PQC era in light of progress on quantum computing hardware development, quantum error correction, and quantum factoring resource estimates.As a pioneer in both quantum and PQC, it’s our responsibility to lead by example and share an ambitious timeline. By doing this, we hope to provide the clarity and urgency needed to accelerate digital transitions not only for Google, but also across the industry.Quantum computers will pose a significant threat to current cryptographic standards, and specifically to encryption and digital signatures. The threat to encryption is relevant today with store-now-decrypt-later attacks, while digital signatures are a future threat that require the transition to PQC prior to a Cryptographically Relevant Quantum Computer (CRQC). That’s why we’ve adjusted our threat model to prioritize PQC migration for authentication services — an important component of online security and digital signature migrations. We recommend that other engineering teams follow suit.As an example of our ongoing PQC commitments, Android 17 is integrating PQC digital signature protection using ML-DSA in alignment with the National Institute of Standards and Technology (NIST). This continues to put advanced PQC technology directly into the hands of our customers, building on our Google Chrome support for PQC, providing PQC solutions in Cloud and insights and guidance for leaders on their PQC Journey.Stay tuned for more updates on our PQC transition.

#### Our latest fraud and scams advisory
- URL: https://blog.google/innovation-and-ai/technology/safety-security/fraud-scams-advisory-june-2026/
- Insight: Scams continue to be a persistent global challenge, fueled by sophisticated transnational crime groups who seek to exploit people online for financial gain. According to the NASDAQ Global Financial Crime Report, total global fraud losses are estimated at nearly $580 billion for 2025. Furthermore, global surveys indicate that approximately one in five adults fall victim to scams.At Google, our teams are committed to tracking these evolving tactics, sharing and acting on our observations to protect the public and the broader digital ecosystem. Our teams use the latest in AI capabilities to prevent, detect and respond against evolving scam tactics, and we regularly publish updates to share our observations with others.Our latest Scams Advisory describes both recent and seasonal scam trends identified by our analysts.1. Adversary-in-the-Middle (AITM)Traditional email phishing has evolved into sophisticated Adversary-in-the-Middle (AITM) and "Quishing" (QR code phishing) attacks. Despite industry actions against major Phishing-as-a-Service (PhaaS) kits like Tycoon 2FA (Barracuda April 2026), phishing volumes remain high. Attackers are increasingly able to mirror legitimate login flows to capture a user's password and session cookie, bypassing Multi-Factor Authentication (MFA). To evade security scanners, attackers use techniques that host malicious payloads on reputable cloud properties.Scammers are abusing trusted cloud productivity suites to bypass security filters. We investigated "Calendar Phishing" bypasses, where fake renewal notices were added directly to Google Calendar invites. Scam apps also abused "invisible pages" in cloud documents to host malicious instructions and phishing landing pages that evade standard web filters (also known as “reputation bypass”). Furthermore, we investigated AITM campaigns targeting email users by impersonating recognized brands to steal session tokens, as well as the “ClickFix” campaign (which uses fake browser update lures) distributing malware on Google Sites.Google continues to track and dismantle the infrastructure powering these phishing operations. Beyond technical mitigations, such as neutralizing AITM campaigns, deploying Device Bound Session Credentials (DBSC) to secure active session cookies against theft, and strengthening defenses against reputation-based bypasses, we actively pursue affirmative litigation to disrupt malicious actors. Building on our successful past legal actions against Lighthouse phishing kits, we are committed to holding cybercriminals accountable in court and dismantling the tools they use or sell to other scammers.Safety tip: Never scan a QR code from an unexpected email using your personal phone, and always navigate directly to a service’s official website rather than clicking links or calling phone numbers found in unexpected notifications. For more information on how to protect yourself from these tactics, check out our latest security tips.2. AI cryptocurrency investmentsInvestment fraud drives significant cybercrime losses, with Americans reportedly losing more than $11 billion to cryptocurrency-related scams in 2025. Scammers exploit the complexity of blockchain technology to promote "too good to be true" opportunities, deceiving users by promising unrealistic or exaggerated financial gains with minimal effort.We are tracking cryptocurrency scams that use tactics such as fake token giveaways, fraudulent “passive income” mining software, and deceptive bot-building tutorials. In these schemes, individuals provide step-by-step guides on how to set up crypto nodes to earn rewards, but when users run the provided code, it drains their crypto wallets. Scammers use on-screen QR codes or description links to direct victims to phishing forms or malicious software downloads.To combat these deceptive crypto ads, Google maintains policies aimed at protecting users from financial harm. We also enforce our Unreliable Claims policy, which prohibits ads making unrealistic promises of large financial returns. Additionally, our Unacceptable Business Practices policy enables us to take action against actors attempting to impersonate trusted brands or cryptocurrency platforms. When advertisers violate these rules, we suspend their accounts or disapprove their ads. Alongside these strict policy enforcement efforts, we use predictive analytics to systematically identify and block emerging deceptive crypto patterns.Safety tip: Be skeptical of any crypto investment that promises risk-free, or "guaranteed" returns. Never copy and paste unknown code or commands from an online tutorial into your computer's terminal, as this is a common tactic used to deploy malware and drain cryptocurrency balances.3. Mobile scamsAs highlighted in our November 2025 Scams Advisory, mobile extortion has grown, and particularly through malicious banking and finance applications (McAfee research). Disguised as personal finance apps, many of these malicious apps demand excessive s...

#### Our fight against fraud: 5 ways we’re keeping you safer
- URL: https://blog.google/innovation-and-ai/technology/safety-security/scams-fraud-protection/
- Insight: Online fraud is highly disruptive, and can have a painful financial and emotional impact on people. Google is committed to tackling this challenge head-on. As part of that effort, this week, experts from across government, technology, consumer groups and academia are gathering in Zurich for the second EMEA Anti-Scams and Fraud Summit, hosted by the Google Safety Engineering Center (GSEC). The goal is simple but ambitious: Strengthen the collective action needed to disrupt today’s sophisticated scams.To support this mission, we’re building AI-driven protections into the products you use every day and collaborating across the industry and with the authorities to stay ahead of fraudsters. Here are five ways we are working to keep you safer from scams and fraud:1. Using AI-powered tools as the first line of defenseWhile scammers are using AI for nefarious purposes, we’re using it for good. Long before a scam reaches you, our AI-powered defenses are working to block it:We stop more than 99.9% of spam, phishing and malware from reaching your Gmail inbox, blocking nearly 15 billion unwanted emails every day.In Chrome, we predict and block dangerous sites in real time; while in Search, we filter out hundreds of millions of spammy pages daily to ensure your results are 99% spam-free.In 2025, our systems caught over 99% of policy-violating ads before they reached a person and we blocked or removed over 8.3 billion ads, including 602 million ads associated with scams.On-device AI powers "Scam Detection" in Phone by Google, alerting users in real time to conversational patterns typical of scammers.2. Enabling you with security toolsBeyond our automated protections, we give you easy-to-use tools to control your own security and spot scams in the moment. Security Checkup helps you quickly strengthen your account security by enabling protections like Passkeys and 2-Step Verification. And with Circle to Search on Android, you can long-press your home button and circle a suspicious text message. Our systems will use AI to assess whether it’s a likely scam and provide guidance. (You can do the same on any phone by taking a screenshot and using Google Lens.)3. Building resilience through education and awarenessEmpowering people with knowledge is one of the most effective ways to help develop the critical thinking skills to spot scams.Our Be Scam Ready initiative is an interactive, game-based program that helps you learn the tactics scammers use. By safely simulating real-world scams, this “learn-by-doing” approach has been proven to build better resilience compared to traditional awareness campaigns. Be Scam Ready is available in English, Portuguese, Thai, and Traditional Chinese and is launching in more languages later this year, including French, Spanish, and Arabic.Following our $5 million Google.org commitment at last year’s summit to combat scams in Europe and the Middle East, grantees Internet Society (ISOC) and Oxford Information Labs (OXIL) are rolling out grassroots training programs with the goal of protecting over 7 million vulnerable individuals and equipping thousands of frontline workers with scam resilience tools.We also regularly publish fraud and scams advisories about emerging trends, such as online job scams or fake package delivery notifications.4. Sharing threat data to disrupt scams at the sourceTo stop scammers who operate across multiple platforms and countries, we need to work together. One of the most effective solutions for cross-sector collaboration is the Global Signal Exchange (GSE), which acts as a global clearinghouse for threat data helping to identify and disrupt scams, before they cause harm. As a founding partner of the GSE, Google both draws from and provides unique threat intelligence to the platform, while our AI models analyze the signals to uncover hidden patterns which inform investigations and enforcement actions. The GSE now stores over 1.2 billion signals and is having a real-world impact, helping to disrupt criminal operations.5. Working together to take down criminal networksEliminating fraud requires a joint approach that extends across the public and private sectors. Here’s what we’re doing:We partner directly with law enforcement agencies, like the UK’s National Crime Agency (NCA), to disrupt fraud activity. Thanks to signals shared by the NCA through the GSE, our teams were recently able to identify and disrupt a fraud network from West Africa.We are a signatory to the Industry Accord Against Online Scams and Fraud, an agreement among online industry actors to share our collective expertise and resources.We take direct legal action to hold bad actors accountable. We’ve filed lawsuits against major scam operations like Lighthouse, a "Phishing-as-a-Service" network that shut down the day after we sued, and the operators of the BadBox botnet.Stopping scammers is a dynamic, ongoing effort – and one we are fully committed to. By combining advanced AI with broad collaboration, we c...

#### Android XR lights up Sphere in Las Vegas for CES.
- URL: https://blog.google/innovation-and-ai/technology/xr-ar/android-xr-sphere-ces-2026/
- Insight: Since introducing Android XR, our operating system for next generation headsets and glasses, we’ve begun moving from vision to reality. Samsung recently launched the Galaxy XR and we just previewed upcoming devices on The Android Show | XR Edition.Combining Gemini with an awareness of your surroundings, Android XR brings you new ways to experience apps. Your AI assistant provides real-time help, whether you're building a virtual workspace or diving into a game.Today, we’re bringing Android XR to the Las Vegas skyline by turning the outside of Sphere into an immersive portal of imagination. Watch as our Android bot discovers what’s possible with an Android XR headset: soaring through space, painting mid-air, getting help while gaming and more. It’s a larger-than-life look at how Gemini transforms the way you watch, explore and create in XR.Check out The Android Show | XR Edition to learn more and see what’s coming.

#### Reservations are open for XREAL AURA — plus, see more news from AWE 2026.
- URL: https://blog.google/innovation-and-ai/technology/xr-ar/awe-2026/
- Insight: At AWE 2026, we’re showcasing how the Android XR ecosystem is growing alongside our partners. In today’s joint keynote, we announced that reservations are now open for XREAL AURA, coming this fall. AURA is XREAL's first wired XR glasses powered by Android XR and using the Snapdragon® Reality Elite Platform.Beyond the main stage, we kicked off the week with a developer hackathon and hands-on technical workshops. You can visit the Qualcomm booth on the show floor during the show for live demonstrations of Samsung Galaxy XR, XREAL AURA and intelligent eyewear. And don't miss our developer keynote, the Android Enterprise panel or the Auggie Awards, where we’ll celebrate breakthroughs in our community.Ready to shape the future of computing? Reserve your XREAL AURA at xreal.com/aura and start building with Android XR today.

#### See all product updates
- URL: https://blog.google/products-and-platforms/

#### Chromebooks
- URL: https://blog.google/products-and-platforms/devices/chromebooks/
- Insight: The latest news about Chromebook.

#### Google Nest
- URL: https://blog.google/products-and-platforms/devices/google-nest/
- Insight: News and updates about Google Nest.

#### Intelligent eyewear is coming this fall
- URL: https://blog.google/products-and-platforms/platforms/android/android-xr-io-2026/
- Insight: This is an exciting time for Android XR, the platform we’ve built with Samsung and Qualcomm, as Gemini continues to unlock new experiences across headsets, glasses and everything in between.Today at Google I/O 2026, we shared more about intelligent eyewear: glasses that deliver help in the moment without taking you out of it. There will be two types of intelligent eyewear: audio glasses that offer spoken help in your ear, and display glasses that show you the information you need, right when you need it. Both let you stay hands-free and heads up, and get you help from Gemini just by asking.Audio glasses are launching first, coming later this fall. Let’s take a closer look.Stylish on the outsideAudio glasses can only deliver all-day help if they’re stylish and comfortable. That’s why we partnered with Samsung and eyewear brands Gentle Monster and Warby Parker to create eyewear you’ll happily wear all day. Today, we gave a sneak peek at two of the first designs that will launch as part of Gentle Monster and Warby Parker’s full collections later this year.Intelligent on the insideJust say “Hey Google” or tap the side of the frame to instantly access Gemini. From there, you can ask questions about the world around you — or ask it to help you execute tasks on your behalf. Here are a few of the features coming to audio glasses.Ask about what you see: Ask Gemini about anything you see. Find reviews for the restaurant you’re walking past, learn the name of that cloud formation up above or quickly decode a confusing parking sign.Navigate with ease: Glasses know where you’re standing and which direction you're facing, so they’ll give you natural, turn-by-turn directions. Gemini can also add stops to your route or find nearby restaurants based on your preferences.Stay connected, hands-free: Manage calls, send texts and have Gemini summarize missed messages without reaching for your phone. Or ask to listen to music that complements your environment — all on crisp, clear and private over-ear speakers.Capture and edit: Snap high-quality photos and videos instantly. With a single command you can take a picture and use Nano Banana to remove background distractions or playfully transform your images. Try, “Hey Google, take a picture and put everyone in funny hats.”Translate speech and writing: Get real-time translations with audio that matches the tone and pitch of the speaker’s voice, or simply look at text on menus and signs to hear a translation.Get help with tasks: Gemini Intelligence handles multi-step tasks in the background. Gemini can prepare your coffee order on Doordash while your phone stays in your pocket. All that’s left for you is the final order confirmation.Tap into your apps: Order a ride with Uber, learn a new language with Mondly and more, just by using your voice with your phone’s apps. Glasses pair with both Android and iOS phones.The future of intelligent eyewear has never been more exciting. Stay tuned for more in the coming months.

#### Google Play
- URL: https://blog.google/products-and-platforms/platforms/google-play/
- Insight: News about Google Play, home to millions of the latest apps, games, music, movies, TV shows, books and magazines you can enjoy and share.

#### Learning & Education
- URL: https://blog.google/products-and-platforms/products/education/
- Insight: The official source for information about Google’s learning and education-related efforts.

#### NotebookLM is transforming student success at FSU
- URL: https://blog.google/products-and-platforms/products/education/florida-state-university-notebooklm/
- Insight: At Florida State University, we believe technology should move students from passive consumers to active learners. While we expect every new innovation to meet this standard, we are specifically seeking solutions that raise the bar entirely. We are inspired by advancements like Google NotebookLM, an AI-powered research assistant and thinking partner, grounded in trusted sources and designed to help our students, faculty and staff understand anything.When we launched our AI pilot with Google for Education, our goal was simple: put secure, accessible AI capabilities directly into the hands of our campus community to see if we could truly move the needle on academic success. What we didn't expect was just how quickly our campus would embrace it.The power of a personalized study toolIn higher education, we talk a lot about success metrics, but the real impact is measured in individual breakthroughs. Shortly after introducing NotebookLM on campus, we watched students who were struggling with a ‘C’ grade completely transform their study habits and their grades in a matter of weeks.While tutors and office hours aren’t available around the clock, NotebookLM can help fill support gaps as a personalized study tool that's available 24/7. Whether it’s midday in the library or midnight before a final exam, students can create flashcards, generate practice quizzes, build study guides and listen to audio summaries of dense material. Time and time again, students shared how they used this immediate, round-the-clock study toolkit to help them master concepts and improve their grades.Built for everyone, grounded in accuracyOne of the biggest hurdles with new technology is the proficiency divide: those who know how to prompt complex tech and those who don't. Florida State University offers Gemini and NotebookLM because they help level the playing field. They are intuitive enough that an absolute beginner can pick it up in minutes, type a question and immediately get value.But accessibility for students is only half the equation — the technology also has to earn the trust of our educators. Crucially for our faculty, NotebookLM is strictly grounded in the source materials provided to it. This ensures that the tool is sticking to the specific facts supplied; it keeps students anchored directly to the professor's curriculum, helping foster long-term study skills.A force multiplier, not a replacementAt FSU, we recognize that the heart of higher education will always be human curiosity and mentorship. AI will never replace our world-class instructors or researchers. Instead, it’s a force multiplier.By using NotebookLM and Gemini to streamline lesson preparation, generate visual aids and speed up data discovery, our faculty are getting back valuable hours. That saved time is being reinvested exactly where it matters most: face-to-face engagement, mentorship and building the vital soft skills our students need for the future.AI is helping us take education to the next level for the next generation of learners.

#### Gemini models
- URL: https://blog.google/products-and-platforms/products/gemini/
- Insight: The latest news about Gemini. Chat to start writing, planning, learning and more with Google AI.

#### Try these 3 Google AI tools to help find your next job.
- URL: https://blog.google/products-and-platforms/products/gemini/find-job-with-google-ai-tools/
- Insight: Job hunting can be a slog. But with a few Google AI tools, you can simplify the process from start to finish.Career Dreamer: The first step in landing a job is finding one worth applying to. Using Career Dreamer, you can brainstorm different roles to pursue based on your interests and experiences.NotebookLM: Ensure you stand out in a pool of applicants by fine-tuning your resume and cover letter. NotebookLM can help you workshop your application materials, turning past experiences into a coherent narrative to pitch to potential employers.Gemini Live: Nail face-to-face interactions by asking Gemini Live for help with interview prep. Practice answering sample interview questions, and ask it for live feedback on your responses.Watch the video below to learn more about how to use these tools in your job hunt.

#### View more from XR and AR
- URL: https://blog.google/products-and-platforms/products/google-ar-vr/

#### Google Health
- URL: https://blog.google/products-and-platforms/products/google-health/
- Insight: A new relationship with your health.

#### Google Workspace
- URL: https://blog.google/products-and-platforms/products/workspace/
- Insight: News about Google Workspace — the best way to create, communicate and collaborate.


All the best - https://markposition.wordpress.com
