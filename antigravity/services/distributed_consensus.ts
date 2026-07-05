import fs from 'fs'
import path from 'path'
import { logAutonomousAction } from '../core'

/**
 * ANTIGRAVITY DISTRIBUTED CONSENSUS SERVICE (Phase 24 Neural Mesh)
 * Implements agent-to-agent collaboration and persistence of strategic directives.
 */

export interface StrategicDirective {
  id: string
  proposal: string
  proposer: string
  votes: Record<string, 'approve' | 'reject'>
  status: 'proposed' | 'accepted' | 'rejected'
  timestamp: string
}

const STORAGE_PATH = path.join(process.cwd(), 'data/consensus_state.json')

export class DistributedConsensusService {
  private directives: StrategicDirective[] = []

  constructor() {
    this.load()
  }

  private load() {
    if (fs.existsSync(STORAGE_PATH)) {
      try {
        const data = fs.readFileSync(STORAGE_PATH, 'utf8')
        this.directives = JSON.parse(data)
      } catch (e) {
        console.error('❌ [Consensus] Failed to load consensus state:', e)
      }
    }
  }

  private save() {
    const dataDir = path.dirname(STORAGE_PATH)
    if (!fs.existsSync(dataDir)) {
      fs.mkdirSync(dataDir, { recursive: true })
    }
    fs.writeFileSync(STORAGE_PATH, JSON.stringify(this.directives, null, 2))
  }

  public async propose(proposal: string, agent: string): Promise<string> {
    const id = `dir_${Math.random().toString(36).substring(2, 11)}`
    const directive: StrategicDirective = {
      id,
      proposal,
      proposer: agent,
      votes: { [agent]: 'approve' },
      status: 'proposed',
      timestamp: new Date().toISOString()
    }
    this.directives.push(directive)
    this.save()
    logAutonomousAction(`🤝 [Consensus] New strategic directive proposed by ${agent}: ${id}`, 'info')
    return id
  }

  public async vote(id: string, agent: string, vote: 'approve' | 'reject') {
    const directive = this.directives.find(d => d.id === id)
    if (directive && directive.status === 'proposed') {
      directive.votes[agent] = vote
      this.evaluate(directive)
      this.save()
      logAutonomousAction(`🤝 [Consensus] ${agent} voted ${vote} on directive ${id}`, 'info')
    }
  }

  private evaluate(directive: StrategicDirective) {
    const votes = Object.values(directive.votes)
    const approvals = votes.filter(v => v === 'approve').length

    // Simple consensus: > 2 approvals for acceptance in Phase 24 simulation
    if (approvals >= 2) {
      directive.status = 'accepted'
      logAutonomousAction(`✅ [Consensus] Directive ${directive.id} ACCEPTED via Neural Mesh consensus.`, 'info')
    } else if (votes.length >= 5 && approvals < 2) {
      directive.status = 'rejected'
      logAutonomousAction(`❌ [Consensus] Directive ${directive.id} REJECTED.`, 'info')
    }
  }

  public getAcceptedDirectives(): StrategicDirective[] {
    return this.directives.filter(d => d.status === 'accepted')
  }

  public getAllDirectives(): StrategicDirective[] {
    return [...this.directives]
  }
}

export const distributedConsensus = new DistributedConsensusService()
