MOD = 10**9 + 7
MAX_B = 10**6

la_nguyen_to = [True] * (MAX_B + 1)
la_nguyen_to[0] = la_nguyen_to[1] = False
for i in range(2, int(MAX_B**0.5) + 1):
    if la_nguyen_to[i]:
        for j in range(i * i, MAX_B + 1, i):
            la_nguyen_to[j] = False
nguyen_to = [i for i, val in enumerate(la_nguyen_to) if val]

def solve(n, p):
    e = 0
    n_chia_p = n // p
    while n_chia_p > 0:
        e += n_chia_p
        n_chia_p //= p
    return e

so_bo_test = int(input())
for _ in range(so_bo_test):
    a, b = map(int, input().split())
    ket_qua = 1
    for p in nguyen_to:
        if p > b:
            break
        so_mu_p = solve(b, p) - solve(a - 1, p)
        if so_mu_p > 0:
            ket_qua = (ket_qua * (2 * so_mu_p + 1)) % MOD
    print(ket_qua)