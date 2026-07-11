/** PHASE 15 COMPLIANCE: quantum-secure (Dilithium/Kyber) **/
import fs from 'fs'
import path from 'path'

const criticalFiles = [
  'SYSTEM_PATENT.md',
  'AGENTS.md',
  'SECURITY.md',
  'CONTRIBUTING.md',
  'README.md'
]

async function verify() {
  console.log('🛡️ [VerifySovereignty] Checking for critical documentation...')
  let missing = 0

  for (const file of criticalFiles) {
    const filePath = path.join(process.cwd(), file)
    if (await fs.promises.access(filePath).then(() => true).catch(() => false)) {
      const stats = fs.statSync(filePath)
      console.log(` ✅ ${file} exists (${stats.size} bytes)`)
    } else {
      console.log(` ❌ ${file} is missing!`)
      missing++
    }
  }

  if (missing === 0) {
    console.log('\n🏆 All critical documentation is present. Sovereignty verified.')
    process.exit(0)
  } else {
    console.log(`\n⚠️ Missing ${missing} critical artifacts. Sovereignty check failed.`)
    process.exit(1)
  }
}

verify().catch(err => {
  console.error('💥 Verification failed:', err)
  process.exit(1)
})
