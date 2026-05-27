import fs from 'fs';
import path from 'path';
import { MongoClient } from 'mongodb';

export interface KnowledgeInsight {
  topic: string;
  insight: string;
  source: string;
  timestamp: string;
}

export class KnowledgeObserver {
  private knowledgeJsonPath = path.join(process.cwd(), 'ai_agents_knowledge.json');
  private knowledgeMdPath = path.join(process.cwd(), 'ai_agents_knowledge.md');

  public processContent(content: string, source: string): KnowledgeInsight[] {
    const insights: KnowledgeInsight[] = [];
    const timestamp = new Date().toISOString();

    // Simplified regex-based extraction for the autonomous organism
    const markers = [
      { topic: 'Architecture', regex: /architecture|design|structure/i },
      { topic: 'Tools', regex: /tool|utility|plugin/i },
      { topic: 'Security', regex: /security|auth|encryption/i }
    ];

    for (const marker of markers) {
      if (marker.regex.test(content)) {
        insights.push({
          topic: marker.topic,
          insight: `Detected ${marker.topic} related information in ${source}`,
          source,
          timestamp
        });
      }
    }

    return insights;
  }

  public async persistKnowledge(newInsights: KnowledgeInsight[]): Promise<void> {
    let existingKnowledge: any = {};
    if (fs.existsSync(this.knowledgeJsonPath)) {
      existingKnowledge = JSON.parse(fs.readFileSync(this.knowledgeJsonPath, 'utf8'));
    }

    // Merge logic
    const updatedKnowledge = {
      ...existingKnowledge,
      last_updated: new Date().toISOString(),
      insights: [...(existingKnowledge.insights || []), ...newInsights].slice(-100) // Keep last 100
    };

    fs.writeFileSync(this.knowledgeJsonPath, JSON.stringify(updatedKnowledge, null, 2));

    // Also update Markdown for human readability
    let mdContent = `# AI Agents Knowledge Base\n\nLast Updated: ${updatedKnowledge.last_updated}\n\n`;
    for (const insight of updatedKnowledge.insights) {
      mdContent += `### ${insight.topic} (${insight.timestamp})\n- **Source:** ${insight.source}\n- **Insight:** ${insight.insight}\n\n`;
    }
    fs.writeFileSync(this.knowledgeMdPath, mdContent);

    // Sync to MongoDB
    const uri = process.env.MONGODB_URI;
    if (uri && newInsights.length > 0) {
      try {
        const client = new MongoClient(uri);
        await client.connect();
        const db = client.db(process.env.MONGODB_DB || 'markposition_db');
        const collection = db.collection('knowledge_base');

        await collection.insertMany(newInsights.map(i => ({
          ...i,
          synced_at: new Date().toISOString()
        })));

        await client.close();
        console.log(`[KnowledgeObserver] Synced ${newInsights.length} insights to MongoDB.`);
      } catch (e) {
        console.error('[KnowledgeObserver] Failed to sync with MongoDB:', e);
      }
    }
  }
}

export const knowledgeObserver = new KnowledgeObserver();
