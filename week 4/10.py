def summer():
    n = int(input())
    if n != 0:
        return n + summer()
    else:
        return 0

print(summer())
