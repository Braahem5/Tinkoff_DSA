import sys

n, k = map(int, sys.stdin.readline().split())

left = 1
right = n * n
ans = 0


def count_less_eq(x):
    count = 0
    for i in range(1, n + 1):
        add = min(x // i, n)
        if add == 0:
            break
        count += add
    return count


while left <= right:
    mid = (left + right) // 2
    cnt = count_less_eq(mid)
    if cnt >= k:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)
