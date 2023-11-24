from urllib.parse import urljoin


class URL:
    HOST = "https://api.spotify.com"

    V1_HOST = urljoin(HOST, "v1")

    ME = f"{V1_HOST}/me"
