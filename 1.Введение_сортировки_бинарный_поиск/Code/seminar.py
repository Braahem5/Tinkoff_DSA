def worst_caseQuickSort(num):
    array = list(range(num, 0, -1))
    return array


n = int(input())
val = worst_caseQuickSort(n)
print(" ".join(map(str, val)))
