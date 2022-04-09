from abc import ABC, abstractmethod
from typing import Any
from pathlib import Path

import joblib

from musicalbum import MusicAlbum


class Serializer(ABC):

    @abstractmethod
    def dump(self, obj: Any, save_path: Path) -> None:
        pass

    @abstractmethod
    def load(self, load_path: Path) -> Any:
        pass


class JoblibSerializer(Serializer):

    def __init__(self, pickle_protocol=5):
        self.pickle_protocol = pickle_protocol

    def dump(self, obj: Any, save_path: Path) -> None:
        joblib.dump(obj, save_path, protocol=self.pickle_protocol)

    def load(self, load_path: Path) -> Any:
        return joblib.load(load_path)


if __name__ == "__main__":
    params = {
        "title": "The Wall",
        "artist": "Pink Floyd",
        "year": 1979,
        "songs": ["ABitW1", "ABiTW2"]
    }
    the_wall = MusicAlbum(**params)
    path = Path("the_wall.joblib")

    joblib_serializer = JoblibSerializer()
    joblib_serializer.dump(the_wall, path)
    the_wall_2 = joblib_serializer.load(path)
    print(the_wall_2)

