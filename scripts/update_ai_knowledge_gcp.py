import json
import os

def update_knowledge():
    json_path = "data/knowledge/ai_agents_knowledge.json"
    md_path = "data/knowledge/ai_agents_knowledge.md"
    system_json_path = "data/knowledge/system_knowledge.json"

    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found.")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        knowledge = json.load(f)

    # Enhanced content from https://cloud.google.com/discover/what-are-ai-agents
    gcp_knowledge = {
        "what-is-an-ai-agent": {
            "title": "What is an AI agent?",
            "content": "AI agents are software systems that use AI to pursue goals and complete tasks on behalf of users. They show reasoning, planning, and memory and have a level of autonomy to make decisions, learn, and adapt. Their capabilities are enabled by the multimodal capacity of generative AI and foundation models (processing text, voice, video, audio, code simultaneously). They can coordinate with other agents for complex workflows."
        },
        "key-features-of-an-ai-agent": {
            "title": "Key features of an AI agent",
            "content": "Modern AI agents utilize the ReAct (Reasoning and Acting) framework and have evolved to include:\n\n- **Reasoning**: Using logic and information to draw conclusions and solve problems.\n- **Acting**: Digital or physical actions based on decisions and plans.\n- **Observing**: Gathering environmental info through computer vision, NLP, or sensors.\n- **Planning**: Developing strategic steps and anticipating future states.\n- **Collaborating**: Working with humans and other agents via communication.\n- **Self-refining**: Continuous performance enhancement through experience and feedback."
        },
        "what-is-the-difference-between-ai-agents-ai-assistants-and-bots": {
            "title": "Difference between AI Agents, AI Assistants, and Bots",
            "content": "The primary distinctions lie in autonomy, complexity, and learning:\n\n- **AI Agents**: Highest autonomy; proactive and goal-oriented; handle complex workflows; employ machine learning to improve.\n- **AI Assistants**: Moderate autonomy; reactive to user prompts; embedded in products; decision-making remains with the user.\n- **Bots**: Lowest autonomy; follow pre-defined rules; basic interactions; limited or no learning."
        },
        "how-do-ai-agents-work": {
            "title": "How do AI agents work?",
            "content": "AI agents are built on four functional pillars:\n\n- **Persona**: Defined role, personality, and communication style.\n- **Memory**: Includes Short-term (immediate), Long-term (historical), Episodic (past interactions), and Consensus (shared information among agents).\n- **Tools**: External resources (APIs, UI-based tools) categorized as physical, graphical, or program-based. Tool learning is essential for effective use.\n- **Model**: LLMs serve as the 'brain', facilitating reason and action."
        },
        "what-are-the-types-of-agents-in-ai": {
            "title": "Types of agents in AI",
            "content": "Agents are categorized by interaction style and scale:\n\n- **Surface Agents (Interactive Partners)**: Direct conversation (customer service, healthcare).\n- **Background Agents (Autonomous Processes)**: Routine task automation and data analysis without direct user input.\n- **Single Agent**: Operates independently with one foundation model.\n- **Multi-agent**: Collaboration or competition among multiple agents, each potentially using different models."
        },
        "based-on-interaction": {
            "title": "Based on interaction",
            "content": "- **Interactive partners (Surface agents)**: Assist with tasks like customer service and education through personalized support and Q&A.\n- **Autonomous background processes (Background agents)**: Automate routine tasks, analyze data, and optimize processes behind the scenes (e.g., workflow agents)."
        },
        "based-on-number-of-agents": {
            "title": "Based on number of agents",
            "content": "- **Single agent**: Best for well-defined tasks using a single foundation model and external tools.\n- **Multi-agent**: Multiple agents collaborating/competing for complex tasks, leveraging diverse roles and multiple foundation models."
        },
        "benefits-of-using-ai-agents": {
            "title": "Benefits of using AI agents",
            "content": "- **Efficiency**: Increased output through simultaneous execution and automation.\n- **Improved Decision-making**: Adaptable strategies and robust reasoning through collaboration.\n- **Enhanced Capabilities**: Complex problem-solving and natural language communication.\n- **Social Interaction**: Realistic simulations and emergent social behaviors."
        },
        "challenges-with-using-ai-agents": {
            "title": "Challenges with using AI agents",
            "content": "- **Empathy**: Difficulty with deep emotional intelligence and nuanced social dynamics.\n- **Ethics**: Lack a moral compass for high-stakes decisions.\n- **Unpredictable Environments**: Struggles in highly dynamic physical environments.\n- **Resources**: Computationally expensive development and deployment."
        },
        "deploy-ai-agents-for-scale-and-efficiency-with-cloud-run": {
            "title": "Deploying AI agents with Cloud Run",
            "content": "Cloud Run provides a serverless platform for scalable AI agents:\n\n- **Scalability**: Auto-scaling (including scale to zero) ensures cost-efficiency.\n- **Orchestration**: Core agent logic runs as a service with stable HTTPS endpoints.\n- **A2A Integration**: Frameworks like the Agent Development Kit (ADK) integrate seamlessly."
        },
        "google-cloud-and-ai-agents": {
            "title": "Google Cloud AI Agents Portfolio",
            "content": "- **Gemini Enterprise App**: Discover, create, and govern agents.\n- **Gemini Enterprise Agent Platform**: Create agents grounded in enterprise data.\n- **Customer Experience Agent Studio**: Build conversational agents via Dialogflow.\n- **Agent Garden**: Curated collection of pre-built samples and tools.\n- **Agent Development Kit (ADK)**: Open-source Python/TS SDK for multi-agent systems.\n- **A2A Protocol**: Open-source framework for interoperable agent communication.\n- **Cloud Run**: Fully managed serverless platform for deployment.\n- **Agent Search**: Google-quality search for enterprise applications."
        },
        "customer-agents": {
            "title": "Customer agents",
            "content": "Deliver personalized customer experiences across multiple channels (web, mobile, POS) using voice or video integration."
        },
        "employee-agents": {
            "title": "Employee agents",
            "content": "Boost productivity by streamlining processes, managing repetitive tasks, and editing/translating critical communications."
        },
        "creative-agents": {
            "title": "Creative agents",
            "content": "Supercharge design by generating content, images, and ideas, and assisting with writing and personalization."
        },
        "data-agents": {
            "title": "Data agents",
            "content": "Built for complex data analysis, finding and acting on meaningful insights while ensuring factual integrity."
        },
        "code-agents": {
            "title": "Code agents",
            "content": "Accelerate software development with AI-enabled code generation and assistance, leading to faster deployment and cleaner code."
        },
        "security-agents": {
            "title": "Security agents",
            "content": "Strengthen security posture by mitigating attacks and increasing the speed of investigations across the lifecycle."
        }
    }

    # Update/Add to JSON
    for slug, data in gcp_knowledge.items():
        knowledge[slug] = data

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(knowledge, f, indent=4, ensure_ascii=False)

    # Sync to Markdown
    with open(md_path, "w", encoding="utf-8") as f:
        url = "https://cloud.google.com/discover/what-are-ai-agents"
        f.write(f"# AI Agents Knowledge base\n\nScraped from: {url}\n\n")
        sorted_keys = sorted(knowledge.keys())
        for slug in sorted_keys:
            item = knowledge[slug]
            f.write(f"### {item.get('title', slug)}\n\n")
            f.write(f"{item.get('content', '')}\n\n")
            if 'source' in item:
                f.write(f"*Source: {item['source']}*\n\n")
            f.write("---\n\n")

        f.write(f"All the best - {url}\n")

    # Update system_knowledge.json
    if os.path.exists(system_json_path):
        with open(system_json_path, "r", encoding="utf-8") as f:
            system_knowledge = json.load(f)

        if "ai_agents_structured" not in system_knowledge:
            system_knowledge["ai_agents_structured"] = []

        url = "https://cloud.google.com/discover/what-are-ai-agents"
        # Remove old entry
        system_knowledge["ai_agents_structured"] = [e for e in system_knowledge["ai_agents_structured"] if e.get("url") != url]

        new_entry = {
            "url": url,
            "title": "What are AI agents? (GCP Discovery)",
            "sections": [
                {"header": data["title"], "content": [data["content"]]} for slug, data in gcp_knowledge.items()
            ]
        }
        system_knowledge["ai_agents_structured"].append(new_entry)

        with open(system_json_path, "w", encoding="utf-8") as f:
            json.dump(system_knowledge, f, indent=2, ensure_ascii=False)

    print(f"Successfully updated {json_path}, {md_path}, and {system_json_path} with comprehensive GCP AI Agents knowledge.")

if __name__ == "__main__":
    update_knowledge()
