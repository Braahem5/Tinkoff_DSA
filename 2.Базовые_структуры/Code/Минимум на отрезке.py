from collections import deque

n, k = map(int, input().strip().split())
values = list(map(int, input().strip().split()))[:n]

# Deque to store indices of the elements
dq = deque()
minArr = []

for i in range(n):
    # Remove elements not in the current window
    if dq and dq[0] < i - k + 1:
        dq.popleft()

    # Remove elements from the deque that are greater than the current element
    while dq and values[dq[-1]] > values[i]:
        dq.pop()

    # Add the current element's index to the deque
    dq.append(i)

    # The first element in the deque is the minimum for the current window
    if i >= k - 1:
        minArr.append(values[dq[0]])

# Print all minimum values on a single line
print(" ".join(map(str, minArr)))
