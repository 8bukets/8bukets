import fs from 'fs'
import path from 'path'
import { logAutonomousAction } from '../antigravity/core'

/**
 * SOVEREIGNTY VERIFICATION SCRIPT (Phase 27)
 * Autonomously verifies the presence and integrity of critical system documentation.
 */
async function verifySovereignty() {
  logAutonomousAction('⚖️ [Sovereignty] Verifying critical documentation integrity...', 'info')

  const criticalFiles = [
    'SYSTEM_PATENT.md',
    'AGENTS.md',
    'SECURITY.md',
    'CONTRIBUTING.md',
    'README.md'
  ]

  let allValid = true
  criticalFiles.forEach(file => {
    const filePath = path.join(process.cwd(), file)
    if (fs.existsSync(filePath)) {
      console.log(`✅ [Sovereignty] ${file} is present.`)
    } else {
      console.error(`❌ [Sovereignty] ${file} is MISSING!`)
      allValid = false
    }
  })

  if (allValid) {
    logAutonomousAction('🚀 [Sovereignty] All critical documentation verified.', 'info')
    process.exit(0)
  } else {
    logAutonomousAction('⚠️ [Sovereignty] Sovereignty gaps detected in documentation.', 'warning')
    process.exit(1)
  }
}

verifySovereignty().catch(err => {
  console.error('💥 [Sovereignty] Verification failed:', err)
  process.exit(1)
})
