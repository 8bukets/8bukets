from .base_agent import BaseAgent, Blackboard

class RobotTxtAgent(BaseAgent):
    def __init__(self):
        super().__init__("RobotTxtAgent", provides=["robots_txt"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Checking robots.txt compliance and secrets...")
        import requests

        target_url = "https://markposition.wordpress.com/robots.txt"
        disallowed = []
        try:
            self.logger.info(f"Fetching {target_url}")
            response = requests.get(target_url, timeout=5)
            if response.status_code == 200:
                lines = response.text.split('\n')
                for line in lines:
                    if line.startswith('Disallow:'):
                        path = line.split(':', 1)[1].strip()
                        if path:
                            disallowed.append(path)
        except Exception as e:
            self.logger.error(f"Failed to fetch robots.txt: {e}")

        last_disallowed = set(self.get_agent_memory("disallowed_paths", []))
        current_disallowed = set(disallowed)

        if current_disallowed != last_disallowed:
            new_paths = current_disallowed - last_disallowed
            if new_paths:
                self.logger.info(f"EVOLUTION: New disallowed paths detected: {new_paths}")
            self.update_agent_memory("disallowed_paths", list(current_disallowed))

        return {
            "robots_txt": {
                "status": "Found" if disallowed else "Not Found",
                "disallowed_paths": disallowed
            }
        }
