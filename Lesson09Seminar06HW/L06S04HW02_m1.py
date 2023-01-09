# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
from random import randint
from my_check import check


@check
def my_func1(lst):
    '''
    list comprehension
    :param lst: список целых чисел от -1000 до 1000
    :return: список из элементов исходного списка, значения которых больше предыдущего элемента
    '''
    return [lst[i] for i in range(1, len(lst)) if lst[i] > lst[i - 1]]


n = 10 ** 7
lst = [randint(-1000, 1000) for _ in range(n)]

if __name__ == '__main__':
    res, mem_diff, time_diff = my_func1(lst)
    print(f"Выполнение заняло {time_diff} сек и {mem_diff} Mib")

'''
Выполнение заняло 0.7272865 сек и 38.66015625 Mib
'''
