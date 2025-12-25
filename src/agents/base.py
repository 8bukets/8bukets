from abc import ABC, abstractmethod
import random

class BaseAgent(ABC):
    def __init__(self, name, message_bus, memory):
        self.name = name
        self.bus = message_bus
        self.memory = memory
        self.setup()

    def setup(self):
        """Initial setup for the agent, registering subscriptions."""
        pass

    @abstractmethod
    def act(self):
        """Perform autonomous action."""
        pass

    def log(self, message):
        print(f"[{self.name}] {message}")

    def learn(self):
        """Analyze past experiences to improve."""
        experiences = self.memory.get_experiences(self.name)
        if not experiences:
            return

        # Simple simulation of learning: Calculate average score
        total_score = sum(exp["score"] for exp in experiences)
        avg_score = total_score / len(experiences)
        self.log(f"Reflecting on performance. Average Score: {avg_score:.2f}")

    def publish(self, topic, content):
        message = {
            "sender": self.name,
            "content": content
        }
        self.bus.publish(topic, message)
