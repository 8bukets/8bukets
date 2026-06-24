# AI Agents Knowledge base

### Benefits of using AI agents

- **Efficiency and productivity**: Increased output through simultaneous execution and repetitive task automation.
- **Improved decision-making**: Robust reasoning through collaboration and adaptable strategies.
- **Enhanced capabilities**: Complex problem-solving by combining agent strengths and natural language communication.
- **Social interaction and simulation**: Emergent social behaviors and realistic simulations.

---

### Challenges with using AI agents

- **Empathy**: Struggle with deep emotional intelligence and nuanced social dynamics (e.g., therapy, conflict resolution).
- **Ethical Stakes**: Lack a moral compass for high-stakes decisions (e.g., law enforcement, judicial decision-making).
- **Physical Environments**: Difficulty adapting to unpredictable physical tasks requiring complex motor skills (e.g., surgery, disaster response).
- **Resource Intensity**: Computationally expensive to develop and deploy at scale.

---

### Code agents

Code agents accelerate software development with AI-enabled code generation and coding assistance, and to ramp up on new languages and code bases. Many organizations are seeing significant gains in productivity, leading to faster deployment and cleaner, clearer code.

---

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

---

### Creative agents

Creative agents supercharge the design and creative process by generating content, images, and ideas, assisting with design, writing, personalization, and campaigns.

---

### Customer agents

Customer agents deliver personalized customer experiences by understanding customer needs, answering questions, resolving customer issues, or recommending the right products and services. They work seamlessly across multiple channels including the web, mobile, or point of sale, and can be integrated into product experiences with voice or video.

---

### Data agents

Data agents are built for complex data analysis. They have the potential to find and act on meaningful insights from data, all while ensuring the factual integrity of their results.

---

### Deploying AI agents with Cloud Run

Cloud Run is a serverless platform ideal for deploying scalable AI agents:

- **Scalability**: Auto-scales container instances and can scale to zero when idle to minimize costs.
- **Orchestration**: Core agent logic runs as a service providing stable HTTPS endpoints for API access.
- **A2A Integration**: Frameworks like the Agent Development Kit (ADK) are designed to integrate seamlessly with Cloud Run.

---

### Docker MCP Catalog

The Docker MCP Catalog is a curated collection of verified MCP servers, packaged as Docker images and distributed through Docker Hub. It solves common challenges with running MCP servers locally: environment conflicts, setup complexity, and security concerns.

The catalog serves as the source of available MCP servers. When you add servers to your profiles, you select them from the catalog. Each server runs as an isolated container, making it portable and consistent across different environments.

Note
E2B sandboxes now include direct access to the Docker MCP Catalog, giving developers access to over 200 tools and services to seamlessly build and run AI agents. For more information, see E2B Sandboxes.

What's in the catalog
The Docker MCP Catalog includes:

Verified servers: All servers are versioned with full provenance and SBOM metadata
Partner tools: Servers from New Relic, Stripe, Grafana, and other trusted partners
Docker-built servers: Locally-running servers built and digitally signed by Docker for enhanced security
Remote services: Cloud-hosted servers that connect to external services like GitHub, Notion, and Linear
Local versus remote servers
The catalog contains two types of servers based on where they run:

Local servers run as containers on your machine. They work offline once downloaded and offer predictable performance and complete data privacy. Docker builds and signs all local servers in the catalog.

Remote servers run on the provider's infrastructure and connect to external services. Many remote servers use OAuth authentication, which the MCP Toolkit handles automatically through your browser.

Browse the catalog
Browse available MCP servers at hub.docker.com/mcp or directly in Docker Desktop:

In Docker Desktop, select MCP Toolkit.
Select the Catalog tab to browse available servers.
Select a server to view its description, tools, and configuration options.
Add servers to a profile
To add a server from the catalog to a profile:

In the Catalog tab, select the checkbox next to a server.
Choose the profile to add it to from the drop-down.
For step-by-step instructions and client connection, see Get started with MCP Toolkit or MCP Profiles.

Custom catalogs
Custom catalogs let you curate focused collections of servers for your team or organization. Instead of exposing all 300+ servers in the Docker catalog, you define exactly which servers are available.

Common use cases:

