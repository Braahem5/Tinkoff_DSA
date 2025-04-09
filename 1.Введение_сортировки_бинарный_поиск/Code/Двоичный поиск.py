n, k = map(int, input().split())
firstArr = sorted(list(map(int, input().split()))[:n])  # Ensure firstArr is sorted
secondArr = list(map(int, input().split()))[:k]


def Binary(val, arr, start, end):
    if start > end:
        return False

    mid = (start + end) // 2

    if val == arr[mid]:
        return True
    elif val < arr[mid]:
        return Binary(val, arr, start, mid - 1)  # Adjust end to mid - 1
    else:
        return Binary(val, arr, mid + 1, end)  # Adjust start to mid + 1


for x in secondArr:
    if Binary(x, firstArr, 0, len(firstArr) - 1):
        print("YES")
    else:
        print("NO")
