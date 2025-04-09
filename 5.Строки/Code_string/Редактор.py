def kmp_search(pattern, text):
    if not pattern:
        return []
    failure = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        j = failure[i - 1]
        while j > 0 and pattern[i] != pattern[j]:
            j = failure[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        failure[i] = j
    j = 0
    res = []
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = failure[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            res.append(i - len(pattern) + 1)
            j = failure[j - 1]
    return res


T = input().strip()
q = int(input())
for _ in range(q):
    s = input().strip()
    if len(s) > len(T):
        print(0)
        continue
    occurrences = kmp_search(s, T)
    print(len(occurrences), end="")
    if occurrences:
        print(" " + " ".join(map(str, occurrences)))
    else:
        print()
