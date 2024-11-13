a = [0] * 1000001
def check():
    a[0] = a[1] = 1
    for k in range(2, 1000):
        if a[k] == 0:
            for j in range(k * k, 1000001, k):
                a[j] = 1
check()
t = int(input())
for _ in range(t):
    n = int(input())
    s = 0
    for i in range(6, n):
        if a[i] == 0 and a[i - 6] == 0 and (a[i - 2] == 0 or a[i - 4] == 0):
            s += 1
    print(s)