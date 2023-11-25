from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

from spotify.objects import SpotifyObject


@dataclass
class ApiToken(SpotifyObject):
    access_token: str
    expires_in: int
    scope: str
    token_type: str
    refresh_token: Optional[str] = None

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> ApiToken:
        return cls(**d)
