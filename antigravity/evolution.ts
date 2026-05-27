import fs from 'fs'
import path from 'path'

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
  console.log('🧠 [Antigravity Evolution] Commencing cognitive analysis...')
  
  const suggestions: EvolutionMetric[] = []
  const scanDirs = [
    path.join(process.cwd(), 'app'),
    path.join(process.cwd(), 'antigravity/services')
  ]

  // Recursive scan to find "bloated" or unoptimized patterns
  async function scan(dir: string) {
    if (!fs.existsSync(dir)) return

    const files = fs.readdirSync(dir)
    for (const file of files) {
      const fullPath = path.join(dir, file)
      const stat = await fs.promises.stat(fullPath);
      if (stat.isDirectory()) {
        await scan(fullPath)
      } else if (file.endsWith('.tsx') || file.endsWith('.ts')) {
        const content = await fs.promises.readFile(fullPath, 'utf8')
        const lines = content.split('\n').length
        
        // Rule 7: Phase 12 Compliance (Upgrade Phase 9 references)
        if (content.includes('Phase 9')) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'PHASE_UPGRADE_REQUIRED: Phase 9 reference detected. System has evolved to Phase 12.'
          })
        }

        // Example Evolutionary Logic: Detect lack of 'use cache' in large async components
        if (lines > 50 && content.includes('async function') && !content.includes("'use cache'")) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'MISSING_CACHE_DIRECTIVE: High complexity async component detected without granular caching.'
          })
        }

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

        // Rule 4: Security and Performance - Detect synchronous I/O and blocking calls
        const syncCalls = ['execSync', 'execFileSync', 'fs.existsSync', 'fs.readFileSync', 'fs.writeFileSync']
        for (const call of syncCalls) {
          if (content.includes(call + '(')) {
            suggestions.push({
              file: fullPath.replace(process.cwd(), ''),
              complexity: lines,
              suggestion: `SECURITY_PERF_VULNERABILITY: Synchronous, blocking call ${call} detected. This degrades performance and scale. Replace with asynchronous/Promise-based equivalent.`
            })
          }
        }
      }
    }
  }

  for (const dir of scanDirs) {
    await scan(dir)
  }

  console.log('✨ [Evolution Report]: Found', suggestions.length, 'potential optimizations.')
  return suggestions
}

/**
 * applyFixes: Autonomous Autocorrection
 * Programmatically fixes common architectural drift issues.
 */
export async function applyFixes(suggestions: EvolutionMetric[]) {
  console.log('🛠️ [Antigravity Evolution] Applying autonomous fixes...')
  
  for (const s of suggestions) {
    const fullPath = path.join(process.cwd(), s.file)
    let content = await fs.promises.readFile(fullPath, 'utf8')

    if (s.suggestion.startsWith('MISSING_CACHE_DIRECTIVE')) {
      console.log(` - Fixing ${s.file}: Injecting 'use cache'`)
      // Inject 'use cache' at the top of the first async function found
      content = content.replace(/async function(.*?)\{/, "async function$1{\n  'use cache'")
      await fs.promises.writeFile(fullPath, content)
    }

    if (s.suggestion.startsWith('SYNC_PROP_VIOLATION')) {
      console.log(` - Fixing ${s.file}: Wrapping params in resolve()`)
      // Add the import if missing
      if (!content.includes('import {') || !content.includes('@/antigravity/core')) {
        content = "import { resolve } from '@/antigravity/core'\n" + content
      } else if (!content.includes('resolve')) {
        content = content.replace(/import \{(.*?)\} from '@\/antigravity\/core'/, "import {$1, resolve} from '@/antigravity/core'")
      }
      
      // Attempt to wrap params usages
      content = content.replace(/(\{.*?params.*?\}.*?)\.then/g, "resolve(params).then")
      await fs.promises.writeFile(fullPath, content)
    }

    if (s.suggestion.startsWith('PHASE_UPGRADE_REQUIRED')) {
      console.log(` - Fixing ${s.file}: Upgrading Phase 9 to Phase 12`)
      content = content.replace(/Phase 9/g, 'Phase 12')
      await fs.promises.writeFile(fullPath, content)
    }

    if (s.suggestion.startsWith('SECURITY_PERF_VULNERABILITY')) {
      console.log(` - Fixing ${s.file}: Adding async refactor TODO for synchronous call`)
      // Inject a TODO near the first detected sync call, ensuring we don't duplicate existing ones
      const syncCalls = ['execSync', 'execFileSync', 'fs.existsSync', 'fs.readFileSync', 'fs.writeFileSync']
      let modified = false
      for (const call of syncCalls) {
        if (content.includes(call + '(')) {
          const todoComment = "/* [Evolution] TODO: Refactor to async */"
          // Pattern matches the sync call only if NOT preceded by the TODO comment
          const pattern = new RegExp(`(?<!${todoComment.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}\\s+)\\b${call}\\(`, 'g')
          if (pattern.test(content)) {
            content = content.replace(pattern, `${todoComment} ${call}(`)
            modified = true
          }
        }
      }
      if (modified) {
        await fs.promises.writeFile(fullPath, content)
      }
    }
  }
  
  console.log('✅ [Antigravity Evolution] Autocorrection complete.')
}

if (require.main === module) {
  evolve().catch(console.error)
}
