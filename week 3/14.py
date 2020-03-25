s = input()
i = 1
while s.find(' ') != -1:
    i += 1
    s = s.replace(' ', '', 1)
print(i)
