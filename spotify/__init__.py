from dataclasses import dataclass
from typing import Dict, Type, TypeVar

import requests

from spotify.constants.url import URL
from spotify.objects.profile import Profile

T = TypeVar("T")


@dataclass
class Spotify:
    access_token: str

    def __post_init__(self) -> None:
        pass

    @property
    def headers(self) -> Dict[str, str]:
        return {"Authorization": f"Bearer {self.access_token}"}

    def __get(self, url: str, class_: Type[T]) -> T:
        r = requests.get(url, headers=self.headers)
        r.raise_for_status()
        c: T = class_(**r.json())
        return c

    def get_profile(self) -> Profile:
        return self.__get(URL.ME, Profile)

    def get_user(self, user_id: str) -> Profile:
        return self.__get(URL.USERS.format(user_id=user_id), Profile)
