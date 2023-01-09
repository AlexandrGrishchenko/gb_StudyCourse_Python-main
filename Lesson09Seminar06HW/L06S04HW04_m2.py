# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их следования в исходном списке.
from random import randint
from my_check import check


@check
def my_func2(lst):
    '''
    Функция создает словать с подсчетом количества значений элементов в списке.
    Создает новый список и запоняет его уникальными значениями.
    :param lst: список натуральных чисел.
    :return: список натуральных чисел, не имеющих повторений в исходном списке.
    '''
    el_dic = {}
    for e in lst:
        el_dic[e] = el_dic.get(e, 0) + 1
    el_lst = []
    for k, v in el_dic.items():
        if v == 1:
            el_lst.append(k)
    return el_lst


n = 10**5
lst = [randint(0, 1000) for _ in range(n)]
#my_func2(lst)

if __name__ == '__main__':
    res, mem_diff, time_diff = my_func2(lst)
    print(f"Выполнение заняло {time_diff} сек и {mem_diff} Mib")

'''
Выполнение заняло 0.12494319 сек и 24.1 Mib
'''