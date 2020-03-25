def merge(A, B):
    C = []
    i = 0
    j = 0
    while i < len(A) or j < len(B):
        if i < len(A) and j < len(B):
            if A[i] > B[j]:
                C.append(B[j])
                j += 1
            elif A[i] > B[j]:
                C.append(B[j])
                j += 1
                C.append(A[i])
                i += 1
            else:
                C.append(A[i])
                i += 1
        elif i < len(A):
            C.append(A[i])
            i += 1
        elif j < len(B):
            C.append(B[j])
            j += 1
    print(*C)

n1 = list(map(int, input().split()))
n2 = list(map(int, input().split()))
merge(n1, n2)
