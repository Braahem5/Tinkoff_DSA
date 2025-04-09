import sys


def to_seconds(h, m, s):
    return h * 3600 + m * 60 + s


n = int(sys.stdin.readline())
events = []

for _ in range(n):
    h1, m1, s1, h2, m2, s2 = map(int, sys.stdin.readline().split())
    start = to_seconds(h1, m1, s1)
    end = to_seconds(h2, m2, s2)
    if start == end:
        # Active all day
        events.append((0, 1))
        events.append((86400, -1))
    elif start < end:
        events.append((start, 1))
        events.append((end, -1))
    else:
        # Wrap around
        events.append((start, 1))
        events.append((86400, -1))
        events.append((0, 1))
        events.append((end, -1))

# Sort events: if time is same, process ends before starts
events.sort(key=lambda x: (x[0], x[1]))

total = 0
active = 0
prev_time = 0

for time, delta in events:
    if prev_time < time:
        duration = time - prev_time
        if active == n:
            total += duration
    active += delta
    prev_time = time

# Check the last segment
if prev_time < 86400 and active == n:
    total += 86400 - prev_time

print(total)
