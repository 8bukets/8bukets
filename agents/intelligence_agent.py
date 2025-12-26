from .base_agent import BaseAgent
import asyncio
import json
import os
import random

class IntelligenceAgent(BaseAgent):
    def __init__(self, shared_state):
        super().__init__("IntelligenceAgent", shared_state)
        self.memory_file = "system_memory.json"
        self.load_memory()

        # Initialize Shared Learning Parameters
        self.shared_state['learning_params'] = {
            'bid_aggressiveness': self.memory.get('bid_aggressiveness', 0.5),
            'content_creativity': self.memory.get('content_creativity', 0.5)
        }

    def load_memory(self):
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as f:
                    self.memory = json.load(f)
            except Exception as e:
                self.log(f"Failed to load memory: {e}")
                self.memory = {}
        else:
            self.memory = {}

        # Initialize default IQ if not present
        if 'iq_score' not in self.memory:
            self.memory['iq_score'] = 25.0
            self.memory['experiences'] = 0
            self.memory['successful_actions'] = 0

    def save_memory(self):
        try:
            with open(self.memory_file, 'w') as f:
                json.dump(self.memory, f, indent=4)
        except Exception as e:
            self.log(f"Failed to save memory: {e}")

    async def process_message(self, message):
        self.log(f"🧠 Received intelligence: {message}")

        if message.get('type') == 'research_complete':
            self.log("Deciding next steps: Trigger Analysis.")

        elif message.get('type') == 'health_alert':
            self.log(f"⚠️ HEALTH ALERT: {message['status']}")

        elif message.get('type') == 'action_feedback':
            # Learning step
            self.learn(message)

    def learn(self, feedback):
        self.memory['experiences'] += 1
        success = feedback.get('success', False)

        if success:
            self.memory['successful_actions'] += 1
            # Increase IQ slightly for success
            improvement = 0.1
            self.memory['iq_score'] += improvement
            self.log(f"📈 SUCCESS! Learned from experience. IQ increased to {self.memory['iq_score']:.2f}")
        else:
            # "Failures" are also learning opportunities, but maybe smaller IQ gain
            self.memory['iq_score'] += 0.01
            self.log(f"📉 Experience recorded. IQ updated to {self.memory['iq_score']:.2f}")

        # Self-Improvement: Adjust parameters based on IQ and success rate
        success_rate = self.memory['successful_actions'] / self.memory['experiences']

        if success_rate > 0.8:
            # We are doing well, maybe be more aggressive
            self.shared_state['learning_params']['bid_aggressiveness'] = min(1.0, self.shared_state['learning_params']['bid_aggressiveness'] + 0.05)
        elif success_rate < 0.3:
            # We are failing, be more conservative
            self.shared_state['learning_params']['bid_aggressiveness'] = max(0.1, self.shared_state['learning_params']['bid_aggressiveness'] - 0.05)

        self.save_memory()

    async def perform_task(self):
        # Autonomous reflection
        self.log(f"🤔 Reflecting on {self.memory['experiences']} experiences. Current IQ: {self.memory['iq_score']:.2f}")
        self.save_memory()
        await asyncio.sleep(10)
