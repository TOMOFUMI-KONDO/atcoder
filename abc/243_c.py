import sys


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    S = list(input())

    groups = {}
    for i in range(N):
        xy = XY[i]
        groups.setdefault(xy[1], [-1, 10 ** 9 + 1])
        if S[i] == "L":
            groups[xy[1]][0] = max(xy[0], groups[xy[1]][0])
        else:
            groups[xy[1]][1] = min(xy[0], groups[xy[1]][1])

    for g in groups.values():
        if g[0] != -1 and g[1] != 10 ** 9 + 1 and g[0] > g[1]:
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
