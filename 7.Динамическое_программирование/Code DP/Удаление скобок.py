s = input().strip()
n = len(s)
dp = [[0] * n for _ in range(n)]
path = [[""] * n for _ in range(n)]

for i in range(n - 1, -1, -1):
    for j in range(i, n):
        if i == j:
            dp[i][j] = 0
            path[i][j] = ""
        else:
            if (
                (s[i] == "(" and s[j] == ")")
                or (s[i] == "[" and s[j] == "]")
                or (s[i] == "{" and s[j] == "}")
            ):
                dp[i][j] = dp[i + 1][j - 1] + 2
                path[i][j] = s[i] + path[i + 1][j - 1] + s[j]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                if dp[i + 1][j] > dp[i][j - 1]:
                    path[i][j] = path[i + 1][j]
                else:
                    path[i][j] = path[i][j - 1]
            for k in range(i, j):
                if dp[i][j] < dp[i][k] + dp[k + 1][j]:
                    dp[i][j] = dp[i][k] + dp[k + 1][j]
                    path[i][j] = path[i][k] + path[k + 1][j]

print(path[0][n - 1])
