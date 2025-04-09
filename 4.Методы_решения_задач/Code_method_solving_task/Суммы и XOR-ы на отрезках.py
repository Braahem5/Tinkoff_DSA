import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

prefix_sum = [0] * (n + 1)
prefix_xor = [0] * (n + 1)

for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]
    prefix_xor[i] = prefix_xor[i - 1] ^ a[i - 1]

for _ in range(m):
    q, l, r = map(int, sys.stdin.readline().split())
    if q == 1:
        res = prefix_sum[r] - prefix_sum[l - 1]
    else:
        res = prefix_xor[r] ^ prefix_xor[l - 1]
    print(res)
