from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List

from spotify.constants.enum.item_type import ItemType
from spotify.objects import SpotifyObjectItem
from spotify.objects.artist import Artist


@dataclass
class Album(SpotifyObjectItem):
    album_type: str
    release_date: str
    release_date_precision: str
    total_tracks: int
    images: List[Dict[str, Any]] = field(default_factory=list)
    artists: List[Artist] = field(default_factory=list)
    available_markets: List[str] = field(default_factory=list)
    external_urls: Dict[str, str] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Album:
        d["type"] = ItemType(d["type"])
        artists: List[Dict[str, Any]] = d.pop("artists")
        d["artists"] = [Artist.from_dict(artist) for artist in artists]
        return cls(**d)
