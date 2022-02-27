import sys


def main():
    N = int(input())
    # N, M = map(int, input().split())
    A = list(map(int, input().split()))
    visited = []
    ans = 0
    for a in A:
        if a in visited:
            continue
        else:
            visited.append(a)
            ans += 1
    print(ans)


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
