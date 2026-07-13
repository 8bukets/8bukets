const fs = require('fs');
const path = require('path');

async function verifySovereignty() {
  console.log('⚖️ [Sovereignty] Verifying critical documentation integrity...');

  const criticalFiles = [
    'SYSTEM_PATENT.md',
    'AGENTS.md',
    'SECURITY.md',
    'CONTRIBUTING.md',
    'README.md'
  ]

  let allValid = true;
  criticalFiles.forEach(file => {
    const filePath = path.join(process.cwd(), file);
    if (fs.existsSync(filePath)) {
      console.log(`✅ [Sovereignty] ${file} is present.`);
    } else {
      console.error(`❌ [Sovereignty] ${file} is MISSING!`);
      allValid = false;
    }
  });

  if (allValid) {
    console.log('🚀 [Sovereignty] All critical documentation verified.');
    process.exit(0);
  } else {
    console.log('⚠️ [Sovereignty] Sovereignty gaps detected in documentation.');
    process.exit(1);
  }
}

verifySovereignty().catch(err => {
  console.error('💥 [Sovereignty] Verification failed:', err);
  process.exit(1);
});
