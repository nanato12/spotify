from dataclasses import dataclass
from typing import Any, Dict, Type, TypeVar

import requests
from requests import Response

from spotify.constants.enum.item_type import ItemType
from spotify.constants.enum.time_range import TimeRange
from spotify.constants.url import URL
from spotify.objects.profile import Profile
from spotify.objects.top_item import TopItem

A = TypeVar("A", Profile, TopItem)


@dataclass
class Spotify:
    access_token: str

    def __post_init__(self) -> None:
        pass

    @property
    def headers(self) -> Dict[str, str]:
        return {"Authorization": f"Bearer {self.access_token}"}

    @staticmethod
    def __convert(r: Response, class_: Type[A]) -> A:
        print(r.json())
        c: A = class_.from_dict(r.json())
        return c

    def __get(
        self, url: str, class_: Type[A], params: Dict[str, Any] = {}
    ) -> A:
        r = requests.get(url, headers=self.headers, params=params)
        r.raise_for_status()
        return self.__convert(r, class_)

    def __put(self, url: str, data: Dict[str, Any] = {}) -> Response:
        r = requests.put(url, headers=self.headers, data=data)
        r.raise_for_status()
        return r

    def __delete(self, url: str) -> Response:
        r = requests.delete(url, headers=self.headers)
        r.raise_for_status()
        return r

    def get_top_items(
        self,
        type: ItemType,
        time_range: TimeRange = TimeRange.MEDIUM_TERM,
        limit: int = 20,
        offset: int = 0,
    ) -> TopItem:
        if not 0 <= limit <= 50:
            raise ValueError("'limit' must be between 0 and 50.")

        return self.__get(
            URL.TOP_ITMES.format(type=type.value),
            TopItem,
            params={
                "time_range": time_range.value,
                "limit": limit,
                "offset": offset,
            },
        )

    def get_profile(self) -> Profile:
        return self.__get(URL.ME, Profile)

    def get_user(self, user_id: str) -> Profile:
        return self.__get(URL.USERS.format(user_id=user_id), Profile)

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
