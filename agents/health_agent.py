import os
from bs4 import BeautifulSoup, SoupStrainer

class HealthAgent:
    def __init__(self, filepath='index.html', robots_path='robots.txt'):
        self.filepath = filepath
        self.robots_path = robots_path

    def check_integrity(self):
        """Check the integrity of the main HTML file."""
        print("[HealthAgent] Performing system integrity check...")
        if not os.path.exists(self.filepath):
            print(f"[HealthAgent] CRITICAL: {self.filepath} missing!")
            return False

        # Optimize: Use SoupStrainer to only parse structural tags
        required_tags = ['html', 'head', 'body', 'header', 'main', 'footer']
        strainer = SoupStrainer(required_tags)

        with open(self.filepath, 'r') as f:
            soup = BeautifulSoup(f, 'html.parser', parse_only=strainer)

        missing = [tag for tag in required_tags if not soup.find(tag)]

        if missing:
            print(f"[HealthAgent] WARNING: Missing structural elements: {missing}")
            return False

        print("[HealthAgent] Structure check passed. Core integrity verified.")
        return True

    def check_robots(self):
        """Verify robots.txt configuration."""
        print("[HealthAgent] Verifying robot communication protocols (robots.txt)...")
        if not os.path.exists(self.robots_path):
            print(f"[HealthAgent] WARNING: {self.robots_path} missing. Creating default...")
            self._create_default_robots()
            return False

        with open(self.robots_path, 'r') as f:
            content = f.read()
            if "User-agent: *" in content and "Allow: /" in content:
                 print("[HealthAgent] Robots.txt is correctly configured for autonomous collaboration.")
                 return True
            else:
                 print("[HealthAgent] WARNING: Robots.txt configuration suboptimal.")
                 return False

    def _create_default_robots(self):
        with open(self.robots_path, 'w') as f:
            f.write("User-agent: *\nAllow: /\n")
        print("[HealthAgent] Autonomously created robots.txt.")

    def run_diagnostics(self):
        integrity = self.check_integrity()
        robots = self.check_robots()

        if integrity and robots:
            print("[HealthAgent] System Health: 100% - Ready for autonomous operations.")
            return True
        else:
            print("[HealthAgent] System Health: DEGRADED - Maintenance required.")
            return False

if __name__ == "__main__":
    agent = HealthAgent()
    agent.run_diagnostics()
