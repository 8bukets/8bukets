from .base import BaseAgent

class ContentCreatorAgent(BaseAgent):
    def __init__(self):
        super().__init__("ContentCreator")

    def run(self, context):
        report = context.get('analysis_report', {})
        if not report:
            self.log_activity("No analysis to base content on.")
            return

        keywords = [w[0] for w in report.get('top_keywords', [])]
        topic = f"The Future of {keywords[0] if keywords else 'Software'}"

        content = f"Title: {topic}\n\nBased on recent trends in {', '.join(keywords)}, we are seeing a shift towards autonomous systems..."
        context['generated_content'] = content
        self.log_activity(f"Generated content draft: {topic}")
