text = open('input.txt', 'r', encoding='utf8')
text = text.readlines()

dic = {}

for line in text:
    for l in line.replace('\ufeff', '').strip().split():
        if l != '':
            dic[l] = dic.get(l, 0) + 1

new_list = []
c = set()

for i in dic:
    c = (dic[i], i)
    new_list.append(c)

a = sorted(new_list, key=lambda x: (-x[0], x[1]))

for i in a:
    print(i[1])
