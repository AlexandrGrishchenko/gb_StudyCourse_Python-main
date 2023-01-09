# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
from random import randint
n = randint(1, 50)
lst = [randint(0, 9) for _ in range(n)]
print(lst)

print(sum([lst[i] for i in range(1, n, 2)]))
print(sum([e for i, e in enumerate(lst) if i % 2]))
