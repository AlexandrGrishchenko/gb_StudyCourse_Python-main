# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint


def get_polynom(n, coef):
    lst = ['' for k in coef if k > 0]
    j = 0
    for i in range(n + 1):
        if coef[i] > 1 or coef[i] == 1 and i == n:
            lst[j] += str(coef[i])
        if coef[i] > 1 and i < n:
            lst[j] += '*'
        if coef[i] > 0 and i < n:
            lst[j] += 'x'
        if n - i > 1 and coef[i] > 0:
            lst[j] += '^' + str(n - i)
        if (coef[i] > 1 or coef[i] == 1 and i == n) or (coef[i] > 0 and i < n):
            j += 1
    return lst


out_file = open('11_output.txt', 'a', encoding='utf8')

n = randint(1, 6)
print(n)

coeff = [randint(0, 100) for _ in range(n + 1)]
print(coeff)

#print(' + '.join(get_polynom(n, coeff)), '= 0')
print(' + '.join(get_polynom(n, coeff)), '= 0', file=out_file)
out_file.close()
