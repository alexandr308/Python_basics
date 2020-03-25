import math

P = int(input())
X = int(input())
Y = int(input())
S = X * 100 + Y
res = (S * (100 + P)) / 100
res_x = res // 100
res_y = res % 100
print(int(res_x), int(res_y))
