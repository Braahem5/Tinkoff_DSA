from collections import deque
import sys


def main():
    m = int(sys.stdin.readline())
    graph = {}
    for _ in range(m):
        line = sys.stdin.readline().strip()
        a, b = line.split(" -> ")
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
    start = sys.stdin.readline().strip()
    target = sys.stdin.readline().strip()
    visited = {start: 0}
    q = deque([start])
    found = False
    while q:
        current = q.popleft()
        if current == target:
            print(visited[current])
            found = True
            break
        if current not in graph:
            continue
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited[neighbor] = visited[current] + 1
                q.append(neighbor)
    if not found:
        print(-1)


if __name__ == "__main__":
    main()
