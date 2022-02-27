import sys


def main():
    # N = int(input())
    x1, y1, x2, y2 = map(int, input().split())
    # A = list(map(int, input().split()))
    points = [
        [x1 - 2, y1 + 1], [x1 - 2, y1 - 1],
        [x1 - 1, y1 + 2], [x1 - 1, y1 - 2],
        [x1 + 1, y1 + 2], [x1 + 1, y1 - 2],
        [x1 + 2, y1 + 1], [x1 - 2, y1 - 1],
    ]
    if [x2 - 2, y2 + 1] in points or [x2 - 2, y2 - 1] in points or \
            [x2 - 1, y2 + 2] in points or [x2 - 1, y2 - 2] in points or \
            [x2 + 1, y2 + 2] in points or [x2 + 1, y2 - 2] in points or \
            [x2 + 2, y2 + 1] in points or [x2 + 2, y2 - 1] in points:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
