from abc import ABC, abstractmethod
import logging
import json
import os
from sqlalchemy import create_engine, Column, String, Text, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime, timezone

MEMORY_FILE = os.getenv("MEMORY_FILE", "data/memory.db")
Base = declarative_base()

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

    def _get_db_session(self):
        os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
        engine = create_engine(f"sqlite:///{MEMORY_FILE}")
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        return Session()

    def update_agent_memory(self, key: str, value: any):
        """Update a specific key in this agent's memory section."""
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

    def get_agent_memory(self, key: str, default=None):
        """Retrieve a specific key from this agent's memory."""
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

    @abstractmethod
    async def run(self, data: list, context: dict) -> dict:
        """
        Run the agent's task.
        :param data: The raw scraped data (list of dicts).
        :param context: A dictionary containing results from previous agents.
        :return: A dictionary containing this agent's output.
        """
        pass
