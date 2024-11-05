def diem(n):
    if 3 <= n <= 4:
        return 2.5
    if 5 <= n <= 6:
        return 3.0
    if 7 <= n <= 9:
        return 3.5
    if 10 <= n <= 12:
        return 4.0
    if 13 <= n <= 15:
        return 4.5
    if 16 <= n <= 19:
        return 5.0
    if 20 <= n <= 22:
        return 5.5
    if 23 <= n <= 26:
        return 6.0
    if 27 <= n <= 29:
        return 6.5
    if 30 <= n <= 32:
        return 7.0
    if 33 <= n <= 34:
        return 7.5
    if 35 <= n <= 36:
        return 8.0
    if 37 <= n <= 38:
        return 8.5
    if 39 <= n <= 40:
        return 9.0
def round_diem(diem):
    if diem % 1 < 0.25:
        return int(diem)
    if diem % 1 >= 0.75:
        return int(diem) + 1.0
    elif (diem % 1 >= 0.25) and (diem % 1 <= 0.75):
        return int(diem) + 0.5
    return round(diem)
t = int(input( ))
for _ in range(t):
    a = input().split()
    r, l = int(a[0]), int(a[1])
    s, w = float(a[2]), float(a[3])
    x = (diem(r) + diem(l) + s + w) / 4.0
    if x - int(x) >= 0.75:
        print(int(x) + 1.0)
    elif x - int(x) >= 0.25:
        print(int(x) + 0.5)
    else:
        print(int(x))