import sys


def main():
    A = list(map(int, input().split()))
    ans = 0
    for _ in range(3):
        ans = A[ans]
    print(ans)


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
