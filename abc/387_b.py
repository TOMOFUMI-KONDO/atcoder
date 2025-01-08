# import sys

INF = 10**18


def main():
    X = int(input())
    # N, M = map(int, input().split())
    # A = list(map(int, input().split()))

    ij = []
    for i in range(1, 10):
        line = []
        for j in range(1, 10):
            line.append(i*j)
        ij.append(line)

    ans = 0
    for i in range(9):
        for j in range(9):
            if ij[i][j] != X:
                ans += ij[i][j]

    print(ans)


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def print_list(l, sep=" "):
    print(sep.join(map(str, l)))


def print_2d_list(l):
    for i in range(len(l)):
        print_list(l[i])


if __name__ == "__main__":
    # sys.setrecursionlimit(10**6)
    main()
