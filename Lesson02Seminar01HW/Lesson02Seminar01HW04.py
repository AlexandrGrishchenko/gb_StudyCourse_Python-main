# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)
def get_num():
    print('Введите номер координатной четверти: ', end='')
    try:
        n = int(input())
    except ValueError:
        n = 0
    if 1 <= n <= 4:
        return n
    return get_num()


num = get_num()

if num == 1:
    print('x > 0, y > 0')
elif num == 2:
    print('x < 0, y > 0')
elif num == 3:
    print('x < 0, y < 0')
else:
    print('x > 0, y < 0')
