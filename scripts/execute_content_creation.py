import json
import os
import logging
import sys
from datetime import datetime
from agents.content_agent import ContentAgent
from agents.base_agent import Blackboard

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("ContentExecution")

async def execute_content_creation(order_id, description):
    logger.info(f"📝 Executing Content Creation for: {order_id}")

    # Initialize Agent and Blackboard
    agent = ContentAgent()
    blackboard = Blackboard()

    # Mock some data that ContentAgent depends on
    blackboard.set("creative_concepts", [description])
    blackboard.set("intelligence_insights", ["Market trend analyzed", "Autonomous generation active"])

    try:
        # Run the agent
        result = await agent.run([], blackboard)
        content = result.get("generated_content", "No content generated.")

        # Save to results
        os.makedirs("results", exist_ok=True)
        filename = f"CONTENT_{order_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        filepath = os.path.join("results", filename)

        with open(filepath, "w") as f:
            f.write(content)

        logger.info(f"✅ Content saved to {filepath}")
        return filepath
    except Exception as e:
        logger.error(f"❌ Content creation failed: {e}")
        raise

if __name__ == "__main__":
    import asyncio
    if len(sys.argv) < 3:
        print("Usage: python3 execute_content_creation.py <order_id> <description>")
        sys.exit(1)

    order_id = sys.argv[1]
    description = sys.argv[2]
    asyncio.run(execute_content_creation(order_id, description))
