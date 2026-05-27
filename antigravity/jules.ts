import { collaborationService } from './services/collaboration';
import { knowledgeObserver } from './services/knowledge_observer';
import { getSystemInsights } from './core';
import fs from 'fs';
import path from 'path';

export class Jules {
  public async executeWorkCycle(): Promise<void> {
    console.log('=== Jules: Starting Autonomous Work Cycle ===');

    // 1. Observe Environment
    const insights = getSystemInsights();
    console.log(`[Jules] System Status: Docker=${insights.docker.status}, Collaboration=${insights.collaboration.status}`);

    // 2. Knowledge Observation (Mock content ingestion)
    const mockContent = 'The system architecture uses Docker for virtualization and Next.js for the frontend.';
    const newInsights = knowledgeObserver.processContent(mockContent, 'System_Internal_Audit');
    knowledgeObserver.persistKnowledge(newInsights);
    console.log(`[Jules] Captured ${newInsights.length} new insights.`);

    // 3. Collaboration Sync
    // Try to load current version and sigma from data/memory.json or default
    let sigmaStatus = 0.95;
    let version = '1.0.0';

    const memoryPath = path.join(process.cwd(), 'data', 'memory.json');
    if (fs.existsSync(memoryPath)) {
      try {
        const memory = JSON.parse(fs.readFileSync(memoryPath, 'utf8'));
        sigmaStatus = memory.sigma_status || sigmaStatus;
        version = memory.version || version;
      } catch (e) {
        console.warn('[Jules] Failed to load memory.json, using defaults.');
      }
    }

    await collaborationService.syncContext(sigmaStatus, version);
    console.log('[Jules] Collaboration synchronization complete.');
    console.log('=== Jules: Work Cycle Finished ===');
  }
}

export const jules = new Jules();
