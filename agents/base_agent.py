from abc import ABC, abstractmethod
from colors import Colors, colorize

class BaseAgent(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def run(self, data):
        """
        Process the data and return a result.
        :param data: List of dictionaries (parsed from links.json)
        :return: A string or dictionary containing the agent's output/report.
        """
        pass

    def log(self, message):
        # Colorize the agent name in CYAN
        agent_tag = colorize(f"[{self.name}]", Colors.CYAN)
        print(f"{agent_tag} {message}")
