from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List

from spotify.constants.enum.item_type import ItemType
from spotify.objects import SpotifyObjectItem
from spotify.objects.album import Album
from spotify.objects.artist import Artist


@dataclass
class Track(SpotifyObjectItem):
    preview_url: str
    track_number: int
    disc_number: int
    popularity: int
    is_local: bool
    explicit: bool
    duration_ms: int
    album: Album
    artists: List[Artist] = field(default_factory=list)
    available_markets: List[str] = field(default_factory=list)
    external_ids: Dict[str, str] = field(default_factory=dict)
    external_urls: Dict[str, str] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Track:
        d["type"] = ItemType(d["type"])
        artists: List[Dict[str, Any]] = d.pop("artists")
        d["artists"] = [Artist.from_dict(artist) for artist in artists]
        d["album"] = Album.from_dict(d["album"])
        return cls(**d)
