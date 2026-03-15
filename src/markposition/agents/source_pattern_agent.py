from .base_agent import BaseAgent
import os
import re
import collections

class SourcePatternAgent(BaseAgent):
    execution_stage = 9 # Runs after most agents
    def __init__(self):
        super().__init__("SourcePatternAgent")

    async def run(self, data: list, context: dict) -> dict:
        self.logger.info("Analyzing system source code patterns...")

        # Analyze entire src directory
        package_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        agents_dir = os.path.join(package_root, "agents")

        patterns = []
        import_counts = collections.Counter()
        async_def_count = 0
        sync_def_count = 0
        file_count = 0

        for root, dirs, files in os.walk(package_root):
            for filename in files:
                if filename.endswith(".py"):
                    file_count += 1
                    filepath = os.path.join(root, filename)
                    with open(filepath, "r") as f:
                        content = f.read()
                        # Imports
                        imports = re.findall(r"from ([\w\.]+) import", content)
                        imports += re.findall(r"import ([\w\.]+)", content)
                        for imp in imports:
                            import_counts[imp.split('.')[0]] += 1

                        # Async vs Sync
                        async_def_count += len(re.findall(r"async def ", content))
                        sync_def_count += len(re.findall(r"def ", content)) - len(re.findall(r"async def ", content))

        patterns.append(f"System Scale: {file_count} Python modules analyzed.")
        patterns.append(f"Concurrency Pattern: {async_def_count} async vs {sync_def_count} sync functions.")

        common_imports = [f"Common dependency: {imp} ({count} uses)" for imp, count in import_counts.most_common(10)]
        patterns.extend(common_imports)

        # 2. Analyze agent stages specifically
        if os.path.exists(agents_dir):
            stage_counts = collections.Counter()
            for filename in os.listdir(agents_dir):
                if filename.endswith(".py") and filename != "base_agent.py":
                    with open(os.path.join(agents_dir, filename), "r") as f:
                        match = re.search(r"execution_stage\s*=\s*(\d+)", f.read())
                        if match:
                            stage_counts[int(match.group(1))] += 1

            stage_dist = [f"Agent Architecture: Stage {s} has {c} specialized agents" for s, c in sorted(stage_counts.items())]
            patterns.extend(stage_dist)

        # Persistence
        for pattern in patterns:
            self.add_vector_insight(f"Source Pattern: {pattern}", {"type": "source_analysis"})

        return {
            "source_code_patterns": patterns,
            "system_complexity_score": file_count
        }
