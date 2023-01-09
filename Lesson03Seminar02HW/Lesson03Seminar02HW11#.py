# Реализуйте алгоритм перемешивания списка.
from random import randint

lst = [i for i in range(21)]
print(lst)

for i in range(len(lst)-1,0,-1):
    j = randint(0, i-1)
    lst[i], lst[j] = lst[j], lst[i]
print(lst)
