from os import environ

from dotenv import load_dotenv

from spotify import Spotify

load_dotenv(verbose=True)

spotify = Spotify(environ["ACCESS_TOKEN"])
print(spotify.get_profile())
print(spotify.get_user("smedjan"))
