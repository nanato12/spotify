from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from spotify.constants.enum.item_type import ItemType
from spotify.objects import SpotifyObjectItem


@dataclass
class Profile(SpotifyObjectItem):
    external_urls: Dict[str, str] = field(default_factory=dict)
    images: List[Dict[str, Any]] = field(default_factory=list)
    followers: Dict[str, Any] = field(default_factory=dict)

    # scope: user-read-private
    country: Optional[str] = None
    explicit_content: Dict[str, bool] = field(default_factory=dict)
    product: Optional[str] = None

    # scope: user-read-email
    email: Optional[str] = None

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> Profile:
        d["type"] = ItemType(d["type"])
        if d.get("display_name"):
            d["name"] = d.pop("display_name")
        return cls(**d)
