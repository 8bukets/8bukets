import { promises as fs } from 'fs'
import path from 'path'
import { logAutonomousAction } from './core'

/**
 * ANTIGRAVITY COGNITIVE EVOLUTION ENGINE
 * This engine analyzes the codebase and proposes autonomous optimizations.
 */

interface EvolutionMetric {
  file: string
  complexity: number
  suggestion: string
}

export async function evolve() {
  logAutonomousAction('🧠 [Antigravity Evolution] Commencing cognitive analysis...', 'info')

  const suggestions: EvolutionMetric[] = []
  const scanDirs = [
    path.join(process.cwd(), 'antigravity'),
    path.join(process.cwd(), 'software-review-platform')
  ]

  // Recursive scan to find "bloated" or unoptimized patterns
  async function scan(dir: string) {
    try {
      await fs.access(dir)
    } catch {
      return // Directory doesn't exist or is not accessible
    }

    const files = await fs.readdir(dir, { withFileTypes: true })
    for (const file of files) {
      const fullPath = path.join(dir, file.name)
      if (file.isDirectory()) {
        await scan(fullPath)
      } else if (file.name.endsWith('.tsx') || file.name.endsWith('.ts')) {
        const content = await fs.readFile(fullPath, 'utf8')
        const lines = content.split('\n').length
        const relativePath = fullPath.replace(process.cwd(), '')

        // Rule 2: Detect large files
        if (lines > 150) {
          suggestions.push({ file: relativePath, complexity: lines, suggestion: 'ARCHITECTURAL_DRIFT: File exceeds complexity limits.' })
        }

        // Rule 3: Detect Sync Access to Params
        if (content.includes('params.') && !content.includes('await params') && !content.includes('resolve(params)')) {
          suggestions.push({ file: relativePath, complexity: lines, suggestion: 'SYNC_PROP_VIOLATION: Direct access to params detected. Must be awaited in Next.js 16.' })
        }

        // Rule 4: Detect console.log
        if (content.includes('console.log(') && !fullPath.includes('.test.') && !fullPath.includes('jules.ts')) {
          suggestions.push({ file: relativePath, complexity: lines, suggestion: 'LOGGING_VIOLATION: console.log detected in production path. Use logAutonomousAction.' })
        }

        // Rule 5: Detect "any" type usage
        if (/\s(as|:)\sany/.test(content)) {
          suggestions.push({ file: relativePath, complexity: lines, suggestion: 'TYPE_SAFETY_VIOLATION: usage of "any" type detected.' })
        }
      }
    }
  }

  for (const dir of scanDirs) {
    await scan(dir)
  }

  logAutonomousAction(`✨ [Evolution Report]: Found ${suggestions.length} potential optimizations.`, 'info')
  return suggestions
}

/**
 * applyFixes: Autonomous Autocorrection
 * Programmatically fixes common architectural drift issues.
 */
export async function applyFixes(suggestions: EvolutionMetric[]) {
  logAutonomousAction('🛠️ [Antigravity Evolution] Applying autonomous fixes...', 'info')

  const fixesByFile = new Map<string, EvolutionMetric[]>()
  for (const s of suggestions) {
    if (!fixesByFile.has(s.file)) {
      fixesByFile.set(s.file, [])
    }
    fixesByFile.get(s.file)!.push(s)
  }

  for (const [file, fileSuggestions] of fixesByFile.entries()) {
    const fullPath = path.join(process.cwd(), file)
    let content = await fs.readFile(fullPath, 'utf8')
    const originalContent = content

    for (const s of fileSuggestions) {
      if (s.suggestion.startsWith('MISSING_CACHE_DIRECTIVE')) {
        // No-op for now, but structure is here
      }

      if (s.suggestion.startsWith('SYNC_PROP_VIOLATION')) {
        logAutonomousAction(` - Fixing ${s.file}: Wrapping params in resolve()`, 'info')
        // Add the import if missing
        if (!content.includes('import {') || !content.includes('@/antigravity/core')) {
          content = "import { resolve } from '@/antigravity/core'\n" + content
        } else if (!content.includes('resolve')) {
          content = content.replace(/import \{(.*?)\} from '@\/antigravity\/core'/, "import {$1, resolve} from '@/antigravity/core'")
        }

        // Attempt to wrap params usages
        content = content.replace(/(\{.*?params.*?\}.*?)\.then/g, 'resolve(params).then')
      }

      // Rule 4 Fix: Replace console.log with logAutonomousAction
      if (s.suggestion.startsWith('LOGGING_VIOLATION')) {
        logAutonomousAction(` - Fixing ${s.file}: Replacing console.log with logAutonomousAction`, 'info')

        // Calculate relative path to core.ts
        const fileDir = path.dirname(fullPath)
        const corePath = path.join(process.cwd(), 'antigravity/core')
        let relativeCorePath = path.relative(fileDir, corePath).replace(/\\/g, '/') // Normalize for windows
        if (!relativeCorePath.startsWith('.')) relativeCorePath = './' + relativeCorePath

        if (!content.includes('logAutonomousAction')) {
          content = `import { logAutonomousAction } from '${relativeCorePath}'\n` + content
        }
        content = content.replace(/console\.log\((.*?)\)/g, "logAutonomousAction($1, 'info')")
      }
    }

    if (content !== originalContent) {
      await fs.writeFile(fullPath, content)
    }
  }

  logAutonomousAction('✅ [Antigravity Evolution] Autocorrection complete.', 'info')
}
