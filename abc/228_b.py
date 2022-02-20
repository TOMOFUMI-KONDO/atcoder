import sys


def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    visited = [False] * N
    ans = 0
    while True:
        if visited[X - 1]:
            break
        ans += 1
        visited[X - 1] = True
        X = A[X - 1]

    print(ans)


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
