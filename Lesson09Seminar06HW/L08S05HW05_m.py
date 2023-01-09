# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint
from memory_profiler import profile


@profile
def my_func1(lst):
    '''
    Функция принимает список натуральных чисел.
    Циклом for переводит числа в текст и записывает в текстовый файл.
    Затем считывает строку из файла, разделяяет ее по пробелу и сохраняет в список.
    Циклом for переводит текст в числа, функцией sum считает сумму элементов.
    :param lst: список натуральных чисел
    :return: сумму чисел из файла
    '''
    for i in range(len(lst)):
        lst[i] = str(lst[i]) + ' '
    with open('input.txt', 'w', encoding='utf-8') as in_file:
        in_file.writelines(lst)
    with open('input.txt', 'r', encoding='utf-8') as in_file:
        nums = in_file.readline().split()
        for i in range(len(nums)):
            nums[i] = int(nums[i])
    return sum(nums)


@profile
def my_func2(lst):
    '''
    Функция принимает список натуральных чисел.
    Встроенной функцией map переводит числа в текст и записывает в текстовый файл.
    Затем считывает строку из файла, разделяяет ее по пробелу на элементы списка.
    Функцией map переводит текст в числа, функцией sum считает сумму.
    :param lst: список натуральных чисел
    :return: сумму чисел из файла
    '''
    with open('input.txt', 'w', encoding='utf-8') as in_file:
        in_file.writelines(list(map(str, lst)))
    with open('input.txt', 'r', encoding='utf-8') as in_file:
        res = sum(list(map(int, in_file.readline().split())))
    return res


s = 10 ** 5
nums = [randint(-100, 100) for _ in range(s)]

my_func1(nums)
my_func2(nums)

'''
my_func1:
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     7     22.3 MiB     22.3 MiB           1   @profile
     8                                         def my_func1(lst):
     9     27.0 MiB      0.0 MiB      100001       for i in range(len(lst)):
    10     27.0 MiB      4.7 MiB      100000           lst[i] = str(lst[i]) + ' '
    11     27.0 MiB      0.0 MiB           1       with open('input.txt', 'w', encoding='utf-8') as in_file:
    12     27.0 MiB      0.0 MiB           1           in_file.writelines(lst)
    13     27.0 MiB      0.0 MiB           1       with open('input.txt', 'r', encoding='utf-8') as in_file:
    14     34.1 MiB      7.1 MiB           1           nums = in_file.readline().split()
    15     34.1 MiB      0.0 MiB      100001           for i in range(len(nums)):
    16     34.1 MiB      0.0 MiB      100000               nums[i] = int(nums[i])
    17     34.1 MiB      0.0 MiB           1       return sum(nums)

my_func2:
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    20     27.2 MiB     27.2 MiB           1   @profile
    21                                         def my_func2(lst):
    22     27.2 MiB      0.0 MiB           1       with open('input.txt', 'w', encoding='utf-8') as in_file:
    23     26.9 MiB     -0.3 MiB           1           in_file.writelines(list(map(str, lst)))
    24     26.9 MiB      0.0 MiB           1       with open('input.txt', 'r', encoding='utf-8') as in_file:
    25     27.6 MiB      0.7 MiB           1           res = sum(list(map(int, in_file.readline().split())))
    26     27.6 MiB      0.0 MiB           1       return res

Применение функции map вместо циклов позволило сократить используемую памать. 
'''
