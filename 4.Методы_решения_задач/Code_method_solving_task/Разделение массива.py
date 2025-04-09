import sys

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))


def is_possible(s):
    current = 0
    parts = 0
    for num in a:
        if num > s:
            return False
        current += num
        if current > s:
            parts += 1
            current = num
    parts += 1
    return parts <= k


left = max(a)
right = sum(a)
ans = sum(a)

while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)
