import { z } from 'zod'
import { autonomousFetch, logAutonomousAction } from '@/antigravity/core'
import fs from 'fs'
import path from 'path'

export const SecurityAuditSchema = z.object({
  status: z.enum(['secure', 'warning', 'critical']),
  issuesFound: z.number(),
  lastAudit: z.string(),
  scannedFiles: z.number()
})

export type SecurityAudit = z.infer<typeof SecurityAuditSchema>

/**
 * Cognitive Security Service
 * Autonomously scans for high-risk patterns and credential leakage.
 */
export async function runSecurityAudit(): Promise<SecurityAudit> {
  try {

  return autonomousFetch(SecurityAuditSchema, async () => {
    'use cache'
    console.log('🛡️ [Cognitive Security] Starting deep-tissue security scan...')
    
    let issuesFound = 0
    let scannedFiles = 0
    const riskPatterns = [
      /mongodb\+srv:\/\//i, // Hardcoded Mongo URIs
      /sb_publishable_.*?_zsZm57QY/i, // Specific Supabase keys
      /process\.env\..*? =/ // Hardcoded env assignments
    ]

    function scan(dir: string) {
      const files = /* [Evolution] TODO: Refactor to async */ fs.readdirSync(dir)
      for (const file of files) {
        const fullPath = path.join(dir, file)
        if (file === 'node_modules' || file === '.git' || file === '.next' || file === 'venv') continue
        
        if (/* [Evolution] TODO: Refactor to async */ fs.statSync(fullPath).isDirectory()) {
          scan(fullPath)
        } else if (file.endsWith('.ts') || file.endsWith('.tsx') || file.endsWith('.js')) {
          scannedFiles++
          const content = /* [Evolution] TODO: Refactor to async */ fs.readFileSync(fullPath, 'utf8')
          for (const pattern of riskPatterns) {
            if (pattern.test(content)) {
              console.warn(`⚠️ [Security Risk] Potential credential leak in: ${file}`)
              issuesFound++
            }
          }
        }
      }
    }

    scan(process.cwd())

    const status = issuesFound > 0 ? 'warning' : 'secure'
    
    if (issuesFound > 0) {
      logAutonomousAction(`[SECURITY] Found ${issuesFound} potential risks during audit.`, 'security')
    }

    return {
      status,
      issuesFound,
      lastAudit: new Date().toISOString(),
      scannedFiles
    }
  }, { life: 'catalog', tags: ['security-audit'] })

  } catch (err) {
    console.error('[Evolution Autocorrect] Unhandled error:', err);
  }
}
