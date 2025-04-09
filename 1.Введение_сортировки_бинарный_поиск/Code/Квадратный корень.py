C = float(input())

left, right = 0, C**0.5
PRECISION = 1e-6

while (right - left) >= PRECISION:
    mid = (right + left) / 2
    equation_value = mid**2 + (mid + 1) ** 0.5

    if equation_value < C:
        left = mid
    else:
        right = mid

print("{:.10f}".format(mid))
