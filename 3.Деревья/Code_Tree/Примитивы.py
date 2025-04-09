n = int(input())
if n == 0:
    print("0 0")
    print()
    exit()
parents = list(map(int, input().split()))

children = [[] for _ in range(n)]
for i in range(1, n):
    parent = parents[i - 1]
    children[parent].append(i)

# Compute depths
depth = [0] * n
for i in range(1, n):
    depth[i] = depth[parents[i - 1]] + 1

max_diameter = 0
heights = [0] * n

stack = []
visited = [False] * n
stack.append((0, False))

while stack:
    node, visited_flag = stack.pop()
    if not visited_flag:
        stack.append((node, True))
        # Process children in reverse order to maintain order
        for child in reversed(children[node]):
            stack.append((child, False))
    else:
        max1 = 0
        max2 = 0
        for child in children[node]:
            current_h = heights[child] + 1
            if current_h > max1:
                max2 = max1
                max1 = current_h
            elif current_h > max2:
                max2 = current_h
        current_candidate = max1 + max2
        if current_candidate > max_diameter:
            max_diameter = current_candidate
        heights[node] = max1

height_of_tree = max(depth)
print(f"{height_of_tree} {max_diameter}")
print(" ".join(map(str, depth)))
