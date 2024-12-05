b, c = [int(x) for x in input().split()]
a = {}
for _ in range(b):
    s = ''
    for i in input().lower() + ' ':
        if not i.isalpha() and not i.isdigit():
            if s != '':
                if s in a:
                    a[s] += 1
                else:
                    a[s] = 1
                s = ''
        else:
            s += i
a = sorted(a.items(), key = lambda x: (-x[1], x[0]))
for i in a:
    if i[1] >= c:
        print(i[0], i[1])