import sys

n, c = map(int, sys.stdin.readline().split())
tasks = []
for i in range(n):
    s, t = map(int, sys.stdin.readline().split())
    end = s + t
    tasks.append((end, s, i + 1))  # Store end, start, original index

# Sort by end time
tasks.sort()

selected = []
last_end = -1
for end, s, idx in tasks:
    if s >= last_end:
        selected.append((s, end, idx))
        last_end = end

# Sort selected tasks by start time to get the order of execution
selected.sort(key=lambda x: x[0])
total = len(selected) * c
print(total)
print(len(selected))
print(" ".join(map(str, [idx for s, end, idx in selected])))
