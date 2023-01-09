# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка (Cell).
# В его конструкторе инициализировать параметр (quantity), соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное
# (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки.
# Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
from random import randint


class CellError(Exception):
    def __init__(self, cell1, cell2):
        self.cell1 = cell1
        self.cell2 = cell2


class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return str(self.quantity)

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity != other.quantity:
            q1, q2 = max(self.quantity, other.quantity), min(self.quantity, other.quantity)
            return Cell(q1 - q2)
        else:
            raise CellError(self, other)

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        quantity = self.quantity // other.quantity
        if quantity:
            return Cell(self.quantity // other.quantity)
        return Cell(other.quantity // self.quantity)


c1 = Cell(randint(1, 10))
c2 = Cell(randint(1, 10))

print(f"cell1 = {c1}, cell2 = {c2}")

print(f"Sum for cells = {c1 + c2}")

try:
    print(f"Sub for cells = {c1 - c2}")
except CellError as ce:
    print(f"Error in sub with cells: {ce.cell1} and {ce.cell2}")

print(f"Mul for cells = {c1 * c2}")

print(f"Div for cells = {c1 / c2}")
