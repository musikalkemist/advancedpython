import pickle
import json
from abc import ABC, abstractmethod
from typing import Any
from pathlib import Path

import yaml


class Serializer(ABC):

    @abstractmethod
    def dump(self, obj: Any, save_path: Path) -> None:
        pass

    @abstractmethod
    def load(self, load_path: Path) -> Any:
        pass


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
