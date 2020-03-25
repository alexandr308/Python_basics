n = int(input())
dic1 = {}
dic2 = {}
while n:
    s = list(map(str, input().split()))
    dic1[s[0]] = s[1]
    dic2[s[1]] = s[0]
    n -= 1

sin = input()

if sin in dic1:
    print(dic1[sin])
else:
    print(dic2[sin])
