import heapq
import sys


def main():
    K = int(sys.stdin.readline())
    if K == 1:
        print(1)
        return
    dist = [float("inf")] * K
    heap = []
    for d in range(1, 10):
        mod = d % K
        if d < dist[mod]:
            dist[mod] = d
            heapq.heappush(heap, (d, mod))
    while heap:
        s, m = heapq.heappop(heap)
        if m == 0:
            print(s)
            return
        if s > dist[m]:
            continue
        for d in range(10):
            new_mod = (m * 10 + d) % K
            new_s = s + d
            if new_s < dist[new_mod]:
                dist[new_mod] = new_s
                heapq.heappush(heap, (new_s, new_mod))
    print(-1)


if __name__ == "__main__":
    main()
