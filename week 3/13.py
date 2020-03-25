s = input()
p = s.find(' ')
p1 = s[:p]
p2 = s[p + 1:]
p1, p2 = p2, p1
print(p1, p2)
