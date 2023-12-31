# spotify

とりあえず、Spotifyをプログラムで扱いたいよね

## Setup

```bash
$ make init
```

### 1. Create Spotify APP

<https://developer.spotify.com/dashboard/create>

**Redirect URI** should be set to `http://127.0.0.1:5000` .

Open `settings` of the created app and transcribe `Client ID` and `Client secret` to `.env` (**CLIENT_ID**, **CLIENT_SECRET**).

### 2. Build a local authentication callback server

```bash
$ python server.py
```

Access `127.0.0.1:5000` .

The refresh token will appear on the screen, so transcribe it to `.env` (**REFRESH_TOKEN**).

## Documentation

Basically, it is implemented based on the following `Web API`.

<https://developer.spotify.com/documentation/web-api>

### Initialization

```python
from os import environ

from dotenv import load_dotenv

from spotify import Spotify

load_dotenv(verbose=True)

CLIENT_ID = environ["CLIENT_ID"]
CLIENT_SECRET = environ["CLIENT_SECRET"]
REFRESH_TOKEN = environ.get("REFRESH_TOKEN", "")

spotify = Spotify(CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN)
```

### Users

#### Get Current User's Profile

```python
spotify.get_profile()
```

#### Get User's Top Items

```python
from spotify.constants.enum.item_type import ItemType
from spotify.constants.enum.time_range import TimeRange

# artists
spotify.get_top_items(ItemType.ARTIST, time_range = TimeRange.LONG_TERM, limit=1)

# tracks
spotify.get_top_items(ItemType.TRACK, limit=1, offset=1)
```

#### Get User's Profile

```python
spotify.get_user("smedjan")
```

#### Follow Playlist

```python
spotify.follow_playlist("3cEYpjA9oz9GiPac4AsH4n", True)
```

#### Unfollow Playlist

```python
spotify.unfollow_playlist("3cEYpjA9oz9GiPac4AsH4n")
```

#### Get Followed Artists

```python
spotify.get_followed_artists(limit=1)
```

#### Follow Artists or Users

```python
spotify.follow_artist_or_user(
    ItemType.ARTIST,
    [
        "2CIMQHirSU0MQqyYHq0eOx",
        "57dN52uHvrHOxijzpIgu3E",
        "1vCWHaC5f2uS3yhpwWbIA6",
    ],
)
```

#### Unfollow Artists or Users

```python
spotify.unfollow_artist_or_user(
    ItemType.ARTIST,
    [
        "2CIMQHirSU0MQqyYHq0eOx",
        "57dN52uHvrHOxijzpIgu3E",
        "1vCWHaC5f2uS3yhpwWbIA6",
    ],
)
```

#### Check If User Follows Artists or Users

```python
spotify.is_follow(
    ItemType.ARTIST,
    [
        "2CIMQHirSU0MQqyYHq0eOx",
        "57dN52uHvrHOxijzpIgu3E",
        "1vCWHaC5f2uS3yhpwWbIA6",
    ],
)
```

#### Check if Users Follow Playlist

```python
spotify.is_playlist_follow(
    "3cEYpjA9oz9GiPac4AsH4n", ["jmperezperez", "thelinmichael", "wizzler"]
)
```
