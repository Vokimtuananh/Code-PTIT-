import math
import sys
t = int(input( ))
for _ in range(t):
    N, X, M = map(float, input().split())
    years = math.ceil(math.log(M / N) / math.log(1 + (X / 100)))
    print(years)