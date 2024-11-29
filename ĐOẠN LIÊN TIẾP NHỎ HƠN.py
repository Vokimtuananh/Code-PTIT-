t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    s = []
    for i in range(n):
        while len(s) > 0 and a[s[-1]] <= a[i]:
            s.pop()
        if len(s) == 0:
            print(i + 1, end = ' ')
        else:
            print(i - s[-1], end = ' ')
        s.append(i)
    print()