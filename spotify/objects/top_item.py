from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union

from spotify.objects import SpotifyObject
from spotify.objects.artist import Artist
from spotify.objects.track import Track


@dataclass
class TopItem(SpotifyObject):
    items: List[Union[Artist, Track]]
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
            result_items: List[Union[Artist, Track]] = []
            result_items.extend(
                [
                    Artist.from_dict(item)
                    for item in filter(lambda x: x["type"] == "artist", items)
                ]
            )
            result_items.extend(
                [
                    Track.from_dict(item)
                    for item in filter(lambda x: x["type"] == "track", items)
                ]
            )
            d["items"] = result_items
        return cls(**d)
