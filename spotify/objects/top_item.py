from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from spotify.objects.profile import Profile


@dataclass
class TopItem:
    items: List[Profile]
    total: int
    limit: int
    offset: int
    href: str
    next: Optional[str]
    previous: Optional[str]

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> TopItem:
        if d.get("items"):
            items: List[Dict[str, Any]] = d.pop("items")
            d["items"] = [Profile.from_dict(item) for item in items]
        return cls(**d)
