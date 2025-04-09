s1 = input().strip()
s2 = input().strip()
n, m = len(s1), len(s2)
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = i
for j in range(m + 1):
    dp[0][j] = j

for i in range(1, n + 1):
    for j in range(1, m + 1):
        cost = 0 if s1[i - 1] == s2[j - 1] else 1
        dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)
        if i > 1 and j > 1 and s1[i - 1] == s2[j - 2] and s1[i - 2] == s2[j - 1]:
            dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + 1)
print(dp[n][m])
