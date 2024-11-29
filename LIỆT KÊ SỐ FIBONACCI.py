a = [0, 1, 1]
b = 1
c = 1
for i in range(3, 93):
    k = b + c
    a = a + [k]
    c = b
    b = k
t = int(input())
for _ in range(t):
    x, y = [int(i) for i in input().split()]
    for i in range(x, y + 1):
        print(a[i], end = " ")
    print()