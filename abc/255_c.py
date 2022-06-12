# import sys

INF = 10 ** 18


def main():
    X, A, D, N = map(int, input().split())

    if D >= 0:
        min_ = A
        max_ = A + D * (N - 1)
    else:
        min_ = A + D * (N - 1)
        max_ = A

    if X <= min_:
        print(min_ - X)
        return

    if X >= max_:
        print(X - max_)
        return

    if D >= 0:
        i = (X - A) // D
        print(min(X - (A + D * i), (A + D * (i + 1)) - X))
    else:
        i = (A - X) // -D
        print(min((A + D * i) - X, X - (A + D * (i + 1))))


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
