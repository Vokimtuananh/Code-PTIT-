from itertools import combinations
n, k = [int (x) for x in input().split()]
s = sorted(set(input().split()))
for i in combinations(s, k):
    print(*i)