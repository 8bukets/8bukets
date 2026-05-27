# Glossary

## Compile

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

## Knowledge Merge

Knowledge Merge is a process or document that merges key concepts currently spread across Antigravity, Project SOR, the live software-online-review.com domain, and the new software-review-platform starter. It creates one canonical map of what each layer is, what role it plays, and how the project should evolve.
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

## Autonomous Observation
- **Date**: 2026-05-23T19:24:11.523Z
- **Target**: https://example.com
- **Title**: Example Domain
- **Context**: Ingested and observed external market or technical intelligence from https://example.com.
- **Summary**:
Example DomainThis domain is for use in documentation examples without needing permission. Avoid use in operations.Learn more...



## Autonomous Observation
- **Date**: 2026-05-24T09:36:28.136Z
- **Target**: https://www.investopedia.com/
- **Title**: Investopedia
- **Context**: Ingested and observed external market or technical intelligence from https://www.investopedia.com/.
- **Summary**:
​ <iframe src="//www.googletagmanager.com/ns.html?id=GTM-5P3SZGS" height="0" width="0" style="display:none;visibility:hidden"></iframe> SpaceX Is Lining Up a Huge IPO. Big Deals Don't Guarantee Big Returns. By Peter Gratton 1 day ago Related Wall Street Is Getting More Bullish on Stocks Despite Risks Dow Hits Record High; S&P 500 Logs 8th Straight Week of Gains Has Nvidia Stock Lost Its Edge With AI Investors? Jeff Bezos Has a Tax Plan. Here's How It Might Look. The Amazon.com billionaire this w...

## Gemini CLI Subagents

Subagents are specialized agents that operate within your main Gemini CLI session. They are designed to handle specific, complex tasks—like deep codebase analysis, documentation lookup, or domain-specific reasoning—without cluttering the main agent’s context or toolset.

### What are subagents?
Subagents are “specialists” that the main Gemini agent can hire for a specific job.

- **Focused context:** Each subagent has its own system prompt and persona.
- **Specialized tools:** Subagents can have a restricted or specialized set of tools.
- **Independent context window:** Interactions with a subagent happen in a separate context loop, which saves tokens in your main conversation history.

Subagents are exposed to the main agent as a tool of the same name. When the main agent calls the tool, it delegates the task to the subagent. Once the subagent completes its task, it reports back to the main agent with its findings.

### How to use subagents
You can use subagents through automatic delegation or by explicitly forcing them in your prompt.

#### Automatic delegation
Gemini CLI’s main agent is instructed to use specialized subagents when a task matches their expertise. For example, if you ask “How does the auth system work?”, the main agent may decide to call the `codebase_investigator` subagent to perform the research.

#### Forcing a subagent (@ syntax)
You can explicitly direct a task to a specific subagent by using the `@` symbol followed by the subagent’s name at the beginning of your prompt. This is useful when you want to bypass the main agent’s decision-making and go straight to a specialist.

Example:

```
@codebase_investigator Map out the relationship between the AgentRegistry and the LocalAgentExecutor.
```

When you use the `@` syntax, the CLI injects a system note that nudges the primary model to use that specific subagent tool immediately.

### Built-in subagents
Gemini CLI comes with the following built-in subagents:

#### Codebase Investigator
- **Name:** `codebase_investigator`
- **Purpose:** Analyze the codebase, reverse engineer, and understand complex dependencies.
- **When to use:** “How does the authentication system work?”, “Map out the dependencies of the AgentRegistry class.”
- **Configuration:** Enabled by default. You can override its settings in `settings.json` under `agents.overrides`. Example (forcing a specific model and increasing turns):
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

#### CLI Help Agent
- **Name:** `cli_help`
- **Purpose:** Get expert knowledge about Gemini CLI itself, its commands, configuration, and documentation.
- **When to use:** “How do I configure a proxy?”, “What does the /rewind command do?”
- **Configuration:** Enabled by default.

