from urllib.parse import urljoin


class URL:
    HOST = "https://api.spotify.com"

    V1_HOST = urljoin(HOST, "v1")

    ME = V1_HOST + "/me"
    TOP_ITMES = ME + "/top/{type}"
    USERS = V1_HOST + "/users/{user_id}"

    PLAYLISTS_FOLLOWERS = V1_HOST + "/playlists/{playlist_id}/followers"
