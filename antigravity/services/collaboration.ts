import fs from 'fs';
import path from 'path';
import { MongoClient } from 'mongodb';

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
    (this as any)._lastSigma = sigmaStatus;
    (this as any)._lastVersion = version;
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

    // Cloud Persistence: Sync to MongoDB system_snapshots
    const uri = process.env.MONGODB_URI;
    if (uri) {
      try {
        const client = new MongoClient(uri);
        await client.connect();
        const db = client.db(process.env.MONGODB_DB || 'markposition_db');
        const snapshots = db.collection('system_snapshots');

        await snapshots.insertOne({
          timestamp: Date.now() / 1000,
          evolution: {
            parameter_shifts: {
              current_version: (this as any)._lastVersion || '1.0'
            },
            status: 'EVOLVED'
          },
          sigma_status: {
            average_impact_score: (this as any)._lastSigma || 0
          },
          source: 'TypeScript_Jules'
        });

        await client.close();
        console.log('[CollaborationService] Persisted snapshot to MongoDB.');
      } catch (e) {
        console.error('[CollaborationService] Failed to persist to MongoDB:', e);
      }
    }
  }
}

export const collaborationService = new CollaborationService();
