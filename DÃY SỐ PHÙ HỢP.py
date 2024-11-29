t = int(input())
for _ in range(t):
    k = 1
    n = int(input())
    a = sorted([int(x) for x in input().split()])
    b = sorted([int(x) for x in input().split()])
    for i in range(n):
        if a[i] > b[i]:
            k = 0
            break
    if k == 1:
        print('YES')
    else:
        print('NO')