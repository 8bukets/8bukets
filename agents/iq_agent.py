from .base_agent import BaseAgent
from typing import List, Dict, Any
from datetime import datetime

class IQAgent(BaseAgent):
    def __init__(self):
        super().__init__("IQ & Self-Learning Agent")

    async def process(self, data: List[Dict], shared_context: Dict[str, Any], knowledge_base: Dict[str, Any]) -> Dict[str, Any]:
        # 1. Calculate Base IQ
        # Formula: (Insights Found * Weight) + (Data Points / 100) + (Success Factors)

        insights_count = len(shared_context.get('trending_keywords', []))
        ads_count = len(shared_context.get('targeting_segments', []))
        data_points = len(data)

        # Load previous weights or defaults
        weights = knowledge_base.get('system_weights', {
            'insight_multiplier': 1.0,
            'ad_multiplier': 1.0,
            'complexity_bonus': 0
        })

        # Calculate Score
        raw_score = (insights_count * 5 * weights['insight_multiplier']) + \
                    (ads_count * 5 * weights['ad_multiplier']) + \
                    (data_points / 50) + \
                    weights['complexity_bonus']

        # Normalize to "IQ" scale (baseline 100 approx)
        iq_score = 100 + int(raw_score)

        # 2. Self-Learning / Improvement Logic
        # Compare with previous run
        history = knowledge_base.get('iq_history', [])
        previous_iq = history[-1]['score'] if history else 90

        improvement_msg = "Stabilizing."
        if iq_score > previous_iq:
            improvement_msg = "Intelligence Increasing. Reinforcing successful patterns."
            # Reward: Slight increase in complexity bonus for next time
            weights['complexity_bonus'] += 1
        elif iq_score < previous_iq:
            improvement_msg = "Intelligence Dip Detected. Adjusting weights to compensate."
            # Adapt: Boost multipliers to find more value next time
            weights['insight_multiplier'] += 0.1
        else:
            # Stagnation
            improvement_msg = "Plateau Detected. Initiating exploratory learning."
            weights['ad_multiplier'] += 0.05

        # 3. Update Knowledge Base
        run_date = datetime.now().strftime('%Y-%m-%d')

        # Ensure iq_history exists
        if 'iq_history' not in knowledge_base:
            knowledge_base['iq_history'] = []

        knowledge_base['iq_history'].append({
            'date': run_date,
            'score': iq_score,
            'delta': iq_score - previous_iq
        })

        knowledge_base['system_weights'] = weights

        # Share for Antigravity
        shared_context['current_iq'] = iq_score
        shared_context['iq_status'] = improvement_msg

        results = {}
        results['Current System IQ'] = iq_score
        results['Evolution Status'] = improvement_msg
        results['Delta from Previous'] = f"{iq_score - previous_iq:+d}"
        results['Self-Correction Params'] = str(weights)

        return results
