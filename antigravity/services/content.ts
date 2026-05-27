import fs from 'fs'
import path from 'path'
import { logAutonomousAction } from '../core'

/**
 * ANTIGRAVITY CONTENT SERVICE
 * Autonomously generates reports and documentation.
 */

export async function generateContent(payload: { title: string; content: string; filename: string }) {
  console.log(`📝 [Content] Generating content: ${payload.title}...`)

  const filePath = path.join(process.cwd(), 'data', payload.filename)

  const fullContent = `# ${payload.title}\n\nGenerated on: ${new Date().toISOString()}\n\n${payload.content}`

  /* [Evolution] TODO: Refactor to async */ /* [Evolution] TODO: Refactor to async */ fs.writeFileSync(filePath, fullContent)

  logAutonomousAction(`[CONTENT] Generated ${payload.filename}`, 'info')

  return { filePath, size: fullContent.length }
}
