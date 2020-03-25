def IsPrime(n):
    i = 2
    while i <= (n ** 0.5):
        if n % i == 0:
            return n % i == 0
        else:
            i += 1
    else:
        return n % i == 0 and n != i

n = int(input())

if IsPrime(n):
    print('NO')
else:
    print('YES')
