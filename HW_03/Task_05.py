# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def Fibonacci(n):
    if n in [1, 2]:                       
        return 1
    else:
        return (Fibonacci(n-1) + Fibonacci(n-2))

def NegaFibonacci(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        number1, number2 = 1, -1
        for i in range(2, n):
            number1, number2 = number2, number1 - number2
        return number2

arr = [0]
number = int(input("Введите число: "))
for i in range(1, number + 1):
    arr.append(Fibonacci(i))
    arr.insert(0, NegaFibonacci(i))
print(arr)