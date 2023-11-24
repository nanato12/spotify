from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class Profile:
    display_name: str
    external_urls: Dict[str, str]
    href: str
    id: str
    images: List[Dict[str, Any]]
    type: str
    uri: str
    followers: Dict[str, Any]
    popularity: Optional[int] = None
    genres: List[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Profile:
        if d.get("name"):
            d["display_name"] = d.pop("name")
        return cls(**d)
