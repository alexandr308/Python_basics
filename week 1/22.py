N = int(input())
n1 = N // 1000
n2 = N // 100 % 10
n3 = N // 10 % 10
n4 = N % 10
p1 = str(n1) + str(n2)
p2 = str(n4) + str(n3)
print(int(p1) - int(p2) + 1)
