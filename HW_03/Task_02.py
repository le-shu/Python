 # Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример: 
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def mult_pairs(arr):
    length = len(arr)//2 + 1 if len(arr) % 2 != 0 else len(arr)//2
    new_arr = [arr[i]*arr[len(arr)-i-1] for i in range(length)]
    print(new_arr)

arr = []
arr = list(map(int, input('Введите числа через пробел:\n').split()))
mult_pairs(arr)