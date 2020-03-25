s = input()
pos = s.find('h')
rev_s = s[::-1]
rev_pos = rev_s.find('h')
l = len(s) - rev_pos - 1
print(s[:pos] + s[l + 1:])