Restrict which servers your organization approves for use
Add your organization's private MCP servers alongside public ones
Control which server versions your team uses
Define the server set available to AI agents using Dynamic MCP
Custom catalogs with Dynamic MCP
Custom catalogs work particularly well with Dynamic MCP, where agents discover and add MCP servers on-demand during conversations. When you run the gateway with a custom catalog, the mcp-find tool searches only within that catalog. If your catalog contains 20 servers instead of 300+, agents work within that focused set, discovering and enabling tools as needed without manual configuration each time.

Import a custom catalog
If someone on your team has created and published a catalog, you can import it using its OCI registry reference.

In Docker Desktop:

Select MCP Toolkit and select the Catalog tab.
Select Import catalog.
Enter the OCI reference for the catalog (for example, registry.example.com/mcp/team-catalog:latest).
Select Import.
Using the CLI:

docker mcp catalog pull <oci-reference>
Once imported, the catalog appears alongside the Docker catalog and you can add its servers to your profiles.

Create and manage custom catalogs
Creating and managing custom catalogs requires the CLI. See Custom catalogs in the CLI how-to for step-by-step instructions, including:

Curating a subset of the Docker catalog
Adding private servers to a catalog
Building a focused catalog from scratch
Pushing a catalog to a registry for your team to import
Contribute an MCP server to the catalog
The MCP server registry is available at https://github.com/docker/mcp-registry. To submit an MCP server, follow the contributing guidelines.

When your pull request is reviewed and approved, your MCP server is available within 24 hours on:

Docker Desktop's MCP Toolkit feature.
The Docker MCP Catalog.
The Docker Hub mcp namespace (for MCP servers built by Docker).

---

### Employee agents

Employee agents boost productivity by streamlining processes, managing repetitive tasks, answering employee questions, as well as editing and translating critical content and communications.

---

### Gemini CLI Remote Subagents

# Remote Subagents

Gemini CLI supports connecting to remote subagents using the Agent-to-Agent (A2A) protocol. This allows Gemini CLI to interact with other agents, expanding its capabilities by delegating tasks to remote services.

Gemini CLI can connect to any compliant A2A agent. You can find samples of A2A agents in the following repositories:

* ADK Samples (Python)
* ADK Python Contributing Samples

## Proxy support
Gemini CLI routes traffic to remote agents through an HTTP/HTTPS proxy if one is configured. It uses the `general.proxy` setting in your `settings.json` file or standard environment variables (`HTTP_PROXY`, `HTTPS_PROXY`).

```json
{
  "general": {
    "proxy": "http://my-proxy:8080"
  }
}
```

## Defining remote subagents
Remote subagents are defined as Markdown files (`.md`) with YAML frontmatter. You can place them in:

* Project-level: `.gemini/agents/*.md` (Shared with your team)
* User-level: `~/.gemini/agents/*.md` (Personal agents)

### Configuration schema

| Field | Type | Required | Description |
|---|---|---|---|
| `kind` | string | Yes | Must be `remote`. |
| `name` | string | Yes | A unique name for the agent. Must be a valid slug (lowercase letters, numbers, hyphens, and underscores only). |
| `agent_card_url` | string | Yes* | The URL to the agent’s A2A card endpoint. Required if `agent_card_json` is not provided. |
| `agent_card_json` | string | Yes* | The inline JSON string of the agent’s A2A card. Required if `agent_card_url` is not provided. |
| `auth` | object | No | Authentication configuration. See Authentication. |

### Single-subagent example

```yaml
---
kind: remote
name: my-remote-agent
agent_card_url: https://example.com/agent-card
---
```

### Multi-subagent example
The loader explicitly supports multiple remote subagents defined in a single Markdown file.

```yaml
---
- kind: remote
  name: remote-1
  agent_card_url: https://example.com/1
- kind: remote
  name: remote-2
  agent_card_url: https://example.com/2
---
```

> **Note**
> Mixed local and remote agents, or multiple local agents, are not supported in a single file; the list format is currently remote-only.

### Inline Agent Card JSON
View formatting options for JSON strings

## Authentication
Many remote agents require authentication. Gemini CLI supports several authentication methods aligned with the A2A security specification. Add an `auth` block to your agent’s frontmatter to configure credentials.

### Supported auth types
Gemini CLI supports the following authentication types:

