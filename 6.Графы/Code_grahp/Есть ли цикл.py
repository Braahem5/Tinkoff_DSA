import sys
from collections import deque


def main():
    n, m = map(int, sys.stdin.readline().split())
    in_degree = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        in_degree[v] += 1
    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)
    processed = 0
    while q:
        u = q.popleft()
        processed += 1
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
    print(1 if processed != n else 0)


if __name__ == "__main__":
    main()
