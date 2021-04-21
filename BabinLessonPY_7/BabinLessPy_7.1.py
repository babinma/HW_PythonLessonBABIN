class Matrix:
    def __init__(self, param):
        self.param = param
        """Проверка введенных параметров"""
        c = []
        f = type(c)
        a = type(self.param)
        h = type(4)
        res = "данные введены верно"
        if a != f:
            print("Неверный тип данных (не список) создайте объект снова")
            return TypeError
        else:
            for el in self.param:
                if type(el) != f:
                    print("Неверный тип данных (не список списков), создайте объект снова")
                    return TypeError
                else:
                    for chislo in el:
                        if type(chislo) != h:
                            print("В веденном списке есть нецелые числа, создайте объект снова, введите целые числа")
                            return TypeError
        print(res)

    def __str__(self, param):
        print("Представление данных в матричном виде:")
        for items in zip(*param):
            print(" ".join(map(str, items)))

    def __add__(self, other):
        f = list(zip(*self.param))
        g = list(zip(*other.param))
        t = list(zip(f, g))
        for item in t:
            v = list(item)
            list1 = [x + y for x, y in zip(*v)]
            print(" ".join(map(str, list1)))

print("Значения в столбцах для первой матрицы")
b = [[23, 23, 56], [43, 56, 56], [67, 24, 45], [23, 45, 78]]
print(b)
mat1 = Matrix(b)
mat1.__str__(b)

print("Значения в столбцах для второй  матрицы")
other = [[25, 267, 569], [433, 56, 546], [667, 20, 42], [19, 45, 88]]
print(other)
mat2 = Matrix(other)
mat2.__str__(other)

print("Итоговая матрица")
mat1.__add__(mat2)