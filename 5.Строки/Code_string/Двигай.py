mod = 10**18 + 3
base = 911382629

a = input().strip()
b = input().strip()
len_a, len_b = len(a), len(b)

if len_b > len_a:
    print(0)
else:
    S = b + b
    len_S = len(S)
    prefix_S = [0] * (len_S + 1)
    power_S = [1] * (len_S + 1)
    for i in range(len_S):
        prefix_S[i + 1] = (prefix_S[i] * base + ord(S[i])) % mod
        power_S[i + 1] = (power_S[i] * base) % mod
    hash_set = set()
    for i in range(len_b):
        end = i + len_b
        current_hash = (prefix_S[end] - prefix_S[i] * power_S[len_b]) % mod
        hash_set.add(current_hash)
    prefix_a = [0] * (len_a + 1)
    power_a = [1] * (len_a + 1)
    for i in range(len_a):
        prefix_a[i + 1] = (prefix_a[i] * base + ord(a[i])) % mod
        power_a[i + 1] = (power_a[i] * base) % mod
    count = 0
    for i in range(len_a - len_b + 1):
        end = i + len_b
        current_hash = (prefix_a[end] - prefix_a[i] * power_a[len_b]) % mod
        if current_hash in hash_set:
            count += 1
    print(count)
