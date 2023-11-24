from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class Profile:
    id: str
    name: str
    type: str
    href: str
    uri: str
    external_urls: Dict[str, str] = field(default_factory=dict)
    images: List[Dict[str, Any]] = field(default_factory=list)
    followers: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Profile:
        if d.get("display_name"):
            d["name"] = d.pop("display_name")
        return cls(**d)
