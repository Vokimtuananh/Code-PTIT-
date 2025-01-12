def split_and_sum(num):
    num_str = str(num)
    n = len(num_str)
    if n == 1:
        return num
    mid = n // 2
    first_half = num_str[:mid]
    second_half = num_str[mid:]
    first_num = int(first_half) if first_half else 0
    second_num = int(second_half)
    return first_num + second_num
def solve(num):
    current = num
    while len(str(current)) > 1:
        current = split_and_sum(current)
        print(current)
number = int(input())
solve(number)