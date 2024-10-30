S1 = input().strip()
S2 = input().strip()
p = int(input())
p -= 1
result = S1[:p] + S2 + S1[p:]
print(result)