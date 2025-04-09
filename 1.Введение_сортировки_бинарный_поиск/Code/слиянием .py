n = int(input())
array = list(map(int, input().strip().split()))[:n]


def Divider(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left, right = arr[:mid], arr[mid:]

        leftArr, leftInversions = Divider(left)
        rightArr, rightInversions = Divider(right)

        mergedArr, splitInversions = Merger(leftArr, rightArr)

        totalInversions = leftInversions + rightInversions + splitInversions

        return mergedArr, totalInversions
    else:
        return arr, 0


def Merger(left, right):
    i = j = 0
    arr, inversion = [], 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            inversion += len(left) - i
            j += 1

    arr.extend(left[i:])
    arr.extend(right[j:])

    return arr, inversion


sortedArr, totInversion = Divider(array)
print(totInversion)
print(" ".join(map(str, sortedArr)))
