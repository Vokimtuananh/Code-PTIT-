import math
t = int(input())
for _ in range(t):
    a = int(input())
    c = str(a)
    d = c[::-1]
    b = int(d)
    if math.gcd(a,b) == 1:
        print('YES')
    else:
        print('NO')