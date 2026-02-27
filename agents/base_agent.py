from abc import ABC, abstractmethod
import logging
import json
import os
from sqlalchemy import create_engine, Column, String, Text, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime, timezone

import asyncio

MEMORY_FILE = os.getenv("MEMORY_FILE", "data/memory.db")
Base = declarative_base()

# Singleton engine and session factory
_engine = None
_SessionFactory = None
_db_lock = asyncio.Lock()

def _get_engine():
    global _engine, _SessionFactory
    if _engine is None:
        os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
        _engine = create_engine(f"sqlite:///{MEMORY_FILE}", connect_args={"check_same_thread": False})
        Base.metadata.create_all(_engine)
        _SessionFactory = sessionmaker(bind=_engine)
    return _engine

class AgentMemory(Base):
    __tablename__ = 'agent_memory'
    agent_name = Column(String, primary_key=True)
    key = Column(String, primary_key=True)
    value = Column(Text)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

class BaseAgent(ABC):
    def __init__(self, name, session=None):
        self.name = name
        self.session = session
        self.logger = logging.getLogger(name)
        _get_engine()

    def _get_db_session(self):
        return _SessionFactory()

    async def update_agent_memory(self, key: str, value: any):
        """Update a specific key in this agent's memory section."""
        async with _db_lock:
            return await asyncio.to_thread(self._sync_update_agent_memory, key, value)

    def _sync_update_agent_memory(self, key: str, value: any):
        session = self._get_db_session()
        try:
            val_str = json.dumps(value)
            entry = session.query(AgentMemory).filter_by(agent_name=self.name, key=key).first()
            if entry:
                entry.value = val_str
            else:
                entry = AgentMemory(agent_name=self.name, key=key, value=val_str)
                session.add(entry)
            session.commit()
        except Exception as e:
            self.logger.error(f"Failed to update agent memory: {e}")
        finally:
            session.close()

    async def get_agent_memory(self, key: str, default=None):
        """Retrieve a specific key from this agent's memory."""
        return await asyncio.to_thread(self._sync_get_agent_memory, key, default)

    def _sync_get_agent_memory(self, key: str, default=None):
        session = self._get_db_session()
        try:
            entry = session.query(AgentMemory).filter_by(agent_name=self.name, key=key).first()
            if entry:
                return json.loads(entry.value)
            return default
        except Exception as e:
            self.logger.error(f"Failed to get agent memory: {e}")
            return default
        finally:
            session.close()

    # Default Stage for Auto-Discovery
    execution_stage = 1

    def add_vector_insight(self, text, meta=None):
        """Add a semantic insight to the global vector memory."""
        try:
            from .vector_memory import VectorMemory
            vm = VectorMemory()
            meta = meta or {}
            meta.update({"agent": self.name, "timestamp": datetime.now(timezone.utc).isoformat()})
            vm.add_entry(text, meta)
        except Exception as e:
            self.logger.error(f"Failed to add vector insight: {e}")

    @abstractmethod
    async def run(self, data: list, context: dict) -> dict:
        """
        Run the agent's task.
        :param data: The raw scraped data (list of dicts).
        :param context: A dictionary containing results from previous agents.
        :return: A dictionary containing this agent's output.
        """
        pass
