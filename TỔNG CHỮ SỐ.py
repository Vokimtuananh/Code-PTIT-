def check(s):
    n = 0
    for i in s:
        n += ord(i) - ord('0')
    return str(n)
a = input()
b = 0
while len(a) > 1:
    a = check(a)
    b += 1
print(b)