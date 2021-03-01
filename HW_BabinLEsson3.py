print(' \n "Урок 3: 1-й Пункт ДЗ"')


def division(a, b):
    """Деление"""
    return a / b


fn = int(input("Введите числитель: "))
dn = int(input("Введите знаменатель: "))
if dn == 0:
    print('Деление на ноль!!!')
    dn = int(input("Введите знаменатель: "))
print(division(fn, dn))

print(' \n "Урок 3: 2-й Пункт ДЗ"')


def dosye(n, s, y, e, t) -> str:
    print(f' Вы ввели следующие данные польщователя: {n}   {s}, {y},{e},{t}')
name = input('Введите имя польщователя: ')
surname = input('Введите фамилию: ')
year_of_birth = input('Введите год рождения: ')
email = input('Укажите E-mail: ')
tel = input('Укажите телефон: ')
dosye(name, surname, year_of_birth, email, tel)

print(' \n "Урок 3: 3-й Пункт ДЗ"')


def summa(n, y, x) -> int:
    list1 = [(n), (y), (x)]
    list1.sort(reverse=True)
    result = list1[0] + list1[1]
    print(result)


n = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
x = int(input('Введите третье число: '))
summa(n, y, x)

print(' \n "Урок 3: 4-й Пункт ДЗ"')


def stepen(a, s):
    n = 1
    f = a
    while n <= abs(s):
        v = 1 / f
        f = f * a
        n = n + 1
    d = a ** s
    print(f'Результат c использованием  цикла: {v}')
    print(f'Результат по формуле a**s: {d}')


g = abs(int(input('Введите положительное число: ')))
m = int(input('Введите отрицательную степень (со знаком минус): '))
while m >= 0:
    print("Ноль или положительная степень!")
    m = int(input('Введите корректно отрицательную степень (со знаком минус): '))
stepen(g, m)

print(' \n "Урок 3: 5-й Пункт ДЗ"')
sum_number = 0
vyhod = False
while True:
    text5 = input(
        "Введите строку чисел разделенных пробелом, если будет введен спецсимвол  изи знак препинания, программа подсчитает числа до знака и остановится: ")
    number = text5.split()
    for el in number:
        if el.isalnum() == False:
            vyhod = True
            break
        if el.isdigit() == False:
            print("Было введено не число!")
            break
        try:
            el = float(el)
        except ValueError:
            pass
        sum_number += int(el)
    print(f'Сумма чисел в строке: {sum_number}')
    if vyhod == True:
        print('Был введен спецсимвол!')
        break

print(' \n "Урок 3: 6-й Пункт ДЗ"')


def upper_first_letter(t):
    list6 = list(t)
    is_exit = False
    for el in list6:
        d = ord(el)
        if d < 97 or d > 122:
            is_exit = True
            break
    if is_exit == False:
        q = t.capitalize()
        return q
    else:
        print('Введено неверно, используйте только маленькие латинские буквы')
        t = input('Введите слово из маленьких латинских букв: ')
        w = upper_first_letter(t)
        return w


text6 = input('Введите слово из маленьких латинских букв: ')
w = upper_first_letter(text6)
print(f'Слово, которое вы ввели, теперь  написано с большой буквы!: {w}')
