t = int(input())
for i in range(t):
    a = str(input( ))
    if all (b in ['0','1','2'] for b in str(a)):
        print('YES')
    else:
        print('NO')