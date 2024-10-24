def nto(n, divior = None):
    if n <= 1:
        return False
    if divior is None:
        divior = int(n ** 0.5)
    if divior < 2:
        return True
    if n % divior == 0:
        return False
    return nto(n, divior - 1)
t = int(input())
for _ in range(t):
    i = int(input())
    a = str(i)
    if a[::2] == nto() or a[-3::] == nto():
        print('YES')
    else:
        print('NO')