| Type | Description |
|---|---|
| `apiKey` | Send a static API key as an HTTP header. |
| `http` | HTTP authentication (Bearer token, Basic credentials, or any IANA-registered scheme). |
| `google-credentials` | Google Application Default Credentials (ADC). Automatically selects access or identity tokens. |
| `oauth` | OAuth 2.0 Authorization Code flow with PKCE. Opens a browser for interactive sign-in. |

### Dynamic values
For `apiKey` and `http` auth types, secret values (key, token, username, password, value) support dynamic resolution:

| Format | Description | Example |
|---|---|---|
| `$ENV_VAR` | Read from an environment variable. | `$MY_API_KEY` |
| `!command` | Execute a shell command and use the trimmed output. | `!gcloud auth print-token` |
| `literal` | Use the string as-is. | `sk-abc123` |
| `$$` / `!!` | Escape prefix. `$$FOO` becomes the literal `$FOO`. | `$$NOT_AN_ENV_VAR` |

> Security tip: Prefer `$ENV_VAR` or `!command` over embedding secrets directly in agent files, especially for project-level agents checked into version control.

### API key (`apiKey`)
Sends an API key as an HTTP header on every request.

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | string | Yes | Must be `apiKey`. |
| `key` | string | Yes | The API key value. Supports dynamic values. |
| `name` | string | No | Header name to send the key in. Default: `X-API-Key`. |

```yaml
---
kind: remote
name: my-agent
agent_card_url: https://example.com/agent-card
auth:
  type: apiKey
  key: $MY_API_KEY
---
```

### HTTP authentication (`http`)
Supports Bearer tokens, Basic auth, and arbitrary IANA-registered HTTP authentication schemes.

#### Bearer token
Use the following fields to configure a Bearer token:

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | string | Yes | Must be `http`. |
| `scheme` | string | Yes | Must be `Bearer`. |
| `token` | string | Yes | The bearer token. Supports dynamic values. |

```yaml
auth:
  type: http
  scheme: Bearer
  token: $MY_BEARER_TOKEN
```

#### Basic authentication
Use the following fields to configure Basic authentication:

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | string | Yes | Must be `http`. |
| `scheme` | string | Yes | Must be `Basic`. |
| `username` | string | Yes | The username. Supports dynamic values. |
| `password` | string | Yes | The password. Supports dynamic values. |

```yaml
auth:
  type: http
  scheme: Basic
  username: $MY_USERNAME
  password: $MY_PASSWORD
```

#### Raw scheme
For any other IANA-registered scheme (for example, Digest, HOBA), provide the raw authorization value.

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | string | Yes | Must be `http`. |
| `scheme` | string | Yes | The scheme name (for example, Digest). |
| `value` | string | Yes | Raw value sent as `Authorization: <scheme> <value>`. Supports dynamic values. |

```yaml
auth:
  type: http
  scheme: Digest
  value: $MY_DIGEST_VALUE
```

### Google Application Default Credentials (`google-credentials`)
Uses Google Application Default Credentials (ADC) to authenticate with Google Cloud services and Cloud Run endpoints. This is the recommended auth method for agents hosted on Google Cloud infrastructure.

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | string | Yes | Must be `google-credentials`. |
| `scopes` | string[] | No | OAuth scopes. Defaults to `https://www.googleapis.com/auth/cloud-platform`. |

```yaml
---
kind: remote
name: my-gcp-agent
agent_card_url: https://my-agent-xyz.run.app/.well-known/agent.json
auth:
  type: google-credentials
---
```

#### How token selection works
The provider automatically selects the correct token type based on the agent’s host:

| Host pattern | Token type | Use case |
|---|---|---|
| `*.googleapis.com` | Access token | Google APIs (Agent Engine, Vertex AI, etc.) |
| `*.run.app` | Identity token | Cloud Run services |

Access tokens authorize API calls to Google services. They are scoped (default: `cloud-platform`) and fetched via `GoogleAuth.getClient()`.
Identity tokens prove the caller’s identity to a service that validates the token’s audience. The audience is set to the target host. These are fetched via `GoogleAuth.getIdTokenClient()`.
Both token types are cached and automatically refreshed before expiry.

#### Setup
`google-credentials` relies on ADC, which means your environment must have credentials configured. Common setups:

