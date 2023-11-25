from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from spotify.objects import SpotifyObject
from spotify.objects.artist import Artist


@dataclass
class Artists(SpotifyObject):
    href: str
    limit: int
    next: Optional[str]
    cursors: List[Dict[str, str]]
    total: int
    items: List[Artist]

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Artists:
        d = d.pop("artists")
        items: List[Dict[str, Any]] = d.pop("items")
        d["items"] = [Artist.from_dict(artist) for artist in items]
        return cls(**d)
