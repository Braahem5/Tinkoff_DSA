import sys
from sys import stdin


def main():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    r = int(input[ptr])
    ptr += 1

    left = []
    right = []
    for _ in range(n):
        l = int(input[ptr])
        ptr += 1
        rt = int(input[ptr])
        ptr += 1
        left.append(l)
        right.append(rt)

    is_avl = True
    stack = [(r, float("-inf"), float("inf"), False)]
    heights = [0] * n

    while stack and is_avl:
        node, min_a, max_a, visited = stack.pop()
        if not visited:
            # Check BST condition
            if not (min_a <= node <= max_a):
                is_avl = False
                continue
            # Push back with visited=True
            stack.append((node, min_a, max_a, True))
            # Process right child first (so left is processed next)
            rc = right[node]
            if rc != -1:
                new_min = node + 1
                new_max = max_a
                stack.append((rc, new_min, new_max, False))
            lc = left[node]
            if lc != -1:
                new_min = min_a
                new_max = node - 1
                stack.append((lc, new_min, new_max, False))
        else:
            lc = left[node]
            rc = right[node]
            left_h = heights[lc] if lc != -1 else 0
            right_h = heights[rc] if rc != -1 else 0
            current_height = 1 + max(left_h, right_h)
            heights[node] = current_height
            if abs(left_h - right_h) > 1:
                is_avl = False

    print(1 if is_avl else 0)


if __name__ == "__main__":
    main()
