from abc import ABC, abstractmethod
from typing import Any, Dict, List

class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name

    def run(self, data: List[Dict[str, Any]], dna: Dict[str, Any] = None, **kwargs) -> Dict[str, Any]:
        """
        Process the data and return a dictionary of results.
        :param data: The list of scraped posts.
        :param dna: The system's DNA configuration.
        :return: A dictionary containing the agent's findings/output.
        """
        # Default implementation if not overridden (for backward compatibility)
        return self._run_legacy(data)

    def _run_legacy(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Fallback for agents that haven't been updated to use DNA yet."""
        return {}

    def format_report(self, results: Dict[str, Any]) -> str:
        """
        Optional helper to format results into a markdown section.
        """
        report = [f"## {self.name} Report"]
        for key, value in results.items():
            report.append(f"### {key.replace('_', ' ').title()}")
            if isinstance(value, list):
                for item in value:
                    report.append(f"- {item}")
            elif isinstance(value, dict):
                for subkey, subval in value.items():
                    report.append(f"- **{subkey}**: {subval}")
            else:
                report.append(str(value))
        return "\n\n".join(report)
