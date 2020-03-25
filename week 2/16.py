n = int(input())
m = -1
max = n
while m < 0:
    p = int(input())
    if p == 0:
        break
    if max < p:
        max = p
print(max)
