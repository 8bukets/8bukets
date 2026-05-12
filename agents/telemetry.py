import json
import time
import logging
import os
from typing import Any, Dict, List
from filelock import FileLock

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter

# Initialize OpenTelemetry Tracer
trace.set_tracer_provider(TracerProvider())
tracer_provider = trace.get_tracer_provider()
tracer_provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))
tracer = trace.get_tracer(__name__)

logger = logging.getLogger("TelemetryManager")

class TelemetryManager:
    """Handles Market Data Structural Telemetry for Ad-related content with atomic locking and OpenTelemetry GenAI semantics."""
    def __init__(self, output_file="data/telemetry.json"):
        self.output_file = output_file
        self.lock_file = output_file + ".lock"
        self.events: List[Dict[str, Any]] = []
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Check stability opt-in for new GenAI conventions
        opt_in_env = os.environ.get("OTEL_SEMCONV_STABILITY_OPT_IN", "")
        self.use_gen_ai_latest = "gen_ai_latest_experimental" in opt_in_env.split(",")

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

    def record_gen_ai_inference_event(self, operation_name: str, **attributes):
        """
        Records the details of a GenAI completion request including chat history and parameters.
        Event name: gen_ai.client.inference.operation.details
        """
        if not self.use_gen_ai_latest:
            # Revert to pre-1.36.0 fallback if not opted in
            return

        with tracer.start_as_current_span(f"gen_ai.inference.{operation_name}") as span:
            event_attrs = {
                "gen_ai.operation.name": operation_name,
            }

            # Map standard attributes if they are present in kwargs
            for key, val in attributes.items():
                if val is not None:
                    # Structure attributes like gen_ai.input.messages usually need to be JSON stringified
                    if isinstance(val, (dict, list)):
                        try:
                            event_attrs[key] = json.dumps(val)
                        except TypeError:
                            pass
                    else:
                        event_attrs[key] = val

            span.add_event("gen_ai.client.inference.operation.details", attributes=event_attrs)
            logger.info(f"Emitted GenAI inference event: {operation_name}")

    def record_gen_ai_evaluation_event(self, evaluation_name: str, **attributes):
        """
        Records the result of evaluating GenAI output for quality, accuracy, or other characteristics.
        Event name: gen_ai.evaluation.result
        """
        if not self.use_gen_ai_latest:
            return

        with tracer.start_as_current_span(f"gen_ai.evaluation.{evaluation_name}") as span:
            event_attrs = {
                "gen_ai.evaluation.name": evaluation_name,
            }

            for key, val in attributes.items():
                if val is not None:
                    event_attrs[key] = val

            span.add_event("gen_ai.evaluation.result", attributes=event_attrs)
            logger.info(f"Emitted GenAI evaluation event: {evaluation_name}")

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
