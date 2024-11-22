def generate_strings(N):
    def is_valid(s):
        a = s.count('A')
        b = s.count('B')
        c = s.count('C')
        return a > 0 and b > 0 and c > 0 and a <= b <= c
    def generate(length, prefix):
        if length == 0:
            if is_valid(prefix):
                results.append(prefix)
            return
        for char in 'ABC':
            generate(length - 1, prefix + char)
    results = []
    for length in range(3, N + 1):
        generate(length, '')
    results.sort(key=lambda x: (len(x), x))
    return results
N = int(input().strip())
for string in generate_strings(N):
    print(string)