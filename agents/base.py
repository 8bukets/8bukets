class BaseAgent:
    def __init__(self, name):
        self.name = name

    def run(self, *args, **kwargs):
        raise NotImplementedError("Agents must implement the run method")
