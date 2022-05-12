from abc import ABC, abstractmethod
from typing import Any
from pathlib import Path


class Serializer(ABC):

    @abstractmethod
    def dump(self, obj: Any, save_path: Path) -> None:
        pass

    @abstractmethod
    def load(self, load_path: Path) -> Any:
        pass


if __name__ == "__main__":
    serializer = Serializer()