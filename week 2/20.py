m = -1
i = 0
while m < 0:
    n = int(input())
    if n == 0:
        break
    if n % 2 == 0:
        i += 1
        continue
print(i)
