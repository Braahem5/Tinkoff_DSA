import sys
from collections import deque


def main():
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    M = int(input[ptr])
    ptr += 1
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u = int(input[ptr])
        ptr += 1
        v = int(input[ptr])
        ptr += 1
        adj[u].append(v)
        adj[v].append(u)
    visited = [False] * (N + 1)
    components = []
    for node in range(1, N + 1):
        if not visited[node]:
            q = deque()
            q.append(node)
            visited[node] = True
            component = []
            while q:
                v = q.popleft()
                component.append(v)
                for nei in adj[v]:
                    if not visited[nei]:
                        visited[nei] = True
                        q.append(nei)
            component.sort()
            components.append(component)
    components.sort(key=lambda x: x[0])
    print(len(components))
    for comp in components:
        print(len(comp))
        print(" ".join(map(str, comp)))


if __name__ == "__main__":
    main()
