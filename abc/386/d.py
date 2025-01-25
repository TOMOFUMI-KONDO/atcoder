# import sys

INF = 10**18


def main():
    N, M = map(int, input().split())

    grid = []
    for _ in range(M):
        X, Y, C = input().split()
        grid.append([int(X), int(Y), C])

    grid.sort(key=lambda x: x[1])
    grid.sort(key=lambda x: x[0])

    min_y = INF
    for g in grid:
        y, c = g[1], g[2]
        if c == "W":
            min_y = min(min_y, y)
        else:
            if y >= min_y:
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
