class tinhV:
    def __init__(self, name, dv, tg):
        a = [i[0] for i in name.split()]
        b = [i[0] for i in dv.split()]
        self.ma = ''.join(b) + ''.join(a)
        self.name = name
        self.dv = dv
        c = tg.split(':')
        self.vt = 120 / (int(c[0]) - 6 + int(c[1]) / 60)
    def __str__(self):
        return f'{self.ma} {self.name} {self.dv} {round(self.vt)} Km/h'
t = int(input())
TinhV = []
for _ in range(t):
    TinhV.append(tinhV(input(), input(), input()))
TinhV = sorted(TinhV, key = lambda x : -x.vt)
print(*TinhV, sep = '\n')