# Напишите программу, которая принимает на вход 2 числа: номер месяца и номер дня в месяце, проверяет является ли день выходным.
# Принимаем начало года на понедельник и считая год не високосным. Учитываем только гос праздники (НГ, 9 мая и т.д.)

a = int(input('Введите номер месяца: '))

while a < 1 or a > 12:
    a = int(input('Нет такого месяца. Введите номер месяца: '))
    
b = int(input('Введите номер дня в месяце: '))

if a == 1:

    while b < 1 or b > 31:
        b = int(input('Нет такого дня. Введите номер дня: '))

    if b == 1:
        print('выходной (Новый год)')
    elif b == 6:
        print('выходной')
    elif b == 7:
        print('выходной (Рождество)')
    elif b == 13:
        print('выходной')
    elif b == 14:
        print('выходной')
    elif b == 20:
        print('выходной')
    elif b == 21:
        print('выходной')
    elif b == 27:
        print('выходной')
    elif b == 28:
        print('выходной')
    else:
        print('будний')

elif a == 2:
    
    while b < 1 or b > 29:
        b = int(input('Нет такого дня. Введите номер дня: '))

    if b == 3:
        print('выходной')
    elif b == 4:
        print('выходной')
    elif b == 10:
        print('выходной')
    elif b == 11:
        print('выходной')
    elif b == 17:
        print('выходной')
    elif b == 18:
        print('выходной')
    elif b == 24:
        print('выходной')
    elif b == 25:
        print('выходной')
    elif b == 23:
        print('выходной (День защитника отечества)')
    else:
        print('будний')

elif a == 3:
    
    while b < 1 or b > 31:
        b = int(input('Нет такого дня. Введите номер дня: '))

    if b == 3:
        print('выходной')
    elif b == 4:
        print('выходной')
    elif b == 10:
        print('выходной')
    elif b == 11:
        print('выходной')
    elif b == 17:
        print('выходной')
    elif b == 18:
        print('выходной')
    elif b == 24:
        print('выходной')
    elif b == 25:
        print('выходной')
    elif b == 31:
        print('выходной')
    elif b == 8:
        print('выходной')
    else:
        print('будний') 

elif a == 4:
    
    while b < 1 or b > 30:
        b = int(input('Нет такого дня. Введите номер дня: '))

    if b == 1:
        print('выходной')
    elif b == 8:
        print('выходной')
    elif b == 7:
        print('выходной')
    elif b == 15:
        print('выходной')
    elif b == 14:
        print('выходной')
    elif b == 22:
        print('выходной')
    elif b == 29:
        print('выходной')
    elif b == 28:
        print('выходной')
    else:
        print('будний')    

elif a == 5:
   
    while b < 1 or b > 31:
        b = int(input('Нет такого дня. Введите номер дня: '))

    if b == 5:
        print('выходной')
    elif b == 6:
        print('выходной')
    elif b == 9:
        print('выходной (День Победы)')
    elif b == 12:
        print('выходной')
    elif b == 13:
        print('выходной')
    elif b == 19:
        print('выходной')
    elif b == 20:
        print('выходной')
    elif b == 26:
        print('выходной')
    elif b == 27:
        print('выходной')
    else:
        print('будний') 

elif a == 6:
    
    while b < 1 or b > 30:
        b = int(input('Нет такого дня. Введите номер дня: '))

    if b == 2:
        print('выходной')
    elif b == 3:
        print('выходной')
    elif b == 9:
        print('выходной')
    elif b == 8:
        print('выходной')
    elif b == 12:
        print('выходной (День России)')
    elif b == 15:
        print('выходной')
    elif b == 16:
        print('выходной')
    elif b == 22:
        print('выходной')
    elif b == 23:
        print('выходной')
    elif b == 29:
        print('выходной')
    elif b == 30:
        print('выходной')
    else:
        print('будний') 

elif a == 7:
   
    while b < 1 or b > 31:
        b = int(input('Нет такого дня. Введите номер дня: '))

    if b == 6:
        print('выходной')
    elif b == 7:
        print('выходной')
    elif b == 13:
        print('выходной')
    elif b == 14:
        print('выходной')
    elif b == 20:
        print('выходной')
    elif b == 21:
        print('выходной')
    elif b == 27:
        print('выходной')
    elif b == 28:
        print('выходной')
    else:
        print('будний') 

elif a == 8:
    
    while b < 1 or b > 31:
        b = int(input('Нет такого дня. Введите номер дня: '))

    if b == 3:
        print('выходной')
    elif b == 4:
        print('выходной')
    elif b == 10:
        print('выходной')
    elif b == 11:
        print('выходной')
    elif b == 17:
        print('выходной')
    elif b == 18:
        print('выходной')
    elif b == 24:
        print('выходной')
    elif b == 25:
        print('выходной')
    elif b == 31:
        print('выходной')
    else:
        print('будний')

elif a == 9:
    
    while b < 1 or b > 30:
        b = int(input('Нет такого дня. Введите номер дня: '))

    if b == 1:
        print('выходной')
    elif b == 7:
        print('выходной')
    elif b == 8:
        print('выходной')
    elif b == 14:
        print('выходной')
    elif b == 15:
        print('выходной')
    elif b == 21:
        print('выходной')
    elif b == 22:
        print('выходной')
    elif b == 28:
        print('выходной')
    elif b == 29:
        print('выходной')
    else:
        print('будний')

elif a == 10:
    
    while b < 1 or b > 31:
        b = int(input('Нет такого дня. Введите номер дня: '))

    if b == 5:
        print('выходной')
    elif b == 6:
        print('выходной')
    elif b == 12:
        print('выходной')
    elif b == 13:
        print('выходной')
    elif b == 19:
        print('выходной')
    elif b == 20:
        print('выходной')
    elif b == 26:
        print('выходной')
    elif b == 27:
        print('выходной')
    else:
        print('будний')

elif a == 11:
    
    while b < 1 or b > 30:
        b = int(input('Нет такого дня. Введите номер дня: '))

    if b == 2:
        print('выходной')
    elif b == 3:
        print('выходной')
    elif b == 4:
        print('выходной (День народного единства)')
    elif b == 9:
        print('выходной')
    elif b == 10:
        print('выходной')
    elif b == 16:
        print('выходной')
    elif b == 17:
        print('выходной')
    elif b == 23:
        print('выходной')
    elif b == 24:
        print('выходной')
    elif b == 30:
        print('выходной')
    else:
        print('будний')

elif a == 12:
    
    while b < 1 or b > 31:
        b = int(input('Нет такого дня. Введите номер дня: '))

    if b == 1:
        print('выходной')
    elif b == 7:
        print('выходной')
    elif b == 8:
        print('выходной')
    elif b == 14:
        print('выходной')
    elif b == 15:
        print('выходной')
    elif b == 21:
        print('выходной')
    elif b == 22:
        print('выходной')
    elif b == 28:
        print('выходной')
    elif b == 29:
        print('выходной')
    else:
        print('будний')