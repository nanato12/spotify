from base64 import b64encode
from dataclasses import dataclass, field
from typing import Any, Dict, Type, TypeVar

import requests
from requests import Response
from requests.exceptions import JSONDecodeError

from spotify.constants.enum.item_type import ItemType
from spotify.constants.enum.time_range import TimeRange
from spotify.constants.url import URL
from spotify.logger import get_file_path_logger
from spotify.objects.api_token import ApiToken
from spotify.objects.profile import Profile
from spotify.objects.top_item import TopItem

A = TypeVar("A", Profile, TopItem, ApiToken)

logger = get_file_path_logger(__name__)


@dataclass
class Spotify:
    client_id: str
    client_secret: str
    refresh_token: str = ""
    access_token: str = field(init=False, default="")

    def __post_init__(self) -> None:
        if self.refresh_token:
            self.generate_access_token()

    @property
    def headers(self) -> Dict[str, str]:
        if self.access_token:
            return {"Authorization": f"Bearer {self.access_token}"}
        return {"Authorization": f"Basic {self.credential}"}

    @property
    def credential(self) -> str:
        return b64encode(
            f"{self.client_id}:{self.client_secret}".encode()
        ).decode("utf-8")

    @staticmethod
    def __validate_response(r: Response) -> None:
        r.raise_for_status()
        try:
            j = r.json()
        except JSONDecodeError:
            j = {}
        logger.debug(j)

    @staticmethod
    def __convert(r: Response, class_: Type[A]) -> A:
        c: A = class_.from_dict(r.json())
        return c

    def __get(self, url: str, params: Dict[str, Any] = {}) -> Response:
        r = requests.get(url, headers=self.headers, params=params)
        self.__validate_response(r)
        return r

    def __post(self, url: str, data: Dict[str, Any] = {}) -> Response:
        r = requests.post(url, headers=self.headers, data=data)
        self.__validate_response(r)
        return r

    def __put(self, url: str, data: Dict[str, Any] = {}) -> Response:
        r = requests.put(url, headers=self.headers, data=data)
        self.__validate_response(r)
        return r

    def __delete(self, url: str) -> Response:
        r = requests.delete(url, headers=self.headers)
        self.__validate_response(r)
        return r

    def generate_refresh_token(self, code: str, redirect_uri: str) -> ApiToken:
        r = self.__convert(
            self.__post(
                URL.API_TOKEN,
                data={
                    "grant_type": "authorization_code",
                    "code": code,
                    "redirect_uri": redirect_uri,
                },
            ),
            ApiToken,
        )

        if r.refresh_token:
            self.refresh_token = r.refresh_token
        self.access_token = r.access_token

        return r

    def generate_access_token(self) -> ApiToken:
        if not self.refresh_token:
            raise ValueError("'refresh_token' must not be empty.")

        r = self.__convert(
            self.__post(
                URL.API_TOKEN,
                {
                    "grant_type": "refresh_token",
                    "refresh_token": self.refresh_token,
                },
            ),
            ApiToken,
        )
        self.access_token = r.access_token

        return r

    def get_top_items(
        self,
        type_: ItemType,
        time_range: TimeRange = TimeRange.MEDIUM_TERM,
        limit: int = 20,
        offset: int = 0,
    ) -> TopItem:
        if not 0 <= limit <= 50:
            raise ValueError("'limit' must be between 0 and 50.")

        return self.__convert(
            self.__get(
                URL.TOP_ITMES.format(type=type_.plural_value),
                params={
                    "time_range": time_range.value,
                    "limit": limit,
                    "offset": offset,
                },
            ),
            TopItem,
        )

    def get_profile(self) -> Profile:
        return self.__convert(self.__get(URL.ME), Profile)

    def get_user(self, user_id: str) -> Profile:
        return self.__convert(
            self.__get(URL.USERS.format(user_id=user_id)), Profile
        )

    def follow_playlist(
        self, playlist_id: str, public: bool = False
    ) -> Response:
        return self.__put(
            URL.PLAYLISTS_FOLLOWERS.format(playlist_id=playlist_id),
            {"public": public},
        )

    def unfollow_playlist(self, playlist_id: str) -> Response:
        return self.__delete(
            URL.PLAYLISTS_FOLLOWERS.format(playlist_id=playlist_id),
        )
