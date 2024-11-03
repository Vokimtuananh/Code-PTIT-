def check(N):
    N = int(N)
    a = 10
    while N > a:
        if N % a >= a // 2:
            N = (N // a) * a + a
        else:
            N = (N // a) * a
        a *= 10
    return N
t = int(input())
for _ in range(t):
    N = input().strip()
    print(check(N))