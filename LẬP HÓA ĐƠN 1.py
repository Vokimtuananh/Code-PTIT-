class HoaDon :
    tien = 0
    def __init__(self, ma, ten, cu, moi) :
        self.ma = ma
        self.ten = ten
        s = moi - cu
        if s <= 50:
            s *= 100
            s += s * 0.02
        elif s <= 100:
            s = 50 * 100 + (s - 50) * 150
            s += s * 0.03
        else:
            s = 50 * 100 + 50 * 150 + (s - 100) * 200
            s += s * 0.05
        self.tien = round(s)
    def output(self) :
        print(self.ma, self.ten, self.tien)
n = int(input())
a = []
for i in range(n) :
    ten = input()
    ma = "KH{:02d}".format(i + 1)
    cu = int(input())
    moi = int(input())
    a.append(HoaDon(ma, ten, cu, moi))
a = sorted(a, key= lambda x : (-x.tien))
for i in a :
    i.output()
