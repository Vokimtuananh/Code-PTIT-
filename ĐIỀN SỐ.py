def missing_elements_count(arr):
    L = min(arr)
    R = max(arr)
    total_elements = R - L + 1
    return total_elements - len(set(arr))
def main():
    T = int(input().strip())
    results = []
    for _ in range(T):
        n = int(input().strip())
        A = list(map(int, input().strip().split()))
        results.append(missing_elements_count(A))
    for res in results:
        print(res)
if __name__ == "__main__":
    main()