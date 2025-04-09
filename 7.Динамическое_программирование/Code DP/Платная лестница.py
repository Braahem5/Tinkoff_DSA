n = int(input())
costs = list(map(int, input().split()))
if n == 0:
    print(0)
else:
    dp = [0] * (n + 1)
    dp[1] = costs[0] if n >= 1 else 0
    for i in range(2, n + 1):
        dp[i] = min(dp[i-1], dp[i-2] if i >= 2 else float('inf')) + costs[i-1]
    print(dp[n])