# import sys

INF = 10 ** 18


def main():
    r, c = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(2)]

    print(A[r - 1][c - 1])


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
