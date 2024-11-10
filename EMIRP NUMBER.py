a = [0] * 1000001
def check():
    a[0] = a[1] = 1
    for i in range(2, 1000):
        if a[i] == 0:
            for j in range(i * i, 1000001, i) : a[j] = 1
check()
t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(1, n):
        k = int(str(i)[::-1])
        if i < k < n and a[i] == 0 and a[k] == 0:
            print(i, k, end = ' ')
    print()