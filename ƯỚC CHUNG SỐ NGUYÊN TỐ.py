import math
def nto(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
t = int(input( ))
for _ in range(t):
    a, b = [int(x) for x in input().split()]
    c = math.gcd(a, b)
    s = 0
    while c > 0:
        s += c % 10
        c = int(c / 10)
    if nto(s):
        print('YES')
    else:
        print('NO')