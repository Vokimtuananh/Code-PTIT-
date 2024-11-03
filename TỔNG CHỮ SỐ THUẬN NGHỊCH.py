def check(n):
    str1 = str(n)
    str2 = str1[::-1]
    if len(str1) > 1 and str1 == str2:
        return True
    return False
def tong(n):
    total = 0
    for digit in n:
        total += int(digit)
    return total
t = int(input())
for _ in range(t):
    b = input()
    c = tong(b)
    d = int(c)
    if check(d):
        print('YES')
    else:
        print('NO')