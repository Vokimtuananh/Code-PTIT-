def max_product(A):
    A.sort()
    max_product_2 = max(A[0] * A[1], A[-1] * A[-2])
    max_product_3 = max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])
    return max(max_product_2, max_product_3)
N = int(input())
A = list(map(int, input().split()))
print(max_product(A))