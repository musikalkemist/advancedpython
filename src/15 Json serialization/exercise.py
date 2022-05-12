from abc import abstractmethod, ABC


class Animal(ABC):

    @property
    @abstractmethod
    def number_of_legs(self) -> int:
        pass

    @abstractmethod
    def make_sound(self) -> None:
        pass


class Dog(Animal):

    @property
    def number_of_legs(self) -> int:
        return 4

    def make_sound(self) -> None:
        print("Woof woof!")


class Duck(Animal):

    @property
    def number_of_legs(self) -> int:
        return 2

    def make_sound(self) -> None:
        print("Quack quack!")


if __name__ == "__main__":
    duck = Duck()
    print(duck.number_of_legs)
    duck.make_sound()