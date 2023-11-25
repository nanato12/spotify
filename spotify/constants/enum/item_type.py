from enum import Enum


class ItemType(Enum):
    USER = "user"
    ARTIST = "artist"
    TRACK = "track"
    ALBUM = "album"


class PluralItemType(Enum):
    ARTISTS = "artists"
    TRACKS = "tracks"
