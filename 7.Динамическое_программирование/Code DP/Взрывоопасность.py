n = int(input())
if n == 0:
    print(0)
else:
    a, b, c = 1, 1, 1
    for _ in range(n - 1):
        new_a = b + c
        new_b = a + b + c
        new_c = new_b
        a, b, c = new_a, new_b, new_c
    print(a + b + c)
