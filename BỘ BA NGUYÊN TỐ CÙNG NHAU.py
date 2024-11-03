import math
def nto(a, b):
    if math.gcd(a, b) == 1:
        return True
    return False
L, R = [int(x) for x in input().split()]
R += 1
for i in range(L, R):
    for j in range(i + 1, R):
        for k in range(j + 1, R):
            if nto(i, j) and nto(j, k) and nto(i, k):
                print('(', end = '')
                print(i, end = ',')
                print(j, end = ',')
                print(k, end = ')\n')