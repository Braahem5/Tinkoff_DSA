import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
coins_input = list(map(int, sys.stdin.readline().split()))
coins = [0] * (n + 1)
for i in range(2, n):
    coins[i] = coins_input[i - 2]
dp = [float("-inf")] * (n + 1)
dp[1] = 0
prev = [-1] * (n + 1)
dq = deque()
dq.append(1)

for i in range(2, n + 1):
    while dq and dq[0] < i - k:
        dq.popleft()
    if not dq:
        break
    max_prev = dq[0]
    dp[i] = dp[max_prev] + coins[i]
    prev[i] = max_prev
    while dq and dp[i] >= dp[dq[-1]]:
        dq.pop()
    dq.append(i)

path = []
current = n
while current != 1:
    path.append(current)
    current = prev[current]
path.append(1)
path.reverse()
print(dp[n])
print(len(path) - 1)
print(" ".join(map(str, path)))
