def so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def tao_day_so_nguyen_to(dai):
    day_so_nguyen_to = []
    so_hien_tai = 2
    while len(day_so_nguyen_to) < dai:
        if so_nguyen_to(so_hien_tai):
            day_so_nguyen_to.append(so_hien_tai)
        so_hien_tai += 1
    return day_so_nguyen_to
def tao_day_ket_qua(n, x):
    day_so_nguyen_to = tao_day_so_nguyen_to(n)
    day_ket_qua = [x]
    for i in range(n):
        x += day_so_nguyen_to[i]
        day_ket_qua.append(x)
    return day_ket_qua
n, x = map(int, input().split())
day_ket_qua = tao_day_ket_qua(n, x)
print(" ".join(map(str, day_ket_qua)))