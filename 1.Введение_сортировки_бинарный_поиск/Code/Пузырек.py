class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 1)

    def update(self, idx, delta=1):
        idx += 1  # 1-based indexing
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & -idx

    def query(self, idx):
        idx += 1  # 1-based indexing
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res


n = int(input())
p = list(map(int, input().split()))
p = [x - 1 for x in p]  # Convert to 0-based

ft = FenwickTree(n)
inserted = set()
current_max = n - 1
result = [1]  # Initial state: all zeros

for pos in p:
    if pos not in inserted:
        ft.update(pos)
        inserted.add(pos)
    # Update current_max
    while current_max >= 0 and current_max in inserted:
        current_max -= 1
    if current_max == -1:
        # All are ones, no passes needed beyond initial check
        result.append(1)
    else:
        count = ft.query(current_max - 1)
        result.append(count + 1)

print(" ".join(map(str, result)))
