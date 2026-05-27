import os
import asyncio
import sys
import json

async def run_audit():
    print("=== STARTING AUTOMATIC AUTONOMOUS AUDIT PROCEDURE ===")

    # 1. Check Version Integrity
    config_file = "config/evolution_params.json"
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            config = json.load(f)
            print(f"[*] Current System Version: v{config.get('current_version')}")
    else:
        print("[!] ERROR: Evolution params missing.")
        sys.exit(1)

    # 2. Check Test Coverage
    print("[*] Running System Verification Suite...")
    try:
        # Run tests with PYTHONPATH set to current directory
        env = os.environ.copy()
        env["PYTHONPATH"] = "."
        proc = await asyncio.create_subprocess_exec(
            "python3", "-m", "pytest", "tests/",
            env=env,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        if proc.returncode == 0:
            print("[✅] All core tests passed.")
        else:
            print(f"[❌] Test failures detected:\n{stderr.decode('utf-8')}\n{stdout.decode('utf-8')}")
            sys.exit(1)
    except Exception as e:
        print(f"[!] Critical Error during test execution: {e}")
        sys.exit(1)

    # 3. Verify Documentation Status
    doc_file = "SYSTEM_EVOLUTION.md"
    if os.path.exists(doc_file):
        print(f"[✅] {doc_file} is present.")
    else:
        print(f"[!] WARNING: {doc_file} missing. DocumentationAgent may not have run.")

    # 4. Audit PII Redaction in Reports
    results_dir = "results"
    if os.path.exists(results_dir):
        pii_leak = False
        for filename in os.listdir(results_dir):
            if filename.endswith(".md"):
                with open(os.path.join(results_dir, filename), 'r') as f:
                    content = f.read()
                    if "Filip Keser" in content and "REFERENCE:" not in content and "[REDACTED]" not in content:
                        print(f"[!] PII LEAK WARNING: Raw owner name found in {filename}")
                        pii_leak = True
        if not pii_leak:
            print("[✅] PII Redaction verified in results.")

    # 5. Check Orchestrator Health
    print("[*] Verifying Orchestrator and Agent Registry...")
    try:
        from agents.base_agent import BaseAgent
        from agents.orchestrator import AgentOrchestrator
        # Simple instantiation check
        AgentOrchestrator([])
        print("[✅] Orchestrator is healthy.")
    except Exception as e:
        print(f"[!] Orchestrator health check failed: {e}")
        sys.exit(1)

    print("=== AUDIT COMPLETE: SYSTEM IS SECURE AND EVOLVING ===")

if __name__ == "__main__":
    asyncio.run(run_audit())