* Local development: Run `gcloud auth application-default login` to authenticate with your Google account.
* CI / Cloud environments: Use a service account. Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your service account key file, or use workload identity on GKE / Cloud Run.

#### Allowed hosts
For security, `google-credentials` only sends tokens to known Google-owned hosts:

* `*.googleapis.com`
* `*.run.app`

Requests to any other host will be rejected with an error. If your agent is hosted on a different domain, use one of the other auth types (`apiKey`, `http`, or `oauth`).

#### Examples
The following examples demonstrate how to configure Google Application Default Credentials.

Cloud Run agent:

```yaml
---
kind: remote
name: cloud-run-agent
agent_card_url: https://my-agent-xyz.run.app/.well-known/agent.json
auth:
  type: google-credentials
---
```

Google API with custom scopes:

```yaml
---
kind: remote
name: vertex-agent
agent_card_url: https://us-central1-aiplatform.googleapis.com/.well-known/agent.json
auth:
  type: google-credentials
  scopes:
    - https://www.googleapis.com/auth/cloud-platform
    - https://www.googleapis.com/auth/compute
---
```

### OAuth 2.0 (`oauth`)
Performs an interactive OAuth 2.0 Authorization Code flow with PKCE. On first use, Gemini CLI opens your browser for sign-in and persists the resulting tokens for subsequent requests.

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | string | Yes | Must be `oauth`. |
| `client_id` | string | Yes* | OAuth client ID. Required for interactive auth. |
| `client_secret` | string | No* | OAuth client secret. Required by most authorization servers (confidential clients). Can be omitted for public clients that don’t require a secret. |
| `scopes` | string[] | No | Requested scopes. Can also be discovered from the agent card. |
| `authorization_url` | string | No | Authorization endpoint. Discovered from the agent card if omitted. |
| `token_url` | string | No | Token endpoint. Discovered from the agent card if omitted. |

```yaml
---
kind: remote
name: oauth-agent
agent_card_url: https://example.com/.well-known/agent.json
auth:
  type: oauth
  client_id: my-client-id.apps.example.com
---
```

If the agent card advertises an `oauth2` security scheme with `authorizationCode` flow, the `authorization_url`, `token_url`, and `scopes` are automatically discovered. You only need to provide `client_id` (and `client_secret` if required).

Tokens are persisted to disk and refreshed automatically when they expire.

### Auth validation
When Gemini CLI loads a remote agent, it validates your auth configuration against the agent card’s declared `securitySchemes`. If the agent requires authentication that you haven’t configured, you’ll see an error describing what’s needed.

`google-credentials` is treated as compatible with `http` Bearer security schemes, since it produces Bearer tokens.

### Auth retry behavior
All auth providers automatically retry on 401 and 403 responses by re-fetching credentials (up to 2 retries). This handles cases like expired tokens or rotated credentials. For `apiKey` with `!command` values, the command is re-executed on retry to fetch a fresh key.

### Agent card fetching and auth
When connecting to a remote agent, Gemini CLI first fetches the agent card without authentication. If the card endpoint returns a 401 or 403, it retries the fetch with the configured auth headers. This lets agents have publicly accessible cards while protecting their task endpoints, or to protect both behind auth.

## Managing Subagents
Users can manage subagents using the following commands within Gemini CLI:

* `/agents list`: Displays all available local and remote subagents.
* `/agents reload`: Reloads the agent registry. Use this after adding or modifying agent definition files.
* `/agents enable <agent_name>`: Enables a specific subagent.
* `/agents disable <agent_name>`: Disables a specific subagent.

> **Tip**
> You can use the `@cli_help` agent within Gemini CLI for assistance with configuring subagents.

### Disabling remote agents
Remote subagents are enabled by default. To disable them, set `enableAgents` to `false` in your `settings.json`:

```json
{
  "experimental": {
    "enableAgents": false
  }
}
```

---

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
> This is a preview feature currently under active development.

#### Prerequisites
The browser agent requires:

