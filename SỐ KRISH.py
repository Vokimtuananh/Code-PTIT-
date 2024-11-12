def giaithua(n):
    if n == 0:
        return True
    return n * giaithua(n - 1)
def check(n):
    s = 0
    m = n
    while n > 0:
        s += giaithua(n % 10)
        n = int(n / 10)
    if s == m:
        return True
    return False
t = int(input())
for _ in range(t):
    a = int(input())
    if check(a):
        print('Yes')
    else:
        print('No')