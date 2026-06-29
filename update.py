import sys
import os

files_to_update = [
    "agents/gitlab_security_agent.md",
    ".gemini/agents/gitlab_security_agent.md"
]

for filepath in files_to_update:
    if not os.path.exists(filepath):
        print(f"{filepath} not found")
        continue
    with open(filepath, "r") as f:
        content = f.read()

    parts = content.split("---\n\n", 1)
    if len(parts) == 2:
        front_matter = parts[0] + "---\n\n"
    else:
        front_matter = ""

    with open("new_prompt.txt", "r") as f:
        new_prompt = f.read()

    if new_prompt.startswith("System prompt\n"):
        new_prompt = new_prompt[len("System prompt\n"):]

    with open(filepath, "w") as f:
        f.write(front_matter + new_prompt)
    print(f"Updated {filepath}")
