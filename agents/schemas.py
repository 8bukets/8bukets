from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional, Dict
from datetime import datetime

class ScrapedPost(BaseModel):
    title: str = Field(..., description="The title of the scraped post")
    date: Optional[str] = None
    datetime: Optional[str] = None
    author: Optional[str] = None
    categories: List[str] = Field(default_factory=list)
    external_link: Optional[str] = None
    domain: Optional[str] = None
    post_url: Optional[str] = None

class EvolutionConfig(BaseModel):
    system_concurrency: int = Field(default=5, ge=1, le=64)
    seo_impact_threshold: float = Field(default=0.5, ge=0.0, le=1.0)
    research_depth: str = "STANDARD"
    evolution_rate: float = 0.05
    current_version: float = 1.0
    last_evolution: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))
