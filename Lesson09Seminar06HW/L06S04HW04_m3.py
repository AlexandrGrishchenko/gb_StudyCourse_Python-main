# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их следования в исходном списке.
from random import randint
from my_check import check


@check
def my_func3(lst):
    '''
    Функция создает словать с подсчетом количества значений элементов в списке.
    :param lst: список натуральных чисел.
    :return: натуральные чисела, не имеющие повторений в исходном списке.
    '''
    el_dic = {}
    for e in lst:
        el_dic[e] = el_dic.get(e, 0) + 1
    for k, v in el_dic.items():
        if v == 1:
            yield k


n = 10**5
lst = [randint(0, 1000) for _ in range(n)]
#my_func3(lst)

if __name__ == '__main__':
    res, mem_diff, time_diff = my_func3(lst)
    print(f"Выполнение заняло {time_diff} сек и {mem_diff} Mib")

'''
Выполнение заняло 0.1043124 сек и 0.0039 Mib
'''