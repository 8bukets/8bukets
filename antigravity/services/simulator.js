/**
 * ANTIGRAVITY TOKEN & COST SIMULATOR
 * Demonstrates the impact of prompt caching and token optimization.
 */
export class TokenSimulator {
    /**
     * Simulates an agent loop.
     * @param steps Number of iterations
     * @param staticSize Size of static prompt (instructions)
     * @param dynamicSize Size of dynamic input per step
     * @param cachingEnabled Whether prompt caching is active
     */
    static simulate(steps, staticSize, dynamicSize, cachingEnabled) {
        let totalTokens = 0;
        let billedTokens = 0;
        let cachedTokens = 0;
        for (let i = 1; i <= steps; i++) {
            const stepTokens = staticSize + (dynamicSize * i); // Context grows linearly
            totalTokens += stepTokens;
            if (cachingEnabled) {
                // In exact-prefix caching, the static prefix is cached after first use
                if (i === 1) {
                    billedTokens += stepTokens;
                }
                else {
                    cachedTokens += staticSize;
                    billedTokens += (dynamicSize * i);
                }
            }
            else {
                billedTokens += stepTokens;
            }
        }
        return {
            steps,
            totalTokens,
            cachedTokens,
            billedTokens,
            costUSD: (billedTokens / 1000) * this.COST_PER_1K_TOKENS
        };
    }
    static compare(steps = 5, staticSize = 2000, dynamicSize = 500) {
        const withoutCaching = this.simulate(steps, staticSize, dynamicSize, false);
        const withCaching = this.simulate(steps, staticSize, dynamicSize, true);
        console.log(`--- Simulation Comparison (${steps} steps) ---`);
        console.log(`[Without Caching] Billed: ${withoutCaching.billedTokens} tokens, Cost: $${withoutCaching.costUSD.toFixed(4)}`);
        console.log(`[With Caching]    Billed: ${withCaching.billedTokens} tokens, Cost: $${withCaching.costUSD.toFixed(4)}`);
        console.log(`Savings: ${((1 - withCaching.billedTokens / withoutCaching.billedTokens) * 100).toFixed(2)}%`);
    }
}
TokenSimulator.COST_PER_1K_TOKENS = 0.01; // Mock cost
export const tokenSimulator = new TokenSimulator();
