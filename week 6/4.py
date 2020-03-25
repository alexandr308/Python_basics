n = int(input())
a = map(int, input().split())
m = int(input())
b = list(map(int, input().split()))

for i in range(len(b)):
    b[i] = [i + 1, b[i]]

b.sort(key=lambda x: x[1])


def find_value(x):
    if(x < b[0][1]):
        return b[0][0]
    if(x > b[-1][1]):
        return b[-1][0]
    i = 0
    j = len(b) - 1
    while(j - i > 1):
        m = (j + i) >> 1
        if(b[m][1] < x):
            i = m
        else:
            j = m
    if(x - b[i][1] < b[j][1] - x):
        return b[i][0]
    else:
        return b[j][0]

print(*[find_value(v) for v in a])
