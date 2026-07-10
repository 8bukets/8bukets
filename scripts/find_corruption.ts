import fs from 'fs';
import path from 'path';

const jsonPath = path.join(process.cwd(), 'data/knowledge/system_knowledge.json');
const content = fs.readFileSync(jsonPath, 'utf8');

try {
    JSON.parse(content);
    console.log("JSON is valid");
} catch (e) {
    console.log("JSON is invalid:", e.message);
    const match = e.message.match(/position (\d+)/);
    if (match) {
        const pos = parseInt(match[1], 10);
        const start = Math.max(0, pos - 100);
        const end = Math.min(content.length, pos + 100);
        console.log("Context around error:");
        console.log(content.substring(start, end));

        // Find line and column
        const lines = content.substring(0, pos).split('\n');
        const line = lines.length;
        const col = lines[lines.length - 1].length + 1;
        console.log(`Error at line ${line}, column ${col}`);
    }
}
