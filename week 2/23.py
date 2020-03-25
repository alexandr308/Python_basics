x = -1
m = 0
max_n = 1
i = 1
while x < 0:
    n = int(input())
    if n == 0:
        break
    if m == n:
        i += 1
        if max_n < i:
            max_n = i
    elif m != n:
        i = 1
    m = n
print(max_n)
