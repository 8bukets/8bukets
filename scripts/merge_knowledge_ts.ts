import * as fs from 'fs';
import * as path from 'path';

/**
 * KNOWLEDGE MERGE (TS)
 * Synthesizes system_knowledge.json into CONSOLIDATED_KNOWLEDGE.md.
 */

async function main() {
    const jsonPath = path.join(process.cwd(), 'data/knowledge/system_knowledge.json');
    const mdPath = path.join(process.cwd(), 'CONSOLIDATED_KNOWLEDGE.md');
    const strategicSource = path.join(process.cwd(), 'KNOWLEDGE_MERGE.md');

    if (!fs.existsSync(jsonPath)) {
        console.error('❌ system_knowledge.json not found.');
        process.exit(1);
    }

    const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
    let mdContent = `# Consolidated Knowledge Base\n\n`;
    mdContent += `**Last Sync:** ${data.metadata.generated_at}\n`;
    mdContent += `**System Version:** ${data.metadata.version}\n\n`;

    // 1. Strategic Mapping
    if (fs.existsSync(strategicSource)) {
        mdContent += `## 🧩 Strategic Identity & Unified Model\n`;
        mdContent += fs.readFileSync(strategicSource, 'utf8');
        mdContent += `\n\n---\n\n`;
    }

    // 2. System Intelligence
    mdContent += `## System Intelligence & Outlook\n`;
    const outlook = data.system_insights?.intelligence_outlook || [];
    if (outlook.length > 0) {
        outlook.forEach((item: string) => mdContent += `- ${item}\n`);
    } else {
        mdContent += `Awaiting autonomous intelligence sync...\n`;
    }
    mdContent += `\n`;

    // 3. AI Agent Foundation
    mdContent += `## 1. AI Agent Foundation\n`;
    const aiAgents = data.ai_agents || {};
    Object.values(aiAgents).forEach((info: any) => {
        if (info.title) {
            mdContent += `### ${info.title}\n\n${info.content}\n\n`;
        }
    });

    // 4. Google Innovation & AI (New)
    const innovation = data.google_innovation_ai || [];
    if (innovation.length > 0) {
        mdContent += `## 2. Google Innovation & AI\n`;
        innovation.forEach((art: any) => {
            if (art.title && art.title.length > 1) {
                mdContent += `- **[${art.title}](${art.url})**\n`;
                if (art.snippet) mdContent += `  * ${art.snippet}\n`;
            }
        });
        mdContent += `\n`;
    }

    // 5. Market Intelligence
    mdContent += `## 3. Market Intelligence (Markposition)\n`;
    const market = data.market_data || {};
    mdContent += `Total Market Data Points: ${market.total_entries || 0}\n\n`;
    (market.all_entries || []).forEach((entry: any) => {
        if (entry.title && entry.title.length > 1) {
            mdContent += `- **${entry.title}**: ${entry.external_link || entry.post_url} (${entry.date})\n`;
        }
    });
    mdContent += `\n`;

    // 6. Legal & Ecosystem
    mdContent += `## 4. Legal & Ecosystem (Wilson Sonsini)\n`;
    const legal = data.legal_ecosystem || {};
    Object.values(legal).forEach((info: any) => {
        if (info.title) {
            mdContent += `### ${info.title}\n\n${info.content}\n\n`;
        }
    });

    // 7. Technical Documentation
    mdContent += `## 5. Technical Documentation\n`;
    const techKeys = ["gemma_model", "intelephense", "litert", "stitch", "vscode_intelephense", "google_ads"];
    techKeys.forEach(key => {
        const techData = data[key];
        if (techData) {
            const title = key.split('_').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
            mdContent += `### ${title}\n`;
            const keysPreview = Object.keys(techData).slice(0, 5).join(', ');
            mdContent += `Topics covered: ${keysPreview}...\n\n`;
        }
    });

    // 8. TypeScript Ecosystem
    const tsSections = data.typescript_sections || {};
    if (Object.keys(tsSections).length > 0) {
        mdContent += `## 6. TypeScript Ecosystem Intelligence\n`;
        Object.entries(tsSections).forEach(([title, tsData]: [string, any]) => {
            mdContent += `### ${title}\n`;
            mdContent += `*Source: ${tsData.metadata?.source || 'Unknown'}*\n\n`;
            (tsData.sections || []).forEach((sec: any) => {
                mdContent += `#### ${sec.header}\n${sec.content}\n\n`;
            });
        });
    }

    fs.writeFileSync(mdPath, mdContent, 'utf8');
    console.log(`✅ [Merge] Generated ${mdPath}`);
}

main().catch(console.error);
