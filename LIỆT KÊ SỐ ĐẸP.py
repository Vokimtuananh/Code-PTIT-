def so_thuan_nghich(n):
    s = str(n)
    r = int(s[::-1])
    return r == n
def so_chan(n):
    s = str(n)
    for i in s:
        if int(i) not in [0, 2, 4, 6, 8]:
            return False
    return True
def check(n):
    output = []
    for i in range(10, n):
        if so_thuan_nghich(i) and so_chan(i):
            if len(str(i)) % 2 == 1:
                output.append(i)
    return output
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        b = int(input())
        output = check(b)
        print(*output)