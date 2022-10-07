import math

def clear():
    print("\n"*50)
availability = {'Шина': 'резина','Антифриз':'Этиленгликоль',
          'Масло': 'секрет', 'Диски': 'сталь'}
price = {'Шина': 60,'Антифриз':12, 'Масло': 37, 'Диски': 90}
amount = {'Шина': 800, 'Масло': 567, 'Антифриз':634,'Диски': 1230}
choice = 50
list = ['Шина', 'Антифриз','Масло', 'Диски']
print('1.  Просмотр описания: название – описание.')
print('2.  Просмотр цены: название – цена.')
print('3.  Просмотр количества: название – количество.')
print('4.  Всю информацию.')
print('5.  Покупка')
print('6.  Вызов меню.')
print('7.  До свидания')
while (choice != 7):
    choice = int(input('Ваш выбор: '))

    if choice == 6:
        print('1.  Просмотр описания: название – описание.')
        print('2.  Просмотр цены: название – цена.')
        print('3.  Просмотр количества: название – количество.')
        print('4.  Всю информацию.')
        print('5.  Покупка')
        print('6.  Вызов меню.')
        print('7.  До свидания')
    if choice == 4:
        for i in range(3):
            str = list[i]
            print()
            print(str, 'Материал', 'Цена', 'Кол-во')
            print('     ', availability[str], '  ', price[str], ' ', amount[str])
            print()
    if choice == 1:
        str = input('Введите название товара: ')
        print('Состав: ', availability[str])
    if choice == 2:
        str = input('Введите название товара: ')
        print('Цена: ', price[str])
    if choice == 3:
        str = input('Введите название товара: ')
        print('Кол-во: ', amount[str])
    if choice == 5:
        str = input('Введите название товара: ')
        print('На складе есть: ', amount[str])
        k = int(input('Введите кол-во: '))
        if k > amount[str]:
            print('На складе недостаточно товара')
            print('Желаете продолжить покупку?')
            print('1. Да')
            print('2. Нет')
            choice2 = int(input())
            if choice2 == 1:
                print('На складе есть: ', amount[str])
                k = int(input('Введите кол-во: '))
                while (k > amount[str]):
                    print('На складе есть: ', amount[str])
                    k = int(input('Введите правильное кол-во: '))
                sum = 0
                sum = sum + k * price[str]
                print('Стоимость:', sum)
                print('Спасибо за покупку!')
                amount[str] = amount[str] - k
        else:
            sum = 0
            sum = sum + k * price[str]
            print('Стоимость:', sum)
            print('Спасибо за покупку!')
            amount[str] = amount[str] - k