def check(s):
    a = 0
    b = 1
    c = 0
    for i in range(len(s)):
        if i % 2 == 0:
            a += int(s[i])
        else:
            if s[i] != '0':
                c = 1
                b *= int(s[i])
    if c == 0:
        b = 0
    return a, b
t = int(input())
for _ in range(t):
    n = input()
    print(*check(n))