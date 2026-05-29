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
        if (!fs.existsSync(jsonPath)) {
            continue;
        }

        try {
            let content = fs.readFileSync(jsonPath, 'utf8');

            if (content.includes('"gemini-cli-remote-subagents"')) {
                continue;
            }

            const newBlockObj = {
                "gemini-cli-remote-subagents": {
                    "title": "Gemini CLI Remote Subagents",
                    "content": newContent
                }
            };

            let newBlockStr = JSON.stringify(newBlockObj, null, 4);
            newBlockStr = newBlockStr.substring(1, newBlockStr.length - 1).trim();

            const rindex = content.lastIndexOf('}');
            if (rindex !== -1) {
                let newContentJson = content.substring(0, rindex).trimEnd();
                if (!newContentJson.endsWith(',')) {
                    newContentJson += ',';
                }
                newContentJson += '\n    ' + newBlockStr.replace(/\n/g, '\n    ') + '\n}';
                fs.writeFileSync(jsonPath, newContentJson, 'utf8');
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
        if (!fs.existsSync(mdPath)) {
            continue;
        }

        try {
            let content = fs.readFileSync(mdPath, 'utf8');

            if (content.includes('## Gemini CLI Remote Subagents')) {
                continue;
            }

            const signature = 'All the best - https://markposition.wordpress.com';
            const newSection = `\n\n## Gemini CLI Remote Subagents\n\n${newContent}\n\n`;

            if (content.includes(signature)) {
                let cleanedContent = content
                    .replace(`---${signature}`, '')
                    .replace(`---\n${signature}`, '')
                    .replace(signature, '')
                    .trim();

                let finalContent = cleanedContent + newSection + `---\n${signature}\n`;
                fs.writeFileSync(mdPath, finalContent, 'utf8');
            } else {
                let finalContent = content.trim() + newSection;
                fs.writeFileSync(mdPath, finalContent, 'utf8');
            }
            console.log(`Updated ${mdPath}`);
        } catch (e) {
            console.error(`Failed to update ${mdPath}: ${e}`);
        }
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
