A = list(map(int, input().split()))
S = A[0]
N = A[1]

B = []
i = 0
while i < N:
    n = int(input())
    B.append(n)
    i += 1

j = 0
B.sort()
for i in B:
    if S - i > 0:
        S = S - i
        j += 1
    else:
        break

print(j)
