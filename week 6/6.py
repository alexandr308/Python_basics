def count_sort(A):
    B = [0] * (max(A) + 1)
    for i in range(len(A)):
        B[A[i]] += 1
    for j in range(len(B)):
        print((str(j) + ' ') * B[j], end='')

my_list = list(map(int, input().split()))
count_sort(my_list)
