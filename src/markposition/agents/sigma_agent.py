from markposition.agents.base_agent import BaseAgent
from markposition.agents.vector_memory import VectorMemory
import statistics

class SigmaOptimizationAgent(BaseAgent):
    """
    Six Sigma Black Belt Agent applying DMAIC principles to system performance
    and SEO intelligence.
    """
    execution_stage = 11 # Final decision-making stage

    def __init__(self):
        super().__init__("SigmaOptimizationAgent")
        self.vm = VectorMemory()

    async def run(self, data: list, context: dict) -> dict:
        self.logger.info("Executing Six Sigma Variance Analysis (DMAIC)...")

        # 1. MEASURE: Extract performance metrics from context
        patterns = context.get("market_patterns", [])
        counts = [int(p.split("(")[1].split()[0]) for p in patterns if "(" in p]

        if not counts:
             return {"sigma_decision": "INSUFFICIENT_DATA"}

        # 2. ANALYZE: Calculate Variance and Sigma Level
        mean = statistics.mean(counts)
        stdev = statistics.stdev(counts) if len(counts) > 1 else 0
        cv = (stdev / mean) if mean > 0 else 0 # Coefficient of Variation

        # 3. IMPROVE: Identify "Critical to Quality" (CTQ) niches
        sigma_findings = []
        for p in patterns:
            if "(" in p:
                val = int(p.split("(")[1].split()[0])
                # If value is > 2 standard deviations from mean, it's a high-potential "Black Belt" niche
                if val > (mean + 2*stdev):
                    sigma_findings.append(f"CTQ Target: {p.split(':')[1].split('(')[0].strip()} (Statistical Outlier)")

        # 4. CONTROL: Decisioning
        decision = "STABLE"
        if cv > 0.5:
             decision = "VOLATILE_OPPORTUNITY"
             sigma_findings.append("Strategy Shift: High variance detected. Diversifying targeting profiles.")
        elif cv < 0.1:
             decision = "MARKET_SATURATION"
             sigma_findings.append("Strategy Shift: Low variance/High saturation. Pivot to niche long-tail keywords.")

        # Persist Black Belt decisions
        for finding in sigma_findings:
             self.vm.add_entry(f"Sigma Black Belt Decision: {finding}", {"type": "sigma_optimization", "sigma_level": decision})

        return {
            "sigma_metrics": {
                "mean_occurrences": mean,
                "stdev": stdev,
                "coefficient_of_variation": cv,
                "status": decision
            },
            "sigma_findings": sigma_findings
        }
