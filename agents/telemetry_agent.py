from .base_agent import BaseAgent, Blackboard
import json
import os

class TelemetryAgent(BaseAgent):
    """Synthesizes all emitted telemetry into a structural report, including External World investigations."""
    def __init__(self):
        super().__init__("TelemetryAgent", dependencies=["autonomous_status"], provides=["telemetry_synthesis"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Synthesizing Market Data Structural Telemetry & External World Connectivity...")

        telemetry_file = "data/telemetry.json"
        synthesis = {
            "total_events": 0,
            "event_types": {},
            "world_context_distribution": {},
            "status": "INITIALIZED"
        }

        if os.path.exists(telemetry_file):
            try:
                with open(telemetry_file, 'r', encoding='utf-8') as f:
                    events = json.load(f)
                    synthesis["total_events"] = len(events)
                    for e in events:
                        etype = e.get("event_type")
                        synthesis["event_types"][etype] = synthesis["event_types"].get(etype, 0) + 1

                        wcontext = e.get("market_data_ref", "DEFAULT")
                        synthesis["world_context_distribution"][wcontext] = synthesis["world_context_distribution"].get(wcontext, 0) + 1

                synthesis["status"] = "SYNCHRONIZED_WITH_WORLD"
            except Exception as e:
                self.logger.error(f"Failed to synthesize telemetry: {e}")
                synthesis["status"] = "ERROR"

        return {"telemetry_synthesis": synthesis}
