def Check(t, s):
    text = s + "&" + t
    n = len(text)
    Z = [0] * n
    L = R = 0

    for i in range(1, n):
        if i > R:
            L = R = i
            while R < n and text[R] == text[R - L]:
                R += 1
            Z[i] = R - L
            R -= 1
        else:
            k = i - L
            if Z[k] < R - i + 1:
                Z[i] = Z[k]
            else:
                while R < n and text[R] == text[R - L]:
                    R += 1
                Z[i] = R - L
                R -= 1

    ans = []
    for x in range(len(Z)):
        if Z[x] == len(s):
            ans.append(x - len(s) - 1)

    return ans


T = "ababcabc"
S = "abc"
print(Check(T, S))
