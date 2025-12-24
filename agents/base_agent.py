from abc import ABC, abstractmethod
from typing import List, Dict, Any

class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    async def process(self, data: List[Dict]) -> Dict[str, Any]:
        """
        Process the data and return a dictionary of results.
        The result dictionary should be suitable for reporting.
        """
        pass

    def format_report(self, results: Dict[str, Any]) -> str:
        """
        Default formatter for the report. Can be overridden.
        """
        report = [f"### {self.name} Report"]
        for key, value in results.items():
            report.append(f"- **{key}**: {value}")
        return "\n".join(report)