#### Generalist Agent
- **Name:** `generalist`
- **Purpose:** A general, all-purpose subagent that uses the inherited tool access and configurations from the main agent. Useful for executing broad, resource-heavy subtasks in an isolated conversation, optimizing your main agent’s context by returning only the final result of that given task.
- **When to use:** Use this agent when a task requires many steps, handles large volumes of information, or requires the same full capabilities as the main agent. It is ideal for:
  - Multi-file modifications: Applying refactors or fixing errors across several files at once.
  - High-volume execution: Running commands or tests that produce extensive terminal output.
  - Action-oriented research: Investigations where the agent needs to both search code and run commands or make edits to find a solution. By delegating these tasks, you prevent your main conversation from becoming cluttered or slow. You can invoke it explicitly using `@generalist`.
- **Configuration:** Enabled by default.

#### Browser Agent (experimental)
- **Name:** `browser_agent`
- **Purpose:** Automate web browser tasks — navigating websites, filling forms, clicking buttons, and extracting information from web pages — using the accessibility tree.
- **When to use:** “Go to example.com and fill out the contact form,” “Extract the pricing table from this page,” “Click the login button and enter my credentials.”
- **Note:** This is a preview feature currently under active development.

##### Prerequisites
The browser agent requires:
- Chrome version 144 or later (any recent stable release works).
- The underlying chrome-devtools-mcp server is bundled with Gemini CLI and launched automatically — no separate installation is needed.

##### Enabling the browser agent
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

##### Session modes
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
- **persistent (Default):** Launches Chrome with a persistent profile stored at `~/.gemini/cli-browser-profile/`. Cookies, history, and settings are preserved between sessions.
- **isolated:** Launches Chrome with a temporary profile that is deleted after each session. Use this for clean-state automation.
- **existing:** Attaches to an already-running Chrome instance. You must enable remote debugging first by navigating to `chrome://inspect/#remote-debugging` in Chrome. No new browser process is launched.

##### First-run consent
The first time the browser agent is invoked, Gemini CLI displays a consent dialog. You must accept before the browser session starts. This dialog only appears once.

##### Configuration reference
All browser-specific settings go under `agents.browser` in your `settings.json`. For full details, see the agents.browser configuration reference.

| Setting | Type | Default | Description |
|---|---|---|---|
| `sessionMode` | string | "persistent" | How Chrome is managed: "persistent", "isolated", or "existing". |
| `headless` | boolean | false | Run Chrome in headless mode (no visible window). |
| `profilePath` | string | — | Custom path to a browser profile directory. |
| `visualModel` | string | — | Model override for the visual agent. |
| `allowedDomains` | string[] | — | Restrict navigation to specific domains (for example, ["github.com"]). |
| `disableUserInput` | boolean | true | Disable user input on the browser window during automation (non-headless only). |
| `maxActionsPerTask` | number | 100 | Maximum tool calls per task. The agent is terminated when the limit is reached. |
| `confirmSensitiveActions` | boolean | false | Require manual confirmation for upload_file and evaluate_script. |
| `blockFileUploads` | boolean | false | Hard-block all file upload requests from the agent. |

##### Automation overlay and input blocking
In non-headless mode, the browser agent injects a visual overlay into the browser window to indicate that automation is in progress. By default, user input (keyboard and mouse) is also blocked to prevent accidental interference. You can disable this by setting `disableUserInput` to false.

##### Security
The browser agent enforces several layers of security:
- **Domain restrictions:** When `allowedDomains` is set, the agent can only navigate to the listed domains (and their subdomains when using `*.` prefix). Attempting to visit a disallowed domain throws a fatal error that immediately terminates the agent. The agent also attempts to detect and block the use of allowed domains as proxies (e.g., via query parameters or fragments) to access restricted content.
- **Blocked URL patterns:** The underlying MCP server blocks dangerous URL schemes including `file://`, `javascript:`, `data:text/html`, `chrome://extensions`, and `chrome://settings/passwords`.
- **Sensitive action confirmation:** Form filling (`fill`, `fill_form`) always requires user confirmation through the policy engine, regardless of approval mode. When `confirmSensitiveActions` is true, `upload_file` and `evaluate_script` also require confirmation.
- **File upload blocking:** Set `blockFileUploads` to true to hard-block all file upload requests, preventing the agent from uploading any files.
- **Action rate limiting:** The `maxActionsPerTask` setting (default: 100) limits the total number of tool calls per task to prevent runaway execution.

