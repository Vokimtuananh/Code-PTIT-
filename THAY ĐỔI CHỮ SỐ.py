t = int(input())
for _ in range(t):
    x, y = [x for x in input().split()]
    a = input().strip()
    if a.count(' '):
        a, b = a.split()
    else:
        b = input()
    c = min(x, y)
    d = max(x, y)
    print(int(a.replace(y, x)) + int(b.replace(y, x)), end = ' ')
    print(int(a.replace(x, y)) + int(b.replace(x, y)))