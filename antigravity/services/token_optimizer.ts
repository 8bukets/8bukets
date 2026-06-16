import { logAutonomousAction } from '../core'

/**
 * ANTIGRAVITY TOKEN OPTIMIZER
 * Utility for managing and reducing token usage in LLM interactions.
 */

export class TokenOptimizer {
  /**
   * Constructs a prompt optimized for caching.
   * Static components are placed first to ensure prefix match hits.
   */
  public static constructCachedPrompt(staticPart: string, dynamicPart: string): string {
    return `${staticPart.trim()}\n\n${dynamicPart.trim()}`
  }

  /**
   * Compresses an object into a custom delimiter-separated string.
   * This reduces the "JSON token tax" by removing syntax overhead.
   */
  public static compressStructuredData(data: Record<string, any>, delimiter: string = '|'): string {
    return Object.entries(data)
      .map(([key, value]) => `${key}:${value}`)
      .join(delimiter)
  }

  /**
   * Decompresses a custom delimiter-separated string back into an object.
   */
  public static decompressStructuredData(compressed: string, delimiter: string = '|'): Record<string, string> {
    const result: Record<string, string> = {}
    compressed.split(delimiter).forEach(pair => {
      const [key, value] = pair.split(':')
      if (key && value) result[key] = value
    })
    return result
  }

  /**
   * Prunes historical context to stay within token budgets while maintaining state.
   */
  public static pruneHistory(history: string[], maxTokens: number = 1000): string[] {
    // Simple heuristic: 1 token ~= 4 characters
    const maxChars = maxTokens * 4
    let currentChars = 0
    const pruned: string[] = []

    for (let i = history.length - 1; i >= 0; i--) {
      if (currentChars + history[i].length > maxChars) break
      pruned.unshift(history[i])
      currentChars += history[i].length
    }

    return pruned
  }

  public static logOptimization(originalSize: number, optimizedSize: number) {
    const reduction = ((originalSize - optimizedSize) / originalSize * 100).toFixed(2)
    logAutonomousAction(`📉 [TokenOptimizer] Reduced size from ${originalSize} to ${optimizedSize} chars (${reduction}% reduction).`, 'info')
  }
}

export const tokenOptimizer = new TokenOptimizer()
