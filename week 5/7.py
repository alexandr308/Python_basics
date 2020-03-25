def ev(n):
    j = 0
    for i in range(0, len(n)):
        if n[i] > 0:
            j += 1
    print(j)

n = list(map(int, input().split()))
ev(n)
