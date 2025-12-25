from collections import defaultdict

class MessageBus:
    def __init__(self):
        self._subscribers = defaultdict(list)
        self._history = []

    def subscribe(self, topic, callback):
        self._subscribers[topic].append(callback)

    def publish(self, topic, message):
        self._history.append((topic, message))
        for callback in self._subscribers[topic]:
            callback(topic, message)

    def get_history(self):
        return self._history
