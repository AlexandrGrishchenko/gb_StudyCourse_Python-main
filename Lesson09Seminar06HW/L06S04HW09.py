# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
from math import sqrt


def prim_div1(n):
    '''
    Функция создает пустой список и заполняет его элементами.
    :param n: натуральное число
    :return: список простых множителей числа N
    '''
    lst = []
    while n % 2 == 0:
        lst.append(2)
        n //= 2
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            lst.append(i)
            n //= i
    if n > 2:
        lst.append(n)
    return lst


def prim_div2(n):
    '''
    Функция-генератор
    :param n: натуральное число
    :return: простые множители числа N
    '''
    while n % 2 == 0:
        yield 2
        n //= 2
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            yield i
            n //= i
    if n > 2:
        yield n


'''
Замеры времени:
prim_div1: 1.3476842
prim_div2: 0.12160039
Использование функции на основе генератора сократило время выполнения программы в несколько раз.
'''