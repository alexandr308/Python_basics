N = int(input())
h = (N // 3600) % 24
m = (N // 60) % 60
s = N % 60
print(h, ':', m // 10, m % 10, ':', s // 10, s % 10, sep='')
