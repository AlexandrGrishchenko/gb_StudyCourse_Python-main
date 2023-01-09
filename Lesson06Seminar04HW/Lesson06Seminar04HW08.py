# Вычислить число c заданной точностью d
# Пример: при d = 0.001, π = 3.141.
# 10^{-1} ≤ d ≤10^{-10}
from random import randint
from math import pi

d = randint(1, 10)
print(d)

p = round(pi, d)
print(p)
