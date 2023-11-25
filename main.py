from logging import DEBUG, basicConfig
from logging.handlers import TimedRotatingFileHandler
from os import environ, makedirs

from dotenv import load_dotenv

from spotify import Spotify
from spotify.constants.enum.item_type import ItemType
from spotify.constants.enum.time_range import TimeRange
from spotify.logger import get_file_path_logger

load_dotenv(verbose=True)

LOG_DIRECTORY = "logs"
CLIENT_ID = environ["CLIENT_ID"]
CLIENT_SECRET = environ["CLIENT_SECRET"]
REFRESH_TOKEN = environ.get("REFRESH_TOKEN", "")

logger = get_file_path_logger(__name__)

makedirs(LOG_DIRECTORY, exist_ok=True)
basicConfig(
    level=DEBUG,
    datefmt="%Y/%m/%d %H:%M:%S",
    format="%(asctime)s [%(levelname)s] %(name)s:%(lineno)s %(message)s",
    handlers=[
        TimedRotatingFileHandler(
            f"{LOG_DIRECTORY}/spotify.log",
            when="midnight",
            backupCount=30,
            interval=1,
            encoding="utf-8",
        )
    ],
)

spotify = Spotify(CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN)
logger.debug(spotify)

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
        ItemType.ARTIST, time_range=TimeRange.LONG_TERM, limit=1
    )
)

# tracks
print(spotify.get_top_items(ItemType.TRACK, limit=1, offset=1))

# followed artists
print(spotify.get_followed_artists(limit=1))

# follow artists
print(
    spotify.follow_artist_or_user(
        ItemType.ARTIST,
        [
            "2CIMQHirSU0MQqyYHq0eOx",
            "57dN52uHvrHOxijzpIgu3E",
            "1vCWHaC5f2uS3yhpwWbIA6",
        ],
    )
)

# unfollow artists
print(
    spotify.unfollow_artist_or_user(
        ItemType.ARTIST,
        [
            "2CIMQHirSU0MQqyYHq0eOx",
            "57dN52uHvrHOxijzpIgu3E",
            "1vCWHaC5f2uS3yhpwWbIA6",
        ],
    )
)
