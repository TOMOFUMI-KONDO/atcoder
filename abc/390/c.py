# import sys

INF = 10**18


def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    a, b, c, d = INF, -1, INF, -1
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                a = min(a, j)
                b = max(b, j)
                c = min(c, i)
                d = max(d, i)

    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                if a <= j <= b and c <= i <= d:
                    print("No")
                    return

    print("Yes")


def judge(cond, yes="Yes", no="No"):
    print(yes if cond else no)


def print_list(l, sep=" "):
    print(sep.join(map(str, l)))


def print_2d_list(l):
    for i in range(len(l)):
        print_list(l[i])


if __name__ == "__main__":
    # sys.setrecursionlimit(10**6)
    main()
