# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
def get_num():
    print(f'Введите целое положительное число: ', end='')
    try:
        n = int(input())
    except ValueError:
        n = 0
    if n > 0:
        return n
    return get_num()


num = get_num()
print(f'Самая большая цифра в числе {num} = ', end='')

max_num = -1
while num > 0:
    if num % 10 > max_num:
        max_num = num % 10
    num //= 10

print(max_num)
