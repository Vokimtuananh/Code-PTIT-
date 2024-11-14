t = int(input())
for k in range(0, t):
    a = int(input())
    b = sorted([int(x) for x in input().split()])
    c = 0
    for i in range(0, a - 2):
        d = i + 1
        e = len(b) - 1
        x = b[i]
        while d < e:
            if x + b[i] + b[e] == 0:
                c += 1
                d += 1
            elif x + b[d] + b[e] < 0:
                d += 1
            else:
                e -= 1
    print(c)