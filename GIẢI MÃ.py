t = int(input())
for _ in range(t):
    a = input()
    for i in range(0, len(a), 2):
        for j in range(0, int(a[i + 1])):
            print(a[i], end = '')
    print()