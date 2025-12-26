from agents.base_agent import BaseAgent
import json
import os

class LearningAgent(BaseAgent):
    def __init__(self):
        super().__init__("Learning")
        self.memory_file = "agent_memory.json"

    async def run(self, context: dict):
        self.log("Learning from cycle execution...")

        memory = self.load_memory()

        # Analyze current run
        health = context.get("health", {})
        is_healthy = health.get("healthy", False)

        # Update run stats
        memory["total_runs"] = memory.get("total_runs", 0) + 1
        if is_healthy:
            memory["successful_runs"] = memory.get("successful_runs", 0) + 1
        else:
            memory["failed_runs"] = memory.get("failed_runs", 0) + 1

        # Evolve parameters
        # Real learning: Adjust system configuration based on health
        config = self.load_config()
        current_limit = config.get("limit", 5)
        current_concurrency = config.get("concurrency", 5)

        # Calculate System IQ
        # Base IQ is 25. Increases by 1 for every 5 successful runs. Decreases by 2 for every failure.
        current_iq = memory.get("system_iq", 25)

        if is_healthy:
            self.log("Run was healthy. Evolving: Incrementing concurrency limit.")
            # Slowly increase concurrency to optimize speed until failure
            new_concurrency = min(current_concurrency + 1, 10)
            config["concurrency"] = new_concurrency
            config["limit"] = current_limit # Keep limit stable or user defined

            # Increase IQ logic
            successful_runs = memory.get("successful_runs", 0)
            if successful_runs % 5 == 0:
                current_iq += 1
                self.log(f"🧠 System IQ increased to {current_iq}!")

        else:
            self.log("Run issues detected. Correcting: Reducing concurrency and limit.")
            # Back off
            config["concurrency"] = max(current_concurrency - 1, 1)
            config["limit"] = max(current_limit - 1, 1)

            # Decrease IQ logic (penalty)
            current_iq = max(25, current_iq - 2) # Don't drop below base 25
            self.log(f"📉 System IQ decreased to {current_iq}.")

        memory["system_iq"] = current_iq
        self.save_config(config)
        self.save_memory(memory)

        context["learning_status"] = {
            "total_runs": memory["total_runs"],
            "system_iq": current_iq,
            "success_rate": f"{(memory.get('successful_runs', 0) / memory['total_runs']) * 100:.1f}%",
            "next_run_config": config
        }

    def load_memory(self):
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return {}

    def save_memory(self, memory):
        with open(self.memory_file, 'w') as f:
            json.dump(memory, f, indent=4)

    def load_config(self):
        if os.path.exists("system_config.json"):
            try:
                with open("system_config.json", 'r') as f:
                    return json.load(f)
            except:
                pass
        return {"limit": 5, "concurrency": 5}

    def save_config(self, config):
        with open("system_config.json", 'w') as f:
            json.dump(config, f, indent=4)
