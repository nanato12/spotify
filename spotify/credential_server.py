from base64 import b64encode
from os import environ

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


@app.route("/")
def hello() -> Response:
    if REFRESH_TOKEN:
        data = {
            "grant_type": "refresh_token",
            "refresh_token": REFRESH_TOKEN,
        }
        headers = {
            "Authorization": "Basic " + generate_credentials(),
        }

        response = requests.post(
            "https://accounts.spotify.com/api/token",
            data=data,
            headers=headers,
        )
        response.raise_for_status()
        return jsonify(response.json())

    code = request.args.get("code")

    if code:
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": URL,
        }
        headers = {
            "Authorization": "Basic " + generate_credentials(),
        }

        response = requests.post(
            "https://accounts.spotify.com/api/token",
            data=data,
            headers=headers,
        )
        response.raise_for_status()
        return jsonify(response.json())

    return redirect(
        AUTHORIZE_URL.format(
            client_id=CLIENT_ID, redirect_uri=URL, scope=SCOPE
        )
    )
