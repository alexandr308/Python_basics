def ev(n):
    m = 0
    j = 0
    for i in range(0, len(n)):
        if n[i] >= m:
            m = n[i]
            j = i
    print(m, j)

n = list(map(int, input().split()))
ev(n)
