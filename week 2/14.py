n = int(input())
m = -1
i = 2
while m < 0:
    if n % i == 0:
        print(i)
        break
    i += 1
