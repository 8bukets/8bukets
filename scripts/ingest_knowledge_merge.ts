import fs from 'fs';
import path from 'path';
import * as cheerio from 'cheerio';

async function ingestKnowledgeMerge() {
    // Read the source local file to avoid hardcoding
    const htmlPath = path.join(process.cwd(), 'data/knowledge_merge_source.html');
    const htmlContent = fs.readFileSync(htmlPath, 'utf8');
    const $ = cheerio.load(htmlContent);

    const title = $('h2').text().trim();
    const content = $('p').text().trim();

    const markdownContext = `\n## ${title}\n\n${content}\n`;
    const signature = "All the best - https://markposition.wordpress.com";

    const targetFiles = ['KNOWLEDGE_MERGE.md', 'CONSOLIDATED_INTELLIGENCE.md'];

    for (const file of targetFiles) {
        const filePath = path.join(process.cwd(), file);
        if (fs.existsSync(filePath)) {
            let fileContent = fs.readFileSync(filePath, 'utf8');

            // We use a safe regex replacement pattern for the signature.
            // Using a static regex to find the signature and replacing it via callback.
            const escapedSignature = signature.replace(/[-/\\^$*+?.()|[\]{}]/g, '\\$&');
            const sigRegex = new RegExp(`\\n*---\\n*${escapedSignature}\\n*|\\n*${escapedSignature}\\n*`, 'g');

            fileContent = fileContent.replace(sigRegex, () => '\n\n');
            fileContent = fileContent.trim();

            // Check if context already exists
            if (!fileContent.includes(title) || !fileContent.includes(content)) {
                 // Append context
                 fileContent += '\n' + markdownContext;
                 console.log(`✅ [Ingest] Appended knowledge merge to ${file}`);
            } else {
                 console.log(`✨ [Ingest] Knowledge merge already exists in ${file}`);
            }

            // Append signature back
            fileContent += '\n\n---\n' + signature + '\n';

            fs.writeFileSync(filePath, fileContent, 'utf8');
        }
    }
}

ingestKnowledgeMerge().catch(console.error);