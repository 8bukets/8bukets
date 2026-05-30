import * as fs from 'fs';
import * as path from 'path';

const KNOWLEDGE_INTEGRATION_PATH = path.join(process.cwd(), 'KNOWLEDGE_INTEGRATION.md');
const MARKPOSITION_REPORT_PATH = path.join(process.cwd(), 'MARKPOSITION_REPORT.md');
const KNOWLEDGE_MERGE_PATH = path.join(process.cwd(), 'KNOWLEDGE_MERGE.md');
const SYSTEM_KNOWLEDGE_PATH = path.join(process.cwd(), 'data/knowledge/system_knowledge.json');
const CONSOLIDATED_INTELLIGENCE_PATH = path.join(process.cwd(), 'CONSOLIDATED_INTELLIGENCE.md');
const AI_AGENTS_KNOWLEDGE_PATH = path.join(process.cwd(), 'ai_agents_knowledge.md');

const SIGNATURE = "All the best - https://markposition.wordpress.com";

function updateSection(content: string, startMarker: string, endMarker: string, newSectionContent: string): string {
    const startIndex = content.indexOf(startMarker);
    const endIndex = content.indexOf(endMarker);

    if (startIndex === -1 || endIndex === -1) {
        console.warn(`⚠️ [Automate] Markers ${startMarker} or ${endMarker} not found. Appending to end.`);
        return content + `\n\n${startMarker}\n${newSectionContent}\n${endMarker}\n`;
    }

    return content.substring(0, startIndex + startMarker.length) +
           '\n' + newSectionContent + '\n' +
           content.substring(endIndex);
}

async function automateKnowledgeIntegration() {
    console.log('🤖 [Automate] Starting Knowledge Integration refinement...');

    if (!fs.existsSync(KNOWLEDGE_INTEGRATION_PATH)) {
        console.log('✨ [Automate] Creating new KNOWLEDGE_INTEGRATION.md');
        fs.writeFileSync(KNOWLEDGE_INTEGRATION_PATH, '# Knowledge Integration\n\nGenerated autonomously.\n\n');
    }

    let kiContent = fs.readFileSync(KNOWLEDGE_INTEGRATION_PATH, 'utf8');

    // 1. Process Markposition Report
    if (fs.existsSync(MARKPOSITION_REPORT_PATH)) {
        const markContent = fs.readFileSync(MARKPOSITION_REPORT_PATH, 'utf8');
        const sectionMatch = markContent.match(/## Recent Market Intelligence([\s\S]*?)---/);
        if (sectionMatch) {
            const extracted = sectionMatch[1].trim();
            kiContent = updateSection(kiContent, '<!-- MARKPOSITION_START -->', '<!-- MARKPOSITION_END -->', extracted);
            console.log(' ✅ [Automate] Integrated Markposition intelligence.');
        }
    }

    // 2. Process Knowledge Merge (Nuggets)
    if (fs.existsSync(KNOWLEDGE_MERGE_PATH)) {
        const mergeContent = fs.readFileSync(KNOWLEDGE_MERGE_PATH, 'utf8');
        const sectionMatch = mergeContent.match(/## 🧠 Discovered Knowledge Nuggets([\s\S]*?)##/);
        if (sectionMatch) {
            const extracted = sectionMatch[1].trim();
            kiContent = updateSection(kiContent, '<!-- KNOWLEDGE_MERGE_START -->', '<!-- KNOWLEDGE_MERGE_END -->', extracted);
            console.log(' ✅ [Automate] Integrated discovered knowledge nuggets.');
        }
    }

    // 3. Process System Knowledge JSON (Metadata summary)
    if (fs.existsSync(SYSTEM_KNOWLEDGE_PATH)) {
        try {
            const systemKnowledge = JSON.parse(fs.readFileSync(SYSTEM_KNOWLEDGE_PATH, 'utf8'));
            const metadata = systemKnowledge.metadata || {};
            let summary = `### System Knowledge Snapshot\n`;
            summary += `- **Generated At**: ${metadata.generated_at || 'N/A'}\n`;
            summary += `- **Sources Processed**: ${metadata.sources_processed ? metadata.sources_processed.length : 0}\n`;

            if (systemKnowledge.market_data) {
                summary += `- **Total Market Data Points**: ${systemKnowledge.market_data.total_entries || 0}\n`;
            }

            kiContent = updateSection(kiContent, '<!-- SYSTEM_KNOWLEDGE_START -->', '<!-- SYSTEM_KNOWLEDGE_END -->', summary);
            console.log(' ✅ [Automate] Integrated system knowledge metadata.');
        } catch (e) {
            console.warn(' ⚠️ [Automate] Failed to parse system_knowledge.json');
        }
    }

    // 4. Process Consolidated Intelligence
    if (fs.existsSync(CONSOLIDATED_INTELLIGENCE_PATH)) {
        const intelContent = fs.readFileSync(CONSOLIDATED_INTELLIGENCE_PATH, 'utf8');
        const sectionsToExtract = [
            { header: "## 🏥 System Sovereignty", next: "##" },
            { header: "## 🛠️ Cognitive State", next: "##" }
        ];

        let extractedIntel = "### Consolidated System Status\n";
        sectionsToExtract.forEach(sec => {
            const regex = new RegExp(`${sec.header.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}([\\s\\S]*?)${sec.next.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}`);
            const match = intelContent.match(regex);
            if (match) {
                extractedIntel += `\n#### ${sec.header.replace(/#/g, '').trim()}\n${match[1].trim()}\n`;
            }
        });

        kiContent = updateSection(kiContent, '<!-- CONSOLIDATED_INTELLIGENCE_START -->', '<!-- CONSOLIDATED_INTELLIGENCE_END -->', extractedIntel);
        console.log(' ✅ [Automate] Integrated consolidated intelligence summary.');
    }

    // 5. Process AI Agents Knowledge
    if (fs.existsSync(AI_AGENTS_KNOWLEDGE_PATH)) {
        const aiAgentsContent = fs.readFileSync(AI_AGENTS_KNOWLEDGE_PATH, 'utf8');
        // Extract everything after the first header
        const extracted = aiAgentsContent.replace(/^# .*\n/, '').trim();
        kiContent = updateSection(kiContent, '<!-- AI_AGENTS_START -->', '<!-- AI_AGENTS_END -->', extracted);
        console.log(' ✅ [Automate] Integrated AI Agents knowledge.');
    }

    // Ensure Signature
    if (!kiContent.includes(SIGNATURE)) {
        kiContent = kiContent.trim() + '\n\n---\n' + SIGNATURE + '\n';
    } else {
        // Move signature to end if it's not already there
        kiContent = kiContent.replace(new RegExp(`\\n*---\\n*${SIGNATURE.replace(/[-/\\^$*+?.()|[\]{}]/g, '\\$&')}\\n*`, 'g'), '').trim();
        kiContent += '\n\n---\n' + SIGNATURE + '\n';
    }

    fs.writeFileSync(KNOWLEDGE_INTEGRATION_PATH, kiContent, 'utf8');
    console.log('✨ [Automate] Knowledge Integration updated successfully.');
}

automateKnowledgeIntegration().catch(console.error);
