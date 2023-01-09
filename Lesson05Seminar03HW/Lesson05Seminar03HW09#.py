# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
from random import randint, uniform
s = randint(3, 15)
lst1 = [str(round(uniform(0, 15), 2)) for _ in range(s)]
print(lst1)

lst2 = [float('0' + e[e.find('.'):]) for e in lst1]
print(max(lst2) - min(lst2))
