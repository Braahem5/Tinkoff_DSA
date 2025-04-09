A, B, C, D = map(int, input().strip().split())

left, right = -1e6, 1e6
precision = 1e-6


def func(x):
    return A * (x**3) + B * (x**2) + C * x + D


if func(left) * func(right) <= 0:
    while right - left > precision:
        mid = (left + right) / 2

        if func(mid) == 0:
            break
        elif func(left) * func(mid) < 0:
            right = mid
        else:
            left = mid

    print(f"{mid:.6f}")
