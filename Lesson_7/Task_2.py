from abc import ABC, abstractmethod


class MyClass(ABC):
    @abstractmethod
    def add_coat(self):
        pass

    @abstractmethod
    def add_suit(self):
        pass

    @abstractmethod
    def sum_material(self):
        pass


class Coat:
    def __init__(self, coat_size):
        self.coat_mat = coat_size / 6.5 + 0.5


class Suit:
    def __init__(self, suit_height):
        self.suit_mat = suit_height * 2 + 0.3


class Clothes(MyClass):
    def __init__(self, name):
        self.name = name

    def add_coat(self, coat_size):
        self.coat = Coat(coat_size)
        return print(f'Количество материала на пальто размера {coat_size}: {self.coat.coat_mat}')

    def add_suit(self, suit_height):
        self.suit = Suit(suit_height)
        return print(f'Количество материала на костюм размера {suit_height}: {self.suit.suit_mat}')

    @property
    def sum_material(self):
        return f'Общее количество материала: {self.coat.coat_mat + self.suit.suit_mat}'


clothes = Clothes('Одежда')
clothes.add_coat(6.5)
clothes.add_suit(3)
print(clothes.sum_material)
