def sum(a, b):
    global x
    if 0 < a:
        x += 1
        sum(a - 1, b)
    elif 0 < b:
        x += 1
        sum(a, b - 1)
    else:
        print(x)

x = 0
a = int(input())
b = int(input())
sum(a, b)
