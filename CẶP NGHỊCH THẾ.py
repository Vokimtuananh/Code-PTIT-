n = 0
t = int(input())
a = [int(x) for x in input().split()]
for u in range(0, t):
    for v in range(u + 1, t):
        if a[u] > a[v]:
            n += 1
        else:
            continue
print(n)