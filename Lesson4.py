print(' \n "Урок 4: 2-й Пункт ДЗ"')

from random import randrange
from random import randint
#print(randrange(10, 1000,7))
list1 = list(el for el in list(range(20,10000)) if el % 23 ==0 or el % 22 ==0)
#print(list1)
list2 = []
n=0
while n <= 9:
    d = randint(0,10)
    list2.append(list1[d])
    n +=1
f = list2
print(f'Рандомный список из 10 элементов: {f}')
list3 = []
j = 1
while j < 10:
    if f[j] > f[j-1]:
       list3.append(f[j])
    j = j+1
print(f'Элементы списка, которые больше чем предыдущие: {list3}')

print(' \n "Урок 4: 3-й Пункт ДЗ"')
print('Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.')
print(list(el for el in list(range(20,241)) if el % 20 ==0 or el % 21 ==0))

print(' \n "Урок 4: 4-й Пункт ДЗ"')

list1= [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 23, 23, 6, 8, 8, 16, 17, 17, 24]
print(f'Заданный список чисел {list1}')
list_result = list(el for el in list1 if list1.count(el) == 1)
print(f'Элементы списка, не имеющие повторений: {list_result}')

print(' \n "Урок 4: 5-й Пункт ДЗ"')
from functools import reduce
list1 = list(range(100,1001, 2))
print(f'Четные числа от 100 до 1000: {list1}')
def multiplication (x, y):
    return x*y
result = reduce(multiplication, list1)
print(f'Произведение всех чисел в этом списке равно: {result}')


print(' \n "Урок 4: 6-й Пункт ДЗ"')

from itertools import count
n = int(input("Для генерации целых чисел введите начальное число: "))
d = int(input("Введите конечное число: "))
for el in count(n):
    if el > d:
        break
    else:
        print(el)
print(f'Все целые числа от {n} до {d} выведены')
print('\n')
from itertools import cycle
с = 0
text = input('Введите элементы списка для повторения через пробел:')
n = int(input('Введите число повторений:'))
list2 = text.split(" ")
for el in cycle(list2):
    if с > n:
        break
    print(el)
    с += 1
print(f'Элементы списка повторены указанное количество раз')

print(' \n "Урок 4: 7-й Пункт ДЗ"')
def generator(n):
    v = 1
    s = 1
    while s <= n:
        v = v * s
        s = s+1
        yield v
d = int (input("Введите  число (n) для расчета факториала: "))
for el in generator(d):
    print(el)
print(f'Первые n-чисел выведены')