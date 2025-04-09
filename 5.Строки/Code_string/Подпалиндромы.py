def count_palindromes(s):
    t = "#".join("^{}$".format(s))
    n = len(t)
    p = [0] * n
    center = right = 0
    count = 0
    for i in range(1, n - 1):
        mirror = 2 * center - i
        if i < right:
            p[i] = min(right - i, p[mirror])
        while t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1
        if i + p[i] > right:
            center, right = i, i + p[i]
        count += (p[i] + 1) // 2
    return count


print(count_palindromes(input().strip()))
