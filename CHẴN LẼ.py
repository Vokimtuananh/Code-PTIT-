def check(n):
    a = str(n)
    b = sum(int(d) for d in a)
    if b % 10 != 0:
        return False
    for i in range(len(a) - 1):
        if abs(int(a[i]) - int(a[i + 1])) != 2:
            return False
    return True
t = int(input())
for _ in range(t):
    n = int(input())
    if check(n):
        print('YES')
    else:
        print('NO')