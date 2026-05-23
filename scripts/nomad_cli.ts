#!/usr/bin/env ts-node

import * as fs from 'fs';
import * as path from 'path';
import { spawn } from 'child_process';
import * as readline from 'readline';

interface NomadOption {
    flag: string;
    description: string;
}

const NOMAD_OPTIONS_FILE = path.join(__dirname, '../data/knowledge/nomad_options.json');

function loadOptions(): NomadOption[] {
    try {
        const data = fs.readFileSync(NOMAD_OPTIONS_FILE, 'utf8');
        return JSON.parse(data);
    } catch (error) {
        console.error(`Error loading options from ${NOMAD_OPTIONS_FILE}:`, error);
        return [];
    }
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function askQuestion(query: string): Promise<string> {
    return new Promise(resolve => rl.question(query, resolve));
}

async function generateConfig(optionsMap: Record<string, string>) {
    console.log('\n--- Generating HCL Configuration ---');
    let configStr = '';

    // Simple basic translation of flags to config structure
    // Note: A robust implementation would need to handle nesting properly (e.g., consul {}, vault {})
    for (const [flag, value] of Object.entries(optionsMap)) {
        const cleanName = flag.replace(/^-+/, '').replace(/-/, '_');

        // Handle boolean flags
        if (value === 'true' || value === '') {
            configStr += `${cleanName} = true\n`;
        } else if (value) {
            // Very simplistic - string quotes
            configStr += `${cleanName} = "${value}"\n`;
        }
    }

    const outputPath = path.join(process.cwd(), 'generated_nomad_agent.hcl');
    fs.writeFileSync(outputPath, configStr);
    console.log(`Configuration saved to: ${outputPath}`);
    console.log(configStr);
    console.log('------------------------------------');
}

async function runNomadCLI() {
    console.log("Welcome to the Nomad Agent CLI Wrapper!\n");

    const allOptions = loadOptions();
    if (allOptions.length === 0) {
        console.log("No options available. Ensure nomad_options.json is present.");
        process.exit(1);
    }

    const commandArgs: string[] = ['agent'];
    const selectedOptionsMap: Record<string, string> = {};

    console.log("Let's configure your nomad agent command.");
    console.log("Leave the value blank to skip an option.");
    console.log("For flag options without values (like -client or -dev), enter 'true' to include them.\n");

    // Interactive prompt for some common options
    const commonFlags = [
        '-dev', '-client', '-server', '-data-dir=<path>', '-bind=<address>'
    ];

    for (const flagQuery of commonFlags) {
        const option = allOptions.find(o => o.flag.includes(flagQuery.split('=')[0]));
        if (option) {
            console.log(`\nOption: ${option.flag}`);
            console.log(`Description: ${option.description}`);

            const isValueless = !option.flag.includes('=');

            const prompt = isValueless
                ? `Include this flag? (true/false) [skip]: `
                : `Enter value for ${option.flag.split('=')[0]} [skip]: `;

            const answer = await askQuestion(prompt);

            if (answer.trim() !== '') {
                const baseFlag = option.flag.split('=')[0];
                if (isValueless && answer.trim().toLowerCase() === 'true') {
                    commandArgs.push(baseFlag);
                    selectedOptionsMap[baseFlag] = 'true';
                } else if (!isValueless) {
                    commandArgs.push(`${baseFlag}=${answer.trim()}`);
                    selectedOptionsMap[baseFlag] = answer.trim();
                }
            }
        }
    }

    // Ask if they want to generate config
    const generateAns = await askQuestion('\nDo you want to generate a configuration file from these options? (y/n) [n]: ');
    if (generateAns.toLowerCase() === 'y' || generateAns.toLowerCase() === 'yes') {
        await generateConfig(selectedOptionsMap);
    }

    // Ask if they want to run the command
    console.log(`\nConstructed command: nomad ${commandArgs.join(' ')}`);
    const runAns = await askQuestion('Do you want to run this command now? (y/n) [y]: ');

    if (runAns.toLowerCase() !== 'n' && runAns.toLowerCase() !== 'no') {
        console.log(`\nRunning: nomad ${commandArgs.join(' ')}\n`);

        // Spawn the nomad process
        const nomadProc = spawn('nomad', commandArgs, {
            stdio: 'inherit',
            shell: true // useful if nomad is in PATH
        });

        nomadProc.on('error', (err) => {
            console.error(`Failed to start nomad: ${err.message}`);
            console.log(`\n(Is Nomad installed and in your PATH?)`);
        });

        nomadProc.on('close', (code) => {
            console.log(`nomad process exited with code ${code}`);
            rl.close();
        });
    } else {
        rl.close();
    }
}

runNomadCLI().catch(console.error);
