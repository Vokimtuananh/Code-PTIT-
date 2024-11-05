def nto(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        return True
def chanle(n):
    x = 0
    for i in range(len(n)):
        if (i % 2) != (int(n[i]) % 2):
            return False
        x += int(n[i])
    if nto(x):
        return True
    return False
t = int(input())
for _ in range(t):
    a = input()
    if chanle(a):
        print('YES')
    else:
        print('NO')