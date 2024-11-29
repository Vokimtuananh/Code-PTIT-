t = int(input())
for _ in range(t):
    a = input()
    b = []
    c = 1
    for i in a:
        if i == '(':
            print(c, end = ' ')
            b.append(c)
            c += 1
        elif i == ')':
            print(b[-1], end = ' ')
            b.pop()
    print()