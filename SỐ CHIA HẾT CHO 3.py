def chia_het_cho_3(N):
    tong = sum(int(digit) for digit in N)
    return "YES" if tong % 3 == 0 else "NO"
so_test = int(input())
for _ in range(so_test):
    N = input()
    print(chia_het_cho_3(N))