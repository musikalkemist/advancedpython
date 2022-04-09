from abc import abstractmethod, ABC


class Animal(ABC):

    @property
    @abstractmethod
    def number_of_legs(self) -> int:
        pass

    @abstractmethod
    def make_sound(self) -> None:
        pass
