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
  const baseDir = path.join(process.cwd(), 'app')

  // Recursive scan to find "bloated" or unoptimized patterns
  function scan(dir: string) {
    const files = fs.readdirSync(dir)
    for (const file of files) {
      const fullPath = path.join(dir, file)
      if (fs.statSync(fullPath).isDirectory()) {
        scan(fullPath)
      } else if (file.endsWith('.tsx') || file.endsWith('.ts')) {
        const content = fs.readFileSync(fullPath, 'utf8')
        const lines = content.split('\n').length
        
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

        // Rule 4: Security - Detect execSync
        if (content.includes('execSync(')) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'SECURITY_VULNERABILITY: execSync detected. Risk of command injection. Refactor to use execFileSync or spawnSync.'
          })
        }

        // Rule 5: Missing Error Handling in Async Functions
        // Skip Next.js page/layout components (often containing 'use cache') to avoid directive displacement
        if (content.includes('async function') && !content.includes('try {') && !content.includes("'use cache'")) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'MISSING_ERROR_HANDLING: Async function detected without try-catch block.'
          })
        }
      }
    }
  }

  scan(baseDir)

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
    let content = fs.readFileSync(fullPath, 'utf8')

    if (s.suggestion.startsWith('MISSING_CACHE_DIRECTIVE')) {
      console.log(` - Fixing ${s.file}: Injecting 'use cache'`)
      // Inject 'use cache' at the top of the first async function found
      content = content.replace(/async function(.*?)\{/, "async function$1{\n  'use cache'")
      fs.writeFileSync(fullPath, content)
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
      fs.writeFileSync(fullPath, content)
    }
    
    // Additional autocorrection logic can be added here
  }
  
  console.log('✅ [Antigravity Evolution] Autocorrection complete.')
}

if (require.main === module) {
  evolve().catch(console.error)
}
