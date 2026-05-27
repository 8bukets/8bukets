#!/usr/bin/env node

const { spawnSync } = require('child_process');
const path = require('path');

const tsFile = path.join(__dirname, 'antigravity.ts');

const result = spawnSync('npx', ['tsx', tsFile, ...process.argv.slice(2)], {
  stdio: 'inherit',
  shell: true,
});

process.exit(result.status ?? 0);
