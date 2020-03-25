n = int(input())
if n < 11 or n > 20:
    if n % 10 == 1:
        print(n, 'korova')
    elif 2 <= n % 10 <= 4:
        print(n, 'korovy')
    elif (5 <= n % 10 <= 9) or n % 10 == 0:
        print(n, 'korov')
else:
    print(n, 'korov')
