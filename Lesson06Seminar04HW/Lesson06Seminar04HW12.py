# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# список коэффициентов (значения от 0 до 100) ???
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


def get_coeff_sum(polynoms):
    poly_dic = {}
    for polynom in polynoms:
        for e in polynom:
            if e.find('x') > -1:
                if e.find('^') > -1:
                    p = int(e[e.find('^') + 1:])
                else:
                    p = 1
                if e.find('*') > -1:
                    k = int(e[:e.find('*')])
                else:
                    k = 1
            else:
                p = 0
                k = int(e)
            poly_dic[p] = poly_dic.get(p, []) + [k]
    n = max(poly_dic.keys())
    return n, [sum(poly_dic.get(i, [0])) for i in range(n, -1, -1)]


file_out = open('12_output.txt', 'w', encoding='utf8')
files_in = ['12_input_1', '12_input_2']

polynoms = []
for file_name in files_in:
    file_in = open(f'{file_name}.txt', 'r', encoding='utf8')
    for line in file_in:
        print(line.rstrip())
        polynoms.append(line.rstrip().replace(' = 0', '').split(' + '))
    file_in.close()

n, coeff = get_coeff_sum(polynoms)
#print(' + '.join(get_polynom(n, coeff)), '= 0')
print(' + '.join(get_polynom(n, coeff)), '= 0', file=file_out)

file_out.close()
