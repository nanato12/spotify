from os import environ

from dotenv import load_dotenv

from spotify import Spotify

load_dotenv(verbose=True)

spotify = Spotify(environ["ACCESS_TOKEN"])
spotify.get_profile()
