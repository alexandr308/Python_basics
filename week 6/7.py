n = int(input())
A = []
for i in range(n):
    lst = list(map(str, input().split()))
    A.append(lst)

A.sort(key=lambda x: int(x[1]), reverse=True)

for i in A:
    print(i[0])
