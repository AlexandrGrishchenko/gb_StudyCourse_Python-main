# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
from random import randint
from math import sqrt


def prim_div(n):
    while n % 2 == 0:
        #print(2, end=' ')
        yield 2
        n //= 2
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            #print(i, end=' ')
            yield i
            n //= i
    if n > 2:
        #print(n, end=' ')
        yield n


n = randint(2, 1000)
print(n)
print(*list(prim_div(n)))
