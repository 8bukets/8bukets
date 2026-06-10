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
  const baseDir = process.cwd()

  // Recursive scan to find "bloated" or unoptimized patterns
  async function scan(dir: string) {
    const files = fs.readdirSync(dir)
    for (const file of files) {
      if (['node_modules', '.git', '.next', 'venv', '__pycache__', 'dist', 'build', '.npm-cache', 'scratch'].includes(file)) continue;

      const fullPath = path.join(dir, file)
      if (fs.statSync(fullPath).isDirectory()) {
        await scan(fullPath)
      } else if (file.endsWith('.tsx') || file.endsWith('.ts')) {
        const content = await fs.promises.readFile(fullPath, 'utf8')
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

        // Rule 4: Security & Performance - Detect blocking execSync/execFileSync
        if (content.includes('execSync(') || content.includes('execFileSync(')) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'SECURITY_PERF_VULNERABILITY: Blocking execSync/execFileSync detected. Risk of command injection and event loop blocking. Refactor to use non-blocking execAsync or execFileAsync via promisify.'
          })
        }

        // Rule 5: Async Hygiene - Detect sync fs in async contexts
        if (content.includes('async function') && (content.includes('fs.readFileSync') || content.includes('fs.writeFileSync') || content.includes('fs.existsSync'))) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'ASYNC_HYGIENE_VIOLATION: Synchronous fs operation detected inside an asynchronous function. This blocks the event loop. Refactor to use fs.promises.'
          })
        }

        // Rule 6: Type Safety - Detect usage of 'any'
        const anyTypeRegex = /:\s*any\b|as\s+any\b/g
        if (anyTypeRegex.test(content)) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'TYPE_SAFETY_VIOLATION: Usage of \'any\' type detected. This weakens the type system and risks runtime errors. Use specific interfaces or Zod schemas instead.'
          })
        }

        // Rule 7: Zero-Latency Sync Compliance (Directive from iCloud)
        if (content.includes('sync') && !content.includes('latency') && lines > 100) {
           suggestions.push({
             file: fullPath.replace(process.cwd(), ''),
             complexity: lines,
             suggestion: 'SYNC_LATENCY_UNOPTIMIZED: Documented goal of <50ms latency for global neural synchronization detected. Code lacks explicit latency monitoring.'
           })
        }

        // Rule 8: Regional Configuration Compliance (Phase 13 APAC Expansion)
        if (content.includes('edge') && !content.includes('region') && lines > 50) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'MISSING_REGIONAL_CONFIG: APAC Phase 13 directive mandates localized regional configuration for edge nodes.'
          })
        }

        // Rule 9: ROI Efficiency Monitoring (Phase 13 ROI Mandate)
        if ((content.includes('autonomousFetch') || content.includes('execAsync')) && !content.includes('trackROI') && !fullPath.includes('core.ts')) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'MISSING_ROI_TRACKING: Resource-intensive service detected without explicit ROI efficiency tracking as per Phase 13 mandate.'
          })
        }

        // Rule 10: Regional Compliance Metadata (Phase 13 APAC Directive)
        if (fullPath.includes('apac') && !content.includes('regionalCompliance')) {
           suggestions.push({
             file: fullPath.replace(process.cwd(), ''),
             complexity: lines,
             suggestion: 'MISSING_REGIONAL_COMPLIANCE: APAC regional service detected without mandatory regionalCompliance metadata.'
           })
        }

        // Rule 11: Quantum Resistance Audit (Phase 13 Directive)
        if ((content.includes('signature') || content.includes('security') || content.includes('auth')) && !content.includes('quantum-resistant') && !content.includes('post-quantum')) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'QUANTUM_VULNERABILITY: Security-critical component detected without documented quantum-resistant upgrade path.'
          })
        }

        // Rule 12: Sovereign Data Clusters (Phase 13 Directive)
        if (content.includes('MongoClient') && !content.includes('sovereignCluster') && !fullPath.includes('core.ts')) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'NON_SOVEREIGN_DATA_CONFIG: MongoDB client initialization detected without APAC localized sovereignty configuration.'
          })
        }

        // Rule 13: APAC Orchestration Compliance (Phase 13 Directive)
        if (content.includes('apac') && !content.includes('getAPACEdgeOrchestratorData') && !fullPath.includes('apac_edge_orchestrator.ts')) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'MISSING_APAC_ORCHESTRATION: APAC-specific service detected without mandatory integration with APACEdgeOrchestrator for status reporting.'
          })
        }

        // Rule 14: Next.js 16 Compliance (connection() requirement)
        if ((content.includes('cookies()') || content.includes('headers()')) && !content.includes('await connection()')) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'NEXT_16_CONNECTION_MISSING: Next.js 16 requires awaiting connection() before using cookies() or headers().'
          })
        }

        // Rule 15: Project Omega Latency Compliance (Phase 13 Directive)
        if (content.includes('sync') && !content.includes('latency < 30') && lines > 80) {
           suggestions.push({
             file: fullPath.replace(process.cwd(), ''),
             complexity: lines,
             suggestion: 'PROJECT_OMEGA_LATENCY_VIOLATION: Project Omega mandates <30ms latency for all synchronization operations. Explicit monitoring or optimization is missing.'
           })
        }

        // Rule 16: Quantum Synergy Compliance (Phase 13 Directive)
        if (content.includes('synergy') && !content.includes('quantum-resistant') && !content.includes('Crystals-Kyber')) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'QUANTUM_SYNERGY_VIOLATION: Strategic synergy patterns detected without documented quantum-resistant orchestration (Crystals-Kyber).'
          })
        }
      }
    }
  }

  await scan(baseDir)

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
      content = content.replace(/async function\s*(\w*)\s*\((.*?)\)\s*\{/, "async function $1($2) {\n  'use cache'")
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

    if (s.suggestion.startsWith('ASYNC_HYGIENE_VIOLATION')) {
       console.log(` - Fixing ${s.file}: Refactoring synchronous fs to fs.promises (safely).`)

       // Only apply if the file likely contains async context already (as per scan rule)
       if (content.includes('async function')) {
         content = content.replace(/fs\.readFileSync\((.*?),\s*['"]utf8['"]\)/g, 'await fs.promises.readFile($1, \'utf8\')')
         content = content.replace(/fs\.readFileSync\((.*?)\)/g, 'await fs.promises.readFile($1)')
         content = content.replace(/fs\.writeFileSync\((.*?)\)/g, 'await fs.promises.writeFile($1)')
         content = content.replace(/fs\.existsSync\((.*?)\)/g, 'await fs.promises.access($1).then(() => true).catch(() => false)')
       }

       await fs.promises.writeFile(fullPath, content);
    }

    if (s.suggestion.startsWith('MISSING_CACHE_DIRECTIVE') && !content.includes("'use cache'")) {
       console.log(` - Fixing ${s.file}: Injecting 'use cache' for Phase 12 optimization.`)
       content = content.replace(/async function\s*(\w*)\s*\((.*?)\)\s*\{/, "async function $1($2) {\n  'use cache'");
       await fs.promises.writeFile(fullPath, content);
    }
    
    // Additional autocorrection logic can be added here
    if (s.suggestion.startsWith('MISSING_ROI_TRACKING')) {
      // Disabled due to syntax corruption in complex async signatures.
      // ROI tracking should be implemented manually or via a more robust AST-based refactor.
    }

    if (s.suggestion.startsWith('NEXT_16_CONNECTION_MISSING')) {
      console.log(` - Fixing ${s.file}: Injecting await connection()`)
      if (!content.includes("from 'next/server'")) {
        content = "import { connection } from 'next/server'\n" + content
      } else if (!content.includes('connection')) {
        content = content.replace(/import \{(.*?)\} from 'next\/server'/, "import {$1, connection} from 'next/server'")
      }
      content = content.replace(/async function\s*(\w*)\s*\((.*?)\)\s*\{/, "async function $1($2) {\n  await connection()")
      await fs.promises.writeFile(fullPath, content)
    }
  }
  
  console.log('✅ [Antigravity Evolution] Autocorrection complete.')
}

if (require.main === module) {
  evolve().catch(console.error)
}
