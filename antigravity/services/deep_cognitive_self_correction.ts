import { logAutonomousAction } from '../core'
import { creationEngine } from './creation_engine'
import fs from 'fs'
import path from 'path'

export class DeepCognitiveSelfCorrectionService {
  public async analyzeAndCorrect(sessions: { branches: any[], workOrders: any[] }) {
    console.log('🔬 [DeepCognitive] Cross-referencing logic against performance benchmarks for autonomous self-correction...')

    const corrections: any[] = []

    // Autonomously detect if there are recurring failures in fix branches
    const fixBranches = sessions.branches.filter(b => b.category === 'fix')

    if (fixBranches.length > 3) {
      corrections.push({
        feature: 'Deep AST Refactor Engine',
        rationale: 'High frequency of bug fixes detected. Initiating deep AST refactor to autonomously rewrite sub-optimal methods and eliminate root cause errors.',
        complexity: 'High'
      })
    }

    // --- NEW CREATIVE ADDITION: Deep Project Scanning ---
    // Scan the `antigravity/services` directory to find files that are too large
    // or contain blocking synchronous methods, and autonomously propose fixes.
    const servicesDir = path.join(process.cwd(), 'antigravity/services')
    if (fs.existsSync(servicesDir)) {
      const files = fs.readdirSync(servicesDir)
      for (const file of files) {
        if (file.endsWith('.ts') && !file.endsWith('.test.ts')) {
          const fullPath = path.join(servicesDir, file)
          const content = fs.readFileSync(fullPath, 'utf8')
          const lines = content.split('\n').length

          if (lines > 100) {
            corrections.push({
              feature: `Autonomous Sharding for ${file}`,
              rationale: `Cognitive Engine detected high architectural complexity (${lines} lines) in ${file}. Proposing vertical micro-sharding to isolate dependencies and improve scale.`,
              complexity: 'High'
            })
          }

          if (content.includes('fs.writeFileSync') || content.includes('fs.readFileSync')) {
            corrections.push({
              feature: `Async Stream Optimizer for ${file}`,
              rationale: `Detected synchronous blocking I/O in ${file}. Proposing autonomous refactor to use non-blocking streams for ultra-high scale throughput.`,
              complexity: 'Medium'
            })
          }
        }
      }
    }

    if (corrections.length > 0) {
      logAutonomousAction(`[DeepCognitive] Synthesized ${corrections.length} deep self-corrections.`, 'cognitive')
      // Deduplicate corrections by feature name to prevent order spam
      const uniqueCorrections = Array.from(new Map(corrections.map(c => [c.feature, c])).values())
      await creationEngine.processIdeas(uniqueCorrections)
    }

    return corrections
  }
}

export const deepCognitiveSelfCorrectionService = new DeepCognitiveSelfCorrectionService()
