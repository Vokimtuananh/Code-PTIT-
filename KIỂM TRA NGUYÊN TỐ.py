def nto(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
t = int(input())
for _ in range(t):
    d = input()
    a = str(d)
    b = a[-4::]
    c = int(b)
    if nto(c):
        print('YES')
    else:
        print('NO')