import os
import asyncio
from .base_agent import BaseAgent, Blackboard
try:
    from motor.motor_asyncio import AsyncIOMotorClient
    MOTOR_AVAILABLE = True
except ImportError:
    MOTOR_AVAILABLE = False

class MongoDBAgent(BaseAgent):
    """
    Agent responsible for synchronizing system state and scraped data
    with a MongoDB Atlas cluster or local MongoDB instance.
    """
    def __init__(self):
        super().__init__("MongoDBAgent",
                         dependencies=["analysis_stats", "research_data", "system_evolution"],
                         provides=["mongodb_sync_status"])
        self.uri = os.environ.get("MONGODB_URI")
        self.db_name = os.environ.get("MONGODB_DB", "markposition_db")

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        if not MOTOR_AVAILABLE:
            self.logger.warning("Motor (MongoDB driver) not installed. Skipping sync.")
            return {"mongodb_sync_status": "DRIVER_MISSING"}

        if not self.uri:
            self.logger.warning("MONGODB_URI not found in environment. Skipping sync.")
            return {"mongodb_sync_status": "URI_MISSING"}

        self.logger.info(f"Synchronizing data to MongoDB database: {self.db_name}")

        try:
            client = AsyncIOMotorClient(self.uri)
            db = client[self.db_name]

            # 1. Sync Scraped Data (Batch Upsert)
            if data:
                posts_collection = db["posts"]
                # Use post_url as unique identifier
                for post in data:
                    if "post_url" in post:
                        await posts_collection.update_one(
                            {"post_url": post["post_url"]},
                            {"$set": post},
                            upsert=True
                        )
                self.logger.info(f"Synced {len(data)} posts to MongoDB.")

            # 2. Sync System Snapshot
            snapshots_collection = db["system_snapshots"]
            snapshot = {
                "timestamp": asyncio.get_event_loop().time(),
                "evolution": blackboard.get("system_evolution"),
                "sigma_status": blackboard.get("sigma_performance_report"),
                "analysis": blackboard.get("analysis_stats"),
                "research": blackboard.get("research_data")
            }
            await snapshots_collection.insert_one(snapshot)

            client.close()
            return {"mongodb_sync_status": "SUCCESS"}

        except Exception as e:
            self.logger.error(f"Failed to sync with MongoDB: {e}")
            return {"mongodb_sync_status": f"FAILED: {str(e)}"}
