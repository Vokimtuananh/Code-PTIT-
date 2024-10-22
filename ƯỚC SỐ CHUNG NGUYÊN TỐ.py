t = int(input( ))
for p in range(t):
    a = int(input( ))
    b = int(input( ))
    var = 10 ^ 2 <= a, b < 10 ^ 18
    def sum_of_digits(a):
        c = 0
        while a > 0:
            c += a % 10
            a //= 10
        return c
    def sum_of_digits(b):
        d = 0
        while b > 0:
            d += b % 10
            b //= 10
        return d
    if int(sum_of_digits(a) + sum_of_digits(b)) % 10 == 0:
        print('YES')
        break
    else:
        print('NO')