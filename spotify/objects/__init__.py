from abc import ABC
from dataclasses import dataclass

from spotify.constants.enum.item_type import ItemType


class SpotifyObject(ABC):
    pass


@dataclass
class SpotifyObjectItem(SpotifyObject):
    id: str
    name: str
    type: ItemType
    href: str
    uri: str
