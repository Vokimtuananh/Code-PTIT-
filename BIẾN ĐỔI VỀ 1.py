while True:
    n = int(input())
    if n == 0:
        break
    a = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            a.append(n)
        elif n % 2 == 1:
            n = n * 3 + 1
            a.append(n)
    print(len(a))