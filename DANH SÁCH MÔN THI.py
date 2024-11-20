t = int(input())
d = {}
for _ in range(t):
    a = input()
    b = input()
    c = input()
    d[a] = [b, c]
for i in sorted(d):
    print(i, d[i][0], d[i][1])