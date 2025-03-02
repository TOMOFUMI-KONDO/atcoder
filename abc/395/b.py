# import sys

INF = 10**18


def main():
    n = int(input())

    math = [[0] * n for _ in range(n)]
    for i in range(1, n + 1):
        j = n + 1 - i
        if i <= j:
            color = "#" if i % 2 == 1 else "."
            for k in range(i, j + 1):
                for k2 in range(i, j + 1):
                    math[k - 1][k2 - 1] = color

    for i in range(n):
        for j in range(n):
            print(math[i][j], end="")
        print("")


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
