from sys import stdin
import copy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, l):
        self.l = l
        self.lst = copy.deepcopy(l)

    def __add__(self, other):
        if len(self.l) == len(other.l) and len(self.l[0]) == len(other.l[0]):
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
        else:
            raise MatrixError(self, other)

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

    def transpose(self):
        tmatrix = list(zip(*self.l))
        self.l = tmatrix
        self.lst = tmatrix
        return Matrix(tmatrix)

    def transposed(self):
        tmatrix = list(zip(*self.l))
        return Matrix(tmatrix)

    def size(self):
        return (len(self.lst), len(self.lst[0]))

exec(stdin.read())
