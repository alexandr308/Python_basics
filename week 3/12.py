s = input()
pos = s.find('f')
s1 = s[:pos + 1]
s2 = s[pos + 1:]
l1 = len(s1)
l2 = len(s2)
pos1 = s1.find('f')
pos2 = s2.find('f')
if s.find('f') < 0:
    print('-2')
elif s1.find('f') >= 0 and s2.find('f') < 0:
    print('-1')
elif s1.find('f') >= 0 and s2.find('f') >= 0:
    print(len(s1) + pos2)
