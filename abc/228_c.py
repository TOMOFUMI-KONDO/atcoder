import sys


def main():
    N, K = map(int, input().split())
    sums = [sum(map(int, input().split())) for _ in range(N)]
    sums_sorted = sorted(sums, reverse=True)
    for s in sums:
        if s + 300 >= sums_sorted[K - 1]:
            print('Yes')
        else:
            print('No')


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
