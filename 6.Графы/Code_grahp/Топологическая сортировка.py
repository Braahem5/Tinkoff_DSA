import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    perm = list(map(int, sys.stdin.readline().split()))
    pos = {v: idx for idx, v in enumerate(perm)}
    valid = True
    for u, v in edges:
        if pos[u] >= pos[v]:
            valid = False
            break
    print("YES" if valid else "NO")


if __name__ == "__main__":
    main()
