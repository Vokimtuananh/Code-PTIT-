def tav(n):
    for a in n:
        if a != '4' and a != '7':
            return False
    return True
t = int(input())
for b in range(t):
    n = input()
    if tav(n):
        print("YES")
    else:
        print("NO")