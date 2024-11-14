from decimal import ROUND_HALF_UP, Decimal
def xep_loai(diem_tb):
    if diem_tb >= 9:
        return "XUAT SAC"
    elif diem_tb >= 8:
        return "GIOI"
    elif diem_tb >= 7:
        return "KHA"
    elif diem_tb >= 5:
        return "TB"
    else:
        return "YEU"
id = 1
class hocsinh:
    mhs = 'HS'
    xeploai = ''
    def __init__(self, ten, diem):
        global id
        self.mhs += '{:02d}'.format(id)
        id += 1
        self.ten = ten
        x = 2 * diem[0] + 2 * diem[1]
        for i in range(2, 10):
            x += diem[i]
        x /= 12
        self.xeploai = xep_loai(x)
        self.diemTrungBinh = x.quantize(Decimal('0.1'), ROUND_HALF_UP)
    def output(self):
        print(self.mhs, self.ten, self.diemTrungBinh, self.xeploai)
t = int(input())
a = []
for _ in range(t):
    b = input()
    c = [Decimal(x) for x in input().split()]
    a.append(hocsinh(b, c))
a = sorted(a, key = lambda x : (-x.diemTrungBinh, x.mhs))
for i in a:
    i.output()