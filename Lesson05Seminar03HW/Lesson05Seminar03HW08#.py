# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import randint
s = randint(2, 10)
lst = [randint(1, 9) for _ in range(s)]
print(lst)

print([e * lst[s-1] for e in lst[:s-1]])
