import math

n = float(input())
n_int = int(n)
n_fl = n - n_int
if n_fl >= 0.5:
    print(math.ceil(n))
else:
    print(math.floor(n))
