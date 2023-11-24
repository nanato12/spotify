from base64 import b64encode
from os import environ
from typing import Any, Dict

import requests
from dotenv import load_dotenv
from flask import Flask, Response, jsonify, redirect, request

HOST = "127.0.0.1"
PORT = 5000

URL = f"http://{HOST}:{PORT}"
SCOPE = "user-top-read"

load_dotenv(verbose=True)

CLIENT_ID = environ["CLIENT_ID"]
CLIENT_SECRET = environ["CLIENT_SECRET"]
REFRESH_TOKEN = environ.get("REFRESH_TOKEN")

AUTHORIZE_URL = "https://accounts.spotify.com/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&scope={scope}&state=state"

app = Flask(__name__)


def generate_credentials() -> str:
    credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
    return b64encode(credentials.encode()).decode("utf-8")


def post_api_token(data: Dict[str, str]) -> Dict[str, Any]:
    response = requests.post(
        "https://accounts.spotify.com/api/token",
        data=data,
        headers={
            "Authorization": "Basic " + generate_credentials(),
        },
    )
    response.raise_for_status()
    return response.json()


@app.route("/")
def hello() -> Response:
    if REFRESH_TOKEN:
        return jsonify(
            post_api_token(
                {
                    "grant_type": "refresh_token",
                    "refresh_token": REFRESH_TOKEN,
                }
            )
        )

    code = request.args.get("code")

    if code:
        return jsonify(
            post_api_token(
                {
                    "grant_type": "authorization_code",
                    "code": code,
                    "redirect_uri": URL,
                }
            )
        )

    return redirect(
        AUTHORIZE_URL.format(
            client_id=CLIENT_ID, redirect_uri=URL, scope=SCOPE
        )
    )
