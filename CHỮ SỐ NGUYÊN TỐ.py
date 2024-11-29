import math
class STron:
    def __init__(self, r):
        self.r = r
    def dt(self):
        return (self.r ^ 2) * math.pi
    def cv(self):
        return self.r * 2 * math.pi
r = int(input())
print(STron(r).dt(), STron(r).cv())