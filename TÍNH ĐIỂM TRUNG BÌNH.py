n = int(input())
a = [float(x) for x in input().split()]
max = max(a)
min = min(a)
s = 0
b = 0
c = 0
for i in a:
    s += i
    if i == max:
        b += 1
    if i == min:
        c += 1
print('{:.2f}'.format((s - b * max - c * min) / (n - b - c)))