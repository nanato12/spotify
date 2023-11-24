from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class Profile:
    display_name: str
    external_urls: Dict[str, str]
    href: str
    id: str
    images: List[str]
    type: str
    uri: str
    followers: Dict[str, Any]
