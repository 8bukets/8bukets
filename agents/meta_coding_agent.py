from .base_agent import BaseAgent
import os
import re

class MetaCodingAgent(BaseAgent):
    execution_stage = 6 # Runs before AutonomousIntelligenceAgent
    def __init__(self):
        super().__init__("MetaCodingAgent")

    async def run(self, data: list, context: dict) -> dict:
        self.logger.info("Running Meta-Coding Analysis...")

        # Pattern Recognition
        analysis = context.get("analysis_stats", {})
        top_categories = analysis.get("top_categories", {})

        actions_taken = []

        for category, count in top_categories.items():
            # If a category is dominant, create a specialized "Category Expert" agent
            # Lower threshold for faster autonomous evolution demonstration
            if count >= 3:
                # Sanitize category for safe class naming and string usage
                safe_category = re.sub(r'[^a-zA-Z0-9 ]', '', category)
                class_name = re.sub(r'\W+', '', safe_category.title()) + "ExpertAgent"
                filename = f"agents/{class_name.lower()}.py"

                if not os.path.exists(filename):
                    self.logger.info(f"Dominant pattern detected: {safe_category}. Generating {class_name}...")

                    code = self.generate_expert_agent_code(class_name, safe_category)
                    with open(filename, "w") as f:
                        f.write(code)

                    actions_taken.append(f"Generated specialized agent: {class_name} for category: {safe_category}")

        return {"meta_coding_actions": actions_taken}

    def generate_expert_agent_code(self, class_name, safe_category):
        # Use a more robust templating approach (triple quotes and escaped brackets)
        # and ensure strings are properly escaped to prevent RCE.
        return f"""from .base_agent import BaseAgent

class {class_name}(BaseAgent):
    execution_stage = 5
    def __init__(self):
        super().__init__("{class_name}")

    async def run(self, data: list, context: dict) -> dict:
        category_name = "{safe_category}"
        self.logger.info(f"Specialized logic for {{category_name}} is executing...")

        # Expert logic: find all posts in this category
        matches = [p for p in data if category_name in p.get("categories", [])]

        return {{
            "{class_name.lower()}_insights": {{
                "match_count": len(matches),
                "summary": f"Detected {{len(matches)}} specialized items in {{category_name}}"
            }}
        }}
"""
