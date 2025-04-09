import sys


def sum_v(n, m, x):
    if x < 1:
        return 0
    return n * (x - 1) * (x + m * (n - 1)) // 2


def sum_h(n, m, y):
    if y < 1:
        return 0
    z = y - 1
    return m * z * (m * z + 1) // 2


def find_best_vertical(n, m, S_half):
    low, high = 1, m
    best_x = 0
    while low <= high:
        mid = (low + high) // 2
        s = sum_v(n, m, mid)
        if s <= S_half:
            best_x = mid
            low = mid + 1
        else:
            high = mid - 1
    candidates = [best_x - 1, best_x, best_x + 1]
    min_diff = float("inf")
    best_x_final = m
    for x in candidates:
        if x < 1 or x > m:
            continue
        current = sum_v(n, m, x)
        diff = abs(current - S_half)
        if diff < min_diff or (diff == min_diff and x < best_x_final):
            min_diff = diff
            best_x_final = x
    return (min_diff, best_x_final)


def find_best_horizontal(n, m, S_half):
    low, high = 1, n
    best_y = 0
    while low <= high:
        mid = (low + high) // 2
        s = sum_h(n, m, mid)
        if s <= S_half:
            best_y = mid
            low = mid + 1
        else:
            high = mid - 1
    candidates = [best_y - 1, best_y, best_y + 1]
    min_diff = float("inf")
    best_y_final = n
    for y in candidates:
        if y < 1 or y > n:
            continue
        current = sum_h(n, m, y)
        diff = abs(current - S_half)
        if diff < min_diff or (diff == min_diff and y < best_y_final):
            min_diff = diff
            best_y_final = y
    return (min_diff, best_y_final)


def main():
    t = int(sys.stdin.readline().strip())  # Read the number of test cases
    results = []
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().strip().split())
        total = n * m
        S = total * (total + 1) // 2
        S_half = S / 2
        diff_v, x = find_best_vertical(n, m, S_half)
        diff_h, y = find_best_horizontal(n, m, S_half)
        if diff_v < diff_h or (diff_v == diff_h and x <= y):
            results.append(f"V {x}")
        else:
            results.append(f"H {y}")

    print("\n".join(results))
