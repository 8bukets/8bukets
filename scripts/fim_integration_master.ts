#!/usr/bin/env node

/**
 * FIM Integration Master - Runs all FIM validation & merge systems
 * Validates merge, workflows, system engine, and knowledge integration
 * 
 * Usage: npx tsx scripts/fim_integration_master.ts
 */

import { execSync } from 'child_process';
import fs from 'fs';
import path from 'path';

interface FIMResult {
  stage: string;
  status: 'PASS' | 'FAIL' | 'WARN';
  message: string;
  duration_ms: number;
}

const results: FIMResult[] = [];

function runStage(
  stageName: string,
  scriptPath: string,
  description: string
): boolean {
  console.log(`\n${'═'.repeat(70)}`);
  console.log(`📋 [FIM] Stage: ${stageName}`);
  console.log(`📝 ${description}`);
  console.log(`${'═'.repeat(70)}\n`);

  const startTime = Date.now();

  try {
    execSync(`npx tsx ${scriptPath}`, {
      stdio: 'inherit',
      cwd: process.cwd()
    });

    const duration = Date.now() - startTime;
    results.push({
      stage: stageName,
      status: 'PASS',
      message: `Completed successfully in ${(duration / 1000).toFixed(2)}s`,
      duration_ms: duration
    });

    return true;
  } catch (error) {
    const duration = Date.now() - startTime;
    results.push({
      stage: stageName,
      status: 'FAIL',
      message: `Failed after ${(duration / 1000).toFixed(2)}s`,
      duration_ms: duration
    });

    console.error(`\n❌ [FIM] Stage failed: ${stageName}`);
    return false;
  }
}

async function main() {
  console.log(`
╔════════════════════════════════════════════════════════════════════╗
║                   FIM INTEGRATION MASTER                           ║
║           Merge • Integrate • Validate • System Engine              ║
╚════════════════════════════════════════════════════════════════════╝
  `);

  const startTime = Date.now();
  let allPassed = true;

  // Stage 1: Merge Conflict Validation
  const stage1Pass = runStage(
    'Merge Conflict Detection',
    'scripts/validate_merge_conflicts.ts',
    'Validate engine config merges and detect conflicts'
  );
  allPassed = allPassed && stage1Pass;

  // Stage 2: Workflow Validation
  const stage2Pass = runStage(
    'Workflow Integration Validation',
    'scripts/validate_workflows.ts',
    'Validate all GitHub workflows for correctness'
  );
  allPassed = allPassed && stage2Pass;

  // Stage 3: System Engine Validation
  const stage3Pass = runStage(
    'System Engine Health Check',
    'scripts/validate_system_engine.ts',
    'Comprehensive system engine status and metrics'
  );
  allPassed = allPassed && stage3Pass;

  // Stage 4: Knowledge Merge
  const stage4Pass = runStage(
    'Intelligent Knowledge Merge',
    'scripts/merge_knowledge_intelligent.ts',
    'Merge and deduplicate knowledge base'
  );
  allPassed = allPassed && stage4Pass;

  // Print summary
  const totalTime = Date.now() - startTime;

  console.log(`\n${'═'.repeat(70)}`);
  console.log('📊 [FIM] INTEGRATION SUMMARY');
  console.log(`${'═'.repeat(70)}\n`);

  const passCount = results.filter((r) => r.status === 'PASS').length;
  const failCount = results.filter((r) => r.status === 'FAIL').length;

  results.forEach((result, i) => {
    const icon = result.status === 'PASS' ? '✅' : '❌';
    console.log(`${i + 1}. ${icon} ${result.stage}`);
    console.log(`   ${result.message}`);
  });

  console.log(`\n${'─'.repeat(70)}`);
  console.log(`Total Time: ${(totalTime / 1000).toFixed(2)}s`);
  console.log(`Passed: ${passCount}/${results.length}`);
  console.log(`Failed: ${failCount}/${results.length}`);
  console.log(`${'─'.repeat(70)}\n`);

  // Save integration report
  const reportPath = path.join(process.cwd(), 'data/fim_integration_report.json');
  fs.mkdirSync(path.dirname(reportPath), { recursive: true });
  fs.writeFileSync(
    reportPath,
    JSON.stringify(
      {
        timestamp: new Date().toISOString(),
        status: allPassed ? 'SUCCESS' : 'FAILURE',
        total_duration_ms: totalTime,
        stages: results
      },
      null,
      2
    )
  );

  if (allPassed) {
    console.log('✅ [FIM] ALL VALIDATION STAGES PASSED');
    console.log(`📄 [FIM] Report saved: ${reportPath}\n`);
    process.exit(0);
  } else {
    console.log('❌ [FIM] SOME VALIDATION STAGES FAILED');
    console.log(`📄 [FIM] Report saved: ${reportPath}\n`);
    process.exit(1);
  }
}

main().catch((error) => {
  console.error('Fatal error:', error);
  process.exit(1);
});
