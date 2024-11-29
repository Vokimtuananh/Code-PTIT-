m = {}
n = int(input())
a = [int(x) for x in input().split()]
for i in a:
    if i in m:
        m[i] += 1
    else:
        m[i] = 1
for i in range(1, 30000):
    if not i in a:
        print(i)
        break