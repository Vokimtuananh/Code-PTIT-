import math

# Giới hạn tối đa
max_n = 10**7 + 1

# Mảng chứa số lượng ước số của từng số
dem_uoc = [0] * max_n

# Tiền xử lý để tính số lượng ước số của từng số
for i in range(1, max_n):
    for j in range(i, max_n, i):
        dem_uoc[j] += 1

def phan_nguyen_to(n):
    max_dem = 0
    ket_qua = n
    for i in range(n, max_n):
        if dem_uoc[i] > max_dem:
            max_dem = dem_uoc[i]
            ket_qua = i
            break
    return ket_qua

# Số bộ test
t = int(input())

for _ in range(t):
    x = int(input())
    print(phan_nguyen_to(x))