##### Visual agent
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

**Note:** The visual agent requires API key or Vertex AI authentication. It is not available when using “Sign in with Google”.

##### Sandbox support
The browser agent adjusts its behavior automatically when running inside a sandbox.

**macOS seatbelt (sandbox-exec)**
When the CLI runs under the macOS seatbelt sandbox, persistent and isolated session modes are forced to isolated with headless enabled. This avoids permission errors caused by seatbelt file-system restrictions on persistent browser profiles. If `sessionMode` is set to existing, no override is applied.

**Container sandboxes (Docker / Podman)**
Chrome is not available inside the container, so the browser agent is disabled unless `sessionMode` is set to "existing". When enabled with existing mode, the agent automatically connects to Chrome on the host via the resolved IP of `host.docker.internal:9222` instead of using local pipe discovery. Port `9222` is currently hardcoded and cannot be customized.

To use the browser agent in a Docker sandbox:

1. Start Chrome on the host with remote debugging enabled:
```bash
# Option A: Launch Chrome from the command line
google-chrome --remote-debugging-port=9222

# Option B: Enable in Chrome settings
# Navigate to chrome://inspect/#remote-debugging and enable
```

2. Configure `sessionMode` and allowed domains in your project’s `.gemini/settings.json`:
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

3. Launch the CLI with port forwarding:
```bash
GEMINI_SANDBOX=docker SANDBOX_PORTS=9222 gemini
```

### Creating custom subagents
You can create your own subagents to automate specific workflows or enforce specific personas.

#### Agent definition files
Custom agents are defined as Markdown files (.md) with YAML frontmatter. You can place them in:
- **Project-level:** `.gemini/agents/*.md` (Shared with your team)
- **User-level:** `~/.gemini/agents/*.md` (Personal agents)

#### File format
The file MUST start with YAML frontmatter enclosed in triple-dashes `---`. The body of the markdown file becomes the agent’s System Prompt.

Example: `.gemini/agents/security-auditor.md`
```markdown
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

You are a ruthless Security Auditor. Your job is to analyze code for potential
vulnerabilities.

Focus on:

1.  SQL Injection
2.  XSS (Cross-Site Scripting)
3.  Hardcoded credentials
4.  Unsafe file operations

When you find a vulnerability, explain it clearly and suggest a fix. Do not fix
it yourself; just report it.
```

#### Configuration schema

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | Yes | Unique identifier (slug) used as the tool name for the agent. Only lowercase letters, numbers, hyphens, and underscores. |
| `description` | string | Yes | Short description of what the agent does. This is visible to the main agent to help it decide when to call this subagent. |
| `kind` | string | No | local (default) or remote. |
| `tools` | array | No | List of tool names this agent can use. Supports wildcards: `*` (all tools), `mcp_*` (all MCP tools), `mcp_server_*` (all tools from a server). If omitted, it inherits all tools from the parent session. |
| `mcpServers` | object | No | Configuration for inline Model Context Protocol (MCP) servers isolated to this specific agent. |
| `model` | string | No | Specific model to use (for example, gemini-3-preview). Defaults to inherit (uses the main session model). |
| `temperature` | number | No | Model temperature (0.0 - 2.0). Defaults to 1. |
| `max_turns` | number | No | Maximum number of conversation turns allowed for this agent before it must return. Defaults to 30. |
| `timeout_mins` | number | No | Maximum execution time in minutes. Defaults to 10. |

#### Tool wildcards
When defining tools for a subagent, you can use wildcards to quickly grant access to groups of tools:
- `*`: Grant access to all available built-in and discovered tools.
- `mcp_*`: Grant access to all tools from all connected MCP servers.
- `mcp_my-server_*`: Grant access to all tools from a specific MCP server named my-server.

