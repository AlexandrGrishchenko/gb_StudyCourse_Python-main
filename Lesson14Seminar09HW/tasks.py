# L06S04HW02
# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
def more_previous(lst):
    return [lst[i] for i in range(1, len(lst)) if lst[i] > lst[i - 1]]


# L06S04HW04
# Представлен список чисел. Определить элементы списка, не имеющие повторений.
def unique_elements(lst):
    el_dic = {}
    for e in lst:
        el_dic[e] = el_dic.get(e, 0) + 1
    return [k for k, v in el_dic.items() if v == 1]


# L11S07HW02
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
class Road:
    mass = 25
    thickness = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_asphalt(self):
        return self._length * self._width * self.mass * self.thickness / 1000


# L12S08HW01
# Реализовать класс Matrix (матрица).
class Matrix(list):
    def __init__(self, list_in):
        self.list_out = [line.copy() for line in list_in]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.list_out])

    def size(self):
        return len(self.list_out), len(self.list_out[0])

    def __add__(self, other):
        size_i, size_j = self.size()
        return Matrix([[self.list_out[i][j] + other.list_out[i][j] for j in range(size_j)] for i in range(size_i)])


# L12S08HW03
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
class ZeroDivError(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def div(x, y):
    if y == 0:
        raise ZeroDivError(x, y)
    return x / y

