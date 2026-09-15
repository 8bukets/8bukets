import { runSecurityAudit } from '../services/cognitive_security';

async function run() {
  const data = await runSecurityAudit();
  console.log('✅ [Workflow] Cognitive Security Audit complete:', JSON.stringify(data, null, 2));
}

run().catch((err) => {
  console.error('❌ [Workflow] Cognitive Security Audit failed:', err);
  process.exit(1);
});
