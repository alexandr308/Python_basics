from sys import stdin
import copy


class Matrix:
    def __init__(self, l):
        self.l = l
        self.lst = copy.deepcopy(l)

    def __str__(self):
        mat = self.lst
        s = ''
        i = 0
        while i < len(mat):
            j = 0
            while j < len(mat[i]):
                s += str(mat[i][j])
                j += 1
                if j < len(mat[i]):
                    s += '\t'
            i += 1
            if i < len(mat):
                s += '\n'
        return s

    def size(self):
        return (len(self.lst), len(self.lst[0]))

exec(stdin.read())
