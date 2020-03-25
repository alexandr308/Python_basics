from sys import stdin
import copy


class Matrix:
    def __init__(self, l):
        self.l = l
        self.lst = copy.deepcopy(l)

    def __add__(self, other):
        mat_oth = other.lst
        mat = self.lst
        s = ''
        i = 0
        while i < len(mat):
            j = 0
            while j < len(mat[i]):
                add_sum = mat[i][j] + mat_oth[i][j]
                s += str(add_sum)
                j += 1
                if j < len(mat[i]):
                    s += '\t'
            i += 1
            if i < len(mat):
                s += '\n'
        return s

    def __mul__(self, n):
        self.n = n
        mat = self.lst
        s = ''
        i = 0
        while i < len(mat):
            j = 0
            while j < len(mat[i]):
                s += str(mat[i][j] * n)
                j += 1
                if j < len(mat[i]):
                    s += '\t'
            i += 1
            if i < len(mat):
                s += '\n'
        return s

    __rmul__ = __mul__

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

m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1 + m2)
