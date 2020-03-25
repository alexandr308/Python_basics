l1 = list(map(int, input().split()))
st = set()
for i in l1:
    if i in st:
        print('YES')
    else:
        print('NO')
    st.add(i)
