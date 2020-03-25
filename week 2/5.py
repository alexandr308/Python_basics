a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a - c > 0:
    v = a - c
else:
    v = c - a
if b - d > 0:
    g = b - d
else:
    g = d - b
if v <= 1 and g <= 1:
    print('YES')
else:
    print('NO')
