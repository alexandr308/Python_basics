a = int(input())
b = int(input())
c = int(input())
i = 0
if a == b:
    i += 1
if b == c:
    i += 1
if a == c:
    i += 1
if i == 0:
    print('0')
elif i == 1:
    print('2')
else:
    print('3')
