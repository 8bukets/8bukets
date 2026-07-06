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
    let mdContent = fs.existsSync(mdPath) ? fs.readFileSync(mdPath, 'utf8') : "";
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
                title: "What are AI agents? (Updated)",
                sections: Object.keys(structuredData).map(key => ({
                    header: structuredData[key].title,
                    content: structuredData[key].content.split(/\\n|\n/)
                }))
            });
            for (const key in structuredData) systemKnowledge[key] = structuredData[key];
            fs.writeFileSync(systemKnowledgePath, JSON.stringify(systemKnowledge, null, 2), 'utf8');
        } catch (e) { console.error(e); }
    }
}
scrapeAiAgentsKnowledge();
