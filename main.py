from os import environ

from dotenv import load_dotenv

from spotify import Spotify
from spotify.constants.enum.item_type import ItemType

load_dotenv(verbose=True)

spotify = Spotify(environ["ACCESS_TOKEN"])
print(spotify.get_profile())
print(spotify.get_user("smedjan"))
print(spotify.follow_playlist("3cEYpjA9oz9GiPac4AsH4n", True))
print(spotify.unfollow_playlist("3cEYpjA9oz9GiPac4AsH4n"))
print(spotify.get_top_items(ItemType.TRACKS, limit=1, offset=1))
