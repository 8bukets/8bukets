import sys
import os

# Add parent directory to path to import agents
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.developer_agent import DeveloperAgent

def test_developer_agent_output():
    agent = DeveloperAgent()
    # Simulate empty results to trigger the Python snippet path
    result = agent.process({})

    print("Generated Code Snippet:")
    print(result)

    if 'password="welcome"' in result:
        print("\n[FAIL] Hardcoded password found.")
    elif 'os.environ.get' in result:
        print("\n[PASS] Environment variable usage found.")
    else:
        print("\n[WARN] Neither hardcoded password nor env var found. Check output.")

if __name__ == "__main__":
    test_developer_agent_output()
