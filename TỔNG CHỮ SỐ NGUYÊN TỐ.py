def nto(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def totalDigitsOfNumber(n):
    total = 0
    for digit in n:
        total += int(digit)
    return total
t = int(input())
for _ in range(t):
    n = input()
    c = totalDigitsOfNumber(n)
    if nto(c):
        print('YES')
    else:
        print('NO')