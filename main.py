import numpy as np
from sage.all import *

p = 1000000007
a = 1
b = -1
E = EllipticCurve(GF(p), [a, b])

g = E.gen(0)

n = E.order()
m = np.random.randint(1000000000) % n

t = g * m
print("generator:", g)
print("point:", t)

sqrt_n = int(n ** 0.5) + 1
baby_steps = {}

for i in range(1, sqrt_n):
    baby_steps[g * i] = i

q = t
step = -sqrt_n * g

found_ans = False
ans = 0

for i in range(sqrt_n):
    if q in baby_steps:
        ans = i * sqrt_n + baby_steps[q]
        found_ans = True
        break
       
    q += step

if (not found_ans):
    print("There's no discrete logarithm for given points")
else:
    print("Discrete logarithm:", ans)
    print("Given point:", t)
    print("g^ans:", g * ans)
