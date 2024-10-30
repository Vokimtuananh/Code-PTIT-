t = int(input( ))
for _ in range(t):
    a = int(input( ))
    b = str(a)
    c = 1
    for i in b:
        if i == '0':
            continue
        d = int(i)
        c *= d
    print(c)