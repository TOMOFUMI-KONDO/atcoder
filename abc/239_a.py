import math
import sys


def main():
    H = int(input())
    # N, M = map(int, input().split())
    # A = list(map(int, input().split()))
    print(math.sqrt(H * (12800000 + H)))


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
