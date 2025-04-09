import sys

n, m, k = map(int, sys.stdin.readline().split())
# Note: The input uses N as rows and M as columns, but check the problem statement.
matrix = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    matrix.append(row)

# Compute prefix sums
prefix = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    row_sum = 0
    for j in range(1, m + 1):
        row_sum += matrix[i - 1][j - 1]
        prefix[i][j] = prefix[i - 1][j] + row_sum

for _ in range(k):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().split())
    # Convert to 1-based indices in prefix
    sum_rect = (
        prefix[y2][x2]
        - prefix[y1 - 1][x2]
        - prefix[y2][x1 - 1]
        + prefix[y1 - 1][x1 - 1]
    )
    print(sum_rect)
