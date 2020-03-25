a = list(map(int, input().split()))
mi = a[0]
ma = a[0]
mi_i = 0
ma_i = 0
for i in range(len(a)):
    if a[i] > ma:
        ma = a[i]
        ma_i = i
    elif a[i] < mi:
        mi = a[i]
        mi_i = i
a[ma_i], a[mi_i] = mi, ma
print(*a)
