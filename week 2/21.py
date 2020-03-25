m = -1
max1 = 0
max2 = 0
while m < 0:
    n = int(input())
    if n == 0:
        break
    if max1 < n:
        max2, max1 = max1, n
    else:
        if n > max2:
            max2 = n
print(max2)
