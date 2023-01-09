# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
from random import randint
from my_check import check


@check
def my_func2(lst):
    '''
    Функция-генератор
    :param lst: список целых чисел от -1000 до 1000
    :return: элемент исходного списка, если значение больше предыдущего элемента
    '''
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            yield lst[i]


n = 10 ** 7
lst = [randint(-1000, 1000) for _ in range(n)]

if __name__ == '__main__':
    my_gen, mem_diff, time_diff = my_func2(lst)
    print(f"Выполнение заняло {time_diff} сек и {mem_diff} Mib")

'''
Выполнение заняло 0.1092852 сек и 0.00390625 Mib
'''