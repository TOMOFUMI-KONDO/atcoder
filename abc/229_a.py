import sys


def main():
    # N = int(input())
    # N, M = map(int, input().split())
    # A = list(map(int, input().split()))
    S = []
    for _ in range(2):
        S.append(list(input()))
    if S[0][0] == "#":
        if S[0][1] == "#":
            print("Yes")
            return
        if S[1][0] == "#":
            print("Yes")
            return
        print("Yes" if S[1][1] != "#" else "No")
    else:
        if S[1][1] == "#":
            print("Yes")
            return
        if S[0][1] == "#":
            print("Yes" if S[1][0] != "#" else "No")
            return
        print("Yes")


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
