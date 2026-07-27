import { z } from 'zod'
import { autonomousFetch, logAutonomousAction } from '@/antigravity/core'
import { promises as fs } from 'fs'
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
  return autonomousFetch(SecurityAuditSchema, async () => {
    logAutonomousAction('🛡️ [Cognitive Security] Starting deep-tissue security scan...', 'info')

    let issuesFound = 0
    let scannedFiles = 0
    const riskPatterns = [
      /mongodb\+srv:\/\//i, // Hardcoded Mongo URIs
      /sb_publishable_.*?_zsZm57QY/i, // Specific Supabase keys
      /process\.env\..*? =/ // Hardcoded env assignments
    ]

    const ignoreDirs = new Set(['node_modules', '.git', '.next', 'dist', 'backups', 'venv']);

    async function scan(dir: string) {
      try {
        const entries = await fs.readdir(dir, { withFileTypes: true });
        const promises = entries.map(async (entry) => {
          const fullPath = path.join(dir, entry.name);
          if (ignoreDirs.has(entry.name)) {
            return;
          }

          if (entry.isDirectory()) {
            await scan(fullPath);
          } else if (entry.isFile() && (entry.name.endsWith('.ts') || entry.name.endsWith('.tsx') || entry.name.endsWith('.js'))) {
            scannedFiles++;
            try {
              const content = await fs.readFile(fullPath, 'utf8');
              for (const pattern of riskPatterns) {
                if (pattern.test(content)) {
                  console.warn(`⚠️ [Security Risk] Potential credential leak in: ${fullPath.replace(process.cwd(), '')}`);
                  issuesFound++;
                }
              }
            } catch (readErr: any) {
              console.error(`❌ [Cognitive Security] Could not read file ${fullPath}: ${readErr.message}`);
            }
          }
        });
        await Promise.all(promises);
      } catch (dirErr: any) {
        console.error(`❌ [Cognitive Security] Could not scan directory ${dir}: ${dirErr.message}`);
      }
    }

    await scan(process.cwd())

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
}
