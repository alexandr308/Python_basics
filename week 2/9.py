a = int(input())
b = int(input())
c = int(input())
if a >= b:
    a, b = b, a
if b >= c:
    b, c = c, b
    if a >= c:
        a, c = c, a
    if a >= b:
        a, b = b, a
print(a, b, c)
