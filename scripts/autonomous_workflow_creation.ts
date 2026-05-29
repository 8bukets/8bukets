import fs from 'fs';
import path from 'path';

const WORKFLOW_DIR = path.join(process.cwd(), '.github', 'workflows');

function generateWorkflow(name: string, scriptName: string) {
  const workflowContent = `name: ${name}

on:
  schedule:
    - cron: '0 3 * * *'
  workflow_dispatch:

permissions:
  contents: write
  pull-requests: write

jobs:
  run-task:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 24

      - name: Install dependencies
        run: npm ci

      - name: Execute Task
        run: npx tsx scripts/${scriptName}.ts

      - name: Commit and Push Changes
        run: |
          git config --global user.name "GitHub Actions Bot"
          git config --global user.email "actions@github.com"
          git add .
          git commit -m "chore: automated updates from ${name}" || true
          git push origin HEAD:\${{ github.ref }}
`;

  const filename = path.join(WORKFLOW_DIR, `generated_${name.toLowerCase().replace(/\s+/g, '_')}.yml`);
  fs.writeFileSync(filename, workflowContent);
  console.log(`Successfully generated workflow: ${filename}`);
}

function main() {
  if (!fs.existsSync(WORKFLOW_DIR)) {
    fs.mkdirSync(WORKFLOW_DIR, { recursive: true });
  }

  generateWorkflow('Dynamic Data Sync', 'autonomous_sync');
  console.log('Workflow creation engine completed.');
}

main();
