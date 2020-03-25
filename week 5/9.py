def ev(n):
    for i in range(0, len(n)):
        if i != 0:
            if n[i] > n[i-1]:
                print(n[i], end=' ')

n = list(map(int, input().split()))
ev(n)
