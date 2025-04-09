def main():
    try:
        n = int(input().strip())
    except Exception:
        return
    arr = []
    while len(arr) < n:
        arr.extend(list(map(int, input().split())))
    stack = [arr[0]]
    answer = 0
    index = 1
    for i in range(1, n + 1):
        if i < n:  # To avoid out of bound Access
            x = arr[index]
            index += 1
            if x == stack[-1]:
                stack.append(x)
                continue  # to avoid the code below if they are 'x' is equal to the top of the stack
        left_bound = len(stack) - 1
        while left_bound >= 0 and stack[left_bound] == stack[-1]:
            left_bound -= 1
        group_count = len(stack) - left_bound - 1
        if group_count >= 3:
            for _ in range(group_count):
                stack.pop()
            answer += group_count
        if i < n:
            stack.append(x)
    print(answer)


if __name__ == "__main__":
    main()
