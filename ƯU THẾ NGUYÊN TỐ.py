def nto(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def check(n):
    if not nto(len(n)):
        return False
    a = 0
    b = 0
    for i in n:
        if nto(int(i)):
            a += 1
        else:
            b += 1
    if a > b:
        return True
    return False
t = int(input())
for _ in range(t):
    n = input()
    if check(n):
        print('YES')
    else:
        print('NO')