# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
def get_num(message):
    n = input(message)
    try:
        return float(n)
    except ValueError:
        return get_num(message)


def my_func(a, b, c):
    nums = sorted([a, b, c])
    return nums[-1] + nums[-2]


a, b, c = [get_num(f'Введите {i+1}-е число: ') for i in range(3)]
print(my_func(a, b, c))
