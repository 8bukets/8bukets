with open("run_system.py", "r") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if "from agents.performance_optimization_agent import PerformanceOptimizationAgent" in line:
        new_lines.append(line)
        new_lines.append("from agents.rag_agent import RagAgent\n")
    elif "SystemAuditAgent(), DocumentationAgent()" in line:
        new_lines.append(line.replace("SystemAuditAgent(), DocumentationAgent()", "SystemAuditAgent(), DocumentationAgent(), RagAgent()"))
    else:
        new_lines.append(line)

with open("run_system.py", "w") as f:
    f.writelines(new_lines)
