# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
def get_sec():
    print(f'Введите время в секундах (неотрицательное целое число): ', end='')
    try:
        n = int(input())
    except ValueError:
        n = -1
    if n >= 0:
        return int(n)
    return get_sec()


num = get_sec()
print('%(h)02d:%(m)02d:%(s)02d' % {'h': num // 60 ** 2, 'm': num // 60 % 60, 's': num % 60})
