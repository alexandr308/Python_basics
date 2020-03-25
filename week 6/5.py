fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')

lst = []
lines = fin.readlines()

for line in lines:
    if line != '\n':
        line = line.replace('\ufeff', '').strip().split()
        line = (line[0], line[1], line[3])
        lst.append(line)

lst.sort(key=lambda x: x[0])
for i in lst:
    print(i[0], i[1], i[2], end='\n', file=fout)
