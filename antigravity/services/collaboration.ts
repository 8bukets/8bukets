import fs from 'fs';
import path from 'path';

export interface CollaborationContext {
  platform: string;
  system_version: string;
  sigma_status: number;
  stakeholders: string[];
  status: string;
  last_sync: string;
}

export class CollaborationService {
  private missionPath = path.join(process.cwd(), '.antigravity', 'mission.md');
  private statePath = path.join(process.cwd(), 'autonomous_state.json');

  public async syncContext(sigmaStatus: number, version: string): Promise<CollaborationContext> {
    const stakeholders = this.extractStakeholders();

    const context: CollaborationContext = {
      platform: 'Antigravity',
      system_version: version,
      sigma_status: sigmaStatus,
      stakeholders,
      status: 'SYNCED',
      last_sync: new Date().toISOString(),
    };

    this.persistState(context);
    await this.notifyStakeholders(stakeholders);

    return context;
  }

  private extractStakeholders(): string[] {
    if (!fs.existsSync(this.missionPath)) return [];

    const content = fs.readFileSync(this.missionPath, 'utf8');
    const stakeholders: string[] = [];
    const lines = content.split('\n');

    for (const line of lines) {
      if (line.includes('@')) {
        const match = line.match(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/);
        if (match) {
          stakeholders.push(match[1]);
        }
      }
    }
    return stakeholders;
  }

  private persistState(context: CollaborationContext): void {
    fs.writeFileSync(this.statePath, JSON.stringify(context, null, 2));
  }

  private async notifyStakeholders(stakeholders: string[]): Promise<void> {
    console.log(`[CollaborationService] Notifying stakeholders: ${stakeholders.join(', ')}`);
    // Mock notification logic as per system memory expectations
  }
}

export const collaborationService = new CollaborationService();
