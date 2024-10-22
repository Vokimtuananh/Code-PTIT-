import math
for t in range(int(input( ))):
    a = input( )
    b= [int(i) for i in a]
    cnt = 0
    dem = 0
    for i in b :
        cnt = cnt + i
        for i in range(len(a)-1):
            if cnt % 10 != 0 or abs(b[i] - b[i + 1]) != 2:
                dem = dem + 1
                if dem == 0:
                    print('YES')
                    break
                else:
                    print('NO')
                    break
        break