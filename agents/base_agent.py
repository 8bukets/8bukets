
import os
import logging
import json
import google.generativeai as genai

class Blackboard(dict):
    pass

class BaseAgent:
    def __init__(self, name, dependencies=None, provides=None):
        self.name = name
        self.dependencies = dependencies or []
        self.provides = provides or []
        self.logger = logging.getLogger(name)

        # Configure Gemini API
        api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-2.0-flash-exp')
        else:
            self.model = None
            self.logger.warning(f"Agent {name}: No Google API key found. LLM calls will be mocked.")

    async def execute_llm_call(self, messages):
        """Executes a call to the Gemini model."""
        if not self.model:
            self.logger.warning("LLM call mocked due to missing API key.")
            return json.dumps({"analysis": "LLM call mocked", "status": "mocked"})

        try:
            # Simple conversion of messages to Gemini format
            prompt = ""
            for msg in messages:
                prompt += f"{msg['role'].upper()}: {msg['content']}\n"

            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            self.logger.error(f"LLM call failed: {e}")
            return json.dumps({"error": str(e), "status": "error"})

    async def run(self, data, blackboard):
        raise NotImplementedError
