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
    try {
      await fs.promises.access(dir)
    } catch {
      return
    }

    const files = await fs.promises.readdir(dir)
    for (const file of files) {
      const fullPath = path.join(dir, file)
      const stat = await fs.promises.stat(fullPath);

      if (stat.isDirectory()) {
        await scan(fullPath)
      } else if (file.endsWith('.tsx') || file.endsWith('.ts')) {
        const content = await fs.promises.readFile(fullPath, 'utf8')
        const lines = content.split('\n').length
        
        // Rule 1: Phase 12 Compliance (Upgrade Phase 9 references)
        if (content.includes('Phase 9')) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'PHASE_UPGRADE_REQUIRED: Phase 9 reference detected. System has evolved to Phase 12.'
          })
        }

        // Rule 2: Detect lack of 'use cache' in large async components
        if (lines > 50 && content.includes('async function') && !content.includes("'use cache'")) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'MISSING_CACHE_DIRECTIVE: High complexity async component detected without granular caching.'
          })
        }

        // Rule 3: Detect large files that should be refactored
        if (lines > 150) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'ARCHITECTURAL_DRIFT: File exceeds complexity limits.'
          })
        }

        // Rule 4: Detect Sync Access to Params (Next.js 16 Violation)
        if (content.includes('params.') && !content.includes('await params') && !content.includes('resolve(params)')) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'SYNC_PROP_VIOLATION: Direct access to params detected. Must be awaited in Next.js 16.'
          })
        }

        // Rule 5: Security and Performance - Detect synchronous I/O and blocking calls
        const syncCalls = ['execSync', 'execFileSync', 'fs.existsSync', 'fs.readFileSync', 'fs.writeFileSync', 'fs.readdirSync', 'fs.statSync']
        for (const call of syncCalls) {
          if (content.includes(call + '(')) {
            suggestions.push({
              file: fullPath.replace(process.cwd(), ''),
              complexity: lines,
              suggestion: `SECURITY_PERF_VULNERABILITY: Synchronous, blocking call ${call} detected. This degrades performance and scale. Replace with asynchronous/Promise-based equivalent.`
            })
          }
        }

        // Rule 6: Error Handling - Detect async functions without try-catch
        const hasAsync = content.includes('async function') || content.includes('async ')
        if (hasAsync && !content.includes('try {') && !content.includes("'use cache'") && lines > 5) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'MISSING_ERROR_HANDLING: Async logic detected without explicit try-catch blocks.'
          })
        }

        // Rule 7: Environment & Imports - Detect direct env access or unsafe static imports
        if (content.includes('process.env.') && !fullPath.includes('antigravity/core.ts') && !fullPath.includes('next.config')) {
           suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'DIRECT_ENV_ACCESS: Use getRuntimeEnv for better cloud-native observability.'
          })
        }

        if ((content.includes("from 'os'") || content.includes("from 'fs'") || content.includes("from 'path'")) && !content.includes('NEXT_RUNTIME')) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'UNSAFE_STATIC_IMPORT: Static import of Node.js built-ins. Prefer dynamic async imports for edge compatibility.'
          })
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

    if (s.suggestion.startsWith('MISSING_ERROR_HANDLING')) {
      console.log(` - Fixing ${s.file}: Adding error handling TODO or safety block`)

      // Safety improvement: Only auto-fix if it's NOT a page/layout file to avoid Next.js directive issues
      const isPageComponent = s.file.includes('page.tsx') || s.file.includes('layout.tsx')

      if (!isPageComponent && s.complexity < 100) {
        // Heuristic: Only inject if not already there and if we find a clear async function start
        if (!content.includes('try {')) {
           content = content.replace(/(async function.*?\{)/, "$1\n  try {")
           const lastBrace = content.lastIndexOf('}')
           if (lastBrace !== -1) {
             content = content.slice(0, lastBrace) + "\n  } catch (err) {\n    console.error('[Evolution Autocorrect] Unhandled error:', err);\n  }\n" + content.slice(lastBrace)
           }
           await fs.promises.writeFile(fullPath, content)
        }
      } else {
        // Inject a TODO instead for complex or page files if not already there
        if (!content.includes('[Evolution] TODO')) {
          content = content.replace(/async function(.*?)\{/, "async function$1{\n  // [Evolution] TODO: Add autonomous error handling (try/catch)")
          await fs.promises.writeFile(fullPath, content)
        }
      }
    }

    if (s.suggestion.startsWith('PHASE_UPGRADE_REQUIRED')) {
      console.log(` - Fixing ${s.file}: Upgrading Phase 9 to Phase 12`)
      content = content.replace(/Phase 9/g, 'Phase 12')
      await fs.promises.writeFile(fullPath, content)
    }

    if (s.suggestion.startsWith('SECURITY_PERF_VULNERABILITY')) {
      console.log(` - Fixing ${s.file}: Adding async refactor TODO for synchronous call`)
      // Inject a TODO near the first detected sync call if not already there
      const syncCalls = ['execSync', 'execFileSync', 'fs.existsSync', 'fs.readFileSync', 'fs.writeFileSync', 'fs.readdirSync', 'fs.statSync']
      for (const call of syncCalls) {
        if (content.includes(call + '(') && !content.includes(`TODO: Refactor to async */ ${call}(`)) {
          content = content.replace(new RegExp(`(\\b${call}\\()`, 'g'), "/* [Evolution] TODO: Refactor to async */ $1")
        }
      }
      await fs.promises.writeFile(fullPath, content)
    }
    
    // Additional autocorrection logic can be added here
  }
  
  console.log('✅ [Antigravity Evolution] Autocorrection complete.')
}

if (require.main === module) {
  evolve().catch(console.error)
}
