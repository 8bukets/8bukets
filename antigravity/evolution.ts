import fs from 'fs'
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
  function scan(dir: string) {
    if (!fs.existsSync(dir)) return
    const files = fs.readdirSync(dir)
    for (const file of files) {
      const fullPath = path.join(dir, file)
      if (fs.statSync(fullPath).isDirectory()) {
        scan(fullPath)
      } else if (file.endsWith('.tsx') || file.endsWith('.ts')) {
        const content = fs.readFileSync(fullPath, 'utf8')
        const lines = content.split('\n').length

        // Rule 2: Detect large files that should be refactored
        if (lines > 150) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'ARCHITECTURAL_DRIFT: File exceeds complexity limits.'
          })
        }

        // Rule 3: Detect Sync Access to Params (Next.js 16 Violation)
        if (content.includes('params.') && !content.includes('await params') && !content.includes('resolve(params)')) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'SYNC_PROP_VIOLATION: Direct access to params detected. Must be awaited in Next.js 16.'
          })
        }

        // Rule 4: Detect console.log in production-like files
        if (content.includes('console.log(') && !fullPath.includes('.test.') && !fullPath.includes('jules.ts')) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'LOGGING_VIOLATION: console.log detected in production path. Use logAutonomousAction.'
          })
        }

        // Rule 5: Detect "any" type usage (Type safety)
        if (content.includes(': any') || content.includes('as any')) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'TYPE_SAFETY_VIOLATION: usage of "any" type detected.'
          })
        }
      }
    }
  }

  for (const dir of scanDirs) {
    scan(dir)
  }

  logAutonomousAction('✨ [Evolution Report]: Found', suggestions.length, 'potential optimizations.', 'info')
  return suggestions
}

/**
 * applyFixes: Autonomous Autocorrection
 * Programmatically fixes common architectural drift issues.
 */
export async function applyFixes(suggestions: EvolutionMetric[]) {
  logAutonomousAction('🛠️ [Antigravity Evolution] Applying autonomous fixes...', 'info')

  for (const s of suggestions) {
    const fullPath = path.join(process.cwd(), s.file)
    let content = fs.readFileSync(fullPath, 'utf8')

    if (s.suggestion.startsWith('MISSING_CACHE_DIRECTIVE')) {
      fs.writeFileSync(fullPath, content)
    }

    if (s.suggestion.startsWith('SYNC_PROP_VIOLATION')) {
      logAutonomousAction(` - Fixing ${s.file}: Wrapping params in resolve(, 'info')`)
      // Add the import if missing
      if (!content.includes('import {') || !content.includes('@/antigravity/core')) {
        content = "import { resolve } from '@/antigravity/core'\n" + content
      } else if (!content.includes('resolve')) {
        content = content.replace(/import \{(.*?)\} from '@\/antigravity\/core'/, "import {$1, resolve} from '@/antigravity/core'")
      }

      // Attempt to wrap params usages
      content = content.replace(/(\{.*?params.*?\}.*?)\.then/g, "resolve(params).then")
      fs.writeFileSync(fullPath, content)
    }

    // Rule 4 Fix: Replace console.log with logAutonomousAction
    if (s.suggestion.startsWith('LOGGING_VIOLATION')) {
      logAutonomousAction(` - Fixing ${s.file}: Replacing console.log with logAutonomousAction`, 'info')

      // Calculate relative path to core.ts
      const fileDir = path.dirname(fullPath)
      const corePath = path.join(process.cwd(), 'antigravity/core')
      let relativeCorePath = path.relative(fileDir, corePath)
      if (!relativeCorePath.startsWith('.')) relativeCorePath = './' + relativeCorePath

      if (!content.includes('logAutonomousAction')) {
        content = `import { logAutonomousAction } from '${relativeCorePath}'\n` + content
      }
      content = content.replace(/console\.log\((.*?)\)/g, "logAutonomousAction($1, 'info')")
      fs.writeFileSync(fullPath, content)
    }

    // Additional autocorrection logic can be added here
  }

  logAutonomousAction('✅ [Antigravity Evolution] Autocorrection complete.', 'info')
}

// if (require.main === module) {
//   evolve().catch(console.error)
// }
