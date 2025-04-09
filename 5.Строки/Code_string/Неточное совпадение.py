import numpy as np

p = input().strip()
t = input().strip()
m, n = len(p), len(t)

if m > n:
    print(0)
    print()
else:
    total_matches = np.zeros(n - m + 1, dtype=int)
    for c in set(p + t):
        A = np.array([1 if ch == c else 0 for ch in t], dtype=np.float64)
        B = np.array([1 if ch == c else 0 for ch in p[::-1]], dtype=np.float64)
        conv = np.fft.irfft(np.fft.rfft(A) * np.fft.rfft(B), len(A) + len(B) - 1)
        valid = np.rint(conv[m - 1 : n]).astype(int)
        total_matches += valid
    mismatches = m - total_matches
    result = np.where(mismatches <= 1)[0]
    print(len(result))
    if len(result) > 0:
        print(" ".join(map(str, result + 1)))
    else:
        print()
