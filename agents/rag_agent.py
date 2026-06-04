import os
import uuid
import asyncio
from typing import List, Dict, Any

from .base_agent import BaseAgent, Blackboard

try:
    import google.auth
    from google.adk.agents import Agent as AdkAgent
    from google.adk.tools.retrieval.vertex_ai_rag_retrieval import VertexAiRagRetrieval
    from vertexai.preview import rag
    ADK_AVAILABLE = True
except ImportError:
    ADK_AVAILABLE = False

class RagAgent(BaseAgent):
    """
    RAG Agent based on the Google ADK sample.
    Integrates Vertex AI RAG retrieval into the autonomous cycle.
    """
    def __init__(self):
        super().__init__("RagAgent", dependencies=["analysis_stats"], provides=["rag_insights"])
        self._setup_adk()

    def _setup_adk(self):
        self.tools = []
        if not ADK_AVAILABLE:
            self.logger.warning("Google ADK libraries not available. RAG Agent will run in mock mode.")
            return

        try:
            _, project_id = google.auth.default()
            os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id or "default-project")
            os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
            os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")
        except Exception as e:
            self.logger.warning(f"Could not configure Google Auth for ADK: {e}")

        rag_corpus = os.environ.get("RAG_CORPUS")
        if rag_corpus:
            try:
                ask_vertex_retrieval = VertexAiRagRetrieval(
                    name="retrieve_rag_documentation",
                    description=(
                        "Use this tool to retrieve documentation and reference materials for the question from the RAG corpus,"
                    ),
                    rag_resources=[
                        rag.RagResource(rag_corpus=rag_corpus)
                    ],
                    similarity_top_k=10,
                    vector_distance_threshold=0.6,
                )
                self.tools.append(ask_vertex_retrieval)
            except Exception as e:
                 self.logger.warning(f"Failed to initialize VertexAiRagRetrieval: {e}")
        else:
             self.logger.info("RAG_CORPUS environment variable not set. RAG retrieval tool will not be added.")

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Running RAG Agent Analysis...")

        analysis = blackboard.get("analysis_stats", {})
        top_cats = analysis.get("top_categories", {})
        query = f"Provide insights on these topics: {', '.join(top_cats.keys())}"

        insights = []

        if ADK_AVAILABLE and self.tools:
            try:
                root_agent = AdkAgent(
                    model="gemini-2.5-flash",
                    name="ask_rag_agent",
                    instruction="You are a helpful assistant that answers questions based on the provided retrieved documents.",
                    tools=self.tools,
                )
                # In a real async environment, we'd use an async call or run in executor.
                # AdkAgent.run() is typically synchronous in the preview version, so we wrap it.
                loop = asyncio.get_event_loop()
                response = await loop.run_in_executor(None, root_agent.run, query)
                insights.append(f"ADK RAG Response: {response}")
            except Exception as e:
                 self.logger.error(f"Error running ADK Agent: {e}")
                 insights.append("ADK RAG query failed due to an error.")
        else:
            self.logger.info("Simulating RAG retrieval (No ADK or tools configured).")
            insights.append("Simulated RAG Insight: Found strong correlation in domain knowledge base regarding top categories.")

        return {
            "rag_insights": insights
        }

    async def review(self, blackboard: Blackboard) -> List[str]:
        rag_data = blackboard.get("rag_insights", [])
        if not rag_data:
            return ["No RAG insights generated."]
        return ["RAG insights successfully integrated."]
