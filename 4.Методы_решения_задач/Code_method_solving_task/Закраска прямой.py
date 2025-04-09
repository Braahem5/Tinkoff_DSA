import sys

n = int(sys.stdin.readline())
intervals = []
for _ in range(n):
    l, r = map(int, sys.stdin.readline().split())
    intervals.append((l, r))

intervals.sort()
merged = []
for interval in intervals:
    if not merged:
        merged.append(interval)
    else:
        last = merged[-1]
        if interval[0] <= last[1]:
            merged[-1] = (last[0], max(last[1], interval[1]))
        else:
            merged.append(interval)

total = 0
for l, r in merged:
    total += r - l

print(total)
