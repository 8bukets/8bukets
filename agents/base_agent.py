"""
Base Agent Module.
Defines the abstract base class for all agents in the system.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List
import json

class BaseAgent(ABC):
    """
    Abstract base class for agents.
    Handles DNA loading and defines the interface.
    """
    def __init__(self, name: str):
        self.name = name
        self.dna = self.load_dna()

    def load_dna(self) -> Dict[str, Any]:
        """Loads the system's DNA configuration."""
        try:
            with open("system_dna.json", "r", encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    @abstractmethod
    def run(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Process the data and return a dictionary of results.
        :param data: The list of scraped posts.
        :return: A dictionary containing the agent's findings/output.
        """

    def format_report(self, results: Dict[str, Any]) -> str:
        """
        Optional helper to format results into a markdown section.
        """
        report = [f"## {self.name} Report"]
        for key, value in results.items():
            report.append(f"### {key.replace('_', ' ').title()}")
            report.append(str(value))
        return "\n\n".join(report)
