from os import environ

from dotenv import load_dotenv

from spotify import Spotify
from spotify.constants.enum.item_type import ItemType
from spotify.constants.enum.time_range import TimeRange

load_dotenv(verbose=True)

spotify = Spotify(environ["ACCESS_TOKEN"])
print(spotify.get_profile())
print(spotify.get_user("smedjan"))
print(spotify.follow_playlist("3cEYpjA9oz9GiPac4AsH4n", True))
print(spotify.unfollow_playlist("3cEYpjA9oz9GiPac4AsH4n"))

# artists
spotify.get_top_items(
    ItemType.ARTISTS, time_range=TimeRange.LONG_TERM, limit=1
)

# tracks
spotify.get_top_items(ItemType.TRACKS, limit=1, offset=1)
