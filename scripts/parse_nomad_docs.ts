import * as fs from 'fs';
import * as path from 'path';

interface NomadOption {
    flag: string;
    description: string;
}

function parseNomadDocs(docsPath: string): NomadOption[] {
    const content = fs.readFileSync(docsPath, 'utf8');
    const lines = content.split('\n');
    const options: NomadOption[] = [];

    let currentOption: NomadOption | null = null;
    let parsingOptions = false;

    for (const line of lines) {
        if (line.trim() === 'Options') {
            parsingOptions = true;
            continue;
        }

        if (!parsingOptions) {
            continue;
        }

        // Match lines starting with a flag (e.g., "-alloc-dir=<path>:" or "vault-cert-file=<path>:")
        const flagMatch = line.match(/^([a-zA-Z0-9-]+=?(?:<[^>]+>)?:)\s*(.*)/);

        if (flagMatch) {
            // If we already have a current option, save it
            if (currentOption) {
                options.push(currentOption);
            }

            // Clean up the flag (remove trailing colon)
            const flag = flagMatch[1].replace(/:$/, '');
            let description = flagMatch[2].trim();

            // Fix missing hyphens for some vault options that were missing them in the raw text
            let finalFlag = flag;
            if (!finalFlag.startsWith('-') && finalFlag.startsWith('vault')) {
                finalFlag = '-' + finalFlag;
            }

            currentOption = {
                flag: finalFlag,
                description: description
            };
        } else if (currentOption && line.trim() !== '') {
            // Append continuation lines to the current description
            currentOption.description += ' ' + line.trim();
        }
    }

    // Push the last option
    if (currentOption) {
        options.push(currentOption);
    }

    return options;
}

const inputPath = path.join(process.cwd(), 'nomad_agent_docs.txt');
const outputPath = path.join(process.cwd(), 'data/knowledge/nomad_options.json');

try {
    const options = parseNomadDocs(inputPath);
    fs.writeFileSync(outputPath, JSON.stringify(options, null, 2));
    console.log(`Successfully parsed ${options.length} options and saved to ${outputPath}`);
} catch (error) {
    console.error('Error parsing docs:', error);
}
