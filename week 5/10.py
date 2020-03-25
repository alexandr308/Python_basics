def ev(n):
    m = 1000
    for i in range(0, len(n)):
        if n[i] > 0:
            if m > n[i]:
                m = n[i]
    print(m)

n = list(map(int, input().split()))
ev(n)
