fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')

lst = []

for i in fin:
    if i != '\n':
        i = i.replace('\n', '').replace('\ufeff', '')
        lst.append(i)

num = len(lst)
dic = {}

for i in lst:
    dic[i] = dic.get(i, 0) + 1

l = []

for i in dic:
    a = (dic[i], i)
    l.append(a)

l.sort(reverse=True)

s1 = set()
s2 = set()
s3 = set()

for i in dic:
    if dic[i] > num / 2:
        s3.add(i)
    else:
        s1.add(l[0][1])
        s2.add(l[1][1])
if s3:
    print(*s3, sep='\n', file=fout)
else:
    print(*s1, *s2, sep='\n', file=fout)

fin.close()
fout.close()
