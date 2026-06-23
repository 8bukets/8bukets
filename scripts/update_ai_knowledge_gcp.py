import json
import os

def update_knowledge():
    json_path = "data/knowledge/ai_agents_knowledge.json"
    md_path = "data/knowledge/ai_agents_knowledge.md"

    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found.")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        knowledge = json.load(f)

    # New/Updated content from https://cloud.google.com/discover/what-are-ai-agents
    # Refined for maximum intelligence value
    gcp_knowledge = {
        "what-is-an-ai-agent": {
            "title": "What is an AI agent?",
            "content": "AI agents are software systems that use AI to pursue goals and complete tasks on behalf of users. They exhibit reasoning, planning, and memory, and possess a degree of autonomy to make decisions, learn, and adapt. Their capabilities are primarily driven by the multimodal capacity of generative AI and foundation models, allowing them to process text, voice, video, and code simultaneously."
        },
        "key-features-of-an-ai-agent": {
            "title": "Key features of an AI agent",
            "content": "Modern AI agents have evolved to include several core cognitive and operational features:\n\n- **Reasoning**: Using logic and available information to draw conclusions and solve problems.\n- **Acting**: The ability to perform digital (sending messages, updating data) or physical (embodied AI) actions.\n- **Observing**: Gathering environmental information through perception (computer vision, NLP, sensors).\n- **Planning**: Developing strategic steps to achieve goals, including anticipating future states.\n- **Collaborating**: Working effectively with humans or other agents via communication and coordination.\n- **Self-refining**: Learning from experience and feedback to continuously enhance performance over time."
        },
        "what-is-the-difference-between-ai-agents-ai-assistants-and-bots": {
            "title": "Difference between AI Agents, AI Assistants, and Bots",
            "content": "The primary distinctions lie in autonomy and complexity:\n\n- **AI Agents**: Highest autonomy; proactive and goal-oriented; can perform complex multi-step actions and make independent decisions.\n- **AI Assistants**: Moderate autonomy; reactive to user prompts; assist with tasks while decision-making remains with the user.\n- **Bots**: Lowest autonomy; follow pre-defined rules; limited learning; automate simple, repetitive tasks."
        },
        "how-do-ai-agents-work": {
            "title": "How do AI agents work?",
            "content": "AI agents are built on four functional pillars:\n\n- **Persona**: A defined role, personality, and communication style that evolves with experience.\n- **Memory**: Includes short-term (immediate interaction), long-term (historical), episodic (past events), and consensus (shared among agents) memory.\n- **Tools**: External resources (APIs, UI-based tools) that allow agents to interact with and manipulate their environment.\n- **Model**: LLMs act as the 'brain', providing the underlying understanding and reasoning capacity."
        },
        "what-are-the-types-of-agents-in-ai": {
            "title": "Types of agents in AI",
            "content": "Agents can be categorized by interaction or scale:\n\n- **Surface Agents (Interactive Partners)**: Engage in direct conversation to assist with customer service, education, or healthcare.\n- **Background Agents (Autonomous Processes)**: Work behind the scenes to automate workflows and optimize processes with limited human interaction.\n- **Single Agent**: Operates independently to achieve a specific goal using a single foundation model.\n- **Multi-agent**: Multiple agents collaborate or compete, potentially using different foundation models for diverse roles."
        },
        "benefits-of-using-ai-agents": {
            "title": "Benefits of using AI agents",
            "content": "- **Efficiency**: Increased output through simultaneous execution and repetitive task automation.\n- **Decision-making**: Robust reasoning through collaboration and adaptable strategies.\n- **Social Interaction**: Emergent social behaviors and realistic simulations.\n- **Problem Solving**: Complex problem-solving by combining agent strengths."
        },
        "challenges-with-using-ai-agents": {
            "title": "Challenges with using AI agents",
            "content": "- **Empathy**: Struggle with deep emotional intelligence and nuanced social dynamics.\n- **Ethical Stakes**: Lack a moral compass for high-stakes decisions (e.g., legal, medical).\n- **Physical Environments**: Difficulty adapting to unpredictable physical tasks requiring complex motor skills.\n- **Resource Intensity**: Computationally expensive to develop and deploy at scale."
        },
        "deploy-ai-agents-for-scale-and-efficiency-with-cloud-run": {
            "title": "Deploying AI agents with Cloud Run",
            "content": "Cloud Run is a serverless platform ideal for deploying scalable AI agents:\n\n- **Scalability**: Auto-scales container instances and can scale to zero when idle to minimize costs.\n- **Orchestration**: Logic runs as a service providing stable HTTPS endpoints for API access.\n- **A2A Integration**: Seamlessly works with the Agent Development Kit (ADK) for multi-agent systems."
        },
        "google-cloud-and-ai-agents": {
            "title": "Google Cloud AI Agents Portfolio",
            "content": "Google Cloud provides a comprehensive set of tools for agent development:\n\n- **Gemini Enterprise App**: Secure platform to govern AI agents across an organization.\n- **Gemini Enterprise Agent Platform**: Build agents grounded in enterprise data using natural language or code.\n- **Customer Experience Agent Studio (Dialogflow)**: Build hybrid conversational agents.\n- **Agent Garden**: A curated collection of pre-built agent samples and tools.\n- **Agent Development Kit (ADK)**: Open-source Python SDK for building sophisticated multi-agent systems.\n- **A2A Protocol**: Open-source framework for interoperable agent-to-agent communication.\n- **Cloud Run**: Fully managed serverless platform for deploying containerized agents."
        },
        "customer-agents": {
            "title": "Customer agents",
            "content": "Customer agents deliver personalized customer experiences by understanding customer needs, answering questions, resolving customer issues, or recommending the right products and services. They work seamlessly across multiple channels including the web, mobile, or point of sale, and can be integrated into product experiences with voice or video."
        },
        "employee-agents": {
            "title": "Employee agents",
            "content": "Employee agents boost productivity by streamlining processes, managing repetitive tasks, answering employee questions, as well as editing and translating critical content and communications."
        },
        "creative-agents": {
            "title": "Creative agents",
            "content": "Creative agents supercharge the design and creative process by generating content, images, and ideas, assisting with design, writing, personalization, and campaigns."
        },
        "data-agents": {
            "title": "Data agents",
            "content": "Data agents are built for complex data analysis. They have the potential to find and act on meaningful insights from data, all while ensuring the factual integrity of their results."
        },
        "code-agents": {
            "title": "Code agents",
            "content": "Code agents accelerate software development with AI-enabled code generation and coding assistance, and to ramp up on new languages and code bases. Many organizations are seeing significant gains in productivity, leading to faster deployment and cleaner, clearer code."
        },
        "security-agents": {
            "title": "Security agents",
            "content": "Security agents strengthen security posture by mitigating attacks or increasing the speed of investigations. They can oversee security across various surfaces and stages of the security life cycle: prevention, detection, and response."
        }
    }

    # Redundant/Legacy slugs to remove (kept the ones needed by KnowledgeAgent)
    redundant_slugs = [
        "key-differences",
        "based-on-interaction",
        "based-on-number-of-agents",
        "efficiency-and-productivity",
        "improved-decision-making",
        "enhanced-capabilities",
        "social-interaction-and-simulation",
        "use-cases-for-ai-agents",
        "key-differences-autonomy-complexity-learning"
    ]

    for slug in redundant_slugs:
        if slug in knowledge:
            del knowledge[slug]

    # Update/Add to JSON
    for slug, data in gcp_knowledge.items():
        knowledge[slug] = data

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(knowledge, f, indent=4, ensure_ascii=False)

    # Sync to Markdown
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# AI Agents Knowledge base\n\n")
        sorted_keys = sorted(knowledge.keys())
        for slug in sorted_keys:
            item = knowledge[slug]
            f.write(f"### {item.get('title', slug)}\n\n")
            f.write(f"{item.get('content', '')}\n\n")
            if 'source' in item:
                f.write(f"*Source: {item['source']}*\n\n")
            f.write("---\n\n")

    print(f"Successfully updated {json_path} and {md_path} with refined GCP AI Agents knowledge.")

if __name__ == "__main__":
    update_knowledge()
