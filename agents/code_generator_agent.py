import os
import asyncio
from .base_agent import BaseAgent, Blackboard

class CodeGeneratorAgent(BaseAgent):
    """
    Agent that autonomously writes, resolves, and merges code changes.
    It processes 'pending_code_updates' from the consensus memory and applies them to the filesystem.
    """
    def __init__(self):
        super().__init__("CodeGeneratorAgent",
                         dependencies=[],
                         provides=["code_generation_status", "applied_updates"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Engaging Code Generation Unit...")
        
        pending_updates = blackboard.get_consensus("pending_code_updates", [])
        if not pending_updates:
            self.logger.info("No pending code updates found.")
            return {"code_generation_status": "IDLE"}

        applied_updates = []
        for update in pending_updates:
            file_path = update.get("file_path")
            snippet = update.get("code_snippet")
            description = update.get("description")

            # Resolve path relative to current working directory (root of sync_repo)
            full_path = os.path.normpath(os.path.join(os.getcwd(), file_path))

            self.logger.info(f"Applying update to {full_path}: {description}")
            
            try:
                # Autonomous Write/Resolve logic
                if os.path.exists(full_path):
                    with open(full_path, 'r') as f:
                        content = f.read()
                    
                    if snippet not in content:
                        # Append or inject logic
                        with open(full_path, 'a') as f:
                            f.write(f"\n// {description}\n{snippet}\n")
                        applied_updates.append({"file": file_path, "status": "APPENDED"})
                    else:
                        applied_updates.append({"file": file_path, "status": "ALREADY_PRESENT"})
                else:
                    # Create new file if it doesn't exist
                    os.makedirs(os.path.dirname(full_path), exist_ok=True)
                    with open(full_path, 'w') as f:
                        f.write(f"// {description}\n{snippet}\n")
                    applied_updates.append({"file": file_path, "status": "CREATED"})

            except Exception as e:
                self.logger.error(f"Failed to apply update to {file_path}: {e}")
                applied_updates.append({"file": file_path, "status": "FAILED", "error": str(e)})

        # Clear pending updates after processing
        await blackboard.update_consensus("pending_code_updates", [])
        
        # Trigger GitHub Evolution
        await blackboard.propose_improvement(self.name, {
            "code_updates_applied": len(applied_updates),
            "status": "READY_FOR_VCS"
        })

        return {
            "code_generation_status": "COMPLETED",
            "applied_updates": applied_updates
        }
