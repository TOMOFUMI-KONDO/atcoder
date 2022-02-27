import sys


def main():
    X = int(input())
    # N, M = map(int, input().split())
    # A = list(map(int, input().split()))
    print(X // 10)


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
