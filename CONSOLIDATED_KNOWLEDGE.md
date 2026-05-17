# Consolidated Knowledge Base

**Last Sync (Python):** 2026-05-17T01:28:31.799502
**System Version:** 1.82

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


---
All the best - https://markposition.wordpress.com
