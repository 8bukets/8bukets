
import logging

class Blackboard(dict):
    pass

class BaseAgent:
    def __init__(self, name, dependencies=None, provides=None):
        self.name = name
        self.dependencies = dependencies or []
        self.provides = provides or []
        self.logger = logging.getLogger(name)

    async def run(self, data, blackboard):
        raise NotImplementedError
