from abc import ABC, abstractmethod
class Clothes(ABC):
    def __init__(self, v, h):
        self.v = v
        self.v = h

    @abstractmethod
    def calculation_of_textile_consumption(self):
        if self.v is not None:
            cts = self.v / 6.5 + 0.5
        else:
            cts = 2 * self.h + 0.3
        return (f'Расход ткани равен: {cts}')
class Coat(Clothes):
    def __init__(self, v, h):
        print("Тип одежды: пальто")
        self.v = v
        self.h = h
        print(f'Размер пальто {self.v}')

    @property
    def calculation_of_textile_consumption(self):
        return Clothes.calculation_of_textile_consumption(self)

class Costume(Clothes):
    def __init__(self, v, h):
        print("Тип одежды: костюм")
        self.v = v
        self.h = h
        print(f'Рост костюма {self.h}')

    @property
    def calculation_of_textile_consumption(self):
        return Clothes.calculation_of_textile_consumption(self)

newcoat = Coat(23, None)
print(newcoat.calculation_of_textile_consumption)

print('\n')

newcostume = Costume(None, 45)
print(newcostume.calculation_of_textile_consumption)