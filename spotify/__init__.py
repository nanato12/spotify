from dataclasses import dataclass
from profile import Profile
from typing import Dict, Type, TypeVar

import requests

from spotify.constants.url import URL

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
