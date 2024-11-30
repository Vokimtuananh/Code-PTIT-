import math
class Hinh:
    def __init__(self, can):
        self.can = can
    def tinh_chu_vi(self):
        pass
    def tinh_dien_tich(self):
        pass
class HinhTron(Hinh):
    def tinh_chu_vi(self):
        return 2 * math.pi * self.can
    def tinh_dien_tich(self):
        return math.pi * (self.can ** 2)
class HinhVuong(Hinh):
    def tinh_chu_vi(self):
        return 4 * self.can
    def tinh_dien_tich(self):
        return self.can ** 2
class HinhTamGiacDeu(Hinh):
    def tinh_chu_vi(self):
        return 3 * self.can
    def tinh_dien_tich(self):
        return (math.sqrt(3) / 4) * (self.can ** 2)
class HinhLucGiacDeu(Hinh):
    def tinh_chu_vi(self):
        return 6 * self.can
    def tinh_dien_tich(self):
        return ((3 * math.sqrt(3)) / 2) * (self.can ** 2)
class HinhNgUgacDeu(Hinh):
    def tinh_chu_vi(self):
        return 5 * self.can
    def tinh_dien_tich(self):
        return (math.sqrt(25 + 10 * math.sqrt(5)) / 4) * (self.can ** 2)
class HinhBatGiacDeu(Hinh):
    def tinh_chu_vi(self):
        return 8 * self.can
    def tinh_dien_tich(self):
        return (2 + 4 / math.sqrt(2)) * (self.can ** 2)
class KhoiTru:
    def __init__(self, hinh, chieu_cao):
        self.hinh = hinh
        self.chieu_cao = chieu_cao
    def tinh_the_tich(self):
        return self.hinh.tinh_dien_tich() * self.chieu_cao
tron = HinhTron(5)
vuong = HinhVuong(4)
tam_giac_deu = HinhTamGiacDeu(3)
luc_giac_deu = HinhLucGiacDeu(6)
ngu_giac_deu = HinhNgUgacDeu(7)
bat_giac_deu = HinhBatGiacDeu(8)
print("Hình Tròn:")
print(f"Chu vi: {tron.tinh_chu_vi()}")
print(f"Diện tích: {tron.tinh_dien_tich()}")
print("\nHình Vuông:")
print(f"Chu vi: {vuong.tinh_chu_vi()}")
print(f"Diện tích: {vuong.tinh_dien_tich()}")
print("\nHình Tam Giác Đều:")
print(f"Chu vi: {tam_giac_deu.tinh_chu_vi()}")
print(f"Diện tích: {tam_giac_deu.tinh_dien_tich()}")
print("\nHình Lục Giác Đều:")
print(f"Chu vi: {luc_giac_deu.tinh_chu_vi()}")
print(f"Diện tích: {luc_giac_deu.tinh_dien_tich()}")
print("\nHình Ngũ Giác Đều:")
print(f"Chu vi: {ngu_giac_deu.tinh_chu_vi()}")
print(f"Diện tích: {ngu_giac_deu.tinh_dien_tich()}")
print("\nHình Bát Giác Đều:")
print(f"Chu vi: {bat_giac_deu.tinh_chu_vi()}")
print(f"Diện tích: {bat_giac_deu.tinh_dien_tich()}")
tron_khoi_tru = KhoiTru(tron, 10)
vuong_khoi_tru = KhoiTru(vuong, 10)
tam_giac_deu_khoi_tru = KhoiTru(tam_giac_deu, 10)
luc_giac_deu_khoi_tru = KhoiTru(luc_giac_deu, 10)
ngu_giac_deu_khoi_tru = KhoiTru(ngu_giac_deu, 10)
bat_giac_deu_khoi_tru = KhoiTru(bat_giac_deu, 10)
print("\nThể tích:")
print(f"Hình Tròn: {tron_khoi_tru.tinh_the_tich()}")
print(f"Hình Vuông: {vuong_khoi_tru.tinh_the_tich()}")
print(f"Hình Tam Giác Đều: {tam_giac_deu_khoi_tru.tinh_the_tich()}")
print(f"Hình Lục Giác Đều: {luc_giac_deu_khoi_tru.tinh_the_tich()}")
print(f"Hình Ngũ Giác Đều: {ngu_giac_deu_khoi_tru.tinh_the_tich()}")
print(f"Hình Bát Giác Đều: {bat_giac_deu_khoi_tru.tinh_the_tich()}")