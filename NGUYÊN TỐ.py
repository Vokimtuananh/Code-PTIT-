def nto(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0 or num != 2:
            return False
        i += 6
    return True
def check():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        if nto(n) == True:
            print("YES")
        else:
            print("NO")
if __name__ == "__main__":
    check()