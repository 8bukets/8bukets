from abc import ABC, abstractmethod
from typing import Any, Dict, List

class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Process the data and return a dictionary of results.
        :param data: The list of scraped posts.
        :return: A dictionary containing the agent's findings/output.
        """
        pass

    def format_report(self, results: Dict[str, Any]) -> str:
        """
        Optional helper to format results into a markdown section.
        """
        report = [f"## {self.name} Report"]
        for key, value in results.items():
            report.append(f"### {key.replace('_', ' ').title()}")
            report.append(str(value))
        return "\n\n".join(report)
