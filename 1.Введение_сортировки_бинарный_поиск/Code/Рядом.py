n, k = map(int, input().split())
array = sorted(list(map(int, input().split()))[:n])
query = list(map(int, input().split()))[:k]


def Binary(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if target < arr[mid]:
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1
        else:
            return mid

    return left


for x in query:
    mid = Binary(array, x)

    # check bounds and find the closest value
    closest = None
    if mid < len(array) and array[mid] == x:
        closest = array[mid]
    else:
        candidates = []
        if mid < len(array):  # check the right hand candidate
            candidates.append(array[mid])
        if mid > 0:  # check the left hand candidat
            candidates.append(array[mid - 1])

        closest = min(candidates, key=lambda val: (abs(val - x), val))

    print(closest)
