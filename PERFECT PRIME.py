def nto(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
# def check(a):
    # if not nto(a):
    #     return False
    # if not nto(int(str(a)[::-1])):
    #     return False
    # for i in str(a):
    #     if not nto(int(i)):
    #         return False
    #     if not nto(sum(int(i))):
    #         return False
    # return True
def check(n):
    m = 0
    s = 0
    x = n
    while n != 0:
        k = n % 10
        if not nto(k):
            return False
        m = m * 10 + k
        s += k
        n = int(n / 10)
    if nto(s) and nto(x) and nto(m):
        return True
    return False
t = int(input())
for _ in range(t):
    a = int(input())
    if check(a):
        print('Yes')
    else:
        print('No')