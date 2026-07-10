import fs from 'fs';
import path from 'path';

const jsonPath = path.join(process.cwd(), 'data/knowledge/system_knowledge.json');
const content = fs.readFileSync(jsonPath, 'utf8');

// Simple regex to remove lines starting with // (ignoring whitespace)
// that are likely raw comments injected into the JSON.
// We need to be careful not to remove // inside strings (like URLs).
// A safer approach for this specific case where comments are on their own lines:
const lines = content.split('\n');
const cleanedLines = lines.filter(line => {
    const trimmed = line.trim();
    return !trimmed.startsWith('//');
});

const cleanedContent = cleanedLines.join('\n');

try {
    JSON.parse(cleanedContent);
    fs.writeFileSync(jsonPath, cleanedContent, 'utf8');
    console.log("Successfully cleaned and validated JSON.");
} catch (e) {
    console.error("Cleaned JSON is still invalid:", e.message);
    // If it's still invalid, maybe there are comments at the end of lines or other issues.
    // Let's try a more aggressive regex that handles comments at end of lines,
    // but ONLY if they are not preceded by a colon (to avoid matching URLs).
    // Actually, let's just use a more robust way to find where the error is.
}
