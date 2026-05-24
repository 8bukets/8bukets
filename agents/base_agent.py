import logging

class Blackboard:
    def __init__(self):
        self.data = {}
    def get(self, key, default=None):
        return self.data.get(key, default)
    def set(self, key, value):
        self.data[key] = value

class BaseAgent:
    def __init__(self, name, dependencies=None, provides=None):
        self.name = name
        self.dependencies = dependencies or []
        self.provides = provides or []
        self.logger = logging.getLogger(name)
        logging.basicConfig(level=logging.INFO)

    async def run(self, data, blackboard: Blackboard):
        raise NotImplementedError
