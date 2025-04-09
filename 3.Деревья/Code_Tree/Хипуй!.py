import sys


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, x):
        self.heap.append(x)
        i = len(self.heap) - 1
        while i > 0 and self.heap[i] > self.heap[(i - 1) // 2]:
            parent = (i - 1) // 2
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent

    def extract_max(self):
        if not self.heap:
            return None  # As per problem statement, this case won't occur
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        i = 0
        n = len(self.heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i
            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right
            if largest == i:
                break
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest
        return max_val


def main():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    heap = MaxHeap()
    output = []
    for _ in range(n):
        cmd = input[ptr]
        ptr += 1
        if cmd == "0":
            x = int(input[ptr])
            ptr += 1
            heap.insert(x)
        else:
            output.append(str(heap.extract_max()))
    print("\n".join(output))


if __name__ == "__main__":
    main()
