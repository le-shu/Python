# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

surplus = ""
number = int(input("Введите число: "))
numb = number

while number != 0:
    surplus = str(number % 2) + surplus
    number //= 2
    
print(f'Десятичное число {numb} соответствует двоичному {surplus}')