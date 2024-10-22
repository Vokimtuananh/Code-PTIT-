t = int(input( ))
for i in range(t):
    d,m =(int(x) for x in input().split())
    if m == 3:
        if d > 20:
            print('Bach Duong')
        else:
            print('Song Ngu')
    elif m == 4:
        if d > 19:
            print('Kim Nguu')
        else:
            print('Bach Duong')
    elif m == 5:
        if d > 20:
            print('Song Tu')
        else:
            print('Kim Nguu')
    elif m == 6:
        if d > 20:
            print('Cu Giai')
        else:
            print('Song Tu')
    elif m == 7:
        if d > 22:
            print('Su Tu')
        else:
            print('Cu Giai')
    elif m == 8:
        if d > 22:
            print('Xu Nu')
        else:
            print('Su Tu')
    elif m == 9:
        if d > 22:
            print('Thien Binh')
        else:
            print('Xu Nu')
    elif m == 10:
        if d > 22:
            print('Thien Yet')
        else:
            print('Thien Binh')
    elif m == 11:
        if d > 22:
            print('Nhan Ma')
        else:
            print('Thien Yet')
    elif m == 12:
        if d > 21:
            print('Ma Ket')
        else:
            print('Nhan Ma')
    elif m == 1:
        if d > 19:
            print('Bao Binh')
        else:
            print('Ma Ket')
    elif m == 2:
        if d > 18:
            print('Song Ngu')
        else:
            print('Bao Binh')