*   **Chrome version 144 or later** (any recent stable release works).
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
| `sessionMode` | `string` | `"persistent"` | How Chrome is managed: `"persistent"`, `"isolated"`, or `"existing"`. |
| `headless` | `boolean` | `false` | Run Chrome in headless mode (no visible window). |
| `profilePath` | `string` | — | Custom path to a browser profile directory. |
| `visualModel` | `string` | — | Model override for the visual agent. |
| `allowedDomains` | `string[]` | — | Restrict navigation to specific domains (for example, `["github.com"]`). |
| `disableUserInput` | `boolean` | `true` | Disable user input on the browser window during automation (non-headless only). |
| `maxActionsPerTask` | `number` | `100` | Maximum tool calls per task. The agent is terminated when the limit is reached. |
| `confirmSensitiveActions` | `boolean` | `false` | Require manual confirmation for `upload_file` and `evaluate_script`. |
| `blockFileUploads` | `boolean` | `false` | Hard-block all file upload requests from the agent. |

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
> The visual agent requires API key or Vertex AI authentication. It is not available when using “Sign in with Google”.

#### Sandbox support
The browser agent adjusts its behavior automatically when running inside a sandbox.

**macOS seatbelt (sandbox-exec)**
When the CLI runs under the macOS seatbelt sandbox, `persistent` and `isolated` session modes are forced to `isolated` with headless enabled. This avoids permission errors caused by seatbelt file-system restrictions on persistent browser profiles. If `sessionMode` is set to `existing`, no override is applied.

**Container sandboxes (Docker / Podman)**
Chrome is not available inside the container, so the browser agent is disabled unless `sessionMode` is set to `"existing"`. When enabled with existing mode, the agent automatically connects to Chrome on the host via the resolved IP of `host.docker.internal:9222` instead of using local pipe discovery. Port `9222` is currently hardcoded and cannot be customized.

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
| `name` | `string` | **Yes** | Unique identifier (slug) used as the tool name for the agent. Only lowercase letters, numbers, hyphens, and underscores. |
| `description` | `string` | **Yes** | Short description of what the agent does. This is visible to the main agent to help it decide when to call this subagent. |
| `kind` | `string` | No | `local` (default) or `remote`. |
| `tools` | `array` | No | List of tool names this agent can use. Supports wildcards: `*` (all tools), `mcp_*` (all MCP tools), `mcp_server_*` (all tools from a server). If omitted, it inherits all tools from the parent session. |
| `mcpServers` | `object` | No | Configuration for inline Model Context Protocol (MCP) servers isolated to this specific agent. |
| `model` | `string` | No | Specific model to use (for example, `gemini-3-preview`). Defaults to `inherit` (uses the main session model). |
| `temperature` | `number` | No | Model temperature (0.0 - 2.0). Defaults to `1`. |
| `max_turns` | `number` | No | Maximum number of conversation turns allowed for this agent before it must return. Defaults to `30`. |
| `timeout_mins` | `number` | No | Maximum execution time in minutes. Defaults to `10`. |

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

## Subagent tool isolation
Subagent tool isolation moves Gemini CLI away from a single global tool registry. By providing isolated execution environments, you can ensure that subagents only interact with the parts of the system they are designed for. This prevents unintended side effects, improves reliability by avoiding state contamination, and enables fine-grained permission control.

With this feature, you can:

*   **Specify tool access:** Define exactly which tools an agent can access using a `tools` list in the agent definition.
*   **Define inline MCP servers:** Configure Model Context Protocol (MCP) servers (which provide a standardized way to connect AI models to external tools and data sources) directly in the subagent’s markdown frontmatter, isolating them to that specific agent.
*   **Maintain state isolation:** Ensure that subagents only interact with their own set of tools and servers, preventing side effects and state contamination.
*   **Apply subagent-specific policies:** Enforce granular rules in your Policy Engine TOML configuration based on the executing subagent’s name.

### Configuring isolated tools and servers
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

### Subagent-specific policies
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

`agents.overrides`
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

`modelConfigs.overrides`
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
Subagents are enabled by default. To disable them, set `enableAgents` to `false` in your `settings.json`:

```json
{
  "experimental": { "enableAgents": false }
}
```

---

### Google Cloud AI Agents Portfolio

Google Cloud provides a comprehensive set of tools for agent development:

