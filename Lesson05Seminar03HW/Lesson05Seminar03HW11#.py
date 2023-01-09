# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
def fib(n):
    fib_lst = [0]
    for i in range(1, n+1):
        if i == 1:
            fib_lst = [1] + fib_lst + [1]
        else:
            fib_lst = [fib_lst[1] - fib_lst[0]] + fib_lst
            fib_lst += [fib_lst[i*2-1] + fib_lst[i*2-2]]
    return fib_lst


num = int(input('Введите целое неотрицательное число: '))
print(*fib(num))
