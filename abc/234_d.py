# ref. https://atcoder.jp/contests/abc234/editorial/3222

import heapq


def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    heap = P[:K]
    heapq.heapify(heap)
    for i in range(K + 1, N + 1):
        minimum = heapq.heappop(heap)
        heapq.heappush(heap, max(minimum, P[i - 1]))
        print(minimum)
    print(heapq.heappop(heap))


if __name__ == "__main__":
    main()
