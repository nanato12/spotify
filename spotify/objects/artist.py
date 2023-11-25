from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from spotify.constants.enum.item_type import ItemType
from spotify.objects.profile import Profile


@dataclass
class Artist(Profile):
    popularity: Optional[int] = None
    genres: List[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Artist:
        d["type"] = ItemType(d["type"])
        return cls(**d)
