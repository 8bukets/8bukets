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
    gcp_knowledge = {
        "what-is-an-ai-agent": {
            "title": "What is an AI agent?",
            "content": "AI agents are software systems that use AI to pursue goals and complete tasks on behalf of users. They show reasoning, planning, and memory and have a level of autonomy to make decisions, learn, and adapt.\n\nTheir capabilities are made possible in large part by the multimodal capacity of generative AI and AI foundation models. AI agents can process multimodal information like text, voice, video, audio, code, and more simultaneously; can converse, reason, learn, and make decisions. They can learn over time and facilitate transactions and business processes. Agents can work with other agents to coordinate and perform more complex workflows."
        },
        "key-features-of-an-ai-agent": {
            "title": "Key features of an AI agent",
            "content": "The key features of an AI agent have evolved beyond reasoning and acting (ReAct Framework):\n\n- Reasoning: Using logic and information to draw conclusions and solve problems.\n- Acting: Taking action or performing tasks based on decisions or plans.\n- Observing: Gathering information about the environment through perception (vision, NLP, sensors).\n- Planning: Developing strategic steps to achieve goals, anticipating future states.\n- Collaborating: Working with humans or other agents via communication and coordination.\n- Self-refining: Learning from experience and feedback to continuously enhance performance."
        },
        "what-is-the-difference-between-ai-agents-ai-assistants-and-bots": {
            "title": "What is the difference between AI agents, AI assistants, and bots?",
            "content": "AI assistants are designed to collaborate directly with users, responding to requests and recommending actions, but decision-making remains with the user. Bots automate simple, rule-based tasks.\n\n| Feature | AI Agent | AI Assistant | Bot |\n| :--- | :--- | :--- | :--- |\n| **Purpose** | Autonomously perform tasks | Assisting users with tasks | Automating simple tasks |\n| **Capabilities** | Complex actions, learns/adapts | Responds to prompts, recommends | Pre-defined rules, limited learning |\n| **Interaction** | Proactive; goal-oriented | Reactive; user-triggered | Reactive; trigger-based |"
        },
        "key-differences-autonomy-complexity-learning": {
            "title": "Key differences: Autonomy, Complexity, Learning",
            "content": "- Autonomy: AI agents have the highest degree, making independent decisions. Assistants require direction; bots follow rules.\n- Complexity: AI agents handle complex workflows; assistants and bots handle simpler tasks.\n- Learning: AI agents employ machine learning to adapt over time. Assistants have some learning; bots have little to none."
        },
        "how-do-ai-agents-work": {
            "title": "How do AI agents work?",
            "content": "Agents are built on four main pillars:\n\n- Persona: A defined role, personality, and communication style.\n- Memory: Equipped with short-term (immediate), long-term (historical), episodic (past interactions), and consensus (shared) memory.\n- Memory Type: Short term memory for immediate interactions, long-term memory for historical data and conversations, episodic memory for past interactions, and consensus memory for shared information among agents.\n- Tools: Functions or resources used to interact with the environment (API, physical, graphical).\n- Model: LLMs serve as the 'brain', enabling understanding, reasoning, and action."
        },
        "what-are-the-types-of-agents-in-ai": {
            "title": "What are the types of agents in AI?",
            "content": "Categorized by interaction or number:\n\n- Interactive Partners (Surface Agents): Directly assist users (e.g., customer service, healthcare).\n- Autonomous Background Processes (Background Agents): Work behind the scenes to automate workflows and optimize processes.\n- Single Agent: Operates independently for well-defined tasks.\n- Multi-agent: Multiple agents collaborate or compete, leveraging diverse roles for complex objectives."
        },
        "benefits-of-using-ai-agents": {
            "title": "Benefits of using AI agents",
            "content": "- Efficiency & Productivity: Increased output via task division, simultaneous execution, and automation.\n- Improved Decision-making: Collaboration, adaptability, and robust reasoning through feedback.\n- Enhanced Capabilities: Complex problem-solving, natural language communication, and tool use.\n- Social Interaction: Realistic simulations and emergent behavior."
        },
        "challenges-with-using-ai-agents": {
            "title": "Challenges with using AI agents",
            "content": "- Emotional Intelligence: Struggle with deep empathy or nuanced human social dynamics.\n- Ethical Stakes: Lack a moral compass for complex ethical judgment (law, healthcare, judicial).\n- Unpredictable Environments: Struggle in dynamic physical environments requiring real-time adaptation (surgery, disaster response).\n- Resource Intensity: Computationally expensive to develop and deploy."
        },
        "deploy-ai-agents-for-scale-and-efficiency-with-cloud-run": {
            "title": "Deploy AI agents with Cloud Run",
            "content": "Cloud Run provides a scalable, serverless platform for agent deployment:\n\n- Scalability: Auto-scales to meet demand and scales to zero when idle.\n- Orchestration: Logic runs as a service with stable HTTPS endpoints.\n- A2A Support: Integrates with Agent Development Kit (ADK) for multi-agent systems."
        },
        "use-cases-for-ai-agents": {
            "title": "Use cases for AI agents",
            "content": "Organizations have been deploying agents across six key categories:\n\n- Customer Agents: Personalized experiences across channels (web, mobile, voice).\n- Employee Agents: Streamline processes, manage repetitive tasks, translate content.\n- Creative Agents: Generate content/images, assist with design and personalization.\n- Data Agents: Complex data analysis with factual integrity.\n- Code Agents: Accelerate development with code generation and assistance.\n- Security Agents: Mitigate attacks, increase investigation speed (prevention, detection, response)."
        },
        "google-cloud-and-ai-agents": {
            "title": "Google Cloud and AI agents portfolio",
            "content": "- Gemini Enterprise App: Discover, create, and govern AI agents.\n- Gemini Enterprise Agent Platform: Build agents grounded in enterprise data.\n- Customer Experience Agent Studio (Dialogflow): Build hybrid conversational agents.\n- Agent Garden: Curated collection of pre-built agent samples.\n- Agent Development Kit (ADK): Open-source Python SDK for multi-agent systems.\n- A2A Protocol: Interoperable framework for building AI agents.\n- Cloud Run: Fully managed serverless platform for containerized agents."
        }
    }

    # Update/Add to JSON
    for slug, data in gcp_knowledge.items():
        knowledge[slug] = data

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(knowledge, f, indent=4, ensure_ascii=False)

    # Sync to Markdown
    # We'll regenerate the markdown from the JSON to ensure they are in sync
    # and follow the existing format (slugs as ### headers)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# AI Agents Knowledge base\n\n")
        # Sort by slug or title? Usually they are appended.
        # Let's keep it sorted by title for better readability
        sorted_keys = sorted(knowledge.keys(), key=lambda x: knowledge[x].get('title', x))
        for slug in sorted_keys:
            item = knowledge[slug]
            f.write(f"### {item.get('title', slug)}\n\n")
            f.write(f"{item.get('content', '')}\n\n")
            if 'source' in item:
                f.write(f"*Source: {item['source']}*\n\n")
            f.write("---\n\n")

    print(f"Successfully updated {json_path} and {md_path} with GCP AI Agents knowledge.")

if __name__ == "__main__":
    update_knowledge()
