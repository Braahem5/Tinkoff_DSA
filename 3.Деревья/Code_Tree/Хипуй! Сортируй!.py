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
    n = int(input[0])
    arr = list(map(int, input[1:n+1]))
    
    heap = MaxHeap()
    for num in arr:
        heap.insert(num)
    
    sorted_desc = []
    for _ in range(n):
        sorted_desc.append(heap.extract_max())
    
    # Reverse to get ascending order
    sorted_asc = sorted_desc[::-1]
    print(' '.join(map(str, sorted_asc)))

if __name__ == '__main__':
    main()