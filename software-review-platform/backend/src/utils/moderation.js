import { runInDevTraceSpan } from '@google/gemini-cli-core';
import { GeminiCliOperation } from '@google/gemini-cli-core/dist/src/telemetry/constants.js';

export async function analyzeSentiment(content) {
  return await runInDevTraceSpan(
    {
      operation: GeminiCliOperation.ToolCall,
      attributes: {
        GEN_AI_AGENT_NAME: 'gemini-cli',
      },
    },
    async ({ metadata }) => {
      metadata.input = { content };
      metadata.attributes['custom.operation'] = 'analyzeSentiment';

      try {
        const normalized = content.toLowerCase();
        let score = 0.1;

        if (normalized.includes("terrible") || normalized.includes("awful") || normalized.includes("bad")) {
          score = -0.7;
        } else if (normalized.includes("great") || normalized.includes("excellent") || normalized.includes("love")) {
          score = 0.8;
        }

        metadata.output = { score };
        return score;
      } catch (e) {
        metadata.error = e;
        throw e;
      }
    }
  );
}

export function detectSpam(content) {
  const normalized = content.toLowerCase();
  return normalized.includes("buy now") || normalized.includes("click here") || normalized.includes("http://");
}
