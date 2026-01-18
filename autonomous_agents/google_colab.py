from .base import BaseAgent
from googlesearch import search

class GoogleColabAgent(BaseAgent):
    def __init__(self):
        super().__init__("GoogleAntigravityColab")

    def run(self, context):
        keywords = context.get('analysis_report', {}).get('top_keywords', [])
        if keywords:
            query = f"trends in {keywords[0][0]}"
            self.log_activity(f"Collaborating with Google Search for: {query}")
            try:
                results = list(search(query, num_results=2))
                context['google_trends'] = results
                self.learn(f"Found external trends: {results}")
            except Exception as e:
                self.logger.error(f"Google search failed: {e}")
                # Fallback for "Antigravity" fun
                context['google_trends'] = ["https://mrdoob.com/projects/chromeexperiments/google-gravity/"]
