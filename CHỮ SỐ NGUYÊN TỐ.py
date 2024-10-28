def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def check_prime_dominant(n):
    num_digits = len(str(n))
    if not isPrime(num_digits):
        return False
    prime_count = 0
    non_prime_count = 0
    for digit in str(n):
        if isPrime(int(digit)):
            prime_count += 1
        else:
            non_prime_count += 1
    return prime_count > non_prime_count
t = int(input())
for _ in range(t):
    n = int(input())
    if check_prime_dominant(n):
        print("YES")
    else:
        print("NO")