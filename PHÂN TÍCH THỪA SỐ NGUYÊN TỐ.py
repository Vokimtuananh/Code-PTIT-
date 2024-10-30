import math
def phan_tich_thua_so_nguyen_to(n):
    ket_qua = []
    for i in range(2, int(math.sqrt(n)) + 1):
        dem = 0
        while n % i == 0:
            n //= i
            dem += 1
        if dem > 0:
            ket_qua.append(f"{i}^{dem}")
    if n > 1:
        ket_qua.append(f"{n}^1")
    return ket_qua
def xu_ly_cac_bo_kiem_tra(danh_sach_n):
    cac_ket_qua = []
    for n in danh_sach_n:
        cac_thua_so = phan_tich_thua_so_nguyen_to(n)
        ket_qua = "1"
        if cac_thua_so:
            ket_qua += " * " + " * ".join(cac_thua_so)
        cac_ket_qua.append(ket_qua)
    return cac_ket_qua
so_bo_kiem_tra = int(input())
danh_sach_n = [int(input()) for _ in range(so_bo_kiem_tra)]
cac_ket_qua = xu_ly_cac_bo_kiem_tra(danh_sach_n)
for ket_qua in cac_ket_qua:
    print(ket_qua)