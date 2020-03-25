fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')

dic = {}

for line in fin:
    if line != '\n':
        lst = line.replace('\ufeff', '').strip().split()
        buyer = lst[0]
        pr = lst[1]
        count = int(lst[2])
        if buyer in dic:
            dic[buyer][pr] = dic[buyer].get(pr, 0) + count
        else:
            dic[buyer] = {}
            dic[buyer][pr] = count

print(dic)
for i in sorted(dic):
    print(i, ':', sep='')
    for j in sorted(dic[i]):
        print(j, dic[i][j])
