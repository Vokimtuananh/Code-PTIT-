def kiem_tra_so_dep(n):
    str_n = str(n)
    if len(str_n) < 2:
        return "NO"
    for i in range(1, len(str_n) - 1):
        if str_n[i - 1] == str_n[i + 1]:
            continue
        else:
            return "NO"
    return "YES"
tong_bo_test = int(input())
while tong_bo_test > 0:
    tong_bo_test -= 1
    n = int(input())
    print(kiem_tra_so_dep(n))