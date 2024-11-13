a, k, n = [int(x) for x in input().split()]
b = k - a % k + a
c = 0
for i in range(b, n + 1, k) :
    c = 1
    print(i - a, end = " ")
if c == 0:
    print("-1")