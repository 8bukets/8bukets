import fs from 'fs'
import path from 'path'
import { logAutonomousAction } from '../core'

/**
 * ANTIGRAVITY CONTENT SERVICE
 * Autonomously generates reports and documentation.
 */

export async function generateContent(payload: { title: string; content: string; filename: string }) {
  try {
    console.log(`📝 [Content] Generating content: ${payload.title}...`)

    const filePath = path.join(process.cwd(), 'data', payload.filename)
    const fullContent = `# ${payload.title}\n\nGenerated on: ${new Date().toISOString()}\n\n${payload.content}`

    await fs.promises.writeFile(filePath, fullContent)

    logAutonomousAction(`[CONTENT] Generated ${payload.filename}`, 'info')

    return { filePath, size: fullContent.length }
  } catch (err) {
    console.error('[Evolution Autocorrect] Unhandled error:', err);
    throw err;
  }
}
