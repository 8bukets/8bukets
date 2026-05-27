/**
 * Feedback Analysis Service
 * Generated autonomously by the Antigravity Singularity Engine.
 * Rationale: Analyzes user feedback and system logs to prioritize feature development and bug fixes.
 */
import { z } from 'zod'
import { autonomousFetch, logAutonomousAction } from '../core'
import fs from 'fs'
import path from 'path'

export const FeedbackAnalysisServiceSchema = z.object({
  status: z.string(),
  lastRun: z.string(),
  insights: z.object({
    errorCount: z.number(),
    warningsCount: z.number(),
    criticalIssues: z.array(z.string()),
    suggestions: z.array(z.string())
  })
})

export async function getFeedbackAnalysisServiceData() {
  return autonomousFetch(FeedbackAnalysisServiceSchema, async () => {
    const logsDir = path.join(process.cwd(), 'logs')
    const collaborationLog = path.join(logsDir, 'collaboration.log')
    const autonomousLog = path.join(process.cwd(), 'autonomous_logs.txt')

    let errorCount = 0
    let warningsCount = 0
    const criticalIssues: string[] = []
    const suggestions: string[] = []

    const processLog = (filePath: string) => {
      if (fs.existsSync(filePath)) {
        const content = fs.readFileSync(filePath, 'utf8')
        const lines = content.split('\n')
        for (const line of lines) {
          if (line.includes('ERROR') || line.includes('❌') || line.includes('💥')) {
            errorCount++
            if (line.includes('CRITICAL') || line.includes('fatal')) {
              criticalIssues.push(line.trim())
            }
          } else if (line.includes('WARN') || line.includes('⚠️')) {
            warningsCount++
          } else if (line.includes('💡') || line.includes('suggestion') || line.includes('IDEATED')) {
            suggestions.push(line.trim())
          }
        }
      }
    }

    processLog(collaborationLog)
    processLog(autonomousLog)

    logAutonomousAction(`[FEEDBACK] Errors: ${errorCount}, Warnings: ${warningsCount}, Critical: ${criticalIssues.length}`, 'info')

    return {
      status: 'active',
      lastRun: new Date().toISOString(),
      insights: {
        errorCount,
        warningsCount,
        criticalIssues: criticalIssues.slice(-5), // Last 5
        suggestions: suggestions.slice(-5) // Last 5
      }
    }
  }, { life: 'minutes', tags: ['feedback-analysis'] })
}
