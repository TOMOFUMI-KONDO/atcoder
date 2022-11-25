# import sys

INF = 10 ** 18


def main():
    N, Q = map(int, input().split())
    ff = {}

    for _ in range(Q):
        t, a, b = map(int, input().split())
        a -= 1
        b -= 1

        if t == 1:
            ff[a, b] = 1
        if t == 2:
            ff[a, b] = 0
        if t == 3:
            judge((a, b) in ff and ff[a, b] and (b, a) in ff and ff[b, a])


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
