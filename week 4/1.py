def min4(a, b, c, d):
    while not a <= b <= c <= d:
        if a > b:
            a, b = b, a
        if b > c:
            b, c = c, b
        if c > d:
            c, d = d, c
    print(a)

a = int(input())
b = int(input())
c = int(input())
d = int(input())

min4(a, b, c, d)
