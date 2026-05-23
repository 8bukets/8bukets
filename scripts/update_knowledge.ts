import * as fs from 'fs';
import * as path from 'path';

function updateKnowledgeBase() {
    const nomadDocsPath = path.join(process.cwd(), 'nomad_agent_docs.txt');
    const systemKnowledgePath = path.join(process.cwd(), 'data/knowledge/system_knowledge.json');
    const mergeMdPath = path.join(process.cwd(), 'KNOWLEDGE_MERGE.md');

    // Read raw docs
    const nomadDocsContent = fs.readFileSync(nomadDocsPath, 'utf8');

    // Update system_knowledge.json
    if (fs.existsSync(systemKnowledgePath)) {
        try {
            const systemKnowledgeContent = fs.readFileSync(systemKnowledgePath, 'utf8');
            const systemKnowledge = JSON.parse(systemKnowledgeContent);

            // Add or update the nomad agent CLI section
            if (!systemKnowledge.nomad) {
                systemKnowledge.nomad = {};
            }
            systemKnowledge.nomad.agent_cli_reference = nomadDocsContent;

            fs.writeFileSync(systemKnowledgePath, JSON.stringify(systemKnowledge, null, 2));
            console.log('Successfully updated system_knowledge.json');
        } catch (error) {
            console.error('Error updating system_knowledge.json:', error);
        }
    } else {
        console.warn(`system_knowledge.json not found at ${systemKnowledgePath}`);
    }

    // Update KNOWLEDGE_MERGE.md
    if (fs.existsSync(mergeMdPath)) {
        try {
            const mergeMdContent = fs.readFileSync(mergeMdPath, 'utf8');
            const header = '## Nomad Agent Command Reference\n\n';

            if (!mergeMdContent.includes('## Nomad Agent Command Reference')) {
                fs.appendFileSync(mergeMdPath, `\n\n${header}${nomadDocsContent}\n`);
                console.log('Successfully appended to KNOWLEDGE_MERGE.md');
            } else {
                console.log('Nomad Agent Command Reference already exists in KNOWLEDGE_MERGE.md');
            }
        } catch (error) {
            console.error('Error updating KNOWLEDGE_MERGE.md:', error);
        }
    } else {
        console.warn(`KNOWLEDGE_MERGE.md not found at ${mergeMdPath}`);
    }
}

updateKnowledgeBase();
