def xep(x):
    return(-x[1], x[2], x[0])
t = int(input())
list = []
for i in range(t):
    a = input()
    b, c = map(int,input().split())
    list.append((a,b,c))
list.sort(key = xep)
for i in list:
    print(i[0], i[1], i[2])