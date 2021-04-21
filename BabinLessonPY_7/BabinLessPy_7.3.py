import math

class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def make_order(self):
        q = self.quantity
        x = math.ceil(q ** .5)
        stroka = (('*' * x +'\n')*(x-1) + (q-x*(x-1)) * '*')
        print(stroka)
    def __add__(self, other):
        sum = self.quantity + other.quantity
        newsell = Cell(sum)
        newsell.make_order()

    def __sub__(self, other):
        subtraction = abs(self.quantity - other.quantity)
        if subtraction !=0:
            newsell = Cell(subtraction)
            newsell.make_order()
        else:
            return "Ошибка! Результат вычитания равен 0!"

    def __mul__(self, other):
        multipication = self.quantity * other.quantity
        newsell = Cell(multipication)
        newsell.make_order()

    def __truediv__(self, other):
        division = self.quantity // other.quantity
        newsell = Cell(division)
        newsell.make_order()


a= int(input('Введите количество ячеек для первой клетки: '))
b = int(input('Введите количество ячеек для второй клетки: '))

first_cell = Cell(a)
second_cell = Cell(b)
print('Количество ячеек в новой клетке в результате объединения:')
first_cell.__add__(second_cell)
print('Количество ячеек в новой клетке в результате вычитания:')
first_cell.__sub__(second_cell)
print('Количество ячеек в новой клетке в результате умножения:')
first_cell.__mul__(second_cell)
print('Количество ячеек в новой клетке в результате деления:')
first_cell.__truediv__(second_cell)