import * as fs from 'fs';

const RAW_FILE = 'data/raw_remote_subagents_docs.md';

const JSON_PATHS = [
    'ai_agents_knowledge.json',
    'data/ai_agents_knowledge.json',
    'data/knowledge/ai_agents_knowledge.json'
];

const MD_PATHS = [
    'ai_agents_knowledge.md',
    'data/knowledge/ai_agents_knowledge.md'
];

function readRawContent(filepath: string): string {
    try {
        return fs.readFileSync(filepath, 'utf8').trim();
    } catch (e) {
        console.error(`Error: ${filepath} not found.`);
        return '';
    }
}

function updateJsonFiles(newContent: string) {
    if (!newContent) return;

    for (const jsonPath of JSON_PATHS) {
        if (!fs.existsSync(jsonPath)) continue;

        try {
            let content = fs.readFileSync(jsonPath, 'utf8');
            let data = JSON.parse(content);
            if (data["gemini-cli-remote-subagents"]) {
                data["gemini-cli-remote-subagents"].content = newContent;
                fs.writeFileSync(jsonPath, JSON.stringify(data, null, 4), 'utf8');
                console.log(`Updated ${jsonPath}`);
            }
        } catch (e) {
            console.error(`Failed to update ${jsonPath}: ${e}`);
        }
    }
}

function updateMdFiles(newContent: string) {
    if (!newContent) return;

    for (const mdPath of MD_PATHS) {
        if (!fs.existsSync(mdPath)) continue;

        let content = fs.readFileSync(mdPath, 'utf8');
        const startIndex = content.indexOf('## Gemini CLI Remote Subagents');
        if (startIndex === -1) continue;

        let nextSectionIndex = content.length;
        const nextHeaderRegex = /\n#{1,3} /g;
        nextHeaderRegex.lastIndex = startIndex + 30; // skip the current header itself
        const match = nextHeaderRegex.exec(content);
        if (match) {
            nextSectionIndex = match.index;
        }

        const newSection = `## Gemini CLI Remote Subagents\n\n${newContent}\n`;
        const newContentText = content.substring(0, startIndex) + newSection + content.substring(nextSectionIndex);

        fs.writeFileSync(mdPath, newContentText, 'utf8');
        console.log(`Updated ${mdPath}`);
    }
}

function main() {
    const rawContent = readRawContent(RAW_FILE);
    if (rawContent) {
        updateJsonFiles(rawContent);
        updateMdFiles(rawContent);
    }
}

main();
