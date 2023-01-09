# Узнайте у пользователя число num. Найдите сумму чисел num + nn + nnn.
def get_num():
    print(f'Введите натуральное число: ', end='')
    try:
        n = int(input())
    except ValueError:
        n = 0
    if n > 0:
        return str(n)
    return get_num()


num = get_num()
print(num, ' + ', num * 2, ' + ', num * 3, ' = ', int(num) + int(num * 2) + int(num * 3), sep='')
