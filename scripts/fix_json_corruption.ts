import fs from 'fs';
import path from 'path';

const filePath = path.join(process.cwd(), 'data/knowledge/system_knowledge.json');

if (fs.existsSync(filePath)) {
    let content = fs.readFileSync(filePath, 'utf8');

    // Remove lines starting with //
    const lines = content.split('\n');
    const cleanedLines = lines.filter(line => !line.trim().startsWith('//'));

    // Also remove trailing // comments on lines that might have them, but be careful with strings
    // However, usually these corruptions are full lines.

    const cleanedContent = cleanedLines.join('\n');

    try {
        JSON.parse(cleanedContent);
        fs.writeFileSync(filePath, cleanedContent, 'utf8');
        console.log('✅ Successfully cleaned and verified system_knowledge.json');
    } catch (e) {
        console.error('❌ JSON still invalid after cleaning full-line comments:', e.message);

        // Try more aggressive cleaning if needed
        // For example, finding position from error and looking around
        const match = e.message.match(/position (\d+)/);
        if (match) {
            const pos = parseInt(match[1]);
            console.log('Error around:', cleanedContent.substring(Math.max(0, pos - 50), Math.min(cleanedContent.length, pos + 50)));
        }
    }
} else {
    console.error('File not found:', filePath);
}
