import asyncio
from markposition.celery_app import app
from markposition.agents.base_agent import BaseAgent
import importlib
import logging

logger = logging.getLogger(__name__)

@app.task(name="markposition.tasks.run_agent_task")
def run_agent_task(agent_module, agent_class, data, context):
    """
    Celery task to run a single agent.
    Note: Since agents are async, we need a bridge to run them in Celery (which is sync-based by default).
    """
    async def _run():
        module = importlib.import_module(agent_module)
        cls = getattr(module, agent_class)
        agent = cls()
        return await agent.run(data, context)

    return asyncio.run(_run())
