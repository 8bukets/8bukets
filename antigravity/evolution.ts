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
        if (content.includes('signature') && !content.includes('quantum-resistant') && !content.includes('post-quantum')) {
          suggestions.push({
            file: fullPath.replace(process.cwd(), ''),
            complexity: lines,
            suggestion: 'QUANTUM_VULNERABILITY: Cryptographic signature detected without documented quantum-resistant upgrade path.'
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

    if (s.suggestion.startsWith('ASYNC_HYGIENE_VIOLATION')) {
       console.log(` - Fixing ${s.file}: Implementing automated try/catch wrapping for async safety.`)
       // Simplistic wrapping of async function bodies that contain sync fs
       content = content.replace(/async function(.*?)\{(.*?)\}/gs, (match, args, body) => {
          if (body.includes('try') && body.includes('catch')) return match;
          return `async function${args}{\n  try {\n${body}\n  } catch (err) {\n    console.error('[Evolution Autocorrect] Unhandled error:', err);\n  }\n}`;
       });
       fs.writeFileSync(fullPath, content);
    }

    if (s.suggestion.startsWith('MISSING_CACHE_DIRECTIVE') && !content.includes("'use cache'")) {
       console.log(` - Fixing ${s.file}: Injecting 'use cache' for Phase 12 optimization.`)
       content = content.replace(/async function(.*?)\{/, "async function$1{\n  'use cache'");
       fs.writeFileSync(fullPath, content);
    }
    
    // Additional autocorrection logic can be added here
    if (s.suggestion.startsWith('MISSING_ROI_TRACKING')) {
      console.log(` - Fixing ${s.file}: Injecting placeholder trackROI call.`)
      // Add trackROI placeholder to autonomousFetch calls
      content = content.replace(/autonomousFetch\((.*?)\)/g, 'autonomousFetch($1).then(res => { console.log("📊 [ROI] Efficiency tracking placeholder"); return res; })')
      fs.writeFileSync(fullPath, content)
    }
  }
  
  console.log('✅ [Antigravity Evolution] Autocorrection complete.')
}

if (require.main === module) {
  evolve().catch(console.error)
}
