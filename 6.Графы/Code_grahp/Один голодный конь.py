import sys
from collections import deque


def main():
    N, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    directions = [
        (-2, -1),
        (-2, 1),
        (-1, -2),
        (-1, 2),
        (1, -2),
        (1, 2),
        (2, -1),
        (2, 1),
    ]
    visited = [[False] * (N + 1) for _ in range(N + 1)]
    parent = [[None] * (N + 1) for _ in range(N + 1)]
    q = deque()
    q.append((x1, y1))
    visited[x1][y1] = True
    found = False
    while q:
        x, y = q.popleft()
        if x == x2 and y == y2:
            found = True
            break
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= N and 1 <= ny <= N and not visited[nx][ny]:
                visited[nx][ny] = True
                parent[nx][ny] = (x, y)
                q.append((nx, ny))
    if not found:
        print(-1)
        return
    path = []
    current = (x2, y2)
    while current != (x1, y1):
        path.append(current)
        current = parent[current[0]][current[1]]
    path.append((x1, y1))
    path.reverse()
    print(len(path) - 1)
    for x, y in path:
        print(x, y)


if __name__ == "__main__":
    main()
