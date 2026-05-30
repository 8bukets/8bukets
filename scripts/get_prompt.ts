import fs from 'fs';
import path from 'path';

interface Prompt {
  number: number;
  category: string;
  title: string;
  prompt: string;
}

function main() {
  const args = process.argv.slice(2);
  const jsonPath = path.join(process.cwd(), '50ty.json');

  if (!fs.existsSync(jsonPath)) {
    console.error('Error: 50ty.json not found in the current directory.');
    process.exit(1);
  }

  const rawData = fs.readFileSync(jsonPath, 'utf8');
  let prompts: Prompt[] = [];
  try {
    prompts = JSON.parse(rawData);
  } catch (_e: unknown) {
    console.error('Error parsing 50ty.json');
    process.exit(1);
  }

  if (args.length === 0 || args[0] === '--help' || args[0] === '-h') {
    console.log('Usage:');
    console.log('  npx tsx scripts/get_prompt.ts list                # List all categories and prompts');
    console.log('  npx tsx scripts/get_prompt.ts <number>            # Get prompt by number (1-50)');
    console.log('  npx tsx scripts/get_prompt.ts category <keyword>  # Get prompts by category');
    process.exit(0);
  }

  const command = args[0].toLowerCase();

  if (command === 'list') {
    let currentCategory = '';
    prompts.forEach(p => {
      if (p.category !== currentCategory) {
        console.log(`\n=== ${p.category} ===`);
        currentCategory = p.category;
      }
      console.log(`${p.number}. ${p.title}`);
    });
  } else if (command === 'category' && args[1]) {
    const keyword = args[1].toLowerCase();
    const matches = prompts.filter(p => p.category.toLowerCase().includes(keyword));
    if (matches.length === 0) {
      console.log(`No categories found matching "${keyword}"`);
    } else {
      matches.forEach(p => {
        console.log(`\n=== Prompt ${p.number} — ${p.title} ===\n`);
        console.log(p.prompt);
      });
    }
  } else if (!isNaN(parseInt(command))) {
    const num = parseInt(command);
    const p = prompts.find(p => p.number === num);
    if (p) {
      console.log(`\nCategory: ${p.category}`);
      console.log(`=== Prompt ${p.number} — ${p.title} ===\n`);
      console.log(p.prompt);
      console.log('\n');
    } else {
      console.error(`Prompt number ${num} not found. Valid numbers are 1-50.`);
    }
  } else {
    console.error('Unknown command or missing arguments. Run with --help for usage.');
  }
}

main();
