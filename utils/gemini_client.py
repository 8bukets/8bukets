import os
import google.generativeai as genai
import logging

logger = logging.getLogger(__name__)

class GeminiClient:
    def __init__(self):
        # In a real scenario, we expect GOOGLE_API_KEY env var
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            logger.warning("GOOGLE_API_KEY not found. Gemini features will be mocked.")
            self.mock_mode = True
        else:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-pro')
            self.mock_mode = False

    def analyze_error(self, error_message, logs):
        if self.mock_mode:
            return "Gemini (Mock): The error seems to be caused by a missing file or configuration. Please check your setup."

        prompt = f"""
        Analyze the following error log from a Python autonomous agent system.
        Provide a concise explanation of the root cause and a suggested fix.

        Error:
        {error_message}

        Recent Logs:
        {logs}
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Failed to call Gemini API: {e}"

    def suggest_improvements(self, report_content):
        if self.mock_mode:
            return "Gemini (Mock): Consider adding more data sources and improving error handling."

        prompt = f"""
        Review the following agent report and suggest 3 high-impact improvements for the next autonomous cycle.

        Report:
        {report_content}
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Failed to call Gemini API: {e}"
