import sys


def main():
    a, b = map(int, input().split())
    # A = list(map(int, input().split()))
    if abs(a - b) == 1 or abs(a - b) == 9:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
