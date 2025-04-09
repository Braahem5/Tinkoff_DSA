s = input().strip()
n = len(s)
if n == 0:
    print("")
else:
    s += s
    i = 0
    for j in range(1, n):
        k = 0
        while k < n and s[i + k] == s[j + k]:
            k += 1
        if k < n and s[i + k] > s[j + k]:
            i = j
    print(s[i : i + n])
