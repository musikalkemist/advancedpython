import pickle
from abc import ABC, abstractmethod
from typing import Any
from pathlib import Path

from musicalbum import MusicAlbum


class Serializer(ABC):

    @abstractmethod
    def dump(self, obj: Any, save_path: Path) -> None:
        pass

    @abstractmethod
    def load(self, load_path: Path) -> Any:
        pass


class PickleSerializer(Serializer):

    def __init__(self,
                 protocol: int = 5,
                 encoding: str = "ASCII") -> None:
        self.protocol = protocol
        self.encoding = encoding

    def dump(self, obj: Any, save_path: Path) -> None:
        with open(save_path, "wb") as file:
            pickle.dump(obj, file, protocol=self.protocol)

    def load(self, load_path: Path) -> Any:
        with open(load_path, "rb") as file:
            return pickle.load(file, encoding=self.encoding)


if __name__ == "__main__":
    params = {
        "title": "The Wall",
        "artist": "Pink Floyd",
        "year": 1979,
        "songs": ["ABitW1", "ABiTW2"]
    }
    the_wall = MusicAlbum(**params)
    #print(the_wall)

    pickle_serializer = PickleSerializer()
    pickle_serializer.dump(the_wall, Path("the_wall.pkl"))

    the_wall_2 = pickle_serializer.load(Path("the_wall.pkl"))
    print(the_wall_2)

