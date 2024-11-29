def check(n , a, b, c):
    if n == 1:
        print(a, '->', b)
        return
    check(n - 1, a, c, b)
    print(a, '->', b)
    check(n - 1, c, b, a)
t = int(input())
check(t, 'A', 'C', 'B')