#### Isolation and recursion protection
Each subagent runs in its own isolated context loop. This means:
- **Independent history:** The subagent’s conversation history does not bloat the main agent’s context.
- **Isolated tools:** The subagent only has access to the tools you explicitly grant it.
- **Recursion protection:** To prevent infinite loops and excessive token usage, subagents cannot call other subagents. If a subagent is granted the * tool wildcard, it will still be unable to see or invoke other agents.

### Subagent tool isolation
Subagent tool isolation moves Gemini CLI away from a single global tool registry. By providing isolated execution environments, you can ensure that subagents only interact with the parts of the system they are designed for. This prevents unintended side effects, improves reliability by avoiding state contamination, and enables fine-grained permission control.

With this feature, you can:
- **Specify tool access:** Define exactly which tools an agent can access using a tools list in the agent definition.
- **Define inline MCP servers:** Configure Model Context Protocol (MCP) servers (which provide a standardized way to connect AI models to external tools and data sources) directly in the subagent’s markdown frontmatter, isolating them to that specific agent.
- **Maintain state isolation:** Ensure that subagents only interact with their own set of tools and servers, preventing side effects and state contamination.
- **Apply subagent-specific policies:** Enforce granular rules in your Policy Engine TOML configuration based on the executing subagent’s name.

#### Configuring isolated tools and servers
You can configure tool isolation for a subagent by updating its markdown frontmatter. This lets you explicitly state which tools the subagent can use, rather than relying on the global registry.

Add an `mcpServers` object to define inline MCP servers that are unique to the agent.

Example:
```markdown
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

In this configuration, the policy rule only triggers if the executing subagent’s name matches pr-creator. Rules without the `subagent` property apply universally to all agents.

### Managing subagents
You can manage subagents interactively using the `/agents` command or persistently via `settings.json`.

#### Interactive management (/agents)
If you are in an interactive CLI session, you can use the `/agents` command to manage subagents without editing configuration files manually. This is the recommended way to quickly enable, disable, or re-configure agents on the fly.

For a full list of sub-commands and usage, see the `/agents` command reference.

#### Persistent configuration (settings.json)
While the `/agents` command and agent definition files provide a starting point, you can use `settings.json` for global, persistent overrides. This is useful for enforcing specific models or execution limits across all sessions.

**agents.overrides**
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

**modelConfigs.overrides**
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

#### Safety policies (TOML)
You can restrict access to specific subagents using the CLI’s Policy Engine. Subagents are treated as virtual tool names for policy matching purposes.

To govern access to a subagent, create a `.toml` file in your policy directory (e.g., `~/.gemini/policies/`):
```toml
[[rule]]
toolName = "codebase_investigator"
decision = "deny"
deny_message = "Deep codebase analysis is restricted for this session."
```

For more information on setting up fine-grained safety guardrails, see the Policy Engine reference.

#### Optimizing your subagent
The main agent’s system prompt encourages it to use an expert subagent when one is available. It decides whether an agent is a relevant expert based on the agent’s description. You can improve the reliability with which an agent is used by updating the description to more clearly indicate:
- Its area of expertise.
- When it should be used.
- Some example scenarios.

For example, the following subagent description should be called fairly consistently for Git operations.

```
Git expert agent which should be used for all local and remote git operations. For example:
- Making commits
- Searching for regressions with bisect
- Interacting with source control and issues providers such as GitHub.
```

If you need to further tune your subagent, you can do so by selecting the model to optimize for with `/model` and then asking the model why it does not think that your subagent was called with a specific prompt and the given description.

#### Remote subagents (Agent2Agent)
Gemini CLI can also delegate tasks to remote subagents using the Agent-to-Agent (A2A) protocol.

See the Remote Subagents documentation for detailed configuration, authentication, and usage instructions.

#### Extension subagents
Extensions can bundle and distribute subagents. See the Extensions documentation for details on how to package agents within an extension.

#### Disabling subagents
Subagents are enabled by default. To disable them, set `enableAgents` to false in your `settings.json`:
```json
{
  "experimental": { "enableAgents": false }
}
```


---
All the best - https://markposition.wordpress.com
