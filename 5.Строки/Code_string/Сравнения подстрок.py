mod = 10**18 + 3
base = 911382629

s = input().strip()
n = len(s)
prefix = [0] * (n + 1)
power = [1] * (n + 1)

for i in range(n):
    prefix[i+1] = (prefix[i] * base + ord(s[i])) % mod
    power[i+1] = (power[i] * base) % mod

m = int(input())
for _ in range(m):
    a, b, c, d = map(int, input().split())
    len1 = b - a + 1
    len2 = d - c + 1
    if len1 != len2:
        print("No")
        continue
    l1, r1 = a-1, b-1
    l2, r2 = c-1, d-1
    hash1 = (prefix[r1+1] - prefix[l1] * power[r1 - l1 + 1]) % mod
    hash2 = (prefix[r2+1] - prefix[l2] * power[r2 - l2 + 1]) % mod
    print("Yes" if hash1 == hash2 else "No")