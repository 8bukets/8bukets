import logging
from agents.content_creation_agent import ContentCreationAgent

logger = logging.getLogger("CreativityAgent")

class CreativityAgent(ContentCreationAgent):
    """Alias for ContentCreationAgent as they share the same creative generation logic."""
    pass
