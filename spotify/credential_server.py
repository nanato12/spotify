from os import environ

from dotenv import load_dotenv
from flask import Flask, Response, redirect, request

from spotify import Spotify
from spotify.constants.enum.scope import Scope

scopes = [
    Scope.USER_TOP_READ,
    Scope.USER_READ_PRIVATE,
    Scope.USER_READ_EMAIL,
    Scope.USER_FOLLOW_READ,
    Scope.PLAYLIST_MODIFY_PUBLIC,
    Scope.PLAYLIST_MODIFY_PRIVATE,
]

HOST = "127.0.0.1"
PORT = 5000

URL = f"http://{HOST}:{PORT}"
SCOPE = " ".join([s.value for s in scopes])

load_dotenv(verbose=True)

CLIENT_ID = environ["CLIENT_ID"]
CLIENT_SECRET = environ["CLIENT_SECRET"]
REFRESH_TOKEN = environ.get("REFRESH_TOKEN")

AUTHORIZE_URL = "https://accounts.spotify.com/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&scope={scope}&state=state"

app = Flask(__name__)


@app.route("/")
def hello() -> Response:
    if REFRESH_TOKEN:
        return Response(f"Refresh token: {REFRESH_TOKEN}")

    code = request.args.get("code")

    if code:
        spotify = Spotify(CLIENT_ID, CLIENT_SECRET)
        r = spotify.generate_refresh_token(code, URL)
        return Response(f"Refresh token: {r.refresh_token}")

    return redirect(
        AUTHORIZE_URL.format(
            client_id=CLIENT_ID, redirect_uri=URL, scope=SCOPE
        )
    )
