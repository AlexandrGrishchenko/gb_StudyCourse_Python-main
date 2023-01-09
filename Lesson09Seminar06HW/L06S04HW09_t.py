from timeit import timeit
from L06S04HW09 import prim_div1, prim_div2
from random import randint

n = randint(1000, 10000)

print(timeit('prim_div1(n)', globals=globals()))
print(timeit('prim_div2(n)', globals=globals()))
