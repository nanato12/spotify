from urllib.parse import urljoin


class URL:
    ACCOUNT_HOST = "https://accounts.spotify.com"
    API_TOKEN = urljoin(ACCOUNT_HOST, "/api/token")

    API_HOST = "https://api.spotify.com"
    V1_HOST = urljoin(API_HOST, "/v1")

    ME = V1_HOST + "/me"
    TOP_ITMES = ME + "/top/{type}"
    USERS = V1_HOST + "/users/{user_id}"

    PLAYLISTS_FOLLOWERS = V1_HOST + "/playlists/{playlist_id}/followers"
