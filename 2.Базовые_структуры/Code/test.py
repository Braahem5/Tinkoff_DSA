import sys
from collections import deque


def equalize(left, right):
    total = len(left) + len(right)
    desired_left = (total + 1) // 2
    while len(left) < desired_left:
        left.append(right.popleft())
    while len(left) > desired_left:
        right.appendleft(left.pop())


def main():
    n = int(sys.stdin.readline())
    left = deque()
    right = deque()
    for _ in range(n):
        parts = sys.stdin.readline().split()
        if not parts:
            continue
        type_op = parts[0]
        if type_op == "+":
            x = int(parts[1])
            right.append(x)
        elif type_op == "*":
            x = int(parts[1])
            left.append(x)
        elif type_op == "-":
            print(left.popleft())
        equalize(left, right)


if __name__ == "__main__":
    main()
