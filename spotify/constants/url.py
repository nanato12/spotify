from urllib.parse import urljoin


class URL:
    ACCOUNT_HOST = "https://accounts.spotify.com"
    API_TOKEN = urljoin(ACCOUNT_HOST, "/api/token")

    API_HOST = "https://api.spotify.com"

    LATEST_VERSION = "v1"

    ME = urljoin(API_HOST, LATEST_VERSION + "/me")
    TOP_ITMES = urljoin(API_HOST, ME + "/top/{type}")
    USERS = urljoin(API_HOST, LATEST_VERSION + "/users/{user_id}")

    PLAYLISTS_FOLLOWERS = urljoin(
        API_HOST, LATEST_VERSION + "/playlists/{playlist_id}/followers"
    )
