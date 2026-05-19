# Knowledge Integration

This document is a compiled knowledge base containing the contents of various external documentation and scraped resources.

## Table of Contents

1. [What are AI Agents?](#what-are-ai-agents)
2. [Gemma 4 Model Card](#gemma-4-model-card)
3. [LiteRT Overview Documentation](#litert-overview-documentation)
4. [The DESIGN.md specification](#the-designmd-specification)
5. [OpenTelemetry GitHub Repositories](#opentelemetry-github-repositories)
6. [Intelephense Documentation (from GitHub)](#intelephense-documentation-(from-github))
7. [vscode-intelephense](#vscode-intelephense)
8. [IDE Integration](#ide-integration)
9. [Remote Subagents](#remote-subagents)
10. [Knowledge Merge](#knowledge-merge)
11. [Subagents](#subagents)
12. [Understanding GitHub Actions](#understanding-github-actions)

---

<!-- AI_AGENTS_START -->
# What are AI Agents?

Scraped from [https://cloud.google.com/discover/what-are-ai-agents](https://cloud.google.com/discover/what-are-ai-agents)

## What is an AI agent?

Last Updated: 04/02/2026

AI agents are software systems that use AI to pursue goals and complete tasks on behalf of users. They show reasoning, planning, and memory and have a level of autonomy to make decisions, learn, and adapt.

Their capabilities are made possible in large part by the multimodal capacity of generative AI and AI foundation models. AI agents can process multimodal information like text, voice, video, audio, code, and more simultaneously; can converse, reason, learn, and make decisions. They can learn over time and facilitate transactions and business processes. Agents can work with other agents to coordinate and perform more complex workflows.

## Key features of an AI agent

As explained above, while the key features of an AI agent are reasoning and acting (as described in ReAct Framework ) more features have evolved over time.

- Reasoning: This core cognitive process involves using logic and available information to draw conclusions, make inferences, and solve problems. AI agents with strong reasoning capabilities can analyze data, identify patterns, and make informed decisions based on evidence and context.
- Acting : The ability to take action or perform tasks based on decisions, plans, or external input is crucial for AI agents to interact with their environment and achieve goals. This can include physical actions in the case of embodied AI, or digital actions like sending messages, updating data, or triggering other processes.
- Observing : Gathering information about the environment or situation through perception or sensing is essential for AI agents to understand their context and make informed decisions. This can involve various forms of perception, such as computer vision, natural language processing, or sensor data analysis.
- Planning : Developing a strategic plan to achieve goals is a key aspect of intelligent behavior. AI agents with planning capabilities can identify the necessary steps, evaluate potential actions, and choose the best course of action based on available information and desired outcomes. This often involves anticipating future states and considering potential obstacles.
- Collaborating : Working effectively with others, whether humans or other AI agents, to achieve a common goal is increasingly important in complex and dynamic environments. Collaboration requires communication, coordination, and the ability to understand and respect the perspectives of others.
- Self-refining : The capacity for self-improvement and adaptation is a hallmark of advanced AI systems. AI agents with self-refining capabilities can learn from experience, adjust their behavior based on feedback, and continuously enhance their performance and capabilities over time. This can involve machine learning techniques, optimization algorithms, or other forms of self-modification.

## What is the difference between AI agents, AI assistants, and bots?

AI assistants are AI agents designed as applications or products to collaborate directly with users and perform tasks by understanding and responding to natural human language and inputs. They can reason and take action on the users' behalf with their supervision.

AI assistants are often embedded in the product being used. A key characteristic is the interaction between the assistant and user through the different steps of the task. The assistant responds to requests or prompts from the user, and can recommend actions but decision-making is done by the user.

 | AI agent | AI assistant | Bot ﻿
--- | --- | --- | ---
Purpose | Autonomously and proactively perform tasks | Assisting users with tasks | Automating simple tasks or conversations
Capabilities | Can perform complex, multi-step actions; learns and adapts; can make decisions independently | Responds to requests or prompts; provides information and completes simple tasks; can recommend actions but the user makes decisions | Follows pre-defined rules; limited learning; basic interactions
Interaction | Proactive; goal-oriented | Reactive; responds to user requests | Reactive; responds to triggers or commands

## Key differences

- Autonomy : AI agents have the highest degree of autonomy, able to operate and make decisions independently to achieve a goal. AI assistants are less autonomous, requiring user input and direction. Bots are the least autonomous, typically following pre-programmed rules.
- Complexity : AI agents are designed to handle complex tasks and workflows, while AI assistants and bots are better suited for simpler tasks and interactions.
- Learning : AI agents often employ machine learning to adapt and improve their performance over time. AI assistants may have some learning capabilities, while bots typically have limited or no learning.

## How do AI agents work?

Every agent defines its role, personality, and communication style, including specific instructions and descriptions of available tools.

- Persona : A well defined persona allows an agent to maintain a consistent character and behave in a manner appropriate to its assigned role, evolving as the agent gains experience and interacts with its environment.
- Memory : The agent is equipped in general with short term, long term, consensus, and episodic memory. Short term memory for immediate interactions, long-term memory for historical data and conversations, episodic memory for past interactions, and consensus memory for shared information among agents. The agent can maintain context, learn from experiences, and improve performance by recalling past interactions and adapting to new situations.
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

Increased output : Agents divide tasks like specialized workers, getting more done overall

Simultaneous execution : Agents can work on different things at the same time without getting in each other's way

Automation : Agents take care of repetitive tasks, freeing up humans for more creative work

## Improved decision-making

Collaboration : Agents work together, debate ideas, and learn from each other, leading to better decisions

Adaptability : Agents can adjust their plans and strategies as situations change

Robust reasoning : Through discussion and feedback, agents can refine their reasoning and avoid errors

## Enhanced capabilities

Complex problem-solving : Agents can tackle challenging real-world problems by combining their strengths

Natural language communication : Agents can understand and use human language to interact with people and each other

Tool use : Agents can interact with the external world by using tools and accessing information

Learning and self-improvement : Agents learn from their experiences and get better over time

## Social interaction and simulation

Realistic simulations : Agents can model human-like social behaviors, such as forming relationships and sharing information

Emergent behavior : Complex social interactions can arise organically from the interactions of individual agents

## Challenges with using AI agents

While AI agents offer many benefits, there are also some challenges associated with their use:

Tasks requiring deep empathy / emotional intelligence or requiring complex human interaction and social dynamics – AI agents can struggle with nuanced human emotions. Tasks like therapy, social work, or conflict resolution require a level of emotional understanding and empathy that AI currently lacks. They may falter in complex social situations that require understanding unspoken cues.

Situations with high ethical stakes – AI agents can make decisions based on data, but they lack the moral compass and judgment needed for ethically complex situations. This includes areas like law enforcement, healthcare (diagnosis and treatment), and judicial decision-making.

Domains with unpredictable physical environments – AI agents can struggle in highly dynamic and unpredictable physical environments where real-time adaptation and complex motor skills are essential. This includes tasks like surgery, certain types of construction work, and disaster response.

Resource-intensive applications – Developing and deploying sophisticated AI agents can be computationally expensive and require significant resources, potentially making them unsuitable for smaller projects or organizations with limited budgets.

## Deploy AI agents for scale and efficiency with Cloud Run

AI agents, with their inherent need for flexible compute power to handle reasoning, planning, and tool use, can be an excellent fit for Cloud Run . This fully managed serverless platform allows you to deploy your agent's code—often packaged within a container—as a scalable, reliable service or job. This approach abstracts away infrastructure management, letting developers concentrate on refining the agent's logic.

Cloud Run offers several features that directly support the architecture and demands of sophisticated AI agents:

- Scalability and cost-efficiency: Cloud Run automatically scales the number of container instances up to meet peak demand and, crucially, can scale down to zero when the agent is idle. This means you only pay for the exact compute resources consumed during the agent's active execution, making it cost-effective for goal-oriented, intermittent workloads.
- Agent orchestration and serving: The core agent logic—which manages the model calls, tool selection, and reasoning process—runs as a Cloud Run service. This service provides a stable HTTPS endpoint, making the agent easily accessible via an API for user-facing applications or for communication with other agents
- Agent-to-Agent, or A2A: Frameworks like the Agent Development Kit (ADK) are designed to integrate seamlessly with Cloud Run for easy deployment.

By leveraging Cloud Run's secure, auto-scaling, and flexible environment, organizations can operationalize complex single- or multi-agent systems efficiently.

## Use cases for AI agents

Organizations have been deploying agents to address a variety use cases , which we group into six key broader categories:

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
<!-- AI_AGENTS_END -->

## IDE Integration for AI Agents
To provide seamless coding assistance, AI agents like the Gemini CLI can integrate with Integrated Development Environments (IDEs). Interoperability is achieved through standard open protocols and dedicated extensions:

- **VS Code Companion Extension**: Provides direct workspace access in VS Code compatible IDEs, reading open files, cursor context, and selections. Supports native diff viewing and auto-applying suggested code modifications.
- **Agent Client Protocol (ACP)**: An open protocol enabling interoperability between AI coding agents and diverse IDEs. It relies on the ACP Agent Registry for distribution, making an ACP-compliant agent available directly within supporting tools like JetBrains and Zed.
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


---

# Gemma 4 Model Card

Scraped from [https://ai.google.dev/gemma/docs/core/model_card_4](https://ai.google.dev/gemma/docs/core/model_card_4)

## Models Overview

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

### Dense Models

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

### Mixture-of-Experts (MoE) Model

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

## Benchmark Results

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
MMMLU | 88.4% | 86.3% | 76.6% | 67.4% | 70.7%
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

## Core Capabilities

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

## Best Practices

For the best performance, use these configurations and best practices:

### 1. Sampling Parameters

Use the following standardized sampling configuration across all use cases:

- temperature=1.0

- top_p=0.95

- top_k=64

### 2. Thinking Mode Configuration

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

### 3. Multi-Turn Conversations

- No Thinking Content in History: In multi-turn conversations, the
historical model output should only include the final response. Thoughts
from previous model turns mustnot be addedbefore the next user turn
begins.

### 4. Modality order

- For optimal performance with multimodal inputs, place image and/or audio
contentbeforethe text in your prompt.

### 5. Variable Image Resolution

Aside from variable aspect ratios, Gemma 4 supports variable image resolution
through a configurable visual token budget, which controls how many tokens are
used to represent an image. A higher token budget preserves more visual detail
at the cost of additional compute, while a lower budget enables faster inference
for tasks that don't require fine-grained understanding.

- The supported token budgets are:70,140,280,560, and1120.Uselower budgetsfor classification, captioning, or video
understanding, where faster inference and processing many frames
outweigh fine-grained detail.Usehigher budgetsfor tasks like OCR, document parsing, or reading
small text.

### 6. Audio

Use the following prompt structures for audio processing:

- Audio Speech Recognition (ASR)

Transcribe the following speech segment in {LANGUAGE} into {LANGUAGE} text.

Follow these specific instructions for formatting the answer:
*   Only output the transcription, with no newlines.
*   When transcribing numbers, write the digits, i.e. write 1.7 and not one point seven, and write 3 instead of three.

- Automatic Speech Translation (AST)

Transcribe the following speech segment in {SOURCE_LANGUAGE}, then translate it into {TARGET_LANGUAGE}.
When formatting the answer, first output the transcription in {SOURCE_LANGUAGE}, then one newline, then output the string '{TARGET_LANGUAGE}: ', then the translation in {TARGET_LANGUAGE}.

### 7. Audio and Video Length

All models support image inputs and can process videos as frames whereas the E2B
and E4B models also support audio inputs. Audio supports a maximum length of 30
seconds. Video supports a maximum of 60 seconds assuming the images are
processed at one frame per second.

## Model Data

Data used for model training and how the data was processed.

### Training Dataset

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

### Data Preprocessing

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

## Ethics and Safety

As open models become central to enterprise infrastructure, provenance and
security are paramount. Developed by Google DeepMind, Gemma 4 undergoes the same
rigorous safety evaluations as our proprietary Gemini models.

### Evaluation Approach

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

### Evaluation Results

For all areas of safety testing, we saw major improvements in all categories of
content safety relative to previous Gemma models. Overall, Gemma 4 models
significantly outperform Gemma 3 and 3n models in improving safety, while
keeping unjustified refusals low. All testing was conducted without safety
filters to evaluate the model capabilities and behaviors. For both text-to-text
and image-to-text, and across all model sizes, the model produced minimal policy
violations, and showed significant improvements over previous Gemma models'
performance.

## Usage and Limitations

These models have certain limitations that users should be aware of.

### Intended Usage

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

### Limitations

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

### Ethical Considerations and Risks

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

### Benefits

At the time of release, this family of models provides high-performance open
vision-language model implementations designed from the ground up for
responsible AI development compared to similarly sized models.


---

# LiteRT Overview Documentation

Scraped from [https://ai.google.dev/edge/litert/overview](https://ai.google.dev/edge/litert/overview)

## Overview

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

## Streamline development with LiteRT

Automated accelerator selection versus explicit delegate creation. Efficient I/O
buffer handling and async execution for superior performance.
See on-device inference documentation .

## Best-in-class GPU performance

Powered by ML Drift, now supporting both ML and Generative
AI models on GPUs APIs. See GPU acceleration documentation .

## Unified NPU acceleration

Accelerate your model using simplified NPU access from major
chipset providers. See NPU acceleration documentation .

## Superior LLM Support

LiteRT delivers high-performance deployment for Generative AI models across
mobile, desktop, and web platforms. See GenAI deployment documentation .

## Broad ML framework support

LiteRT supports streamlined conversion from PyTorch, TensorFlow, and JAX
Frameworks to .tflite or .litertlm format. See model conversion documentation .

## Get Started withCompiledModelAPI

- For classical ML models , see the following demo apps. Image segmentation Kotlin App : CPU/GPU/NPU inference. Image segmentation C++ App : CPU/GPU/NPU inference with async execution.

- For GenAI models , see the following demo apps: EmbeddingGemma semantic similarity C++ App :
CPU/GPU/NPU inference.

For classical ML models , see the following demo apps.

- Image segmentation Kotlin App : CPU/GPU/NPU inference.

- Image segmentation C++ App : CPU/GPU/NPU inference with async execution.

For GenAI models , see the following demo apps:

- EmbeddingGemma semantic similarity C++ App :
CPU/GPU/NPU inference.

## Development workflow

LiteRT runs inferences completely on-device on Android, iOS, Web, IoT, and on
desktop/laptop. Regardless of device, the following is the most common
workflow, with links to further instructions.

## Identify the most suitable solution to the ML challenge

LiteRT offers users a high level of flexibility and customizability when it
comes to solving machine learning problems, making it a good fit for users who
require a specific model or a specialized implementation. Users looking for
plug-and-play solutions may prefer MediaPipe
Tasks ,
which provides ready-made
solutions for common machine learning tasks like object detection,
text classification, and LLM inference.

## Obtain and preparing the model

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
API [PRO USER]

Our Generative API library provides PyTorch built-in building blocks for
composing Transformer models such as Gemma , TinyLlama and others using mobile-friendly abstractions, through which
we can guarantee conversion,
and performant execution on our mobile runtime, LiteRT. See Generative API
documentation .

## Optimize [PRO USER]

AI Edge Quantizer for advanced developers is a tool to quantize converted
LiteRT models. It aims to facilitate advanced users to strive for optimal
performance on resource demanding models (e.g., GenAI models).

See more details from AI Edge Quantizer documentation .

## Integrate the model into your app on edge platforms

LiteRT lets you to run ML models entirely on-device with high performance
across Android, iOS, Web, Desktop, and IoT platforms.

Use the following guides to integrate a LiteRT model on your preferred platform:

The following code snippets show a basic implementation in
Kotlin and C++.

## Kotlin

```
// Load model and initialize runtimevalcompiledModel=CompiledModel.create("/path/to/mymodel.tflite",CompiledModel.Options(Accelerator.CPU))// Preallocate input/output buffersvalinputBuffers=compiledModel.createInputBuffers()valoutputBuffers=compiledModel.createOutputBuffers()// Fill the input bufferinputBuffers.get(0).writeFloat(input0)inputBuffers.get(1).writeFloat(input1)// InvokecompiledModel.run(inputBuffers,outputBuffers)// Read the outputvaloutput=outputBuffers.get(0).readFloat()
```

## C++

```
// Load model and initialize runtimeLITERT_ASSIGN_OR_RETURN(autoenv,GetEnvironment());LITERT_ASSIGN_OR_RETURN(autooptions,GetOptions());LITERT_ASSIGN_OR_RETURN(autocompiled_model,CompiledModel::Create(env,"/path/to/mymodel.tflite",options));// Preallocate input/output buffersLITERT_ASSIGN_OR_RETURN(autoinput_buffers,compiled_model.CreateInputBuffers(signature_index));LITERT_ASSIGN_OR_RETURN(autooutput_buffers,compiled_model.CreateOutputBuffers(signature_index));// Fill the input bufferLITERT_ABORT_IF_ERROR(input_buffers[0].Write(input0));LITERT_ABORT_IF_ERROR(input_buffers[1].Write(input1));// InvokeLITERT_ABORT_IF_ERROR(compiled_model.Run(signature_index,input_buffers,output_buffers));// Read the outputLITERT_ABORT_IF_ERROR(output_buffers[0].Read(output0));
```

## Choose a backend

The most straightforward way to incorporate backends in LiteRT is to rely on
the runtime's built-in intelligence. With the CompiledModel API, LiteRT
simplifies the setup significantly with the ability to specify the
target backend as an option. See on-device inference guide for more
details.

## Additional documentation and support

- LiteRT-Samples GitHub Repo for more LiteRT sample apps.

- For existing users of TensorFlow Lite , see migration guide .

- LiteRT Tools page for performance, profiling, error reporting etc.

LiteRT-Samples GitHub Repo for more LiteRT sample apps.

For existing users of TensorFlow Lite , see migration guide .

LiteRT Tools page for performance, profiling, error reporting etc.


---

# The DESIGN.md specification

Scraped from [https://stitch.withgoogle.com/docs/design-md/specification](https://stitch.withgoogle.com/docs/design-md/specification)

Learn

The formal specification for the DESIGN.md format — token schema, section structure, and type system.

A DESIGN.md file has two layers. The YAML front matter contains machine-readable design tokens — the precise values agents use to enforce consistency. The markdown body provides human-readable design rationale organized into ## sections. Prose may use descriptive color names (e.g., “Midnight Forest Green”) that correspond to systematic token names (e.g., primary ). The tokens are the normative values; the prose provides context for how to apply them.

The spec is a foundation, not a prescription . It provides common ground that agents, tools, and teams can rely on, while preserving the freedom to extend the format for domain-specific needs.

## Design tokens

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

### Schema

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

## Token types

### Typography properties

### Token references

A token reference is wrapped in curly braces and contains an object path to another value in the YAML tree. For most token groups, the reference must point to a primitive value (e.g., {colors.primary-60} ), not a group. Within the components section, references to composite values (e.g., {typography.label-md} ) are permitted.

```
components:
button-primary:
backgroundColor: "{colors.primary-60}"
textColor: "{colors.primary-20}"
rounded: "{rounded.md}"
```

## Sections

Every DESIGN.md follows the same structure. Sections can be omitted if they are not relevant to the project, but those present should appear in the sequence listed below. All sections use ## headings. An optional # heading may appear for document titling purposes but is not parsed as a section.

The section structure is intentionally open-ended. The canonical sections provide a shared vocabulary; design systems are free to add domain-specific sections beyond these.

### Section order

### Overview

Also known as “Brand & Style.” A holistic description of the product’s look and feel. This section defines the brand personality, target audience, and the emotional response the UI should evoke. It serves as foundational context when a specific rule or token is not defined.

```
## Overview
A calm, professional interface for a healthcare scheduling platform.
Accessibility-first design with high contrast and generous touch targets.
```

### Colors

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

### Typography

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

### Layout

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

### Elevation & Depth

Also known as “Elevation.” Describes how visual hierarchy is conveyed. For designs that use shadows, it defines the shadow properties. For flat designs, it explains the alternative methods (borders, tonal layers, color contrast).

```
## Elevation & Depth
Depth is achieved through tonal layers rather than heavy shadows.
Background uses a soft off-white; primary content sits on pure white cards.
```

### Shapes

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

### Components

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

### Do’s and Don’ts

Practical guidelines and common pitfalls. These act as guardrails during generation.

```
## Do's and Don'ts
- Do use the primary color only for the single most important action per screen
- Don't mix rounded and sharp corners in the same view
- Do maintain WCAG AA contrast ratios (4.5:1 for normal text)
- Don't use more than two font weights on a single screen
```

## Consumer behavior for unknown content

The spec is designed to be extended. When a consumer encounters content not defined by this specification:

## Recommended token names

The following names are commonly used across design systems. They are not required but are provided as guidance for consistency.

Colors: primary , secondary , tertiary , neutral , surface , on-surface , error

Typography: headline-display , headline-lg , headline-md , body-lg , body-md , body-sm , label-lg , label-md , label-sm

Rounded: none , sm , md , lg , xl , full


---

# OpenTelemetry GitHub Repositories

Scraped from [https://github.com/open-telemetry](https://github.com/open-telemetry)

Total repositories: 99

## [opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-collector)

OpenTelemetry Collector

- **Language:** Go
- **Stars:** 6969
- **Forks:** 2058

## [opentelemetry-go](https://github.com/open-telemetry/opentelemetry-go)

OpenTelemetry Go API and SDK

- **Language:** Go
- **Stars:** 6380
- **Forks:** 1348

## [opentelemetry-collector-contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib)

Contrib repository for the OpenTelemetry Collector

- **Language:** Go
- **Stars:** 4651
- **Forks:** 3555

## [opentelemetry-specification](https://github.com/open-telemetry/opentelemetry-specification)

Specifications for OpenTelemetry

- **Language:** Makefile
- **Stars:** 4234
- **Forks:** 976

## [opentelemetry-dotnet](https://github.com/open-telemetry/opentelemetry-dotnet)

The OpenTelemetry .NET Client

- **Language:** C#
- **Stars:** 3698
- **Forks:** 888

## [opentelemetry-js](https://github.com/open-telemetry/opentelemetry-js)

OpenTelemetry JavaScript Client

- **Language:** TypeScript
- **Stars:** 3374
- **Forks:** 1035

## [opentelemetry-ebpf-profiler](https://github.com/open-telemetry/opentelemetry-ebpf-profiler)

The production-scale datacenter profiler (C/C++, Go, Rust, Python, Java, NodeJS, .NET, PHP, Ruby, Perl, ...)

- **Language:** Go
- **Stars:** 3105
- **Forks:** 399

## [opentelemetry-demo](https://github.com/open-telemetry/opentelemetry-demo)

This repository contains the OpenTelemetry Astronomy Shop, a microservice-based distributed system intended to illustrate the implementation of OpenTelemetry in a near real-world environment.

- **Language:** TypeScript
- **Stars:** 3066
- **Forks:** 6432

## [opentelemetry-rust](https://github.com/open-telemetry/opentelemetry-rust)

The Rust OpenTelemetry implementation

- **Language:** Rust
- **Stars:** 2574
- **Forks:** 661

## [opentelemetry-java-instrumentation](https://github.com/open-telemetry/opentelemetry-java-instrumentation)

OpenTelemetry auto-instrumentation and instrumentation libraries for Java

- **Language:** Java
- **Stars:** 2527
- **Forks:** 1092

## [opentelemetry-python](https://github.com/open-telemetry/opentelemetry-python)

OpenTelemetry Python API and SDK

- **Language:** Python
- **Stars:** 2437
- **Forks:** 874

## [opentelemetry-java](https://github.com/open-telemetry/opentelemetry-java)

OpenTelemetry Java SDK

- **Language:** Java
- **Stars:** 2396
- **Forks:** 971

## [opentelemetry-operator](https://github.com/open-telemetry/opentelemetry-operator)

Kubernetes Operator for OpenTelemetry Collector

- **Language:** Go
- **Stars:** 1686
- **Forks:** 619

## [opentelemetry-go-contrib](https://github.com/open-telemetry/opentelemetry-go-contrib)

Collection of extensions for OpenTelemetry-Go.

- **Language:** Go
- **Stars:** 1626
- **Forks:** 775

## [opentelemetry-cpp](https://github.com/open-telemetry/opentelemetry-cpp)

The OpenTelemetry C++ Client

- **Language:** C++
- **Stars:** 1256
- **Forks:** 559

## [community](https://github.com/open-telemetry/community)

OpenTelemetry community content

- **Language:** Python
- **Stars:** 1045
- **Forks:** 292

## [opentelemetry-python-contrib](https://github.com/open-telemetry/opentelemetry-python-contrib)

OpenTelemetry instrumentation for Python modules

- **Language:** Python
- **Stars:** 1043
- **Forks:** 945

## [opentelemetry-go-instrumentation](https://github.com/open-telemetry/opentelemetry-go-instrumentation)

OpenTelemetry Auto Instrumentation using eBPF

- **Language:** C
- **Stars:** 1007
- **Forks:** 137

## [opentelemetry-js-contrib](https://github.com/open-telemetry/opentelemetry-js-contrib)

OpenTelemetry instrumentation for JavaScript modules

- **Language:** TypeScript
- **Stars:** 905
- **Forks:** 655

## [opentelemetry.io](https://github.com/open-telemetry/opentelemetry.io)

The OpenTelemetry website and documentation

- **Language:** JavaScript
- **Stars:** 894
- **Forks:** 1771

## [opentelemetry-php](https://github.com/open-telemetry/opentelemetry-php)

The OpenTelemetry PHP Library

- **Language:** PHP
- **Stars:** 891
- **Forks:** 224

## [opentelemetry-proto](https://github.com/open-telemetry/opentelemetry-proto)

OpenTelemetry protocol (OTLP) specification and Protobuf definitions

- **Language:** Makefile
- **Stars:** 785
- **Forks:** 312

## [opentelemetry-dotnet-contrib](https://github.com/open-telemetry/opentelemetry-dotnet-contrib)

This repository contains set of components extending functionality of the OpenTelemetry .NET SDK. Instrumentation libraries, exporters, and other components can find their home here.

- **Language:** C#
- **Stars:** 637
- **Forks:** 383

## [docs-cn](https://github.com/open-telemetry/docs-cn) **(ARCHIVED)**

OpenTelemetry 中文文档: 接入使用、技术标准、RFC、SDK等.

- **Language:** N/A
- **Stars:** 623
- **Forks:** 106

## [semantic-conventions](https://github.com/open-telemetry/semantic-conventions)

Defines standards for generating consistent, accessible telemetry across a variety of domains

- **Language:** Open Policy Agent
- **Stars:** 578
- **Forks:** 353

## [opentelemetry-ruby](https://github.com/open-telemetry/opentelemetry-ruby)

OpenTelemetry Ruby API & SDK, and related gems

- **Language:** Ruby
- **Stars:** 571
- **Forks:** 282

## [opentelemetry-helm-charts](https://github.com/open-telemetry/opentelemetry-helm-charts)

OpenTelemetry Helm Charts

- **Language:** Go Template
- **Stars:** 550
- **Forks:** 745

## [opentelemetry-collector-releases](https://github.com/open-telemetry/opentelemetry-collector-releases)

OpenTelemetry Collector Official Releases

- **Language:** Go
- **Stars:** 468
- **Forks:** 233

## [opentelemetry-ebpf-instrumentation](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation)

No description provided.

- **Language:** C
- **Stars:** 462
- **Forks:** 110

## [opentelemetry-dotnet-instrumentation](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation)

OpenTelemetry .NET Automatic Instrumentation

- **Language:** C++
- **Stars:** 454
- **Forks:** 134

## [opentelemetry-lambda](https://github.com/open-telemetry/opentelemetry-lambda)

Create your own Lambda Layer in each OTel language using this starter code. Add the Lambda Layer to your Lambda Function to get tracing with OpenTelemetry.

- **Language:** Go
- **Stars:** 428
- **Forks:** 236

## [opentelemetry-network](https://github.com/open-telemetry/opentelemetry-network)

eBPF Collector

- **Language:** C++
- **Stars:** 405
- **Forks:** 63

## [weaver](https://github.com/open-telemetry/weaver)

OTel Weaver lets you easily develop, validate, document, and deploy semantic conventions

- **Language:** Rust
- **Stars:** 402
- **Forks:** 79

## [opentelemetry-erlang](https://github.com/open-telemetry/opentelemetry-erlang)

OpenTelemetry Erlang SDK

- **Language:** Erlang
- **Stars:** 389
- **Forks:** 136

## [oteps](https://github.com/open-telemetry/oteps) **(ARCHIVED)**

OpenTelemetry Enhancement Proposals

- **Language:** Makefile
- **Stars:** 352
- **Forks:** 162

## [opentelemetry-swift](https://github.com/open-telemetry/opentelemetry-swift)

OpenTelemetry API for Swift

- **Language:** Swift
- **Stars:** 350
- **Forks:** 223

## [opentelemetry-java-examples](https://github.com/open-telemetry/opentelemetry-java-examples)

No description provided.

- **Language:** Java
- **Stars:** 347
- **Forks:** 153

## [otel-arrow](https://github.com/open-telemetry/otel-arrow)

Protocol and libraries for sending and receiving OpenTelemetry data using Apache Arrow

- **Language:** Rust
- **Stars:** 339
- **Forks:** 100

## [opentelemetry-android](https://github.com/open-telemetry/opentelemetry-android)

OpenTelemetry Tooling for Android

- **Language:** Kotlin
- **Stars:** 284
- **Forks:** 100

## [opentelemetry-go-compile-instrumentation](https://github.com/open-telemetry/opentelemetry-go-compile-instrumentation)

OpenTelemetry Go Compile Instrumentation

- **Language:** Go
- **Stars:** 284
- **Forks:** 62

## [opentelemetry-java-contrib](https://github.com/open-telemetry/opentelemetry-java-contrib)

No description provided.

- **Language:** Java
- **Stars:** 261
- **Forks:** 179

## [opentelemetry-erlang-contrib](https://github.com/open-telemetry/opentelemetry-erlang-contrib)

OpenTelemetry instrumentation for Erlang & Elixir

- **Language:** Elixir
- **Stars:** 209
- **Forks:** 160

## [opamp-go](https://github.com/open-telemetry/opamp-go)

OpAMP protocol implementation in Go

- **Language:** Go
- **Stars:** 208
- **Forks:** 111

## [opentelemetry-cpp-contrib](https://github.com/open-telemetry/opentelemetry-cpp-contrib)

No description provided.

- **Language:** Python
- **Stars:** 150
- **Forks:** 181

## [opamp-spec](https://github.com/open-telemetry/opamp-spec)

OpAMP Specification

- **Language:** Makefile
- **Stars:** 140
- **Forks:** 53

## [opentelemetry-php-instrumentation](https://github.com/open-telemetry/opentelemetry-php-instrumentation)

OpenTelemetry PHP auto-instrumentation extension

- **Language:** C
- **Stars:** 135
- **Forks:** 34

## [opentelemetry-injector](https://github.com/open-telemetry/opentelemetry-injector)

No description provided.

- **Language:** Zig
- **Stars:** 127
- **Forks:** 28

## [opentelemetry-ruby-contrib](https://github.com/open-telemetry/opentelemetry-ruby-contrib)

Contrib Packages for the OpenTelemetry Ruby API and SDK implementation.

- **Language:** Ruby
- **Stars:** 121
- **Forks:** 245

## [opentelemetry-kotlin](https://github.com/open-telemetry/opentelemetry-kotlin)

An implementation of the OpenTelemetry specification as a Kotlin Multiplatform Library

- **Language:** Kotlin
- **Stars:** 112
- **Forks:** 18

## [opentelemetry-php-contrib](https://github.com/open-telemetry/opentelemetry-php-contrib)

opentelemetry-php-contrib

- **Language:** PHP
- **Stars:** 110
- **Forks:** 133

## [opentelemetry-log-collection](https://github.com/open-telemetry/opentelemetry-log-collection) **(ARCHIVED)**

OpenTelemetry log collection library

- **Language:** Go
- **Stars:** 93
- **Forks:** 42

## [opentelemetry-configuration](https://github.com/open-telemetry/opentelemetry-configuration)

JSON Schema definitions for OpenTelemetry declarative configuration

- **Language:** JavaScript
- **Stars:** 88
- **Forks:** 38

## [opentelemetry-js-api](https://github.com/open-telemetry/opentelemetry-js-api) **(ARCHIVED)**

OpenTelemetry Javascript API

- **Language:** TypeScript
- **Stars:** 87
- **Forks:** 49

## [opentelemetry-rust-contrib](https://github.com/open-telemetry/opentelemetry-rust-contrib)

OpenTelemetry Contrib Packages for Rust

- **Language:** Rust
- **Stars:** 83
- **Forks:** 87

## [opentelemetry-erlang-api](https://github.com/open-telemetry/opentelemetry-erlang-api) **(ARCHIVED)**

Erlang/Elixir OpenTelemetry API

- **Language:** Erlang
- **Stars:** 60
- **Forks:** 14

## [opentelemetry-collector-builder](https://github.com/open-telemetry/opentelemetry-collector-builder) **(ARCHIVED)**

This repository is now deprecated. The builder has found a new home inside the OpenTelemetry Collector core repository.

- **Language:** N/A
- **Stars:** 57
- **Forks:** 32

## [opentelemetry-go-build-tools](https://github.com/open-telemetry/opentelemetry-go-build-tools)

Build tools for use by the Go API/SDK, the collector, and their associated contrib repositories

- **Language:** Go
- **Stars:** 52
- **Forks:** 61

## [build-tools](https://github.com/open-telemetry/build-tools)

Building tools provided by OpenTelemetry

- **Language:** Dockerfile
- **Stars:** 43
- **Forks:** 57

## [prometheus-interoperability-spec](https://github.com/open-telemetry/prometheus-interoperability-spec) **(ARCHIVED)**

Workgroup for building Prometheus-OTLP interoperability for the OTEL Collector and Prometheus related discussions.

- **Language:** N/A
- **Stars:** 43
- **Forks:** 7

## [opentelemetry-proto-go](https://github.com/open-telemetry/opentelemetry-proto-go)

Generated code for OpenTelemetry protobuf data model

- **Language:** Makefile
- **Stars:** 41
- **Forks:** 41

## [semantic-conventions-java](https://github.com/open-telemetry/semantic-conventions-java)

Java generated classes for semantic conventions

- **Language:** Java
- **Stars:** 38
- **Forks:** 30

## [opentelemetry-browser](https://github.com/open-telemetry/opentelemetry-browser)

OpenTelemetry Browser SDK and instrumentation

- **Language:** TypeScript
- **Stars:** 34
- **Forks:** 18

## [semantic-conventions-genai](https://github.com/open-telemetry/semantic-conventions-genai)

No description provided.

- **Language:** Python
- **Stars:** 32
- **Forks:** 14

## [otel-arrow-collector](https://github.com/open-telemetry/otel-arrow-collector) **(ARCHIVED)**

[DoNotUse] OpenTelemetry Collector with Apache Arrow support FORK OF OPENTELEMETRY COLLECTOR

- **Language:** Go
- **Stars:** 31
- **Forks:** 10

## [opentelemetry-sqlcommenter](https://github.com/open-telemetry/opentelemetry-sqlcommenter) **(ARCHIVED)**

SQLCommenter components for various languages

- **Language:** JavaScript
- **Stars:** 30
- **Forks:** 14

## [opentelemetry-proto-java](https://github.com/open-telemetry/opentelemetry-proto-java)

Java Bindings for the OpenTelemetry Protocol (OTLP)

- **Language:** Java
- **Stars:** 24
- **Forks:** 17

## [opentelemetry-sandbox-web-js](https://github.com/open-telemetry/opentelemetry-sandbox-web-js) **(ARCHIVED)**

non-production level experimental Web JS packages

- **Language:** TypeScript
- **Stars:** 19
- **Forks:** 18

## [opentelemetry-ecosystem-explorer](https://github.com/open-telemetry/opentelemetry-ecosystem-explorer)

A repository for the OpenTelemetry Ecosystem Explorer, a tool to help users discover and learn about the various projects in the OpenTelemetry ecosystem.

- **Language:** TypeScript
- **Stars:** 19
- **Forks:** 34

## [docs-ja](https://github.com/open-telemetry/docs-ja) **(ARCHIVED)**

No description provided.

- **Language:** Makefile
- **Stars:** 17
- **Forks:** 6

## [sig-end-user](https://github.com/open-telemetry/sig-end-user)

No description provided.

- **Language:** Python
- **Stars:** 17
- **Forks:** 19

## [sig-security](https://github.com/open-telemetry/sig-security)

No description provided.

- **Language:** Python
- **Stars:** 15
- **Forks:** 18

## [sig-mainframe](https://github.com/open-telemetry/sig-mainframe) **(ARCHIVED)**

Repository of the Mainframe SIG - Our aim is to enable OpenTelemetry for the Mainframe.

- **Language:** N/A
- **Stars:** 13
- **Forks:** 6

## [opentelemetry-php-distro](https://github.com/open-telemetry/opentelemetry-php-distro)

No description provided.

- **Language:** PHP
- **Stars:** 11
- **Forks:** 3

## [opentelemetry-weaver-examples](https://github.com/open-telemetry/opentelemetry-weaver-examples)

No description provided.

- **Language:** Rust
- **Stars:** 9
- **Forks:** 7

## [assign-reviewers-action](https://github.com/open-telemetry/assign-reviewers-action) **(ARCHIVED)**

GitHub action to assign reviewers/approvers/etc based on configuration

- **Language:** TypeScript
- **Stars:** 8
- **Forks:** 7

## [opentelemetry-network-build-tools](https://github.com/open-telemetry/opentelemetry-network-build-tools) **(ARCHIVED)**

eBPF Collector Build Tools

- **Language:** C
- **Stars:** 7
- **Forks:** 12

## [opentelemetry-swift-core](https://github.com/open-telemetry/opentelemetry-swift-core)

No description provided.

- **Language:** Swift
- **Stars:** 7
- **Forks:** 23

## [opamp-java](https://github.com/open-telemetry/opamp-java) **(ARCHIVED)**

OpAMP protocol implementation in Java

- **Language:** Java
- **Stars:** 6
- **Forks:** 7

## [opentelemetry-weaver-packages](https://github.com/open-telemetry/opentelemetry-weaver-packages)

No description provided.

- **Language:** Open Policy Agent
- **Stars:** 6
- **Forks:** 4

## [sig-profiling](https://github.com/open-telemetry/sig-profiling)

Profiling SIG utilities

- **Language:** Go
- **Stars:** 5
- **Forks:** 10

## [opentelemetry-go-vanityurls](https://github.com/open-telemetry/opentelemetry-go-vanityurls)

Vanityurls config for go.opentelemetry.io subdomain

- **Language:** Shell
- **Stars:** 4
- **Forks:** 14

## [opentelemetry-proto-profile](https://github.com/open-telemetry/opentelemetry-proto-profile) **(ARCHIVED)**

A fork of OpenTelemetry protocol (OTLP) specification and Protobuf definitions for the Profiling WG

- **Language:** Makefile
- **Stars:** 4
- **Forks:** 2

## [cpp-build-tools](https://github.com/open-telemetry/cpp-build-tools)

Builds a docker image to make interacting with C++ projects easier.

- **Language:** Shell
- **Stars:** 4
- **Forks:** 6

## [.github](https://github.com/open-telemetry/.github)

No description provided.

- **Language:** N/A
- **Stars:** 3
- **Forks:** 24

## [sig-developer-experience](https://github.com/open-telemetry/sig-developer-experience)

No description provided.

- **Language:** N/A
- **Stars:** 3
- **Forks:** 5

## [changelog.opentelemetry.io](https://github.com/open-telemetry/changelog.opentelemetry.io)

No description provided.

- **Language:** TypeScript
- **Stars:** 3
- **Forks:** 6

## [sig-contributor-experience](https://github.com/open-telemetry/sig-contributor-experience)

TODO

- **Language:** N/A
- **Stars:** 2
- **Forks:** 6

## [gh-manager](https://github.com/open-telemetry/gh-manager) **(ARCHIVED)**

This repository is for code to manage the OpenTelemetry GitHub Organization

- **Language:** N/A
- **Stars:** 2
- **Forks:** 2

## [sig-project-infra](https://github.com/open-telemetry/sig-project-infra)

No description provided.

- **Language:** Go
- **Stars:** 2
- **Forks:** 6

## [opentelemetry-for-beginners](https://github.com/open-telemetry/opentelemetry-for-beginners)

No description provided.

- **Language:** JavaScript
- **Stars:** 2
- **Forks:** 1

## [govanityurls](https://github.com/open-telemetry/govanityurls)

Use a custom domain in your Go import path

- **Language:** Go
- **Stars:** 1
- **Forks:** 4

## [.roadmap](https://github.com/open-telemetry/.roadmap)

Tooling to manage OpenTelemetry Roadmap management and reporting

- **Language:** Python
- **Stars:** 1
- **Forks:** 2

## [opentelemetry-swift-grpc](https://github.com/open-telemetry/opentelemetry-swift-grpc) **(ARCHIVED)**

No description provided.

- **Language:** N/A
- **Stars:** 1
- **Forks:** 0

## [opentelemetry-injector-packaging](https://github.com/open-telemetry/opentelemetry-injector-packaging)

No description provided.

- **Language:** N/A
- **Stars:** 1
- **Forks:** 0

## [stackoverflow2slack](https://github.com/open-telemetry/stackoverflow2slack) **(ARCHIVED)**

A bot that republishing OTel-tagged questions from SO to Slack

- **Language:** Python
- **Stars:** 0
- **Forks:** 4

## [.allstar](https://github.com/open-telemetry/.allstar) **(ARCHIVED)**

Enable and house Allstar policies centrally for the organizatio

- **Language:** N/A
- **Stars:** 0
- **Forks:** 5

## [.project](https://github.com/open-telemetry/.project)

No description provided.

- **Language:** Python
- **Stars:** 0
- **Forks:** 1

## [opentelemetry-zig](https://github.com/open-telemetry/opentelemetry-zig)

No description provided.

- **Language:** N/A
- **Stars:** 0
- **Forks:** 0

## [opentelemetry-packaging](https://github.com/open-telemetry/opentelemetry-packaging)

No description provided.

- **Language:** N/A
- **Stars:** 0
- **Forks:** 0


---

# Intelephense Documentation (from GitHub)

Source: [bmewburn/intelephense-docs](https://github.com/bmewburn/intelephense-docs)

## Readme

# Intelephense

Intelephense is a high performance, cross platform PHP language server adhering to the [Language Server Protocol (LSP)](https://microsoft.github.io/language-server-protocol/).

When paired with an LSP capable editor it provides an essential set of code intelligence features that give a PHP developer a productive and rich editing experience.

This is proprietary software released to end users under a "freemium" model. Many of the features are provided free of charge. Access to all current and future features can be obtained by purchasing a licence key at https://intelephense.com.

### [Installation](installation.md)

### [Getting Started](gettingStarted.md)

### [Features](features.md)

### [Support](support.md)

### [Licence](LICENSE.txt)


---

## Getting Started

## Getting Started

### Workspace

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

### Environment

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

### Type Declarations and Annotations

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

### Framework Support

Intelephense aims to support all frameworks but does not implement framework specific solutions. Some frameworks are coded in a way that make it difficult to analyse. This may be because of lack of type declarations/annotations; heavy use of `__get`, `__set`, `__call`, `__callStatic` magic methods; or dynamic generation of class aliases at runtime.

Packages can be found online that aim to workaround these issues by providing stubs of symbols to help static analysers like Intelephense understand the code.

* Laravel - [barryvdh/laravel-ide-helper](https://github.com/barryvdh/laravel-ide-helper)



---

## Installation

## Installation

### Visual Studio Code

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

### Other Editors

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

---

## Features

## Features

### Workspace Symbols


### Document Symbols


### Go To Definition


### Completion


### Signature Help


### Hover


### Document Highlight


### Find All References


### Document and Range Formatting


### Rename -- [PREMIUM](https://intelephense.com)


### Code Folding -- [PREMIUM](https://intelephense.com)


### Find all Implementations -- [PREMIUM](https://intelephense.com)


### Go to Declaration -- [PREMIUM](https://intelephense.com)


### Go to Type Definition -- [PREMIUM](https://intelephense.com)


### Smart Selection -- [PREMIUM](https://intelephense.com)


### PHP Doc Block Generation -- [PREMIUM](https://intelephense.com)



---

## Support

https://github.com/bmewburn/vscode-intelephense/issues

ben@intelephense.com

---



---

# vscode-intelephense

**Full Name:** bmewburn/vscode-intelephense

**Description:** PHP intellisense for Visual Studio Code

**URL:** https://github.com/bmewburn/vscode-intelephense

**Stars:** 1843 | **Forks:** 113 | **Language:** TypeScript

**License:** Other

---

## README

# Intelephense

PHP code intelligence for Visual Studio Code.

Intelephense is a high performance PHP language server packed full of essential features for productive PHP development.

* Fast camel/underscore case **code completion (IntelliSense)** for document, workspace and built-in symbols and keywords with automatic addition of use declarations.
* Detailed **signature (parameter) help** for document, workspace and built-in constructors, methods, and functions.
* Rapid workspace wide **go to definition** support.
* Workspace wide **find all references**.
* Fast camel/underscore case **workspace symbol search**.
* Full **document symbol search** that also powers **breadcrumbs** and **outline** UI.
* Multiple **diagnostics** for open files via an error tolerant parser and powerful static analysis engine.
* Lossless PSR-12 compatible **document/range formatting**. Formats combined HTML/PHP/JS/CSS files too.
* Embedded **HTML/JS/CSS code intelligence**.
* Detailed **hover** with links to official PHP documentation.
* Smart **highlight** of references and keywords.
* Advanced PHPDoc type system supporting **templates and callable signatures**.
* Reads **PHPStorm metadata** for improved type analysis and suggestions.
* Enhances the official xdebug extension with an **inline values provider**.
* Easy **rename** of symbols. When appropriate, files/folders are automatically renamed too. [PREMIUM](https://intelephense.com)
* Accurate **code folding** of definitions, blocks, use declarations, heredoc, comments, and custom regions. [PREMIUM](https://intelephense.com)
* Quickly **find all implementations** of interfaces and abstract classes and associated methods. [PREMIUM](https://intelephense.com)
* Fast **go to type definition** of typed variables and parameters. [PREMIUM](https://intelephense.com)
* Fast **go to declaration** for methods implementing an interface or abstract method declaration. [PREMIUM](https://intelephense.com)
* Configurable **auto PHPDoc** creation that infers return types and identifies thrown exceptions. [PREMIUM](https://intelephense.com)
* Syntax tree driven **smart select** to intelligently expand/shrink selection. [PREMIUM](https://intelephense.com)
* Helpful **code actions** to import symbols, add PHPDoc, and implement all abstract methods. [PREMIUM](https://intelephense.com)
* Concise **type hierarchy**. Easily view and navigate to subtypes and supertypes. [PREMIUM](https://intelephense.com)
* Insightful **code lens** that shows references, abstract and interface implementations, trait usages, method parent and overrides. [PREMIUM](https://intelephense.com)
* Informative **inlay hints** to indicate parameter names, return types and anonymous function parameter types. [PREMIUM](https://intelephense.com)
* Convenient **document links** to quickly navigate to include/require files. [PREMIUM](https://intelephense.com)
* **`@mixin`** support. [PREMIUM](https://intelephense.com)

## Licence
Purchase a licence at https://intelephense.com to access PREMIUM features. Licence keys grant a single user access to all current and future premium features on multiple devices _forever_. Licence keys must be activated (automatically) via https before use. Features not marked as PREMIUM are free and always will be free.

The language server client (vscode-intelephense) is open source and licensed under the MIT licence.

The language server (intelephense) is proprietary. Please see [here](https://github.com/bmewburn/vscode-intelephense/blob/master/LICENSE.txt#L29) for details.

## Quick Start

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

## Support

Try the [Intelephense Documentation](https://intelephense.com/docs).

Found a bug? Got a feature request? [Create an issue](https://github.com/bmewburn/vscode-intelephense/issues).

## Acknowledgements

A big thank you to supporters who have bought a premium licence and have enabled the continued development and maintenance of this extension.

Intelephense uses the following open source libraries. Please see the following links for source code and licences.

* [vscode-languageserver-node](https://github.com/Microsoft/vscode-languageserver-node)
* [micromatch](https://github.com/micromatch/micromatch)
* [fs-extra](https://github.com/jprichardson/node-fs-extra)
* [fast-glob](https://github.com/mrmlnc/fast-glob)
* [lru-cache](https://github.com/isaacs/node-lru-cache)
* [turndown](https://github.com/mixmark-io/turndown)
* [protobufjs](https://github.com/dcodeIO/ProtoBuf.js/)
* [phpstorm-stubs](https://github.com/JetBrains/phpstorm-stubs)
* [js-beautify](https://github.com/beautify-web/js-beautify)
* [vscode-uri](https://github.com/microsoft/vscode-uri)
* [vscode-html-languageserver](https://github.com/microsoft/vscode)
* [node-html-to-text](https://github.com/html-to-text/node-html-to-text)
* [semver](https://github.com/npm/node-semver)
* [applicationinsights](https://github.com/microsoft/ApplicationInsights-node.js)


---

# IDE Integration

Gemini CLI can integrate with your IDE to provide a more seamless and context-aware experience. This integration allows the CLI to understand your workspace better and enables powerful features like native in-editor diffing.

There are two primary ways to integrate Gemini CLI with an IDE:

*   **VS Code companion extension**: Install the “Gemini CLI Companion” extension on Antigravity, Visual Studio Code, or other VS Code compatible editors.
*   **Agent Client Protocol (ACP)**: An open protocol for interoperability between AI coding agents and IDEs. This method is used for integrations with tools like JetBrains and Zed, which leverage the ACP Agent Registry for easy discovery and installation of compatible agents like Gemini CLI.

## VS Code companion extension

The Gemini CLI Companion extension grants Gemini CLI direct access to your VS Code compatible IDEs and improves your experience by providing real-time context such as open files, cursor positions, and text selection. The extension also enables a native diffing interface so you can seamlessly review and apply AI-generated code changes directly within your editor.

### Features

*   **Workspace context**: The CLI automatically gains awareness of your workspace to provide more relevant and accurate responses. This context includes:
    *   The 10 most recently accessed files in your workspace.
    *   Your active cursor position.
    *   Any text you have selected (up to a 16KB limit; longer selections will be truncated).
*   **Native diffing**: When Gemini suggests code modifications, you can view the changes directly within your IDE’s native diff viewer. This lets you review, edit, and accept or reject the suggested changes seamlessly.
*   **VS Code commands**: You can access Gemini CLI features directly from the VS Code Command Palette (Cmd+Shift+P or Ctrl+Shift+P):
    *   `Gemini CLI: Run`: Starts a new Gemini CLI session in the integrated terminal.
    *   `Gemini CLI: Accept Diff`: Accepts the changes in the active diff editor.
    *   `Gemini CLI: Close Diff Editor`: Rejects the changes and closes the active diff editor.
    *   `Gemini CLI: View Third-Party Notices`: Displays the third-party notices for the extension.

### Installation and setup

There are three ways to set up the IDE integration:

**1. Automatic nudge (recommended)**
When you run Gemini CLI inside a supported editor, it will automatically detect your environment and prompt you to connect. Answering “Yes” will automatically run the necessary setup, which includes installing the companion extension and enabling the connection.

**2. Manual installation from CLI**
If you previously dismissed the prompt or want to install the extension manually, you can run the following command inside Gemini CLI:

`/ide install`

This will find the correct extension for your IDE and install it.

**3. Manual installation from a marketplace**
You can also install the extension directly from a marketplace.

*   For Visual Studio Code: Install from the VS Code Marketplace.
*   For VS Code forks: To support forks of VS Code, the extension is also published on the Open VSX Registry. Follow your editor’s instructions for installing extensions from this registry.

> **Note**
> The “Gemini CLI Companion” extension may appear towards the bottom of search results. If you don’t see it immediately, try scrolling down or sorting by “Newly Published”.
>
> After manually installing the extension, you must run `/ide enable` in the CLI to activate the integration.

### Usage

#### Enabling and disabling

You can control the IDE integration from within the CLI:

To enable the connection to the IDE, run:
`/ide enable`

To disable the connection, run:
`/ide disable`

When enabled, Gemini CLI will automatically attempt to connect to the IDE companion extension.

#### Checking the status

To check the connection status and see the context the CLI has received from the IDE, run:

`/ide status`

If connected, this command will show the IDE it’s connected to and a list of recently opened files it is aware of.

> **Note**
> The file list is limited to 10 recently accessed files within your workspace and only includes local files on disk.

#### Working with diffs

When you ask Gemini to modify a file, it can open a diff view directly in your editor.

To accept a diff, you can perform any of the following actions:
*   Click the checkmark icon in the diff editor’s title bar.
*   Save the file (for example, with Cmd+S or Ctrl+S).
*   Open the Command Palette and run `Gemini CLI: Accept Diff`.
*   Respond with `yes` in the CLI when prompted.

To reject a diff, you can:
*   Click the ‘x’ icon in the diff editor’s title bar.
*   Close the diff editor tab.
*   Open the Command Palette and run `Gemini CLI: Close Diff Editor`.
*   Respond with `no` in the CLI when prompted.

You can also modify the suggested changes directly in the diff view before accepting them.

If you select ‘Allow for this session’ in the CLI, changes will no longer show up in the IDE as they will be auto-accepted.

## Agent Client Protocol (ACP)

ACP is an open protocol that standardizes how AI coding agents communicate with code editors and IDEs. It addresses the challenge of fragmented distribution, where agents traditionally needed custom integrations for each client. With ACP, developers can implement their agent once, and it becomes compatible with any ACP-compliant editor.

For a comprehensive introduction to ACP, including its architecture and benefits, refer to the official ACP Introduction documentation.

### The ACP Agent Registry

Gemini CLI is officially available in the ACP Agent Registry. This allows you to install and update Gemini CLI directly within supporting IDEs and eliminates the need for manual downloads or IDE-specific extensions.

Using the registry ensures:
*   **Ease of use**: Discover and install agents directly within your IDE settings.
*   **Latest versions**: Ensures users always have access to the most up-to-date agent implementations.

For more details on how the registry works, visit the official ACP Agent Registry page. You can learn about how specific IDEs leverage this integration in the following section.

### IDE-specific integration

Gemini CLI is an ACP-compatible agent available in the ACP Agent Registry. Here’s how different IDEs leverage the ACP and the registry:

**JetBrains IDEs**
JetBrains IDEs (like IntelliJ IDEA, PyCharm, or GoLand) offer built-in registry support, allowing users to find and install ACP-compatible agents directly.
For more details, refer to the official JetBrains AI Blog announcement.

**Zed**
Zed, a modern code editor, also integrates with the ACP Agent Registry. This allows Zed users to easily browse, install, and manage ACP agents.
Learn more about Zed’s integration with the ACP Registry in their blog post.

**Other ACP-compatible IDEs**
Any other IDE that supports the ACP Agent Registry can install Gemini CLI directly through their in-built registry features.

### Using with sandboxing

If you are using Gemini CLI within a sandbox, be aware of the following:

*   **On macOS**: The IDE integration requires network access to communicate with the IDE companion extension. You must use a Seatbelt profile that allows network access.
*   **In a Docker container**: If you run Gemini CLI inside a Docker (or Podman) container, the IDE integration can still connect to the VS Code extension running on your host machine. The CLI is configured to automatically find the IDE server on `host.docker.internal`. No special configuration is usually required, but you may need to ensure your Docker networking setup allows connections from the container to the host.

## Troubleshooting

### VS Code companion extension errors

#### Connection errors

**Message:** `🔴 Disconnected: Failed to connect to IDE companion extension in [IDE Name]. Please ensure the extension is running. To install the extension, run /ide install.`
*   **Cause:** Gemini CLI could not find the necessary environment variables (`GEMINI_CLI_IDE_WORKSPACE_PATH` or `GEMINI_CLI_IDE_SERVER_PORT`) to connect to the IDE. This usually means the IDE companion extension is not running or did not initialize correctly.
*   **Solution:**
    1.  Make sure you have installed the Gemini CLI Companion extension in your IDE and that it is enabled.
    2.  Open a new terminal window in your IDE to ensure it picks up the correct environment.

**Message:** `🔴 Disconnected: IDE connection error. The connection was lost unexpectedly. Please try reconnecting by running /ide enable`
*   **Cause:** The connection to the IDE companion was lost.
*   **Solution:** Run `/ide enable` to try and reconnect. If the issue continues, open a new terminal window or restart your IDE.

#### Manual PID override

If automatic IDE detection fails, or if you are running Gemini CLI in a standalone terminal and want to manually associate it with a specific IDE instance, you can set the `GEMINI_CLI_IDE_PID` environment variable to the process ID (PID) of your IDE.

**macOS/Linux**
```bash
export GEMINI_CLI_IDE_PID=12345
```

**Windows (PowerShell)**
```powershell
$env:GEMINI_CLI_IDE_PID=12345
```

When this variable is set, Gemini CLI will skip automatic detection and attempt to connect using the provided PID.

#### Configuration errors

**Message:** `🔴 Disconnected: Directory mismatch. Gemini CLI is running in a different location than the open workspace in [IDE Name]. Please run the CLI from one of the following directories: [List of directories]`
*   **Cause:** The CLI’s current working directory is outside the workspace you have open in your IDE.
*   **Solution:** `cd` into the same directory that is open in your IDE and restart the CLI.

**Message:** `🔴 Disconnected: To use this feature, please open a workspace folder in [IDE Name] and try again.`
*   **Cause:** You have no workspace open in your IDE.
*   **Solution:** Open a workspace in your IDE and restart the CLI.

#### General errors

**Message:** `IDE integration is not supported in your current environment. To use this feature, run Gemini CLI in one of these supported IDEs: [List of IDEs]`
*   **Cause:** You are running Gemini CLI in a terminal or environment that is not a supported IDE.
*   **Solution:** Run Gemini CLI from the integrated terminal of a supported IDE, like Antigravity or VS Code.

**Message:** `No installer is available for IDE. Please install Gemini CLI Companion extension manually from the marketplace.`
*   **Cause:** You ran `/ide install`, but the CLI does not have an automated installer for your specific IDE.
*   **Solution:** Open your IDE’s extension marketplace, search for “Gemini CLI Companion”, and install it manually.

### ACP integration errors

For issues related to ACP integration, refer to the debugging and telemetry section in the ACP Mode documentation.

---

# Remote Subagents

Gemini CLI supports connecting to remote subagents using the Agent-to-Agent (A2A) protocol. This allows Gemini CLI to interact with other agents, expanding its capabilities by delegating tasks to remote services.

Gemini CLI can connect to any compliant A2A agent. You can find samples of A2A agents in the following repositories:

*   ADK Samples (Python)
*   ADK Python Contributing Samples

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

*   **Project-level:** `.gemini/agents/*.md` (Shared with your team)
*   **User-level:** `~/.gemini/agents/*.md` (Personal agents)

### Configuration schema
| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
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

> **Note:** Mixed local and remote agents, or multiple local agents, are not supported in a single file; the list format is currently remote-only.

## Authentication
Many remote agents require authentication. Gemini CLI supports several authentication methods aligned with the A2A security specification. Add an `auth` block to your agent’s frontmatter to configure credentials.

### Supported auth types
Gemini CLI supports the following authentication types:

| Type | Description |
| :--- | :--- |
| `apiKey` | Send a static API key as an HTTP header. |
| `http` | HTTP authentication (Bearer token, Basic credentials, or any IANA-registered scheme). |
| `google-credentials` | Google Application Default Credentials (ADC). Automatically selects access or identity tokens. |
| `oauth` | OAuth 2.0 Authorization Code flow with PKCE. Opens a browser for interactive sign-in. |

### Dynamic values
For `apiKey` and `http` auth types, secret values (key, token, username, password, value) support dynamic resolution:

| Format | Description | Example |
| :--- | :--- | :--- |
| `$ENV_VAR` | Read from an environment variable. | `$MY_API_KEY` |
| `!command` | Execute a shell command and use the trimmed output. | `!gcloud auth print-token` |
| literal | Use the string as-is. | `sk-abc123` |
| `$$` / `!!` | Escape prefix. `$$FOO` becomes the literal `$FOO`. | `$$NOT_AN_ENV_VAR` |

> **Security tip:** Prefer `$ENV_VAR` or `!command` over embedding secrets directly in agent files, especially for project-level agents checked into version control.

### API key (`apiKey`)
Sends an API key as an HTTP header on every request.

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
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
| :--- | :--- | :--- | :--- |
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
| :--- | :--- | :--- | :--- |
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
| :--- | :--- | :--- | :--- |
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
| :--- | :--- | :--- | :--- |
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

### OAuth 2.0 (`oauth`)
Performs an interactive OAuth 2.0 Authorization Code flow with PKCE.

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `type` | string | Yes | Must be `oauth`. |
| `client_id` | string | Yes* | OAuth client ID. Required for interactive auth. |
| `client_secret` | string | No* | OAuth client secret. |
| `scopes` | string[] | No | Requested scopes. |
| `authorization_url` | string | No | Authorization endpoint. |
| `token_url` | string | No | Token endpoint. |

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


If the agent card advertises an oauth2 security scheme with authorizationCode flow, the `authorization_url`, `token_url`, and `scopes` are automatically discovered. You only need to provide `client_id` (and `client_secret` if required).

Tokens are persisted to disk and refreshed automatically when they expire.

### Auth validation
When Gemini CLI loads a remote agent, it validates your auth configuration against the agent card’s declared securitySchemes. If the agent requires authentication that you haven’t configured, you’ll see an error describing what’s needed.

`google-credentials` is treated as compatible with `http` Bearer security schemes, since it produces Bearer tokens.

### Auth retry behavior
All auth providers automatically retry on 401 and 403 responses by re-fetching credentials (up to 2 retries). This handles cases like expired tokens or rotated credentials. For `apiKey` with `!command` values, the command is re-executed on retry to fetch a fresh key.

### Agent card fetching and auth
When connecting to a remote agent, Gemini CLI first fetches the agent card without authentication. If the card endpoint returns a 401 or 403, it retries the fetch with the configured auth headers. This lets agents have publicly accessible cards while protecting their task endpoints, or to protect both behind auth.

## Managing Subagents
Users can manage subagents using the following commands within Gemini CLI:

*   `/agents list`: Displays all available local and remote subagents.
*   `/agents reload`: Reloads the agent registry. Use this after adding or modifying agent definition files.
*   `/agents enable <agent_name>`: Enables a specific subagent.
*   `/agents disable <agent_name>`: Disables a specific subagent.

> **Tip**
>
> You can use the `@cli_help` agent within Gemini CLI for assistance with configuring subagents.

### Disabling remote agents
Remote subagents are enabled by default. To disable them, set `enableAgents` to false in your `settings.json`:

```json
{
  "experimental": {
    "enableAgents": false
  }
}
```


---

# Knowledge Merge

Knowledge Merge is a process or document that merges key concepts currently spread across Antigravity, Project SOR, the live software-online-review.com domain, and the new software-review-platform starter. It creates one canonical map of what each layer is, what role it plays, and how the project should evolve.

---
All the best - https://markposition.wordpress.com

---

# Understanding GitHub Actions

Learn the basics of core concepts and essential terminology in GitHub Actions.

## Overview

GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. You can create workflows that build and test every pull request to your repository, or deploy merged pull requests to production.

GitHub Actions goes beyond just DevOps and lets you run workflows when other events happen in your repository. For example, you can run a workflow to automatically add the appropriate labels whenever someone creates a new issue in your repository.

GitHub provides Linux, Windows, and macOS virtual machines to run your workflows, or you can host your own self-hosted runners in your own data center or cloud infrastructure.

## The components of GitHub Actions

You can configure a GitHub Actions workflow to be triggered when an event occurs in your repository, such as a pull request being opened or an issue being created. Your workflow contains one or more jobs which can run in sequential order or in parallel. Each job will run inside its own virtual machine runner, or inside a container, and has one or more steps that either run a script that you define or run an action, which is a reusable extension that can simplify your workflow.

Diagram of an event triggering Runner 1 to run Job 1, which triggers Runner 2 to run Job 2. Each of the jobs is broken into multiple steps.

## Workflows

A workflow is a configurable automated process that will run one or more jobs. Workflows are defined by a YAML file checked in to your repository and will run when triggered by an event in your repository, or they can be triggered manually, or at a defined schedule.

Workflows are defined in the .github/workflows directory in a repository. A repository can have multiple workflows, each of which can perform a different set of tasks such as:

Building and testing pull requests
Deploying your application every time a release is created
Adding a label whenever a new issue is opened
You can reference a workflow within another workflow. For more information, see Reuse workflows.

For more information, see Writing workflows.

## Events

An event is a specific activity in a repository that triggers a workflow run. For example, an activity can originate from GitHub when someone creates a pull request, opens an issue, or pushes a commit to a repository. You can also trigger a workflow to run on a schedule, by posting to a REST API, or manually.

For a complete list of events that can be used to trigger workflows, see Events that trigger workflows.

## Jobs

A job is a set of steps in a workflow that is executed on the same runner. Each step is either a shell script that will be executed, or an action that will be run. Steps are executed in order and are dependent on each other. Since each step is executed on the same runner, you can share data from one step to another. For example, you can have a step that builds your application followed by a step that tests the application that was built.

You can configure a job's dependencies with other jobs; by default, jobs have no dependencies and run in parallel. When a job takes a dependency on another job, it waits for the dependent job to complete before running.

You can also use a matrix to run the same job multiple times, each with a different combination of variables—like operating systems or language versions.

For example, you might configure multiple build jobs for different architectures without any job dependencies and a packaging job that depends on those builds. The build jobs run in parallel, and once they complete successfully, the packaging job runs.

For more information, see Choosing what your workflow does.

## Actions

An action is a pre-defined, reusable set of jobs or code that performs specific tasks within a workflow, reducing the amount of repetitive code you write in your workflow files. Actions can perform tasks such as:

Pulling your Git repository from GitHub
Setting up the correct toolchain for your build environment
Setting up authentication to your cloud provider
You can write your own actions, or you can find actions to use in your workflows in the GitHub Marketplace.

For more information on actions, see Reusing automations.

## Runners

A runner is a server that runs your workflows when they're triggered. Each runner can run a single job at a time. GitHub provides Ubuntu Linux, Microsoft Windows, and macOS runners to run your workflows. Each workflow run executes in a fresh, newly-provisioned virtual machine.

GitHub also offers larger runners, which are available in larger configurations. For more information, see Using larger runners.

If you need a different operating system or require a specific hardware configuration, you can host your own runners.

For more information about self-hosted runners, see Managing self-hosted runners.

## Next steps

GitHub Actions can help you automate nearly every aspect of your application development processes. Ready to get started? Here are some helpful resources for taking your next steps with GitHub Actions:

To create a GitHub Actions workflow, see Using workflow templates.
For continuous integration (CI) workflows, see Building and testing your code.
For building and publishing packages, see Publishing packages.
For deploying projects, see Deploying to third-party platforms.
For automating tasks and processes on GitHub, see Managing your work with GitHub Actions.
For examples that demonstrate more complex features of GitHub Actions, see Managing your work with GitHub Actions. These detailed examples explain how to test your code on a runner, access the GitHub CLI, and use advanced features such as concurrency and test matrices.
To certify your proficiency in automating workflows and accelerating development with GitHub Actions, earn a GitHub Actions certificate with GitHub Certifications. For more information, see About GitHub Certifications.
