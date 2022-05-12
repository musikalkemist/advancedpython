import pickle
import json
from abc import ABC, abstractmethod
from typing import Any
from pathlib import Path

import yaml

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


class JsonSerializer(Serializer):

    def __init__(self,
                 sort_keys: bool = True,
                 indent: int = 4):
        self.sort_keys = sort_keys
        self.indent = indent

    def dump(self, obj: Any, save_path: Path) -> None:
        with open(save_path, "w") as file:
            json.dump(obj, file, sort_keys=self.sort_keys, indent=self.indent)

    def load(self, load_path: Path) -> Any:
        with open(load_path, "r") as file:
            return json.load(file)


class YamlSerializer(Serializer):

    def __init__(self, default_flow_style: bool = False) -> None:
        self.default_flow_style = default_flow_style

    def dump(self, obj: Any, save_path: Path) -> None:
        with open(save_path, "w") as file:
            yaml.dump(obj, file, default_flow_style=self.default_flow_style)

    def load(self, load_path: Path) -> Any:
        with open(load_path, "r") as file:
            return yaml.safe_load(file)


if __name__ == "__main__":
    params = {
        "title": "The Wall",
        "artist": "Pink Floyd",
        "year": 1979,
        "songs": ["ABitW1", "ABiTW2"]
    }
    the_wall = MusicAlbum(**params)
    the_wall_dict = the_wall.dict()
    path = Path("the_wall.yaml")

    yaml_serializer = YamlSerializer(True)
    yaml_serializer.dump(the_wall_dict, path)
    the_wall_dict_loaded = yaml_serializer.load(path)
    the_wall_2 = MusicAlbum(**the_wall_dict_loaded)
    print(the_wall_2)

