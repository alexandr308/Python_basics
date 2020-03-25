fin = open('input.txt', 'r', encoding='utf-8')
mainDict = {}

for line in fin:
    listLine = line.strip().split()
    cust = listLine[0]
    prod = listLine[1]
    coun = int(listLine[2])
    if cust in mainDict:
        mainDict[cust][prod] = mainDict[cust].get(prod, 0) + coun
    else:
        mainDict[cust] = {}
        mainDict[cust][prod] = coun

for entry in sorted(mainDict):
    print(entry, ':', sep='')
    for entry2 in sorted(mainDict[entry]):
        print(entry2, mainDict[entry][entry2])

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
