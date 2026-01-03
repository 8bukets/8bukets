import unittest
import json
import os
import shutil
from agents.learning_agent import LearningAgent
from agents.market_simulation_agent import MarketSimulationAgent
from agents.code_generator_agent import CodeGeneratorAgent

class TestAutonomousSystem(unittest.TestCase):
    def setUp(self):
        # Backup DNA if exists
        if os.path.exists("dna.json"):
            shutil.copy("dna.json", "dna.json.bak")
        else:
            with open("dna.json", "w") as f:
                json.dump({"system_iq": 25}, f)

    def tearDown(self):
        # Restore DNA
        if os.path.exists("dna.json.bak"):
            shutil.move("dna.json.bak", "dna.json")
        if os.path.exists("generated_code"):
            shutil.rmtree("generated_code")

    def test_learning_agent_evolution(self):
        agent = LearningAgent()
        feedback = {"market_score": 80, "feedback": "Increase bid"}

        new_dna = agent.process(feedback)

        self.assertGreater(new_dna["system_iq"], 25)
        self.assertIn("evolution_generation", new_dna)

    def test_market_simulation(self):
        agent = MarketSimulationAgent()
        result = agent.process("Some content", {"targeting": {"keywords": ["Cloud"]}})

        self.assertIn("market_score", result)
        self.assertIn("projected_revenue", result)

    def test_code_generation(self):
        agent = CodeGeneratorAgent()
        dna = {"system_iq": 30, "evolution_generation": 2}
        intel = {"strategic_insight": "Attack"}

        status = agent.process(dna, intel)

        expected_file = "generated_code/strategy_v2.py"
        self.assertTrue(os.path.exists(expected_file))

        with open(expected_file, 'r') as f:
            content = f.read()
            self.assertIn("def execute_strategy():", content)

if __name__ == "__main__":
    unittest.main()
