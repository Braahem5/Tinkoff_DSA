n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
max_side = 0
x, y = 0, 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            if dp[i][j] > max_side:
                max_side = dp[i][j]
                x = i - max_side + 1
                y = j - max_side + 1

print(max_side, x + 1, y + 1)
