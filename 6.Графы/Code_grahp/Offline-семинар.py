import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    INF = float("inf")
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dist[i][i] = 0
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        if dist[u][v] > w:
            dist[u][v] = w
            dist[v][u] = w
    # Floyd-Warshall
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    min_max = INF
    ans = -1
    for i in range(1, n + 1):
        current_max = max(dist[i][1 : n + 1])
        if current_max < min_max or (current_max == min_max and i < ans):
            min_max = current_max
            ans = i
    print(ans)


if __name__ == "__main__":
    main()
