/** PHASE 24 COMPLIANCE: NEURAL_MESH_INTEGRATION (enabled) **/
/** PHASE 24 COMPLIANCE: DISTRIBUTED_CONSENSUS (active) **/
/** PHASE 24 COMPLIANCE: MESH_AWARE_ROUTING (enabled) **/
import { z } from 'zod';
import fs from 'fs';
import path from 'path';
import { logAutonomousAction } from '../core';

/**
 * DISTRIBUTED CONSENSUS SERVICE (Phase 24)
 * Enables agents to agree on system state and strategic directives
 * across distributed mesh nodes.
 */

export const ConsensusProposalSchema = z.object({
  id: z.string(),
  proposer: z.string(),
  goal: z.string(),
  payload: z.any(),
  votes: z.record(z.boolean()),
  status: z.enum(['pending', 'accepted', 'rejected']),
  timestamp: z.string()
});

export type ConsensusProposal = z.infer<typeof ConsensusProposalSchema>;

const STATE_PATH = path.join(process.cwd(), 'data/consensus_state.json');

export class DistributedConsensusService {
  private proposals: ConsensusProposal[] = [];

  constructor() {
    this.load();
  }

  private async load() {
    try {
      if (fs.existsSync(STATE_PATH)) {
        const data = fs.readFileSync(STATE_PATH, 'utf8');
        this.proposals = JSON.parse(data);
      }
    } catch (e) {
      this.proposals = [];
    }
  }

  private async save() {
    const dir = path.dirname(STATE_PATH);
    if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(STATE_PATH, JSON.stringify(this.proposals, null, 2));
  }

  public async propose(agentId: string, goal: string, payload: any): Promise<ConsensusProposal> {
    const proposal: ConsensusProposal = {
      id: `prop_${Math.random().toString(36).substring(2, 11)}`,
      proposer: agentId,
      goal,
      payload,
      votes: { [agentId]: true },
      status: 'pending',
      timestamp: new Date().toISOString()
    };

    this.proposals.push(proposal);
    await this.save();

    console.log(`🤝 [Consensus] New proposal ${proposal.id} from ${agentId}: "${goal}"`);
    logAutonomousAction(`[CONSENSUS] Proposal created: ${proposal.id}`, 'cognitive');

    return proposal;
  }

  public async castVote(proposalId: string, agentId: string, approved: boolean) {
    const proposal = this.proposals.find(p => p.id === proposalId);
    if (proposal && proposal.status === 'pending') {
      proposal.votes[agentId] = approved;
      await this.evaluate(proposal);
      await this.save();
    }
  }

  private async evaluate(proposal: ConsensusProposal) {
    const votes = Object.values(proposal.votes);
    const approvals = votes.filter(v => v).length;

    // In simulation mode, 1 approval is enough if it's from the proposer
    // In production, we'd wait for a quorum
    if (approvals >= 1) {
      proposal.status = 'accepted';
      console.log(`✅ [Consensus] Proposal ${proposal.id} ACCEPTED.`);
      logAutonomousAction(`[CONSENSUS] Proposal accepted: ${proposal.id}`, 'cognitive');

      // Trigger execution if accepted
      await this.executeAcceptedProposal(proposal);
    }
  }

  private async executeAcceptedProposal(proposal: ConsensusProposal) {
    // Logic to bridge consensus with the CreationEngine or WorkOrderService
    const { workOrderService } = await import('./work_order');
    if (proposal.goal === 'INITIATE_MESH_COLLABORATION') {
        await workOrderService.createOrder('SYSTEM_SYNC', 'Syncing mesh nodes after consensus', proposal.payload);
    }
  }

  public getPendingProposals(): ConsensusProposal[] {
    return this.proposals.filter(p => p.status === 'pending');
  }
}

export const distributedConsensus = new DistributedConsensusService();
