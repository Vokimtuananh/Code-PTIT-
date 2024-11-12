import math
def check(a,b):
    if math.gcd(a,b) == 1:
        return True
    return False
t = int(input())
a = sorted([int(x) for x in input().split()])
for i in range(t):
    for j in range(i + 1, t):
        if check(a[i], a[j]):
            print(a[i], a[j])