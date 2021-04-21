print("\n5 урок, 1 пункт домашнего задания\n")

f = open("BabinLess5.1.txt", "w")
while True:
    d = input("Введите текст для записи, для прекращения ввода no: ")
    if d != 'no':
        f.write(f'{d}\n')
    else:
        f.write("\n")
        break
f.close()
print("Данные введены в файл BabinLess5.1")

print("\n5 урок, 2 пункт домашнего задания\n")

my_text = open("BabinLess5.2.txt", "r")
Stroki = my_text.readlines()
v = 0
for el in Stroki:
    v = v + 1
print(f' Количество строк в файле BabinLess5.2 - {v}')
v=0
for el in Stroki:
    v = v + 1
    s = el.count(" ")+1
    print(f' В {v} строке количество слов равно - {s}')
my_text.close()

print("\n5 урок, 3 пункт домашнего задания\n")
my_text3 = open("BabinLess5.3.txt", "r", encoding="utf-8")
stroki = my_text3.readlines()
tabel_Less_20000 = []
el = "Список тех кому нужно срочно повысить зарплату:\n"
tabel_Less_20000.append(el)
fot = []
n = 0
for el in stroki:
    s = el.find(' - ')
    r = el.find(' р.')
    name = el[0:s]
    salary = int(el[(s+3):r])
    fot.append(salary)
    n = n+1
    if salary <= 20000:
        e = (f'{name} - {salary} р.\n')
        tabel_Less_20000.append(e)
print(''.join(tabel_Less_20000))
average_salary = sum(fot) // n
print(f'Средняя зарплата всех сотрудников - {average_salary} р.')
my_text3.close()

print("\n5 урок, 4 пункт домашнего задания\n")
my_dict = {'One': 'Один', 'Two': 'Два','Three': 'Три', 'Four': 'Четыре'}
my_text4 = open("BabinLess5.4.txt","r", encoding="utf-8")
stroki = my_text4.readlines()
list_new_text = []
for el in stroki:
    for key in my_dict.keys():
        v = el.find(key)
        if v >= 0:
            s = el.replace(key, my_dict.setdefault(key))
            list_new_text.append(s)
new_text = open("BabinLess5.4_new_text.txt", "w")
new_text.writelines(list_new_text)
new_text.close()
my_text4.close()
print("Русские числительные записаны в файл BabinLess5.4.txt!")

print("\n5 урок, 5 пункт домашнего задания\n")
from random import randint
from functools import reduce

list1 = list(el for el in list(range(20,10000)) if el % 23 ==0 or el % 22 ==0)
list2 = []
n = 0
while n <= 9:
    d = randint(0,10)
    list2.append(str((list1[d])))
    n = n + 1
list_numbers = (" ".join(list2))
new_text = open("BabinLess5.5_numbers.txt", "w")
new_text.write(list_numbers)
new_text.close()
new_text1 = open("BabinLess5.5_numbers.txt", "r")
content = new_text1.read()
h = content.split(" ")
print(f'Рандомный список чисел записанный в файл: {h}')
k = 0
g = []
for el in h:
    k = int(el)
    g.append(k)
sum_all = reduce(lambda x,y: x + y, g)
print(f'Сумма всех чисел считанных из файла - {sum_all}')
new_text1.close()

print("\n5 урок, 6 пункт домашнего задания\n")
from re import findall

new_text6 = open("BabinLess5.6_lectures.txt", "r", encoding="utf-8")
print("Перечень предметов и занятий:")
stroki6 = new_text6.read()
print(stroki6)
new_text6.close()
new_text6 = open("BabinLess5.6_lectures.txt", "r", encoding="utf-8")
stroki6 = new_text6.readlines()
dict_lectures = {}
for el in stroki6:
    s = [int(i) for i in findall(r'\d+', el)]
    n = reduce(lambda x,y: x+y, s)
    l = el[0:(el.find(':'))]
    dict_lecture = {l:n}
    dict_lectures.update(dict_lecture)
print('\nИТОГО расчет общего количества занятий по предметам:')
for k, v in dict_lectures.items():
    print(f'{k}: {v}')
new_text6.close()

print("\n5 урок, 7 пункт домашнего задания\n")

import json

new_text7 = open("BabinLess5.7_firms.txt", "r", encoding="utf-8")
print("Заданный перечень фирм с показателями выручки и издержек:")
print(new_text7.read())
new_text7.close()
new_text7 = open("BabinLess5.7_firms.txt", "r", encoding="utf-8")
stroki7 = new_text7.readlines()
total_number_of_firms = len(stroki7)
dict_firms= {}
profit_list = []
for el in stroki7:
    s = [int(i) for i in findall(r'\d+', el)]
    profit_firm = reduce(lambda x,y: x-y, s)
    name = el[0:(el.find(' '))]
    dict_firm = {name : profit_firm}
    dict_firms.update(dict_firm)
    if profit_firm >= 0:
        profit_list.append(profit_firm)
profit_total = reduce(lambda x,y: x+y,profit_list)
average_profit = profit_total//total_number_of_firms
dict_average_profit = {'average profit': average_profit}
new_text7.close()
final_list = [dict_firms,dict_average_profit]
print("Итоговый список из словаря с фирмами и словаря со средней прибылью:")
print(final_list)
with open("file7.json", "w") as write_f:
    json.dump(final_list, write_f)
with open("file7.json") as read_f:
    data = json.load(read_f)
print("Результат обратной выгрузки данных из json-файла:")
print(data)
print(type(data))
