import asyncio
import os
import json
import logging
from typing import Any, Dict
from agents.base_agent import BaseAgent, Blackboard

class SandboxAgent(BaseAgent):
    """
    Autonomous agent responsible for evaluating and securely executing code
    in a Vercel Sandbox. It decides the runtime and manages the sandbox lifecycle.
    """
    def __init__(self):
        super().__init__(
            name="SandboxDecisionAgent",
            dependencies=["generated_code"],  # Assuming another agent provides code to test
            provides=["sandbox_execution_results"]
        )
        self.token = os.environ.get("VERCEL_SANDBOX_TOKEN")

    def _get_base_cmd(self) -> list:
        cmd = ["sandbox"]
        if self.token:
            cmd.extend(["--token", self.token])
        return cmd

    async def _execute_cli(self, args: list) -> tuple[int, str, str]:
        cmd = self._get_base_cmd() + args
        self.logger.info(f"Executing Sandbox CLI: {' '.join(cmd)}")
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        return process.returncode, stdout.decode('utf-8').strip(), stderr.decode('utf-8').strip()

    def _determine_runtime(self, code: str, language: str) -> str:
        """Autonomously determine the best runtime based on the language/code."""
        lang_lower = language.lower()
        if 'python' in lang_lower or 'py' in lang_lower:
            return 'python3.13'
        # Default to latest Node.js supported by sandbox as per docs
        return 'node24'

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        """
        Executes generated code in a secure sandbox and returns the results.
        """
        # 1. Fetch code to execute from the blackboard
        generated_code_info = blackboard.get("generated_code", {})
        if not generated_code_info:
            self.logger.warning("No generated_code found on blackboard. Skipping sandbox execution.")
            return {"sandbox_execution_results": {"status": "skipped", "reason": "no code provided"}}

        code = generated_code_info.get("code", "")
        language = generated_code_info.get("language", "python")
        if not code:
            return {"sandbox_execution_results": {"status": "skipped", "reason": "empty code"}}

        # 2. Decision logic: Determine the appropriate runtime
        runtime = self._determine_runtime(code, language)
        self.logger.info(f"Decided on runtime '{runtime}' for language '{language}'.")

        # 3. Create sandbox
        # Using --silent ensures only the sandbox ID is output.
        create_args = ["create", "--runtime", runtime, "--timeout", "5m", "--silent"]
        retcode, stdout, stderr = await self._execute_cli(create_args)
        if retcode != 0:
            self.logger.error(f"Failed to create sandbox: {stderr}")
            return {"sandbox_execution_results": {"status": "error", "error": f"Creation failed: {stderr}"}}

        sandbox_id = stdout.strip()

        if not sandbox_id or not sandbox_id.startswith("sb_"):
            return {"sandbox_execution_results": {"status": "error", "error": f"Could not extract sandbox ID. Output: {stdout}"}}

        self.logger.info(f"Sandbox created successfully: {sandbox_id}")

        results = {
            "sandbox_id": sandbox_id,
            "runtime": runtime,
            "execution_output": "",
            "execution_error": "",
            "status": "success"
        }

        import tempfile
        import uuid

        # 4. Copy file to sandbox and execute
        # Write code to a local temporary file using a unique name to avoid concurrent race conditions
        ext = ".py" if "python" in runtime else ".js"
        temp_filename = f"temp_exec_{uuid.uuid4().hex}{ext}"

        # We need an absolute path to write the local file securely
        local_temp_path = os.path.join(tempfile.gettempdir(), temp_filename)
        with open(local_temp_path, "w") as f:
            f.write(code)

        try:
            # Copy to sandbox
            dest_path = f"/app/{temp_filename}" if "node" in runtime else f"/home/sandbox/{temp_filename}"
            copy_args = ["copy", local_temp_path, f"{sandbox_id}:{dest_path}"]
            retcode, stdout, stderr = await self._execute_cli(copy_args)

            if retcode != 0:
                results["status"] = "error"
                results["execution_error"] = f"Failed to copy file: {stderr}"
            else:
                # Execute in sandbox
                exec_cmd = "python3" if "python" in runtime else "node"
                exec_args = ["exec", sandbox_id, exec_cmd, dest_path]
                retcode, stdout, stderr = await self._execute_cli(exec_args)
                results["execution_output"] = stdout
                if retcode != 0:
                    results["status"] = "failed"
                    results["execution_error"] = stderr
        finally:
            # Clean up local file
            if os.path.exists(local_temp_path):
                os.remove(local_temp_path)

            # 5. Stop the sandbox
            stop_args = ["stop", sandbox_id]
            await self._execute_cli(stop_args)
            self.logger.info(f"Sandbox {sandbox_id} stopped.")

        return {"sandbox_execution_results": results}
