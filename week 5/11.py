N = int(input())
myList = list(map(int, input().split()))
x = int(input())
newList = []
if myList.count(x) > 0:
    print(x)
else:
    for i in range(N):
        newList.append(abs(myList[i] - x))
        ind = newList.index(min(newList))
    print(myList[ind])
