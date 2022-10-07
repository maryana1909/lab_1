try:
    n = input('2+3= ')
    n = int(n)
    if n!=5:
        print("ой, кажется вам меньше 7-ми лет..")
    else:
        print("Все нормально. Ответ:", n)
except ValueError:
    print("НУЖНА ЦИФРА!")
finally: # выполняется в любом случае
    print("Конец программы")