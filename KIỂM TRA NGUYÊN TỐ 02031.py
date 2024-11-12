def nto(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
a, b = [int(x) for x in input().split()]
for _ in range(a):
    a = [int(x) for x in input().split()]
    for i in a:
        if nto(i):
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()