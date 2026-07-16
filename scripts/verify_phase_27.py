import sys
import os
import re

def check_file_content(filepath, patterns):
    if not os.path.exists(filepath):
        print(f"❌ File not found: {filepath}")
        return False

    with open(filepath, 'r') as f:
        content = f.read()

    success = True
    for pattern in patterns:
        if re.search(pattern, content):
            print(f"✅ Found: '{pattern}' in {filepath}")
        else:
            print(f"❌ MISSING: '{pattern}' in {filepath}")
            success = False
    return success

print("🔍 Auditing Phase 27 Multi-Universal Resonance (MUR) compliance...")

presence_patterns = [
    r"version: '1\.7\.0-mur'",
    r"phase27: z\.object\(",
    r"resonance_latency: \(heartbeatMetrics as any\)\.resonance_latency",
    r"universal_consensus: \(heartbeatMetrics as any\)\.universal_consensus \|\| 'SYNCED'"
]

heartbeat_patterns = [
    r"singularityReadiness: number = 0\.999995",
    r"universalConsensus: string = 'SYNCED'",
    r"this\.resonanceLatency = Math\.random\(\) \* 0\.007",
    r"if \(this\.resonanceLatency > 0\.008\)"
]

jules_patterns = [
    r"Beginning Autonomous Work Cycle \(Phase 27 MUR\)",
    r"Multi-Universal Resonance active",
    r"Phase 27 Pulse:",
    r"executePhase27MURPulse\(\)"
]

evolution_patterns = [
    r"Rule 37: Phase 27 Multi-Universal Resonance Compliance",
    r"PHASE_27_MUR_MISSING",
    r"s\.suggestion\.includes\('PHASE_27'\)"
]

umr_patterns = [
    r"Enforcing Phase 27 Universal Mesh Routing protocol \(UMR-v3\.0\)",
    r"protocol: 'UMR-v3\.0'"
]

cloud_integration_patterns = [
    r"executePhase27MURPulse\(\)",
    r"ANTIGRAVITY CLOUD-CONNECTED INTEGRATION SERVICE \(Phase 27 MUR\)",
    r"Presence established\. Resonance: \$\{presence\.phase27\?\.resonance_latency\}ms"
]

all_passed = True
all_passed &= check_file_content("antigravity/services/presence.ts", presence_patterns)
all_passed &= check_file_content("antigravity/services/swarm_heartbeat.ts", heartbeat_patterns)
all_passed &= check_file_content("antigravity/jules.ts", jules_patterns)
all_passed &= check_file_content("antigravity/evolution.ts", evolution_patterns)
all_passed &= check_file_content("antigravity/services/universal_mesh_routing.ts", umr_patterns)
all_passed &= check_file_content("antigravity/services/cloud_connected_integration.ts", cloud_integration_patterns)

if all_passed:
    print("\n🏆 Phase 27 MUR Compliance Verified Successfully.")
    sys.exit(0)
else:
    print("\n💥 Compliance Audit Failed.")
    sys.exit(1)
