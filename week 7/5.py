n = int(input())
a = set(range(1, n + 1))
lst = []

while n:
    s = input()
    if s == 'HELP':
        break
    st = set(map(int, s.split()))
    ans = input()
    if ans == 'YES':
        a &= st
    elif ans == 'NO':
        a -= st

lst += list(a)

print(*sorted(lst))
