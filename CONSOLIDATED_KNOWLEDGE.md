# Consolidated Knowledge Base

**Last Sync (Python):** 2026-05-15T03:54:20.356726
**System Version:** 1.68

## System Intelligence & Outlook
- Scaling Strategy: Implementing simultaneous execution across agent tiers.
- R&D Strategy: Developing realistic simulations for human-agent interaction.
- Operational Strategy: Enhancing agent debate and feedback loops.

## 1. AI Agent Foundation
### Compile

prepare best value of knowledge integration - To compile means to gather information from various sources and arrange it into a structured format, such as a report, list, book, or file. In computing, it refers to translating human-readable source code into machine-readable, executable instructions.

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

Knowledge Merge is a process or document that merges key concepts currently spread across Antigravity, Project SOR, the live software-online-review.com domain, and the new software-review-platform starter. It creates one canonical map of what each layer is, what role it plays, and how the project should evolve. All the best - https://markposition.wordpress.com

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
