# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
def get_num():
    print('Введите номер дня недели: ', end='')
    try:
        n = int(input())
    except ValueError:
        n = 0
    if 1 <= n <= 7:
        return n
    return get_num()


num = get_num()

if 1 <= num <= 5:
    print('нет')
elif 6 <= num <= 7:
    print('да')
