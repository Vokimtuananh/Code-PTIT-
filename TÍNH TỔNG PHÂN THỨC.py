t = int(input())
for _ in range(t):
    n = int(input())
    a = 0
    b = 2
    if n % 2 == 1:
        b = 1
    for i in range(b, n + 1, 2):
        a += 1/i
    print('{:.6f}'.format(a))