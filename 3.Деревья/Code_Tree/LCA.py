n = int(input())
parents = list(map(int, input().split()))

# Build parent array
parent = [-1] * n  # parent[0] is -1 (root)
for i in range(1, n):
    parent[i] = parents[i - 1]

m = int(input())
output = []

for _ in range(m):
    u, v = map(int, input().split())
    # Collect all ancestors of u including itself
    u_ancestors = set()
    current = u
    while current != -1:
        u_ancestors.add(current)
        current = parent[current]

    # Find the first common ancestor in v's path
    lca = -1
    current = v
    while current != -1:
        if current in u_ancestors:
            lca = current
            break
        current = parent[current]

    output.append(str(lca))

print("\n".join(output))
