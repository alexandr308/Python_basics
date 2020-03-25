import sys

text = sys.stdin.read()

dic = {}

j = 0
for i in text:
    dic[i] = dic.get(i, 0) + 1
    if dic[i] > j:
        j = dic[i]

l = []
for i in dic:
    if dic[i] == j:
        l.append(i)

l.sort()
print(l[0])
