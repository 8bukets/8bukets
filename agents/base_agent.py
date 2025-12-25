from abc import ABC, abstractmethod

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
        print(f"[{self.name}] {message}")
