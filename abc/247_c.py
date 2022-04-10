import copy
import sys

INF = 10 ** 18


def main():
    N = int(input())

    S = [[1]]
    for i in range(N - 1):
        prev = copy.copy(S[i])
        next = [*prev, i + 2, *prev]
        S.append(next)

    print_list(S[-1])


def judge(cond, yes='Yes', no='No'):
    print(yes if cond else no)


def print_list(l, sep=" "):
    print(sep.join(map(str, l)))


def print_2d_list(l):
    for i in range(len(l)):
        print_list(l[i])


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
