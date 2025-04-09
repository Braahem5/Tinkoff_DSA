import sys
from collections import deque


def main():
    data = sys.stdin.read().strip().split("\n")

    n = int(data[0])
    queLeft = deque()
    queRight = deque()
    output = []

    for line in data[1 : n + 1]:
        parts = line.strip().split()
        if not parts:
            continue

        op = parts[0]
        if op == "+":
            x = parts[1]
            queRight.append(x)
        elif op == "*":
            x = parts[1]
            queLeft.append(x)  # O(n) time complexity
        elif op == "-":
            if queLeft:
                output.append(queLeft.popleft())

        total = len(queLeft) + len(queRight)
        desiredMid = (total + 1) // 2
        while len(queLeft) > desiredMid:
            queRight.appendleft(queLeft.pop())
        while len(queLeft) < desiredMid:
            queLeft.append(queRight.popleft())

    print("\n".join(output))


if __name__ == "__main__":
    main()
