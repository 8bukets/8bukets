import * as fs from 'fs';
import * as cheerio from 'cheerio';

const htmlContent = `
<div id="compile-knowledge">
    <h2>Compile</h2>
    <p class="intro">To compile means to gather information from various sources and arrange it into a structured format, such as a report, list, book, or file. In computing, it refers to translating human-readable source code into machine-readable, executable instructions.</p>

    <h3>Key Definitions of Compile</h3>
    <ul>
        <li><strong>Gathering Information</strong>: To collect and put together data, facts, or documents (e.g., to compile a report or compile a list).</li>
        <li><strong>Creating Works</strong>: To produce a book, anthology, or database from various materials.</li>
        <li><strong>Computing</strong>: To convert high-level programming code (like C++ or Java) into machine code, allowing a computer to execute the program.</li>
    </ul>

    <h3>Usage Examples</h3>
    <ul>
        <li>"She is compiling a list of clients for the newsletter."</li>
        <li>"It took years to compile the dictionary."</li>
        <li>"The developer needs to compile the code before running the application."</li>
    </ul>

    <h3>Synonyms</h3>
    <ul>
        <li>Assemble</li>
        <li>Collect</li>
        <li>Gather</li>
        <li>Compose</li>
        <li>Accumulate</li>
        <li>Organize</li>
        <li>Synthesize</li>
    </ul>

    <h3>Contextual Usage</h3>
    <ul>
        <li><strong>General</strong>: Focuses on the act of assembling information or materials (e.g., compile a report).</li>
        <li><strong>Computing</strong>: Focuses on the automatic transformation of code using a tool known as a compiler.</li>
    </ul>
</div>
`;

fs.writeFileSync('data/knowledge/compile_raw.html', htmlContent);

const rawHtml = fs.readFileSync('data/knowledge/compile_raw.html', 'utf-8');
const $ = cheerio.load(rawHtml);

let markdown = `## ${$('h2').text()}\n\n`;
markdown += `${$('.intro').text()}\n\n`;

$('h3').each((i, el) => {
    markdown += `### ${$(el).text()}\n\n`;
    const ul = $(el).next('ul');
    ul.find('li').each((j, li) => {
        const strong = $(li).find('strong').text();
        if (strong) {
            const rest = $(li).text().replace(strong + ':', '').trim();
            markdown += `- **${strong}**: ${rest}\n`;
        } else {
            markdown += `- ${$(li).text()}\n`;
        }
    });
    markdown += '\n';
});

console.log('🤖 [Ingest] Extracted Compile Knowledge from raw HTML.');

// Update KNOWLEDGE_MERGE.md safely
const mergePath = 'KNOWLEDGE_MERGE.md';
let mergeContent = fs.readFileSync(mergePath, 'utf-8');

// Use callback to avoid $$ replacement issues, and negative lookahead for safety
const mergeRegex = /## Compile\n(?:(?!## Knowledge Merge)[\s\S])*/;

if (mergeContent.match(mergeRegex)) {
    mergeContent = mergeContent.replace(mergeRegex, () => markdown.trim() + '\n\n');
    fs.writeFileSync(mergePath, mergeContent, 'utf-8');
    console.log('✅ [Ingest] Updated Compile knowledge in KNOWLEDGE_MERGE.md');
} else {
    // Append it
    const newContent = mergeContent + '\n\n' + markdown.trim() + '\n\n';
    fs.writeFileSync(mergePath, newContent, 'utf-8');
    console.log('✅ [Ingest] Appended Compile knowledge in KNOWLEDGE_MERGE.md');
}

// Update CONSOLIDATED_INTELLIGENCE.md
const ciPath = 'CONSOLIDATED_INTELLIGENCE.md';
if (fs.existsSync(ciPath)) {
    let ciContent = fs.readFileSync(ciPath, 'utf-8');
    if (!ciContent.includes('## Compile')) {
        const signature = 'All the best - https://markposition.wordpress.com';
        if (ciContent.includes(signature)) {
            ciContent = ciContent.replace(signature, () => `\n${markdown}\n---\n${signature}`);
        } else {
            ciContent += `\n${markdown}\n`;
        }
        fs.writeFileSync(ciPath, ciContent, 'utf-8');
        console.log('✅ [Ingest] Appended Compile knowledge to CONSOLIDATED_INTELLIGENCE.md');
    } else {
        const ciRegex = /## Compile\n(?:(?!## |---)[\s\S])*/;
        if (ciContent.match(ciRegex)) {
            ciContent = ciContent.replace(ciRegex, () => markdown.trim() + '\n\n');
            fs.writeFileSync(ciPath, ciContent, 'utf-8');
            console.log('✅ [Ingest] Updated Compile knowledge in CONSOLIDATED_INTELLIGENCE.md');
        }
    }
}

console.log('✅ [Ingest] Ingestion complete.');
