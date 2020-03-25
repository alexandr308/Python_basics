x = int(input())
y = int(input())
m = (y - (x - 1))
res = y // m
if y % m == 0:
    print('YES')
else:
    print('NO')
