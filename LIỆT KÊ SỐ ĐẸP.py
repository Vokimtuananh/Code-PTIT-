a = []
b = ['0', '2', '4', '6', '8']
def check(s):
    k = list(s)
    k.reverse()
    k = int(s + ''.join(k))
    global a
    a = a + [k]
    if len(s) != 3:
        for i in b:
            check(s + i)
for i in range(1, 5):
    check(b[i])
a.sort()
t = int(input())
for _ in range(t):
    n = int(input())
    for j in a:
        if j < n:
            print(j, end = ' ')
        else:
            break
    print()