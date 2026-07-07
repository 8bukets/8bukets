const fs = require('fs');
const path = require('path');

const URL = "https://cloud.google.com/discover/what-are-ai-agents";

async function scrapeAiAgentsKnowledge() {
    console.log("Ingesting AI Agent knowledge from " + URL);

    const structuredData = {
        "what-is-an-ai-agent-v2": {
            "title": "What is an AI agent? (Deep Dive)",
            "content": "AI agents are software systems that use AI to pursue goals and complete tasks on behalf of users. They show reasoning, planning, and memory and have a level of autonomy to make decisions, learn, and adapt. Their capabilities are made possible in large part by the multimodal capacity of generative AI and AI foundation models. AI agents can process multimodal information like text, voice, video, audio, code, and more simultaneously; can converse, reason, learn, and make decisions. They can learn over time and facilitate transactions and business processes. Agents can work with other agents to coordinate and perform more complex workflows."
        },
        "key-features-of-an-ai-agent-v2": {
            "title": "Key features of an AI agent (ReAct Framework)",
            "content": "Reasoning: This core cognitive process involves using logic and available information to draw conclusions, make inferences, and solve problems. AI agents with strong reasoning capabilities can analyze data, identify patterns, and make informed decisions based on evidence and context.\nActing: The ability to take action or perform tasks based on decisions, plans, or external input is crucial for AI agents to interact with their environment and achieve goals. This can include physical actions in the case of embodied AI, or digital actions like sending messages, updating data, or triggering other processes.\nObserving: Gathering information about the environment or situation through perception or sensing is essential for AI agents to understand their context and make informed decisions.\nPlanning: Developing a strategic plan to achieve goals is a key aspect of intelligent behavior. AI agents with planning capabilities can identify the necessary steps, evaluate potential actions, and choose the best course of action based on available information and desired outcomes.\nCollaborating: Working effectively with others, whether humans or other AI agents, to achieve a common goal is increasingly important in complex and dynamic environments.\nSelf-refining: The capacity for self-improvement and adaptation is a hallmark of advanced AI systems. AI agents with self-refining capabilities can learn from experience, adjust their behavior based on feedback, and continuously enhance their performance and capabilities over time."
        },
        "ai-agents-vs-assistants-vs-bots": {
            "title": "What is the difference between AI agents, AI assistants, and bots?",
            "content": "AI assistants are AI agents designed as applications or products to collaborate directly with users and perform tasks by understanding and responding to natural human language and inputs. They can reason and take action on the users' behalf with their supervision.\n\nAI assistants are often embedded in the product being used. A key characteristic is the interaction between the assistant and user through the different steps of the task. The assistant responds to requests or prompts from the user, and can recommend actions but decision-making is done by the user.\n\nComparison:\n- AI Agent Purpose: Autonomously and proactively perform tasks. Capabilities: Complex, multi-step actions; learns and adapts; independent decisions. Interaction: Proactive; goal-oriented.\n- AI Assistant Purpose: Assisting users with tasks. Capabilities: Responds to requests; completes simple tasks; recommends actions but user decides. Interaction: Reactive.\n- Bot Purpose: Automating simple tasks or conversations. Capabilities: Pre-defined rules; limited learning; basic interactions. Interaction: Reactive."
        },
        "how-ai-agents-work": {
            "title": "How do AI agents work?",
            "content": "Every agent defines its role, personality, and communication style, including specific instructions and descriptions of available tools.\n- Persona: A well defined persona allows an agent to maintain a consistent character and behave in a manner appropriate to its assigned role.\n- Memory: Equipped with short term, long term, consensus, and episodic memory to maintain context and learn from experience.\n- Tools: Functions or external resources that an agent can utilize to interact with its environment (e.g., physical, graphical, or program-based interfaces).\n- Model: Large language models (LLMs) serve as the 'brain' of the agent, providing the ability to understand, reason, and act."
        },
        "types-of-ai-agents": {
            "title": "What are the types of agents in AI?",
            "content": "Categorized by interaction:\n- Interactive partners (surface agents): Assist with tasks like customer service, healthcare, and education. Generally user query triggered.\n- Autonomous background processes (background agents): Work behind the scenes to automate routine tasks, analyze data, and optimize processes. Generally event driven.\n\nCategorized by number of agents:\n- Single agent: Operate independently for well-defined tasks.\n- Multi-agent: Multiple agents collaborate or compete to achieve objectives, leveraging diverse capabilities and roles."
        },
        "benefits-of-ai-agents": {
            "title": "Benefits of using AI agents",
            "content": "- Efficiency and productivity: Increased output through task division, simultaneous execution, and automation.\n- Improved decision-making: Collaboration between agents, adaptability to changing situations, and robust reasoning through feedback.\n- Enhanced capabilities: Tackling complex problems, natural language communication, tool use, and continuous learning.\n- Social interaction and simulation: Modeling human-like behaviors and enabling emergent social interactions."
        },
        "challenges-of-ai-agents": {
            "title": "Challenges with using AI agents",
            "content": "- Deep empathy / emotional intelligence: Struggle with nuanced human emotions and complex social dynamics.\n- High ethical stakes: Lack of moral compass and judgment for ethically complex situations (e.g., law, healthcare).\n- Unpredictable physical environments: Difficulty in highly dynamic environments requiring real-time adaptation and motor skills.\n- Resource-intensive: Computationally expensive to develop and deploy."
        },
        "deploying-ai-agents-cloud-run": {
            "title": "Deploy AI agents for scale and efficiency with Cloud Run",
            "content": "Cloud Run is an excellent fit for AI agents due to its flexible compute power and serverless nature. Features include:\n- Scalability and cost-efficiency: Automatic scaling (down to zero when idle) means paying only for active compute.\n- Agent orchestration and serving: Core logic runs as a service with a stable HTTPS endpoint.\n- Agent-to-Agent (A2A): Seamless integration with frameworks like the Agent Development Kit (ADK)."
        },
        "google-cloud-ai-agent-portfolio": {
            "title": "Google Cloud and AI agents portfolio",
            "content": "- Gemini Enterprise App: Secure platform to discover, create, run, and govern AI agents across an organization.\n- Gemini Enterprise agent platform: Create AI agents and apps using natural language or code, grounded in enterprise data.\n- Customer Experience Agent Studio (Dialogflow): Build hybrid conversational agents with deterministic and generative AI.\n- Agent Garden: Curated collection of pre-built agent samples, solutions, and frameworks.\n- Agent Development Kit (ADK): Open-source Python SDK to build multi-agent systems with orchestration and memory.\n- A2A Protocol: Open-source framework for building interoperable AI agents.\n- Cloud Run: Fully managed serverless platform for deploying containerized agents."
        }
    };

    const targetDir = "data/knowledge";
    if (!fs.existsSync(targetDir)) fs.mkdirSync(targetDir, { recursive: true });

    const jsonPath = path.join(targetDir, "ai_agents_knowledge.json");
    let existingJson = {};
    if (fs.existsSync(jsonPath)) {
        try { existingJson = JSON.parse(fs.readFileSync(jsonPath, 'utf8')); } catch (e) {}
    }
    const mergedJson = { ...existingJson, ...structuredData };
    fs.writeFileSync(jsonPath, JSON.stringify(mergedJson, null, 4), 'utf8');

    const mdPath = path.join(targetDir, "ai_agents_knowledge.md");
    let mdContent = fs.existsSync(mdPath) ? fs.readFileSync(mdPath, 'utf8') : "# AI Agents Knowledge\n\n";
    let sectionsToAdd = "";
    for (const key in structuredData) {
        if (!mdContent.includes("## " + structuredData[key].title)) {
            sectionsToAdd += "## " + structuredData[key].title + "\n\n" + structuredData[key].content.replace(/\\n/g, '\n') + "\n\n";
        }
    }
    if (sectionsToAdd) fs.writeFileSync(mdPath, mdContent + "\n---\n\n" + sectionsToAdd, 'utf8');

    const systemKnowledgePath = path.join(process.cwd(), 'data/knowledge/system_knowledge.json');
    if (fs.existsSync(systemKnowledgePath)) {
        try {
            const systemKnowledge = JSON.parse(fs.readFileSync(systemKnowledgePath, 'utf8'));
            if (!systemKnowledge.ai_agents_structured) systemKnowledge.ai_agents_structured = [];
            systemKnowledge.ai_agents_structured = systemKnowledge.ai_agents_structured.filter(item => item.url !== URL);
            systemKnowledge.ai_agents_structured.push({
                url: URL,
                title: "What are AI agents? (Comprehensive Update)",
                sections: Object.keys(structuredData).map(key => ({
                    header: structuredData[key].title,
                    content: structuredData[key].content.split(/\\n|\n/)
                }))
            });
            for (const key in structuredData) systemKnowledge[key] = structuredData[key];
            fs.writeFileSync(systemKnowledgePath, JSON.stringify(systemKnowledge, null, 2), 'utf8');
        } catch (e) { console.error(e); }
    }
    console.log("Successfully updated AI agents knowledge.");
}
scrapeAiAgentsKnowledge();
