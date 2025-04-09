import sys


def can_place(stalls, k, d):
    count = 1
    last = stalls[0]
    for stall in stalls:
        if stall - last >= d:
            count += 1
            last = stall
            if count >= k:
                return True
    return False


n, k = map(int, sys.stdin.readline().split())
stalls = list(map(int, sys.stdin.readline().split()))
stalls.sort()

left = 0
right = stalls[-1] - stalls[0]
ans = 0

while left <= right:
    mid = (left + right) // 2
    if can_place(stalls, k, mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)
