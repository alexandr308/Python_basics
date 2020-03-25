x = -1
m = 0
i = 1
while x < 0:
    n = int(input())
    if n == 0:
        break
    if m <= n:
        if m == n:
            i += 1
        else:
            i = 1
        m = n
print(i)
