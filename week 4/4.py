def MinDivisor(n):
    i = 2
    while i <= (n ** 0.5):
        if n % i == 0:
            print(i)
            break
        i += 1
    else:
        print(n)

n = int(input())

MinDivisor(n)
