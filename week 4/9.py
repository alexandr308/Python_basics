def ReduceFraction(n, m):
    def gbc(a, b):
        while a % b != 0:
            a, b = b, a % b
        return b
    g = gbc(n, m)
    p, q = int(n / g), int(m / g)
    return p, q

n = int(input())
m = int(input())
print(*ReduceFraction(n, m))
