import json
import time
import logging
import os
from typing import Any, Dict, List
from filelock import FileLock

logger = logging.getLogger("TelemetryManager")

class TelemetryManager:
    """Handles Market Data Structural Telemetry for Ad-related content with atomic locking."""
    def __init__(self, output_file="data/telemetry.json"):
        self.output_file = output_file
        self.lock_file = output_file + ".lock"
        self.events: List[Dict[str, Any]] = []
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

    def record_event(self, agent_name: str, event_type: str, data: Dict[str, Any], market_ref: str = "AD_ADS_ADVERTISE"):
        """Records a structural telemetry event."""
        event = {
            "timestamp": time.time(),
            "agent": agent_name,
            "event_type": event_type,
            "market_data_ref": market_ref,
            "payload": data
        }
        self.events.append(event)
        self.logger_event(event)

    def logger_event(self, event: Dict[str, Any]):
        logger.info(f"[TELEMETRY] {event['agent']} emitted {event['event_type']} for {event['market_data_ref']}")

    def save_telemetry(self):
        """Persists telemetry events to disk using atomic file locking."""
        if not self.events:
            return

        lock = FileLock(self.lock_file)
        try:
            with lock.acquire(timeout=10):
                # Append to existing or create new
                existing = []
                if os.path.exists(self.output_file):
                    with open(self.output_file, 'r', encoding='utf-8') as f:
                        try:
                            existing = json.load(f)
                        except json.JSONDecodeError:
                            existing = []

                existing.extend(self.events)

                with open(self.output_file, 'w', encoding='utf-8') as f:
                    json.dump(existing, f, indent=4)

                self.events = [] # Clear memory after save
        except Exception as e:
            logger.error(f"Failed to save telemetry with lock: {e}")

# Global instance for easy integration
telemetry_manager = TelemetryManager()
