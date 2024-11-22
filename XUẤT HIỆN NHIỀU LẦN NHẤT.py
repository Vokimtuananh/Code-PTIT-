t = int(input())
for _ in range(t):
    a = int(input())
    for _ in range(a):
        b = int(input()).split()
        for i in b:
            if len(i) > len(b):
                print(len(i))
            else:
                print('NO')
        print()
    print()