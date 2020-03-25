s = input()
pos = s.find('f')
rev_s = s[::-1]
rev_pos = rev_s.find('f')
l = len(s) - rev_pos - 1
if pos != -1:
    if l != pos:
        print(pos, l)
    elif l == pos:
        print(pos)
