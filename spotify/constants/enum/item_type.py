from enum import Enum


class ItemType(Enum):
    USER = "user"
    ARTIST = "artist"
    TRACK = "track"
    ALBUM = "album"

    @property
    def plural_value(self) -> str:
        return f"{self.value}s"
