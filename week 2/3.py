A = int(input())
B = int(input())
C = int(input())
if A > B:
    if B >= C:
        print(A)
    else:
        if A >= C:
            print(A)
        else:
            print(C)
else:
    if A >= C:
        print(B)
    else:
        if B >= C:
            print(B)
        else:
            print(C)
