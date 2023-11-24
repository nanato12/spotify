# spotify

とりあえず、Spotifyをプログラムで扱いたいよね

## セットアップ

```bash
$ make init
```

### 1. Spotifyのアプリを作成

以下のURLからアプリを作成する。

<https://developer.spotify.com/dashboard/create>

**Redirect URI** は `http://127.0.0.1:5000`

（他のホストやポートを使う場合は適宜変更）

作成したアプリの `settings` を開き、 `Client ID` と `Client secret` を `.env` に転記する（**CLIENT_ID**, **CLIENT_SECRET**）。

### 2. ローカルの認証サーバーを建てる

```bash
$ python server.py
```

そのまま `127.0.0.1:5000` にアクセスする。

画面にリフレッシュトークンが出てくるので、 `.env` に転記する（**REFRESH_TOKEN**）。

### 3. アクセストークンの取得

サーバー起動状態で、`127.0.0.1:5000` にアクセスするとアクセストークンが表示される。

`.env` に転記する（**ACCESS_TOKEN**）。

## Documentation

基本的に以下の `Web API` を実装する。

<https://developer.spotify.com/documentation/web-api>

### 初期化

```python
from os import environ

from dotenv import load_dotenv

from spotify import Spotify

load_dotenv(verbose=True)

spotify = Spotify(environ["ACCESS_TOKEN"])
```

### Users

#### Get Current User's Profile

```python
spotify.get_profile()
```

#### Get User's Top Items

#### Get User's Profile

```python
spotify.get_user("smedjan")
```
