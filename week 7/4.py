import sys

text = sys.stdin.read()
st = set(text.replace(';', '; ').replace('.', '. ').replace(',', ', ').split())

print(len(st))
