def printer_back():
    n = int(input())
    if n != 0:
        return str(printer_back()) + ',' + str(n)
    else:
        return str(n)

s = printer_back()
print(s.replace(',', '\n'))
