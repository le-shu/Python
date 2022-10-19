# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def dif(arr):
    max = 0
    min = 1
    for i in range(len(arr)):
        fl_part = arr[i] - int(arr[i])
        if fl_part > max:
            max = fl_part
        if 0 < fl_part < min:
            min = fl_part
    print(f'Разница между максимальным и минимальным значением дробной части элементов: {abs(round(max-min,2))}')

arr = []
arr = list(map(float, input('Введите числа через пробел:\n').split()))
print(f'Для списка: {arr}')
dif(arr)