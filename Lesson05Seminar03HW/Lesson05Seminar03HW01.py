# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def get_num(message):
    n = input(message)
    try:
        return float(n)
    except ValueError:
        return get_num(message)


def get_ratio(n, d):
    return n / d


num = get_num('Введите делимое: ')
div = get_num('Введите делитель: ')

try:
    print(get_ratio(num, div))
except ZeroDivisionError:
    print('На ноль делить нельзя!')
