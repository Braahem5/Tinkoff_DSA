import sys

n = int(input())
left, right = 1, n

while left <= right:
    mid = (left + right) // 2
    print(mid)
    sys.stdout.flush()
    response = input().strip()
    if response == "<":
        right = mid - 1
    else:
        left = mid + 1

print(f"! {right}")
sys.stdout.flush()
