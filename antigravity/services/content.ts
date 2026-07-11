import fs from 'fs'
import path from 'path'
import { logAutonomousAction } from '../core'

/**
 * ANTIGRAVITY CONTENT SERVICE
 * Autonomously generates reports and documentation.
 */

export async function generateContent(payload: { title: string, content: string, filename: string, directory?: string }) {
  logAutonomousAction(`📝 [Content] Generating content: ${payload.title}...`, 'info')

  const baseDir = payload.directory || 'data'
  const fullBaseDir = path.isAbsolute(baseDir) ? baseDir : path.join(process.cwd(), baseDir)

  if (!fs.existsSync(fullBaseDir)) {
    fs.mkdirSync(fullBaseDir, { recursive: true })
  }

  const filePath = path.join(fullBaseDir, payload.filename)

  const fullContent = `# ${payload.title}\n\nGenerated on: ${new Date().toISOString()}\n\n${payload.content}`

  fs.writeFileSync(filePath, fullContent)

  logAutonomousAction(`[CONTENT] Generated ${payload.filename} in ${baseDir}`, 'info')

  return { filePath, size: fullContent.length }
}
