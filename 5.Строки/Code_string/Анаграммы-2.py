from collections import defaultdict


def main():
    import sys

    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    a = list(map(int, input[ptr : ptr + n]))
    ptr += n
    m = int(input[ptr])
    ptr += 1
    b = list(map(int, input[ptr : ptr + m]))
    ptr += m

    max_len = 0
    min_len = min(n, m)

    for l in range(min_len, 0, -1):
        a_subs = set()
        # Process array a
        freq = defaultdict(int)
        for i in range(l):
            freq[a[i]] += 1
        key = tuple(sorted(freq.items()))
        a_subs.add(key)
        for i in range(1, n - l + 1):
            # Remove left element
            outgoing = a[i - 1]
            freq[outgoing] -= 1
            if freq[outgoing] == 0:
                del freq[outgoing]
            # Add right element
            incoming = a[i + l - 1]
            freq[incoming] += 1
            key = tuple(sorted(freq.items()))
            a_subs.add(key)

        # Process array b
        b_subs = set()
        freq_b = defaultdict(int)
        for i in range(l):
            freq_b[b[i]] += 1
        key = tuple(sorted(freq_b.items()))
        b_subs.add(key)
        for i in range(1, m - l + 1):
            outgoing = b[i - 1]
            freq_b[outgoing] -= 1
            if freq_b[outgoing] == 0:
                del freq_b[outgoing]
            incoming = b[i + l - 1]
            freq_b[incoming] += 1
            key = tuple(sorted(freq_b.items()))
            b_subs.add(key)

        if a_subs & b_subs:
            print(l)
            return
    print(0)


if __name__ == "__main__":
    main()
