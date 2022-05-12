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


if __name__ == "__main__":
    doggo = Dog()
    print(doggo.number_of_legs)
    doggo.make_sound()