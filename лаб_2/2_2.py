import math
import random


def get_key(num, value):
    for k, v in num.items():
        if v == value:
            return k


def type_per(n):
    if type(n) == list:
        print(set([int(x) for x in n]))
        sum = 0
        for element in range(len(n)):
            l = int(n[element])
            if l < 0:
                sum = sum + l
        print("Сумма отрицательных: ")
        return (sum)
    if type(n) == dict:
        print(" Три минимальных элемента: ")
        for i in range(3):
            min_val = min(n.values())
            print(min_val)
            l = get_key(n, min_val)
            del n[l]
    if type(n) == int:
        for i in range(2, n + 1):
            n = 1
            for j in range(2, i):
                if i % j == 0:
                    n = 0
            if n == 1:
                print(i)
            else:
                n = 0

    if type(n) == str:

        gl = ['а', 'о', 'я', 'у', 'ю', 'е', 'ё', 'э', 'ы', 'и']
        sogl = 'йцкнгшщзхъждлрпвфчсмтьб'
        razm = len(n)
        k1 = 0
        k2 = 0
        k3 = 0
        p = " "
        for i in range(razm):
            c = 0
            for j in range(10):
                if n[i] == gl[j]:
                    k1 = k1 + 1
                    c = 1
            if c == 0:
                for y in range(23):
                    if n[i] == sogl[y]:
                        k2 = k2 + 1
        if k1 == k2:
            for i in range(n):
                for j in range(10):
                    if n[i] == n[j]:
                        print(n[i])
        else:
            print(f"Количество гласных: {k1}, согласных: {k2}")
        for i in range(razm):
            if n[i] == p:
                k3 = k3 + 1
        print("количество слов: ", k3 + 1)
        print("Самое длинное слово: ", max(n.split( ), key=len))


print('С каким типом данных вы хотите работать?')
print('1.  Список.')
print('2.  Словарь.')
print('3.  Целочисленный.')
print('4.  Строковый.')
print('5.  ВЫХОД')
choice = 50
while (choice != 5):
    choice = int(input('Ваш выбор: '))
    if choice == 1:
        num = [i for i in input('Введите значения списка ').split()]
        print(type_per(num))
    if choice == 2:
        from random import randint

        num = 5
        num = {key: sum([int(i) for i in str(key)]) for key in {randint(11, 999): _ for _ in range(5)}}
        print(num)
        print(type_per(num))
    if choice == 3:
        num = int(input("Введите число: "))
        print(f"Простые числа до {num}: ")
        print(type_per(num))
    if choice == 4:
        print("Введите строку")
        num = input()
        print(type_per(num))
    if choice == 5:
        print(":3")
