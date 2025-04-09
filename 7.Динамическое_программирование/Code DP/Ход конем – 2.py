from collections import deque

n, m = map(int, input().split())

# Directions the knight can move (8 possible moves)
moves = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]

# Initialize a DP table to store the number of ways to reach each cell
dp = [[0] * m for _ in range(n)]
dp[0][0] = 1  # Starting position

# Queue for BFS, storing tuples of (distance, i, j)
queue = deque()
queue.append((0, 0, 0))  # (distance, row, col)

# Visited array to track the minimal distance to each cell
visited = [[-1] * m for _ in range(n)]
visited[0][0] = 0

while queue:
    dist, i, j = queue.popleft()

    # If we've already found a shorter path to (i, j), skip
    if dist > visited[i][j]:
        continue

    for di, dj in moves:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m:
            if visited[ni][nj] == -1 or visited[ni][nj] == dist + 1:
                dp[ni][nj] += dp[i][j]
                if visited[ni][nj] == -1:
                    visited[ni][nj] = dist + 1
                    queue.append((dist + 1, ni, nj))
            elif visited[ni][nj] > dist + 1:
                visited[ni][nj] = dist + 1
                dp[ni][nj] = dp[i][j]
                queue.append((dist + 1, ni, nj))

print(dp[n - 1][m - 1] if visited[n - 1][m - 1] != -1 else 0)
