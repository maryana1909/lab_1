# import math
# a = int(input("Введтие число: "))
# print(f"Факториал {a}: {math.factorial(a)}")
def fact():
    n = int(input("Введтие число: "))
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return (factorial)


print(fact())
