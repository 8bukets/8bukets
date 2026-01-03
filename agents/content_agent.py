from core.base_agent import BaseAgent
import os

class ContentAgent(BaseAgent):
    def __init__(self):
        super().__init__("ContentAgent")

    def run_cycle(self, context):
        idea = context.get('creative_idea', {})
        if not idea:
            self.log("No creative idea to process.")
            return

        self.log(f"Transforming idea '{idea.get('title')}' into physical assets...")

        # Ensure output directory exists
        output_dir = "generated_output"
        os.makedirs(output_dir, exist_ok=True)

        # 1. Write the code to disk (Physical Code Integration)
        # Sanitize filename
        safe_title = "".join([c if c.isalnum() else "_" for c in idea['title']]).lower()
        filename = os.path.join(output_dir, f"{safe_title}.py")

        try:
            with open(filename, 'w') as f:
                f.write("# Autonomous Generated Code\n")
                f.write(idea.get('code_snippet', '# No code generated'))
            self.log(f"Code successfully written to {filename}")
        except Exception as e:
            self.logger.error(f"Failed to write code: {e}")

        # 2. Create content meta-data for the system
        content_asset = {
            "file_path": filename,
            "type": "code/module",
            "quality_potential": idea.get('innovative_factor', 0.5)
        }

        context['produced_content'] = content_asset