- **Gemini Enterprise App**: Secure platform to govern AI agents across an organization.
- **Gemini Enterprise Agent Platform**: Create agents grounded in enterprise data using natural language or code.
- **Customer Experience Agent Studio (Dialogflow)**: Build hybrid conversational agents with both deterministic and generative AI.
- **Agent Garden**: A curated collection of pre-built agent samples and tools.
- **Agent Development Kit (ADK)**: Open-source Python SDK for building sophisticated multi-agent systems.
- **A2A Protocol**: Open-source framework for interoperable agent-to-agent communication.
- **Cloud Run**: Fully managed serverless platform for deploying containerized agents.
- **Agent Search**: Build Google-quality search for enterprise apps and experiences.
- **Agentic SOC**: Delivering better security outcomes with AI agents.

---

### How do AI agents work?

AI agents are built on four functional pillars:

- **Persona**: A defined role, personality, and communication style that evolves with experience.
- **Memory**: Includes short-term (immediate interaction), long-term (historical), episodic (past events), and consensus (shared among agents) memory.
- **Tools**: External resources (APIs, UI-based tools) that allow agents to interact with and manipulate their environment.
- **Model**: LLMs act as the 'brain', providing the underlying understanding and reasoning capacity.

---

### Intelephense Legacy Documentation

This section contains historical documentation for Intelephense previously stored in this file.

---

### Jules Tools

Jules Tools is a lightweight command-line interface (CLI) for interacting with Jules, Google’s autonomous AI coding agent. It allows you to manage coding sessions, inspect progress, and integrate Jules into your existing development workflows and scripts directly from your terminal.

Think of Jules Tools as both a command surface and a dashboard for your coding agent, designed to keep you in your flow without needing to switch to a web browser.

- Installation: `npm install -g @google/jules`.
- Authentication: `jules login` and `jules logout`.
- Commands: `version`, `remote` (list, new, pull), `completion`.
- Dashboard (TUI): Run `jules` without arguments for an interactive experience.

---

### Key features of an AI agent

Modern AI agents have evolved to include several core cognitive and operational features:

- **Reasoning**: Using logic and available information to draw conclusions and solve problems.
- **Acting**: The ability to perform digital (sending messages, updating data) or physical (embodied AI) actions.
- **Observing**: Gathering environmental information through perception (computer vision, NLP, sensors).
- **Planning**: Developing strategic steps to achieve goals, including anticipating future states.
- **Collaborating**: Working effectively with humans or other agents via communication and coordination.
- **Self-refining**: Learning from experience and feedback to continuously enhance performance over time.

---

### Knowledge Merge

Knowledge Merge is a process or document that merges key concepts currently spread across Antigravity, Project SOR, the live software-online-review.com domain, and the new software-review-platform starter. It creates one canonical map of what each layer is, what role it plays, and how the project should evolve.

---

### React Agent Deployment Logic

The react agent deployment logic is responsible for verifying the deployment of react agents and improving the workflow run.

*Source: manual*

---

### Security agents

Security agents strengthen security posture by mitigating attacks or increasing the speed of investigations. They can oversee security across various surfaces and stages of the security life cycle: prevention, detection, and response.

---

### Types of agents in AI

Agents can be categorized by interaction or scale:

- **Surface Agents (Interactive Partners)**: Engage in direct conversation to assist with customer service, education, or healthcare.
- **Background Agents (Autonomous Processes)**: Work behind the scenes to automate workflows and optimize processes with limited human interaction.
- **Single Agent**: Operates independently to achieve a specific goal using a single foundation model.
- **Multi-agent**: Multiple agents collaborate or compete, potentially using different foundation models for diverse roles.

---

### What is an AI agent?

AI agents are software systems that use AI to pursue goals and complete tasks on behalf of users. They exhibit reasoning, planning, and memory, and possess a degree of autonomy to make decisions, learn, and adapt. Their capabilities are primarily driven by the multimodal capacity of generative AI and foundation models, allowing them to process text, voice, video, audio, code, and more simultaneously.

---

### Difference between AI Agents, AI Assistants, and Bots

The primary distinctions lie in autonomy and complexity:

- **AI Agents**: Highest autonomy; proactive and goal-oriented; can perform complex multi-step actions and make independent decisions.
- **AI Assistants**: Moderate autonomy; reactive to user prompts; assist with tasks while decision-making remains with the user.
- **Bots**: Lowest autonomy; follow pre-defined rules; limited learning; automate simple, repetitive tasks.

---

