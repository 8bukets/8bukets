# What are AI Agents?

Scraped from [https://cloud.google.com/discover/what-are-ai-agents](https://cloud.google.com/discover/what-are-ai-agents)

## What is an AI agent?

Last Updated: 04/02/2026

AI agents are software systems that use AI to pursue goals and complete tasks on behalf of users. They show reasoning, planning, and memory and have a level of autonomy to make decisions, learn, and adapt.

Their capabilities are made possible in large part by the multimodal capacity of generative AI and AI foundation models. AI agents can process multimodal information like text, voice, video, audio, code, and more simultaneously; can converse, reason, learn, and make decisions. They can learn over time and facilitate transactions and business processes. Agents can work with other agents to coordinate and perform more complex workflows.

## Key features of an AI agent

As explained above, while the key features of an AI agent are reasoning and acting (as described in ReAct Framework) more features have evolved over time.

- Reasoning: This core cognitive process involves using logic and available information to draw conclusions, make inferences, and solve problems. AI agents with strong reasoning capabilities can analyze data, identify patterns, and make informed decisions based on evidence and context.
- Acting : The ability to take action or perform tasks based on decisions, plans, or external input is crucial for AI agents to interact with their environment and achieve goals. This can include physical actions in the case of embodied AI, or digital actions like sending messages, updating data, or triggering other processes.
- Observing : Gathering information about the environment or situation through perception or sensing is essential for AI agents to understand their context and make informed decisions. This can involve various forms of perception, such as computer vision, natural language processing, or sensor data analysis.
- Planning : Developing a strategic plan to achieve goals is a key aspect of intelligent behavior. AI agents with planning capabilities can identify the necessary steps, evaluate potential actions, and choose the best course of action based on available information and desired outcomes. This often involves anticipating future states and considering potential obstacles.
- Collaborating : Working effectively with others, whether humans or other AI agents, to achieve a common goal is increasingly important in complex and dynamic environments. Collaboration requires communication, coordination, and the ability to understand and respect the perspectives of others.
- Self-refining : The capacity for self-improvement and adaptation is a hallmark of advanced AI systems. AI agents with self-refining capabilities can learn from experience, adjust their behavior based on feedback, and continuously enhance their performance and capabilities over time. This can involve machine learning techniques, optimization algorithms, or other forms of self-modification.

## What is the difference between AI agents, AI assistants, and bots?

AI assistants are AI agents designed as applications or products to collaborate directly with users and perform tasks by understanding and responding to natural human language and inputs. They can reason and take action on the users' behalf with their supervision.

AI assistants are often embedded in the product being used. A key characteristic is the interaction between the assistant and user through the different steps of the task. The assistant responds to requests or prompts from the user, and can recommend actions but decision-making is done by the user.

 | AI agent | AI assistant | Bot
--- | --- | --- | ---
Purpose | Autonomously and proactively perform tasks | Assisting users with tasks | Automating simple tasks or conversations
Capabilities | Can perform complex, multi-step actions; learns and adapts; can make decisions independently | Responds to requests or prompts; provides information and completes simple tasks; can recommend actions but the user makes decisions | Follows pre-defined rules; limited learning; basic interactions
Interaction | Proactive; goal-oriented | Reactive; responds to user requests | Reactive; responds to triggers or commands

AI agent

AI assistant

Bot

Purpose

Autonomously and proactively perform tasks

Assisting users with tasks

Automating simple tasks or conversations

Capabilities

Can perform complex, multi-step actions; learns and adapts; can make decisions independently

Responds to requests or prompts; provides information and completes simple tasks; can recommend actions but the user makes decisions

Follows pre-defined rules; limited learning; basic interactions

Interaction

Proactive; goal-oriented

Reactive; responds to user requests

Reactive; responds to triggers or commands

## Key differences

- Autonomy : AI agents have the highest degree of autonomy, able to operate and make decisions independently to achieve a goal. AI assistants are less autonomous, requiring user input and direction. Bots are the least autonomous, typically following pre-programmed rules.
- Complexity : AI agents are designed to handle complex tasks and workflows, while AI assistants and bots are better suited for simpler tasks and interactions.
- Learning : AI agents often employ machine learning to adapt and improve their performance over time. AI assistants may have some learning capabilities, while bots typically have limited or no learning.

## How do AI agents work?

Every agent defines its role, personality, and communication style, including specific instructions and descriptions of available tools.

- Persona : A well defined persona allows an agent to maintain a consistent character and behave in a manner appropriate to its assigned role, evolving as the agent gains experience and interacts with its environment.
- Memory : The agent is equipped in general with short term, long term, consensus, and episodic memory. Short term memory for immediate interactions, long-term memory for historical data and conversations, episodic memory for past interactions, and consensus memory for shared information among agents. The agent can maintain context, learn from experiences, and improve performance by recalling past interactions and adapting to new situations.
- Tools : Tools are functions or external resources that an agent can utilize to interact with its environment and enhance its capabilities. They allow agents to perform complex tasks by accessing information, manipulating data, or controlling external systems, and can be categorized based on their user interface, including physical, graphical, and program-based interfaces. Tool learning involves teaching agents how to effectively use these tools by understanding their functionalities and the context in which they should be applied.
- Model : Large language models (LLMs) serve as the foundation for building AI agents, providing them with the ability to understand, reason, and act. LLMs act as the "brain" of an agent, enabling them to process and generate language, while other components facilitate reason and action.

## What are the types of agents in AI?

AI agents can be categorized in various ways based on their capabilities, roles, and environments. Here are some key categories of agents:

There are different definitions of agent types and agent categories.

## Based on interaction

One way to categorize agents is by how they interact with users. Some agents engage in direct conversation, while others operate in the background, performing tasks without direct user input:

- Interactive partners (also known as, surface agents): Assisting us with tasks like customer service, healthcare, education, and scientific discovery, providing personalized and intelligent support. Conversational agents include Q&A, chit chat, and world knowledge interactions with humans. They are generally user query triggered and fulfill user queries or transactions.
- Autonomous background processes (also known as, background agents): Working behind the scenes to automate routine tasks, analyze data for insights, optimize processes for efficiency, and proactively identify and address potential issues. They include workflow agents. They have limited or no human interaction and are generally driven by events and fulfill queued tasks or chains of tasks.

## Based on number of agents

- Single agent : Operate independently to achieve a specific goal. They utilize external tools and resources to accomplish tasks, enhancing their functional capabilities in diverse environments. They are best suited for well defined tasks that do not require collaboration with other AI agents. Can only handle one foundation model for its processing.
- Multi-agent : Multiple AI agents that collaborate or compete to achieve a common objective or individual goals. These systems leverage the diverse capabilities and roles of individual agents to tackle complex tasks. Multi-agent systems can simulate human behaviors, such as interpersonal communication, in interactive scenarios. Each agent can have different foundation models that best fit their needs.

## Benefits of using AI agents

AI agents can enhance the capabilities of language models by providing autonomy, task automation, and the ability to interact with the real world through tools and embodiment.

## Efficiency and productivity

Increased output: Agents divide tasks like specialized workers, getting more done overall

Simultaneous execution: Agents can work on different things at the same time without getting in each other's way

Automation: Agents take care of repetitive tasks, freeing up humans for more creative work

## Improved decision-making

Collaboration: Agents work together, debate ideas, and learn from each other, leading to better decisions

Adaptability: Agents can adjust their plans and strategies as situations change

Robust reasoning: Through discussion and feedback, agents can refine their reasoning and avoid errors

## Enhanced capabilities

Complex problem-solving: Agents can tackle challenging real-world problems by combining their strengths

Natural language communication: Agents can understand and use human language to interact with people and each other

Tool use: Agents can interact with the external world by using tools and accessing information

Learning and self-improvement: Agents learn from their experiences and get better over time

## Social interaction and simulation

Realistic simulations: Agents can model human-like social behaviors, such as forming relationships and sharing information

Emergent behavior: Complex social interactions can arise organically from the interactions of individual agents

## Challenges with using AI agents

While AI agents offer many benefits, there are also some challenges associated with their use:

Tasks requiring deep empathy / emotional intelligence or requiring complex human interaction and social dynamics – AI agents can struggle with nuanced human emotions. Tasks like therapy, social work, or conflict resolution require a level of emotional understanding and empathy that AI currently lacks. They may falter in complex social situations that require understanding unspoken cues.

Situations with high ethical stakes – AI agents can make decisions based on data, but they lack the moral compass and judgment needed for ethically complex situations. This includes areas like law enforcement, healthcare (diagnosis and treatment), and judicial decision-making.

Domains with unpredictable physical environments – AI agents can struggle in highly dynamic and unpredictable physical environments where real-time adaptation and complex motor skills are essential. This includes tasks like surgery, certain types of construction work, and disaster response.

Resource-intensive applications – Developing and deploying sophisticated AI agents can be computationally expensive and require significant resources, potentially making them unsuitable for smaller projects or organizations with limited budgets.

## Deploy AI agents for scale and efficiency with Cloud Run

AI agents, with their inherent need for flexible compute power to handle reasoning, planning, and tool use, can be an excellent fit for Cloud Run. This fully managed serverless platform allows you to deploy your agent's code—often packaged within a container—as a scalable, reliable service or job. This approach abstracts away infrastructure management, letting developers concentrate on refining the agent's logic.

Cloud Run offers several features that directly support the architecture and demands of sophisticated AI agents:

- Scalability and cost-efficiency: Cloud Run automatically scales the number of container instances up to meet peak demand and, crucially, can scale down to zero when the agent is idle. This means you only pay for the exact compute resources consumed during the agent's active execution, making it cost-effective for goal-oriented, intermittent workloads.
- Agent orchestration and serving: The core agent logic—which manages the model calls, tool selection, and reasoning process—runs as a Cloud Run service. This service provides a stable HTTPS endpoint, making the agent easily accessible via an API for user-facing applications or for communication with other agents
- Agent-to-Agent, or A2A: Frameworks like the Agent Development Kit (ADK) are designed to integrate seamlessly with Cloud Run for easy deployment.

By leveraging Cloud Run's secure, auto-scaling, and flexible environment, organizations can operationalize complex single- or multi-agent systems efficiently.

## Use cases for AI agents

Organizations have been deploying agents to address a variety use cases, which we group into six key broader categories:

## Customer agents

Customer agents

Customer agents deliver personalized customer experiences by understanding customer needs, answering questions, resolving customer issues, or recommending the right products and services. They work seamlessly across multiple channels including the web, mobile, or point of sale, and can be integrated into product experiences with voice or video.

## Employee agents

Employee agents

Employee agents boost productivity by streamlining processes, managing repetitive tasks, answering employee questions, as well as editing and translating critical content and communications.

## Creative agents

Creative agents

Creative agents supercharge the design and creative process by generating content, images, and ideas, assisting with design, writing, personalization, and campaigns.

## Data agents

Data agents

Data agents are built for complex data analysis. They have the potential to find and act on meaningful insights from data, all while ensuring the factual integrity of their results.

## Code agents

Code agents

Code agents accelerate software development with AI-enabled code generation and coding assistance, and to ramp up on new languages and code bases. Many organizations are seeing significant gains in productivity, leading to faster deployment and cleaner, clearer code.

## Security agents

Security agents

Security agents strengthen security posture by mitigating attacks or increasing the speed of investigations. They can oversee security across various surfaces and stages of the security life cycle: prevention, detection, and response.

## Google Cloud and AI agents

Google Cloud provides a portfolio of products and solutions in the AI agent space. These include integrated AI assistants, pre-built AI agents, AI applications, and a platform of agent and developer tools to build custom AI agents.

- Gemini Enterprise App Secure platform to discover, create, run, and govern AI agents across your organization.
- Gemini Enterprise Agent Platform Create AI agents and applications using natural language or a code-first approach. Easily ground your agents or apps in enterprise data with a range of options.
- Customer Experience Agent Studio Build hybrid conversational agents with both deterministic and generative AI functionality.
- Agent Garden Curated collection of pre-built agent samples, solutions, tools, and frameworks to accelerate the development and deployment of AI agents.
- Agent Development Kit (ADK) Open-source Python SDK to build sophisticated multi-agent systems with orchestration, memory, and developer tools.
- A2A Protocol An open-source framework originally developed by Google to help build AI agents. An AI agent built with A2A Protocol will be interoperable with any service, platform, or infrastructure.
- Cloud Run A fully managed serverless platform that allows you to deploy containerized agents and applications, providing auto-scaling and pay-per-use efficiency.


All the best - https://cloud.google.com/discover/what-are-ai-agents
---

# Manual Knowledge Additions

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

## Jules Tools

Jules Tools is a lightweight command-line interface (CLI) for interacting with Jules, Google’s autonomous AI coding agent. It allows you to manage coding sessions, inspect progress, and integrate Jules into your existing development workflows and scripts directly from your terminal.

Think of Jules Tools as both a command surface and a dashboard for your coding agent, designed to keep you in your flow without needing to switch to a web browser.

- Installation: `npm install -g @google/jules`.
- Authentication: `jules login` and `jules logout`.
- Commands: `version`, `remote` (list, new, pull), `completion`.
- Dashboard (TUI): Run `jules` without arguments for an interactive experience.

## Knowledge Merge

Knowledge Merge is a process or document that merges key concepts currently spread across Antigravity, Project SOR, the live software-online-review.com domain, and the new software-review-platform starter. It creates one canonical map of what each layer is, what role it plays, and how the project should evolve.

## Gemini CLI Remote Subagents

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


## Gemini CLI Subagents

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


## Docker MCP Catalog

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

