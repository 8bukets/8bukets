from dataclasses import dataclass, field
from typing import List, Optional
import datetime

@dataclass
class Post:
    title: str
    date: str
    external_link: Optional[str]
    author: str
    categories: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    image_url: Optional[str] = None
    original_url: Optional[str] = None
    meta_description: Optional[str] = None
    word_count: int = 0
    h1_count: int = 0
    image_alt: Optional[str] = None

    def to_dict(self):
        return {
            "title": self.title,
            "date": self.date,
            "external_link": self.external_link,
            "author": self.author,
            "categories": self.categories,
            "tags": self.tags,
            "image_url": self.image_url,
            "original_url": self.original_url,
            "meta_description": self.meta_description,
            "word_count": self.word_count,
            "h1_count": self.h1_count,
            "image_alt": self.image_alt
        }
