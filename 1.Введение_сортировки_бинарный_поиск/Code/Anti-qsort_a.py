def find_adversary(n):
    data = list(range(n))
    result = [0] * n

    for k in range(n - 1, -1, -1):
        result[data[k // 2]] = k + 1
        data[k // 2], data[k] = data[k], data[k // 2]

    # Swap positions of 1 and 2
    idx1 = result.index(1)
    idx2 = result.index(2)
    result[idx1], result[idx2] = result[idx2], result[idx1]

    return result


def quick_sort(data, left, right, count):
    key = data[(left + right) // 2]
    i = left
    j = right

    while i <= j:
        while data[i] < key:
            count[0] += 1
            i += 1
        while key < data[j]:
            count[0] += 1
            j -= 1

        if i <= j:
            data[i], data[j] = data[j], data[i]
            i += 1
            j -= 1

    if left < j:
        quick_sort(data, left, j, count)
    if i < right:
        quick_sort(data, i, right, count)


def main():
    n = int(input())  # You can change this value to generate a larger permutation
    adversary = find_adversary(n)

    print(" ".join(map(str, adversary)))

    count = [0]
    quick_sort(adversary, 0, n - 1, count)


if __name__ == "__main__":
    main()
