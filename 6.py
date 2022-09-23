import math
import random

kort = tuple([random.randint(-100, 100) for _ in range(10)])
c = 0
n = len(kort)
print(kort)
for i in range(n):
    x = kort[i]
    x1 = int(x)
    if x1 < 0 :
        min = x1
        c = 1
if c == 0:
    print("отрицательного элемента нет")
else:
    print(min)