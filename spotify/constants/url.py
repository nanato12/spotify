from urllib.parse import urljoin


class URL:
    HOST = "https://api.spotify.com"

    V1_HOST = urljoin(HOST, "v1")

    ME = V1_HOST + "/me"
    USERS = V1_HOST + "/users/{user_id}"
