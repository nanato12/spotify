from os import environ

from dotenv import load_dotenv

from spotify import Spotify
from spotify.constants.enum.item_type import ItemType
from spotify.constants.enum.time_range import TimeRange

load_dotenv(verbose=True)

spotify = Spotify(environ["ACCESS_TOKEN"])

# show your profile
print(spotify.get_profile())

# show smedjan's profile
print(spotify.get_user("smedjan"))

# follow paylist (id: 3cEYpjA9oz9GiPac4AsH4n)
print(spotify.follow_playlist("3cEYpjA9oz9GiPac4AsH4n", True))

# unfollow paylist (id: 3cEYpjA9oz9GiPac4AsH4n)
print(spotify.unfollow_playlist("3cEYpjA9oz9GiPac4AsH4n"))

# artists
print(
    spotify.get_top_items(
        ItemType.ARTISTS, time_range=TimeRange.LONG_TERM, limit=1
    )
)

# tracks
print(spotify.get_top_items(ItemType.TRACKS, limit=1, offset=1))
