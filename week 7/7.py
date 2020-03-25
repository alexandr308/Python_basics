fin = open('input.txt', 'r', encoding='utf8')
dic = {}

for line in fin:
    text = line.split()
    for j in text:
        dic[j] = dic.get(j, 0) + 1
        print(int(dic[j]) - 1)
