#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
from random import randint
n = randint(1, 100)
print(n)

#Вариант1
print(f'{n:b}')

#Вариант2
nbin = ''
while n > 0:
    nbin = str(n % 2) + nbin
    n //= 2
print(nbin)
