from collections import defaultdict
def tinh_luong_mua_trung_binh():
    so_luot_do = int(input())
    thong_tin_tram = defaultdict(lambda: {"ten_tram": None, "tong_luong_mua": 0, "tong_thoi_gian": 0})
    for _ in range(so_luot_do):
        ten_tram = input()
        thoi_diem_bat_dau = input().split(":")
        thoi_diem_ket_thuc = input().split(":")
        luong_mua = float(input())
        thoi_gian_mua = (int(thoi_diem_ket_thuc[0]) * 60 + int(thoi_diem_ket_thuc[1])) - (int(thoi_diem_bat_dau[0]) * 60 + int(thoi_diem_bat_dau[1]))
        if thoi_gian_mua < 0:
            thoi_gian_mua = 24 * 60 - abs(thoi_gian_mua)
        if thong_tin_tram[ten_tram]["ten_tram"] is None:
            thong_tin_tram[ten_tram]["ten_tram"] = ten_tram
        thong_tin_tram[ten_tram]["tong_luong_mua"] += luong_mua
        thong_tin_tram[ten_tram]["tong_thoi_gian"] += thoi_gian_mua
    ma_tram = 1
    for ten_tram, thong_tin in thong_tin_tram.items():
        if thong_tin["tong_thoi_gian"] > 0:
            luong_mua_trung_binh = (thong_tin["tong_luong_mua"] / thong_tin["tong_thoi_gian"]) * 60
            print(f"T{ma_tram:02d} {thong_tin['ten_tram']} {luong_mua_trung_binh:.2f}")
            ma_tram += 1
if __name__ == "__main__":
    tinh_luong_mua_trung_binh()