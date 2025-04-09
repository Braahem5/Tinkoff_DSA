import sys
from collections import deque


def main():
    data = sys.stdin.read().split()  # Read all input tokens at once.
    n = int(data[0])
    d = deque()
    pos_by_id = {}
    gone = 0
    output_lines = []

    index = 1  # Pointer to traverse tokens in `data`
    for _ in range(n):
        query_type = int(data[index])
        index += 1

        if query_type == 1:
            id_val = int(data[index])
            index += 1
            pos_by_id[id_val] = len(d) + gone  # what does this does?
            d.append(id_val)
        elif query_type == 2:
            d.popleft()
            gone += 1
        elif query_type == 3:
            d.pop()
        elif query_type == 4:
            q_val = int(data[index])
            index += 1
            output_lines.append(str(pos_by_id[q_val] - gone))  # And this line also?
        else:
            output_lines.append(str(d[0]))

    sys.stdout.write("\n".join(output_lines))


if __name__ == "__main__":
    main()
