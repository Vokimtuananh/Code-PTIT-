def check(s):
    a = 1
    b = 0
    c = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] != '0':
                c = 1
                a *= int(s[i])
        else: b += int(s[i])
    if c == 0:
        a = 0
    return a, b
t = int(input())
for _ in range(t):
    n = input()
    print(*check(n))